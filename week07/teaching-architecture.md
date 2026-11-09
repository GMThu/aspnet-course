# 東海大學 ASP.NET 第七週教學架構

**主題：驗證通過之後，讓小安的活動報名真的留下來**  
**技術假設：ASP.NET Core Razor Pages + EF Core + SQL Server**  
**課程長度：3 × 50 分鐘｜投影片：約 24 頁｜初學者導向**

---

## 1. 課程定位

### 承接前兩週
- **Week05**：小安能把校園活動報名表 `POST` 到 `PageModel`。
- **Week06**：小安把四個欄位收進 `RegistrationInput`，用 DataAnnotations、`ModelState` 與三路測試判斷「可不可以接受」。
- **Week07**：只有驗證通過的資料，才轉成資料庫 Entity、寫入 SQL Server，再由 GET 查出；停止網站後重啟，報名仍存在。

### 本週一句話
> Week06 決定「可不可以收」；Week07 才決定「要不要留下來」。

### 學生下課前能做到
1. 用自己的話區分 **Input Model、Entity、DbContext、SQL Server**。
2. 說明 migration 是「把程式中的資料形狀轉成可追蹤的資料庫結構變更」，不是一般的存檔動作。
3. 讓 `ModelState.IsValid` 成為寫入前的閘門。
4. 將合法的 `RegistrationInput` 明確轉成 `Registration` Entity，執行 `Add` 與 `SaveChangesAsync`。
5. 在 GET 讀出報名清單，並以「停止網站 → 重啟 → 再查詢」證明資料持久化。

### 教學原則
- **people-first**：不先講 ORM 定義，先解決小安「成功畫面出現，但重啟就不見」的困擾。
- **短講解 → 教師示範 → 學生實作 → 可觀察檢核**。
- 全週只走一條最小閉環：**合法報名 → 寫入 → GET 查詢 → 重啟仍在**。
- 不把 EF Core 變成一堂 SQL、完整 CRUD 或架構分層課。

---

## 2. 課前準備與共同起點

### 教師需先備妥
- Week06 完成版專案，保留同一組欄位：
  - `DisplayName`
  - `Email`
  - `Session`
  - `Note`
- 一份 **已驗證可連線** 的 SQL Server 環境與對應連線設定；Windows、Docker、遠端 SQL Server 的連線字串不同，不在上課中臨時猜。
- 一份可直接開始的 Week07 starter：
  - 目標框架沿用現有課程專案（目前 Week06 為 `net10.0`）。
  - `Microsoft.EntityFrameworkCore.SqlServer` 與 `Microsoft.EntityFrameworkCore.Design` 已鎖定在課程測過且彼此相容的版本線。
  - `dotnet-ef` 已由教師在教室環境確認可用。
  - 不含完成版 Entity、DbContext、migration 與 SaveChanges 程式碼。
- 一份 recovery starter：若學生環境在 5 分鐘內仍無法連線，可切換到已完成資料庫基礎設定的檢查點，繼續學習資料流。

### 開課前 3 分鐘快速檢查
- `dotnet restore` 成功。
- 專案能啟動，Week06 三路測試仍成立。
- SQL Server 可連線；資料庫帳號有建立／更新本課資料庫的權限。
- 在**含 `.csproj` 的專案目錄**中執行 `dotnet ef --version` 可取得版本資訊。
- 不在投影片或儲存庫展示真實密碼；連線祕密由教師預先配置。

### 課前風險決策
- **不把 SQL Server 安裝或 Docker 映像下載排進本週 150 分鐘。** 這些是先備條件，不是學生本週學習成果。
- 若教室有 macOS／Apple Silicon，教師需事前驗證所採 SQL Server 方案；不能假設 SQL Server 能像一般 macOS App 原生執行。
- 學生使用同一份 starter 與同一路徑命令，避免一半用 Visual Studio Package Manager Console、一半用 CLI。

---

## 3. 3 × 50 分鐘節奏總表

| 節次 | 核心問題 | 頁次 | 講解／示範 | 實作停點 | 檢核／收束 | 合計 |
|---|---|---:|---:|---:|---:|---:|
| 第一節 | 程式怎麼知道要把哪種資料放到哪裡？ | 1–8 | 29 分 | 18 分 | 3 分 | 50 分 |
| 第二節 | 程式中的 Entity 如何成為資料庫的表？ | 9–16 | 25 分 | 18 分 | 7 分 | 50 分 |
| 第三節 | 如何只存合法資料，並證明重啟後仍在？ | 17–24 | 24 分 | 20 分 | 6 分 | 50 分 |

