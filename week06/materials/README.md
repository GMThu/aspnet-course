# 第六週｜收到不等於接受

從第五週可 POST 的報名表接續，先理解 RegistrationInput，再加入 DataAnnotations、ModelState 與三路測試。

## 起跑條件
- 第五週專案能啟動，表單能送出並顯示摘要。
- 若尚未完成，可用本包的 `Week05-recovery-handler.txt` 對照補齊。

## 三輪實作
1. 畫出 Input Model：分清 PageModel、Input Model、屬性與型別。
2. 加入驗證：Required、EmailAddress、StringLength、ModelState 與 validation-for。
3. 測試證據：空白、Email=abc、合法假資料，再測 20／21 字邊界。

> 完成仍不代表資料已保存；本週沒有資料庫。
