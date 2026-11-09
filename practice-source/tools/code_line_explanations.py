import re
fields={'DisplayName':'顯示名稱','Email':'Email','Session':'場次','Note':'備註'}
def explain(source,kind,week=6):
 rows=[];stack=[];previous=''
 for n,line in enumerate(source.splitlines(),1):
  t=line.strip();why=None
  if not t:why='空白行：分隔不同段落，方便閱讀；不會改變執行結果。'
  elif t=='{':
   block=previous;stack.append(block);why='開始 '+block+' 的內容；大括號決定哪些程式屬於這個範圍。'
  elif t=='}':
   block=stack.pop();why='結束 '+block+' 的範圍；括號要成對，下一段程式應放在正確範圍。'
  elif kind=='handler':
   fixed={
    'using Microsoft.AspNetCore.Mvc;':'引入 MVC 命名空間，讓下方可以直接寫 [BindProperty]；不是安裝套件。',
    'using Microsoft.AspNetCore.Mvc.RazorPages;':'引入 Razor Pages 型別，讓 IndexModel 可以繼承 PageModel。',
    'using System.ComponentModel.DataAnnotations;':'引入 Required、EmailAddress、StringLength 等標註；規則會用到這些名稱。',
    f'namespace {"Week05Registration" if week==5 else "Week06Validation"}.Pages;':'將類別歸在此專案的 Pages 命名空間。這是檔案範圍語法，後面不用再加 namespace 的大括號；需與本週專案一致。',
    'public class IndexModel : PageModel':'宣告可存取的頁面處理類別。冒號表示繼承 PageModel，才能使用 ModelState 等 Razor Pages 功能。',
    '[BindProperty]':'告訴 ASP.NET：「POST 送來的表單，請填進下一行的 Input。」例如送來 Input.DisplayName=小安，OnPost 開始時就能讀到小安。若本例刪掉它又沒有其他接收程式，Input 不會因此自動拿到表單。初次 GET 只是顯示頁面，仍保留這行等 POST 使用。',
    'public RegistrationInput Input { get; set; } = new();':'建立頁面可使用的 Input 屬性，型別是 RegistrationInput。new() 先建立一份空物件，才能讀取裡面的欄位；POST 時再填入學生的資料。public 讓框架可存取，get 允許讀取、set 允許設定，與 HTTP GET／POST 無關。這不是保存資料，每次請求重新建立。',
    'public bool Submitted { get; set; }':'給 Razor 判斷是否顯示摘要的屬性。bool 預設 false，剛開頁面就不會誤顯示「已收到」；get 供畫面讀取，set 供 OnPost 設定。Submitted 是我們自訂的名字，不是框架自動改成 true 的功能。每次請求有新的頁面模型，這個旗標不會保存上次狀態。',
    'public void OnGet() { }':'瀏覽首頁時處理 GET；這裡沒有額外工作，所以方法內容留空。void 表示不回傳值。',
    'public void OnGet() {}':'瀏覽首頁時處理 GET；這裡沒有額外工作，所以方法內容留空。void 表示不回傳值。',
    'public void OnPost()':'表單用 method="post" 送出時，Razor Pages 依命名慣例呼叫這個 public 方法；欄位繫結會先完成。void 表示不回傳值，方法結束後仍會呈現此頁。把設定旗標放在這裡，是為了只在收到 POST 時顯示摘要，而不是初次 GET 就顯示。',
    'if (!ModelState.IsValid)':'! 表示反向：如果繫結或驗證結果有錯誤，就進入這個區塊。這行只讀取先前繫結與驗證的結果，不是開始驗證的指令。少了這個 if 與 return，即使有錯誤也會往下設定成功旗標。',
    'return;':'提早離開這次 OnPost，避免繼續設定成功旗標。此方法是 void，因此寫 return;，不是 return Page();。',
    'Submitted = true;':'將本次請求標示為顯示成功摘要。完成版必須先通過上方閘門；第 02 步尚無閘門，所以有規則仍可能顯示成功。',
    'public class RegistrationInput':'宣告表單資料型別；class 是資料的結構定義，RegistrationInput 是自訂名稱。這一行不會建立物件，也不會建立資料表。',
    'public string? Note { get; set; }':'Note 承接備註。string? 允許 null（沒有值），get/set 可讀寫；不需要先填空字串。能否留白與長度規則還要看驗證標註。'
   }
   why=fixed.get(t)
   if t.startswith('//'):why='這是給讀者看的 C# 註解，不會執行；提醒 Input Model 與 IndexModel 是同一檔案中的兩個同層類別。'
   m=re.fullmatch(r'public string (\w+) \{ get; set; \} = string.Empty;',t)
   if m:
    f=m[1];why=f'{f} 承接「{fields[f]}」。public 讓框架可存取，string 存文字，get 讀取、set 寫入；= string.Empty 將初始值設為空字串，分號結束宣告。空字串不代表已填寫或通過驗證。'
    if f=='Email':why+=' 名叫 Email 不會自動檢查格式；要靠 [EmailAddress]。'
    if f=='Session':why+=' 選單送來的是 option 的 value，本週用文字而非數字。'
   if t.startswith('[Required('):why='要求下方屬性有非空白值；ErrorMessage 是不符合時顯示的中文提示。明寫規則是為了表達必填意圖並指定易懂訊息。本專案的非 nullable string 另有隱含必填，刪掉此標註不代表空白能通過；但會失去自訂中文訊息。'
   if t.startswith('[EmailAddress('):why='檢查下方 Email 的格式；是否必填由 [Required] 負責。此標註不能證明信箱存在或收得到信。'
   if t.startswith('[StringLength('):
    limit=re.search(r'StringLength\((\d+)',t)[1];why=f'限制下方字串最多 {limit} 個 .NET 字串長度單位；ErrorMessage 同步寫上限。這不是必填規則；邊界測試使用英文字母，避免 emoji 計數差異。'
  else:
   if t=='@page':why='宣告這個 .cshtml 是可處理請求的 Razor Page；放在檔案最上方。它不是顯示在畫面上的 HTML。'
   elif t=='@model IndexModel':why='指定此畫面使用 IndexModel。下方的 Model 是這次請求的頁面模型物件，不是 RegistrationInput 類別本身。'
   elif t.startswith('@{ ViewData['):why='Razor 的 C# 區塊：設定頁面標題，由共用 _Layout 讀取，常用於瀏覽器分頁；不是表單欄位。'
   elif t.startswith('<section '):why='開始一個內容區塊。class 是外觀樣式：activity-hero／registration-result 由課程 CSS 定義，mb-4／alert／alert-success 來自 Bootstrap；不負責資料驗證。'
   elif t=='</section>':why='關閉對應的 section 區塊，讓下方內容不再屬於這個區塊。'
   elif t.startswith('<div '):
    if 'asp-validation-summary' in t:why='顯示模型層級錯誤。ModelOnly 不列出欄位錯誤，所以本週通常留白；欄位提示靠各自的 span。text-danger 設定紅字，role="alert" 提供輔助科技語意。'
    elif 'card-body' in t:why='開始卡片內容區；card-body 與 p-4 提供 Bootstrap 的內距，避免表單緊貼邊框。'
    elif 'mb-3' in t:why='把同一欄位的標籤、輸入框、錯誤提示包成一組；mb-3 增加下方間距，屬於排版用途。'
   elif t=='</div>':why='關閉最近尚未結束的 div 容器；縮排幫助你分清是欄位群組還是整張卡片。'
   elif t.startswith('<form '):why='建立送出表單。method="post" 把欄位送到同一頁的 OnPost；novalidate 只略過瀏覽器原生驗證，後端仍檢查。本版不載入 jQuery 驗證；Form Tag Helper 會加入防偽權杖。'
   elif t=='</form>':why='結束表單範圍。送出按鈕與要送出的欄位必須在表單內；不要再套第二層 form。'
   elif t.startswith('<label ') and 'asp-for' not in t:
    target=re.search(r'for="([^"]+)"',t)[1];why=f'label 是給人看的標籤；for="{target}" 對應輸入元件的 id，點標籤即可聚焦。form-label 只控制外觀，不是送出的欄位名稱。'
   elif t.startswith('<label '):
    f=re.search(r'Input\.(\w+)',t)[1];why=f'顯示「{fields[f]}」標籤；asp-for="Input.{f}" 讓 Tag Helper 產生對應輸入框的 for，點標籤就能聚焦欄位。form-label 只控制外觀。'
   elif t.startswith('<input ') and 'asp-for' not in t:
    f=re.search(r'Input\.(\w+)',t)[1];why=f'建立單行輸入框。id 供標籤與畫面辨識；name="Input.{f}" 才是 POST 的欄位名稱。先預留後端路徑，尚未引用不存在的 C# 屬性；form-control 是外觀，input 不需結束標籤。'
   elif t.startswith('<input '):
    f=re.search(r'Input\.(\w+)',t)[1];why=f'單行輸入框。asp-for="Input.{f}" 產生 name、id 與目前值，讓 POST 找到同名屬性；也會依型別／標註產生 type 與驗證屬性。form-control 是 Bootstrap 外觀，input 不需結束標籤。'
   elif t.startswith('<span '):
    f=re.search(r'Input\.(\w+)',t)[1];why=f'顯示 Input.{f} 的驗證錯誤。路徑要與同欄位 asp-for 一致；沒有錯誤時留空。text-danger 將提示顯示成紅字，並不是固定寫死的錯誤。少了這個 span，後端仍會擋下錯誤，但學生在此處看不到原因；它不負責啟動驗證。'
   elif t.startswith('<select '):why='建立場次選單。asp-for="Input.Session" 產生欄位名稱並依目前值選回選項，錯誤後能保留選擇；form-select 控制外觀。'
   elif t.startswith('<option '):
    value=re.search(r'value="(.*?)"',t)[1];why='預設提示的 value 刻意是空字串；未選場次送出空值，後端 [Required] 才能擋下。顯示文字與送出的 value 是兩回事。' if not value else f'顯示並送出「{value}」這個場次值。value 是送到 Input.Session 的內容；本週 [Required] 只檢查有值，尚未驗證值是否屬於合法場次清單。'
   elif t=='</select>':why='結束場次選單；所有 option 都放在 select 裡。'
   elif t.startswith('<textarea '):why='多行備註欄位。asp-for 對到 Input.Note；rows="3" 設定可見高度，不是最多三行或長度限制。需要成對的結束標籤，100 字上限在後端。'
   elif t.startswith('<button '):why='type="submit" 讓按鈕送出所在表單；btn 與 btn-primary 只決定外觀。按下後仍必須由後端決定能否成功。'
   elif t=='@if (Model.Submitted)':why='Razor 在伺服器檢查這次請求的成功旗標，只有 true 才輸出下方摘要；不是瀏覽器 JavaScript，也不代表資料已保存。'
   elif t.startswith('<dl '):why='開始名稱／值對照的摘要列表；dt 寫欄位名稱、dd 寫資料。mb-3 增加下方間距。'
   elif t=='</dl>':why='結束摘要的名稱／值列表。'
   elif t.startswith('<dt>'):why='摘要中的欄位名稱，例如參加者或 Email；只是閱讀標籤，不會再送出一份表單資料。'
   elif t.startswith('<dd>@Model.Input.'):
    f=re.search(r'Input\.(\w+)',t)[1];why=f'用 Razor 的 @ 讀取 Model.Input.{f}，輸出這次送來的{fields[f]}。預設會做 HTML 編碼；這是顯示資料，不是新增輸入框或寫入資料庫。'
   elif t.startswith('<dd>@('):why='先判斷備註是否為 null、空字串或純空白；? 左側條件成立就顯示「無」，否則顯示 Input.Note。@(...) 把完整 C# 運算式的結果輸出到摘要。'
   elif t.startswith('<h1>'):why='活動的主要標題。h1 表達內容層級，標題文字本身不參與資料繫結。'
   elif t.startswith('<h2 '):why='區塊的次標題：表單區或成功摘要。h4 類別只調整字體外觀，HTML 語意仍然是 h2。'
   elif t.startswith('<p '):
    if '<strong>' in t:why='顯示課程限制提醒；strong 強調重點，mb-0 移除段落下方間距。這段文字不會執行驗證或儲存資料。'
    elif 'text-uppercase' in t:why='顯示活動分類；fw-bold 設粗體、mb-2 設下方間距，text-uppercase 對英文字母轉大寫，對中文字不會產生大小寫變化。'
    else:why='顯示給使用者看的操作說明；lead 調整導讀文字外觀，mb-0 去掉下方間距，不影響表單送出。'
  if kind=='form' and 'maxlength="200"' in t:why+=' maxlength="200" 明訂瀏覽器最多輸入 200 字，讓教學能送出 21／101 字；後端仍按 20／100 字拒絕，novalidate 不會取消 maxlength。'
  if kind=='form' and t.startswith('<section ') and 'card shadow-sm' in t:why='開始表單卡片區塊；card 與 shadow-sm 是 Bootstrap 的卡片與淡陰影樣式。section 表示內容分區，不是驗證規則。'
  if kind=='form' and t.startswith('<section ') and 'role="status"' in t:why='開始成功摘要區。alert／alert-success 是 Bootstrap 的成功樣式，registration-result 是課程自訂樣式；role="status" 提供輔助科技狀態語意。是否顯示由上方 @if 決定，並不是 class 決定成功。'
  if week==5:
   if t=='Submitted = true;':why='把本次請求的摘要旗標改成 true；這行不負責把資料放進 Input，因為繫結已先完成。下一步的 @if (Model.Submitted) 讀到 true 才輸出摘要；若刪除此行，Input 仍可能接到值，但摘要不會顯示。本週尚未驗證或保存資料。'
   if t.startswith('<form '):why='開始表單。method="post" 指定用 POST 送回同一頁；第 05 步加入 OnPost 後才有本週的處理邏輯。保留 _ViewImports 的 Tag Helpers，框架會加入防偽權杖。'
   if t.startswith('<option '):
    value=re.search(r'value="(.*?)"',t)[1];why='預設提示的 value 為空字串：未選場次就送空值。第五週尚未用必填規則阻擋，驗證留到第六週。' if not value else f'選到這項時送出 value「{value}」。標籤內的文字給人看，value 給後端；練習更換場次時要兩者一起改。'
   if t.startswith('<select ') and 'asp-for' not in t:why='建立場次下拉選單。id="session" 與 label 的 for 相連；name="Input.Session" 是送往後端的欄位名稱。form-select 只控制樣式。'
   if t.startswith('<textarea '):why=('建立多行備註。asp-for 指向 Input.Note，產生欄位名稱與目前內容。' if 'asp-for' in t else '建立多行備註。id 與 label 相連；name="Input.Note" 指定送出欄位名稱。')+'rows="3" 只決定可見高度，不是字數限制。textarea 需要結束標籤；本週尚未限制備註長度。'
   if t.startswith('<button '):why='type="submit" 讓按鈕送出所在表單，觸發後端的 POST 處理；btn／btn-primary 是外觀。看到摘要不代表已驗證或存入資料庫。'
   if t.startswith('<div ') and 'mb-3' in t:why='把一個欄位的標籤與輸入元件放成一組；mb-3 留出下方間距，方便分辨各欄位。這個容器不負責繫結資料。'
   if t.startswith('public string Email '):why+=' 本週先接收文字，Email 格式驗證留到第六週。'
  if why is None:raise ValueError((kind,n,t))
  rows.append({'line':n,'code':line,'why':why})
  if t:previous=t
 return rows