> 三次停點分別為第 **7、13、22 頁**；投影時停留在該頁，不邊走邊加講新觀念。

---

# 4. 24 頁「一頁一觀點」大綱

## 第一節（第 1–8 頁，共 50 分鐘）

### 第 1 頁｜小安今天要解決的不是「送出」，而是「留下」【4 分】
**唯一觀點：** 成功訊息不是持久化證據。  
- 畫面 A：Week06 合法送出後顯示成功。
- 畫面 B：網站停止重啟，資料不存在。
- 今天的終點：重啟後仍能看到小安的活動報名。

**教師動作：** 先問「上週的資料放在哪裡？」接受「記憶體／PageModel／其實沒存」等初步答案，再揭示今日任務。  
**學生可說出：** 「Week06 只驗證，還沒有資料庫。」

### 第 2 頁｜沿用 Week06 的三路測試，不重開新故事【5 分】
**唯一觀點：** 資料庫加入後，既有驗證行為不能退步。  
- 路 1：全空白 → 顯示必填錯誤 → **資料列不增加**。
- 路 2：`Email = abc` → 顯示格式錯誤 → **資料列不增加**。
- 路 3：合法資料 → 顯示成功 → **資料列增加 1**。
- 本週另加持久化證據：停止與重啟後，合法那筆仍可查到。

**教師提醒：** 「重啟測試」是持久化檢核，不是取代 Week06 的三路驗證測試。

### 第 3 頁｜一筆報名會經過四個角色【5 分】
**唯一觀點：** 每個角色只負責資料旅程中的一段。  
以箭頭圖呈現：

`表單 → RegistrationInput → Registration Entity → DbContext → SQL Server`

GET 方向：

`SQL Server → DbContext 查詢 → PageModel 清單 → Razor Page`

- Input Model：接收與驗證使用者輸入。
- Entity：描述要持久化的資料形狀。
- DbContext：應用程式與資料庫之間的工作入口。
- SQL Server：程序停止後仍保留資料。

**檢核問句：** 「DataAnnotations 的錯誤訊息主要留在哪個角色？」答案：Input Model。

### 第 4 頁｜Entity 是「要留下的報名」，不是整張表單【6 分】
**唯一觀點：** Entity 只放本週真的要保存的欄位與資料庫識別。  
建議最小模型：

```csharp
public class Registration
{
    public int Id { get; set; }
    public string DisplayName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public string Session { get; set; } = string.Empty;
    public string? Note { get; set; }
    public DateTime CreatedAt { get; set; }
}
```

- `Id`：每筆資料的識別值，新增後由資料庫產生。
- `CreatedAt`：由伺服器決定，不要求小安在表單輸入。
- 不把「成功訊息」「確認按鈕」之類畫面狀態放進 Entity。

**教師避免：** 本頁不延伸主鍵策略、索引、正規化。

### 第 5 頁｜Input Model 與 Entity 分開，才能看見信任邊界【5 分】
**唯一觀點：** 接收到的資料不等於可以直接保存的資料。  
- `RegistrationInput`：仍保留 Week06 的 `[Required]`、`[EmailAddress]`、`[StringLength]`。
- `Registration`：是通過閘門後才建立的資料庫物件。
- 以明確 mapping 表達選擇：

```csharp
var registration = new Registration
{
    DisplayName = Input.DisplayName,
    Email = Input.Email,
    Session = Input.Session,
    Note = Input.Note,
    CreatedAt = DateTime.UtcNow
};
```

**初學者語句：** 「先驗票，再把可入場的人換成正式名單。」

### 第 6 頁｜DbContext 是本次資料工作的入口【4 分】
**唯一觀點：** `DbSet<Registration>` 讓程式能以 Entity 集合的方式新增與查詢。  

```csharp
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options) { }

    public DbSet<Registration> Registrations => Set<Registration>();
}
```

**口頭拆解：**
- `AppDbContext`：這個網站的資料庫工作入口。
- `Registrations`：本週唯一要操作的 Entity 集合。
- 本週不教 repository，不再包一層抽象。

### 第 7 頁｜實作停點 1：建立資料角色【18 分】
**投影標示：** `暫停講解・學生實作 18:00`

#### 學生現在完成
1. 建立 `Models/Registration.cs`，加入 `Id`、四個報名欄位與 `CreatedAt`。
2. 建立 `Data/AppDbContext.cs`。
3. 在 `AppDbContext` 加入 `DbSet<Registration> Registrations`。
4. 執行 build，修到專案可編譯。

#### 完成條件
- 專案 build 成功。
- 能指給同學看：哪一個類別接表單、哪一個類別會進資料庫。
- 能回答：`CreatedAt` 為何不放在小安填寫的 Input Model？

#### 老師現在巡視
- 是否把 `RegistrationInput` 直接改名成 Entity，導致 Week06 驗證角色消失。
- 是否漏掉 `public`、`get; set;`、namespace 或必要 using。
- `Note` 是否仍允許空值；字串欄位是否初始化，避免初學者被 nullable 警告淹沒。
- 是否誤以為建立 class 就已建立資料庫表。

#### 分流
- **較慢者：** 提供兩個檔案骨架，只補屬性與 `DbSet`。
- **提早完成者：** 在紙上畫出 Input → Entity 的五條 mapping，不先做 CRUD。
- **第 9 分鐘提醒：** 「先求 build 成功，再整理資料夾。」

### 第 8 頁｜第一節收束：現在只有地圖，還沒有道路【3 分】
**唯一觀點：** Entity 與 DbContext 已建立，但尚未連線、尚未產生資料表。  
Exit ticket：學生在便利貼完成兩句：
1. `Registration` 代表＿＿＿＿。
2. `AppDbContext` 代表＿＿＿＿。

---

## 第二節（第 9–16 頁，共 50 分鐘）

### 第 9 頁｜先註冊 DbContext，程式才知道連去哪裡【3 分】
**唯一觀點：** `Program.cs` 把 Context 與 SQL Server 連線設定交給 DI。  

```csharp
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("CampusDb")));
```

- `CampusDb` 是設定鍵，不是資料庫名稱保證，也不是密碼本身。
- PageModel 稍後透過建構子取得 `AppDbContext`。

**教師提醒：** 本頁只講「註冊與取得」，不展開 DI lifetime。

### 第 10 頁｜連線字串是地址與通行方式，不是課堂投影片內容【5 分】
**唯一觀點：** 程式碼只讀設定鍵；真實連線資訊依環境提供。  
- 教師示範 `ConnectionStrings:CampusDb` 的位置與讀取方式。
- Windows 整合驗證、SQL 帳密、Docker 對外連接埠可能產生不同字串。
- 不要求學生互抄密碼；不把正式帳密提交到 Git。
- 若本機開發使用需要信任開發憑證的設定，說明那是**開發環境選擇**，不是安全萬用解。

**檢核問句：** 「換電腦時通常先改 Entity 還是連線設定？」答案：連線設定。

### 第 11 頁｜Migration 是可追蹤的結構變更說明【7 分】
**唯一觀點：** migration 連接「程式模型」與「資料庫結構」，但不等於把報名資料存進去。  
- `dotnet ef migrations add InitialCreate`：依目前模型產生 migration 檔與 snapshot。
- `dotnet ef database update`：把尚未套用的 migration 套到目標資料庫。
- migration 檔應保留在專案中；資料庫不是靠口頭記憶建出來。

**教師示範順序：**
1. 確認終端機位於含 `.csproj` 的專案目錄。
2. 執行 `dotnet ef migrations add InitialCreate`。
3. 停下來看新增的 `Migrations/`，只辨識名稱與 `Up`／`Down`，不逐行講 SQL。
4. 執行 `dotnet ef database update`。

**重要語句：** 「add migration 產生變更檔；database update 才把變更套進資料庫。」

### 第 12 頁｜看到資料表，才算結構真的到位【4 分】
**唯一觀點：** 命令顯示成功只是線索，資料庫中的表才是可觀察證據。  
- 用教師選定的資料庫檢視工具確認：
  - 本課資料庫存在。
  - `Registrations` 表存在。
  - 欄位至少含 `Id`、四個報名欄位、`CreatedAt`。
  - migrations history 表存在。
- 此時 `Registrations` 可是 0 筆；本節目標是結構，不是新增資料。

### 第 13 頁｜實作停點 2：把模型變成資料庫結構【18 分】
**投影標示：** `暫停講解・學生實作 18:00`

#### 學生現在完成
1. 在 `Program.cs` 註冊 `AppDbContext` 與 `UseSqlServer(...)`。
2. 確認 `CampusDb` 連線設定由課程指定位置提供。
3. 在正確專案目錄執行：
   - `dotnet ef migrations add InitialCreate`
   - `dotnet ef database update`
4. 用課程指定檢視方式找到 `Registrations` 表。

#### 完成條件
- 專案可 build。
- `Migrations/` 內出現初始 migration 與 model snapshot。
- `database update` 成功完成。
- 能指出資料庫中的 `Registrations` 表與至少三個欄位。
- 能口頭區分兩個命令各自做什麼。

#### 老師現在巡視
- 終端機是否跑在錯誤資料夾；這通常比程式碼錯誤更常見。
- `dotnet ef` 找不到：先判斷工具未安裝、PATH 問題，或工具版本與專案不相容；不要讓學生盲目裝「最新版」。
- `No DbContext was found`：檔案是否編譯、namespace／DI 設定是否正確。
- `Login failed`、連線逾時、憑證錯誤：先歸類為環境／連線問題，不要叫學生反覆改 Entity。
- 同一 migration 名稱已存在、資料庫已有舊結構：停下來確認學生是否使用舊 starter，不直接亂刪 production-like 資料庫。

#### 分流
- **較慢者：** 5 分鐘仍卡在環境時，切換到教師 recovery checkpoint；仍須親自辨識 migration 與資料表。
- **提早完成者：** 在 migration 的 `Up` 找到建立 `Registrations` 的區段，只圈出表名與主鍵，不改檔。
- **第 9 分鐘提醒：** 「現在驗收的是表，不是報名資料。」

### 第 14 頁｜Migration 與 SaveChanges 是兩件不同的事【5 分】
**唯一觀點：** 前者改結構，後者改資料。  
對照表：

| 問題 | 使用什麼 |
|---|---|
| 新增／改變 Entity 後，資料表結構要跟上 | migration + database update |
| 小安送出一筆合法報名 | `Add` + `SaveChangesAsync` |
| 頁面載入時顯示既有報名 | LINQ query + `ToListAsync` |

**快速判斷：** 教師說三個情境，學生舉「結構」「資料」「查詢」卡。

### 第 15 頁｜DbContext 由 PageModel 建構子取得【4 分】
**唯一觀點：** PageModel 不自行 `new AppDbContext()`；使用 DI 提供的同一設定。  

```csharp
private readonly AppDbContext _db;

public IndexModel(AppDbContext db)
{
    _db = db;
}
```

- 這讓 PageModel 專注處理 GET／POST 流程。
- 本週只接受「Context 從建構子進來」的最小心智模型。

### 第 16 頁｜第二節檢核：空表不是失敗，是下一步的起點【4 分】
**唯一觀點：** 到這裡應有「可連線的空資料表」，尚未有報名資料。  
兩人互問：
1. 「`migrations add` 和 `database update` 差在哪？」
2. 「為何現在資料表是空的？」

教師收束預期答案：因為還沒有在合法 POST 中呼叫 `SaveChangesAsync`。

---

## 第三節（第 17–24 頁，共 50 分鐘）

### 第 17 頁｜寫入必須放在 ModelState 閘門之後【4 分】
**唯一觀點：** 任何新增 Entity 的程式碼都不能越過 Week06 的驗證閘門。  

```csharp
if (!ModelState.IsValid)
{
    Registrations = await _db.Registrations
        .OrderByDescending(x => x.CreatedAt)
        .ToListAsync();
    return Page();
}
```

- 無效輸入：留在原頁、顯示錯誤、重新準備頁面清單、**不 Add、不 Save**。
- 教師可故意把 `Add` 放到 if 前面，請學生指出危險位置，再修正。

### 第 18 頁｜合法 Input 要明確轉成 Entity【5 分】
**唯一觀點：** mapping 是「哪些使用者輸入被允許保存」的清單。  
- 沿用第 5 頁 mapping。
- `CreatedAt` 由伺服器填 `DateTime.UtcNow`。
- 不使用 `Registration = Input`，也不讓表單直接綁整個 Entity。

**檢核問句：** 「小安可以自行 POST 一個任意的 `Id` 或 `CreatedAt` 嗎？」本週設計：不可以，因為 Input Model 沒有這些欄位，mapping 也不接受。

### 第 19 頁｜Add 只是追蹤；SaveChangesAsync 才送出資料變更【6 分】
**唯一觀點：** 必須完成兩步，資料才會進 SQL Server。  

```csharp
_db.Registrations.Add(registration);
await _db.SaveChangesAsync();
```

- `Add`：告訴 DbContext 這是一筆待新增 Entity。
- `SaveChangesAsync`：把待處理變更送到資料庫。
- 方法簽名改為 `public async Task<IActionResult> OnPostAsync()`。
- 漏掉 `await` 或 `SaveChangesAsync`，不能宣稱完成保存。

### 第 20 頁｜POST 完成後 Redirect，GET 再準備畫面【5 分】
**唯一觀點：** 使用 Post/Redirect/Get，重新整理不應再次送出同一張表單。  

```csharp
TempData["Message"] = "報名成功";
return RedirectToPage();
```

- 合法 POST：保存 → redirect。
- 瀏覽器接著 GET：查詢清單 → 顯示資料。
- 不在本週深入 TempData provider；只把它當成一次性成功訊息。

### 第 21 頁｜GET 從資料庫查詢，畫面才有持久化證據【4 分】
**唯一觀點：** 顯示的清單必須來自 `_db.Registrations`，不是本機 List 或上一個 POST 的欄位。  

```csharp
public List<Registration> Registrations { get; set; } = [];

public async Task OnGetAsync()
{
    Registrations = await _db.Registrations
        .OrderByDescending(x => x.CreatedAt)
        .ToListAsync();
}
```

Razor 只需最小清單：名稱、場次、報名時間；Email 是否公開顯示由教師採最小揭露原則決定，預設不投影完整 Email。

### 第 22 頁｜實作停點 3：完成「驗證 → 保存 → 查詢 → 重啟」閉環【20 分】
**投影標示：** `暫停講解・學生實作 20:00`

#### 學生現在完成
1. 將 `AppDbContext` 注入 PageModel。
2. 保留 Week06 的 `RegistrationInput`、DataAnnotations 與 `ModelState` 閘門。
3. 在合法分支中 mapping 成 `Registration`，執行 `Add`、`await SaveChangesAsync()`，再 redirect。
4. 在 GET 查詢 `Registrations`，於頁面顯示最小報名清單。
5. 依序跑三路測試，再停止網站、重新啟動、刷新清單。

#### 完成條件
- 空白送出：顯示驗證錯誤，資料列數不增加。
- `Email = abc`：顯示格式錯誤，資料列數不增加。
- 合法的小安報名：成功 redirect，清單增加 1 筆。
- 重新整理結果頁不會再新增 1 筆。
- 完全停止網站程序並重新啟動後，那筆合法報名仍出現在 GET 清單。
- 學生能指出：閘門、mapping、`SaveChangesAsync`、GET query 各在哪一段。

#### 老師現在巡視
- `Add`／`SaveChangesAsync` 是否誤放在 `ModelState` 判斷之前。
- 無效 POST 回傳 `Page()` 時，清單是否需要重新查詢；否則畫面可能看似「資料消失」。
- 是否真的 `await SaveChangesAsync()`，以及 handler 回傳型別是否配合 async。
- 是否 redirect，還是刷新就重複 POST。
- 清單來源是否真的是 `_db.Registrations`，不是 `new List<Registration>()` 假資料。
- 「重啟」是否真的停止程序再啟動，而不只是瀏覽器重新整理。
- 是否因舊資料誤判測試；要求先記錄測試前後筆數，不只看畫面上有名字。

#### 分流
- **較慢者：** 提供四段待排序程式卡（validate、map、save、redirect），先排對順序再貼入骨架。
- **提早完成者：** 加入「同 Email + 同場次」的思考題，只描述規則放哪裡，不在本週實作唯一索引或商業規則。
- **第 10 分鐘提醒：** 「先取得一筆合法資料，再做重啟證據；不要先美化表格。」

### 第 23 頁｜用四張證據驗收，不用「我覺得有成功」【3 分】
**唯一觀點：** 完成是可觀察、可重現的。  
學生兩人互驗並出示：
1. 無效資料的欄位錯誤，且筆數不變。
2. 合法報名後清單多一筆。
3. 資料庫檢視工具中存在同一筆資料。
4. 停止／重啟網站後 GET 清單仍有該筆。

**同儕口頭題：** 「哪一行保證只有合法資料會走到保存？」預期指向 `if (!ModelState.IsValid) return Page();` 所形成的控制流程。

### 第 24 頁｜本週完成：小安的報名真的留下來【3 分】
**唯一觀點：** 本週只完成 Create + Read 的最小持久化閉環，刻意不做完整 CRUD。  
收束圖：

`POST → Input 驗證 → Entity → SaveChanges → Redirect → GET 查詢 → 重啟仍在`

Exit ticket：
- 今天最重要的安全順序：＿＿＿＿之後才能＿＿＿＿。
- migration 改的是＿＿＿＿；SaveChanges 改的是＿＿＿＿。
- 下週若要修改報名，還需要學＿＿＿＿（只預告，不開教）。

---

## 5. 三次實作停點總覽

| 停點 | 時間 | 學生產出 | 最小完成證據 | 教師優先巡視 |
|---|---:|---|---|---|
| 1：資料角色 | 18 分 | `Registration`、`AppDbContext`、`DbSet` | build 成功；能區分 Input 與 Entity | 是否直接拿 Input 當 Entity、nullable／namespace 錯誤 |
| 2：資料庫結構 | 18 分 | DI 設定、initial migration、database update | migration 檔存在；SQL Server 看得到表 | 工具版本、工作目錄、連線／權限、舊資料庫衝突 |
| 3：持久化閉環 | 20 分 | 驗證後 mapping/save、GET query、PRG | 三路測試 + 重啟後仍在 | Save 是否在閘門後、是否 await、GET 是否真查 DB、是否重複 POST |

---

## 6. 全課完成條件（可作為教師驗收單）

學生需全部達成：

- [ ] 原有 `RegistrationInput` 與 DataAnnotations 仍存在。
- [ ] 有獨立的 `Registration` Entity，包含 `Id` 與伺服器產生的 `CreatedAt`。
- [ ] 有 `AppDbContext` 與 `DbSet<Registration>`，並透過 DI 註冊 SQL Server provider。
- [ ] 有可追蹤的 initial migration，且已成功 `database update`。
- [ ] 無效 POST 不執行新增；空白與錯誤 Email 都不增加資料列。
- [ ] 合法 POST 明確 mapping、`Add`、`await SaveChangesAsync()`，並 redirect。
- [ ] GET 使用資料庫查詢顯示清單，而非假資料或記憶體 List。
- [ ] 刷新 redirect 後的頁面不會再次新增同一筆。
- [ ] 停止網站、重新啟動後仍能查到合法報名。
- [ ] 學生能用一句話分辨 migration 與 SaveChanges。

**建議判定：** 前 9 項是功能證據；第 10 項是理解證據。只貼上完成版但無法指出資料流，不算完整完成。

---

## 7. 教師巡視優先順序

### 第一優先：資料正確性
1. 無效資料有沒有被寫入。
2. 合法資料是否只新增一次。
3. 畫面是否真從資料庫查詢。
4. 重啟證據是否真的是程序重啟。

### 第二優先：概念混淆
- 把 Input Model 當 Entity。
- 把 migration 當成每次送表單都要跑。
- 以為 `Add` 已經寫入資料庫。
- 以為瀏覽器刷新等於應用程式重啟。
- 以為「看見成功訊息」就等於資料已保存。

### 第三優先：環境與工具
- CLI 所在目錄。
- provider／Design package／`dotnet-ef` 的相容性。
- SQL Server 是否正在執行、連線埠與帳號權限。
- 連線字串讀取鍵是否一致。
- 舊 migration、舊資料庫、同名資料庫造成的狀態污染。

### 教師現場用語
- 不先說「你 EF 壞了」，先問：「目前卡在模型、工具、連線、結構、資料，哪一層？」
- 不替學生整段重打，先要求指出資料流目前走到哪一格。
- 5 分鐘無法排除純環境問題即切 recovery checkpoint，保留核心學習時間。

---

## 8. 本週邊界

### 本週一定教
- 一個 `Registration` Entity。
- 一個 `AppDbContext` 與一個 `DbSet`。
- SQL Server provider 註冊與連線設定鍵的概念。
- 一次 initial migration 與 database update。
- 驗證成功後的明確 Input → Entity mapping。
- `Add`、`SaveChangesAsync`、Post/Redirect/Get。
- 一個 GET read-all 查詢與最小清單。
- 三路驗證測試與停止／重啟持久化證據。

### 本週明確不教
- 完整 CRUD：不做 Edit、Delete、Details。
- 關聯、外鍵、導覽屬性、多資料表。
- Repository、Service layer、CQRS、Clean Architecture。
- Identity、登入、授權、個人資料權限。
- 搜尋、排序 UI、分頁、報表、CSV 匯出。
- 唯一索引、重複報名商業規則、交易與並行控制。
- Raw SQL、SQL 語法教學、資料庫正規化、效能調校。
- Production migration／部署、自動化發版、正式祕密管理。
- SQL Server／Docker 從零安裝。

### 可以口頭預告，但不現場實作
- 下週若要修改或取消報名，才會需要找出單筆資料、Edit／Delete 與更完整的 CRUD 流程。
- 真實系統還要處理重複報名、授權、個資顯示、例外與並行問題。

---

## 9. 可能的教學風險與備案

| 風險 | 現象 | 教師備案 |
|---|---|---|
| SQL Server 未啟動／未安裝 | timeout、connection refused | 課前完成環境；課中切 recovery DB／已設定 starter，不現場下載大型映像 |
| macOS／Apple Silicon 環境差異 | 容器無法啟動、映像架構不合 | 教師事前在同型機驗證；必要時統一遠端 SQL Server，而非臨場猜參數 |
| EF 套件與 `dotnet-ef` 不相容 | tools runtime／design-time 錯誤 | starter 鎖版並課前測過；學生不自行更新最新版 |
| CLI 在錯誤目錄 | 找不到 project／DbContext | 投影片固定顯示「含 `.csproj` 的目錄」；先 `pwd`／確認檔案再重跑 |
| 連線字串或權限錯誤 | login failed、certificate、database create denied | 使用課前測過的設定；把錯誤分類為連線層，不重寫 Entity |
| 舊 migration／舊資料庫污染 | 表已存在、migration 同名、欄位不一致 | 每位學生用課程指定資料庫名；教師提供乾淨重置流程，但不把「隨便刪資料庫」當通用答案 |
| 無效 POST 清單空白 | validation 顯示但既有清單不見 | 無效分支回 Page 前重新查詢清單，或以共用載入方法準備頁面資料 |
| 忘記 redirect | F5 重新提交造成重複資料 | 明確採 PRG；刷新後以筆數確認沒有多一筆 |
| 把 Entity 直接 Bind | 多綁欄位、信任邊界消失 | 保留獨立 Input Model 與明確 mapping；本週不使用整個 Entity 作表單模型 |
| 實作時間被美化吃掉 | CSS 完成但資料未持久化 | 停點 3 先完成一筆合法資料與重啟證據，畫面美化不列入驗收 |

---

## 10. 命令與版本說明（教師版）

本課使用的核心命令語法：

```bash
dotnet ef --version
dotnet ef migrations add InitialCreate
dotnet ef database update
```

若建立全新專案，官方文件所列 provider／design package 命令語法為：

```bash
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Design
```

但**學生課堂 starter 應預先鎖定課程驗證過的版本**；不要在課中無條件安裝或更新「最新版本」。若 `dotnet-ef` 未就緒，教師應依課程鎖定版本提供 recovery 指令，而不是在投影片硬寫一個未驗證的版本號。

### 官方核對來源
- EF Core CLI tools reference：<https://learn.microsoft.com/ef/core/cli/dotnet>
- EF Core migrations overview：<https://learn.microsoft.com/ef/core/managing-schemas/migrations/>
- EF Core SQL Server provider：<https://learn.microsoft.com/ef/core/providers/sql-server/>

---

## 11. 教師最後一句收束

> 小安的資料不是因為「畫面說成功」而被保存；它是因為先通過驗證、被明確轉成 Entity、由 DbContext 寫入 SQL Server，再由新的 GET 查回來，而且網站重啟後證據仍在。
