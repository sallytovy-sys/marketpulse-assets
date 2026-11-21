# QUY TRÌNH VẬN HÀNH MARKETPULSE (OPS) – Sally chốt 21/11/2026

Đọc cùng RULES.md (thiết kế, nội dung). File này nói **làm thế nào và khi nào**.

## 0. Nguyên tắc lưu trữ và Buffer
- Bài được chuẩn bị TRƯỚC và lưu trong repo này (thư mục theo ngày). Repo là kho bài; Sally xem trước ở đây.
- **Buffer chỉ nhận bài đúng lúc đăng** (mode=shareNow). KHÔNG hẹn giờ trước trên Buffer, không để bài chờ (gói Free, giới hạn 10 bài chờ). Story: đợi 5 phút sau bài feed rồi shareNow.
- Ngoại lệ duy nhất: không có.
- Mỗi bài chỉ đăng 1 lần trên mỗi kênh. Lỗi (kể cả Instagram "flagged as potential spam", "unknown error") thì KHÔNG đăng lại, báo Sally.

## 1. Cấu trúc thư mục một bài ("bài sẵn sàng")
`<YYYY-MM-DD>/<slot>/` với slot ∈ sang, chieu (ảnh nằm ngay `<YYYY-MM-DD>/` cho bài chiều), toi, nen, pa. Bài sẵn sàng khi có đủ:
- ảnh slide (`mp_*.png`), `story.jpg`, `caption_ig.txt`, `caption_fb.txt`, file dữ liệu (`data.json` / `data_phien.json`) và `story.json`.
- Chuyện F0: ảnh trong `chuyen-f0/tap<N>/` (tap<N>_1..6.png, story.jpg), caption và altText trong `chuyen-f0/queue.json`.

## 2. Thiết lập chung (mọi phiên)
1. add_repo owner=sallytovy-sys repo=marketpulse-assets access=push; `git clone --depth 1 https://github.com/sallytovy-sys/marketpulse-assets /home/claude/marketpulse-assets` (timeout dài). Đọc RULES.md và OPS.md.
2. Font (khi cần dựng ảnh): `mkdir -p ~/.fonts && cd ~/.fonts && curl -sSLf -o InterTight.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/intertight/InterTight%5Bwght%5D.ttf" && curl -sSLf -o BeVietnamPro-Bold.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/bevietnampro/BeVietnamPro-Bold.ttf" && fc-cache -f`.
3. Push: commit (kết thúc message bằng "Co-Authored-By: Claude <noreply@anthropic.com>"), `git -c push.negotiate=true push origin main`; bị từ chối thì `git fetch --depth=50 origin main:refs/remotes/origin/main && git rebase origin/main` rồi push lại.
4. Buffer: organizationId 654ca3e8e1ed273c76333fd9; Instagram channelId 6afd869dece6dfde5f0963f4 (marketpulse.vn), Facebook channelId 6afd8e12ece6dfde5f09b740 (MarketPulse.Vn). Kiểm tra lại bằng list_channels nếu lỗi.

## 3. THỦ TỤC ĐĂNG (dùng cho mọi slot)
1. Kiểm tra trùng: list_posts hôm nay, tìm bài có tiêu đề slot (VD "DOANH NGHIỆP SÁNG NAY", "CHUYỆN F0 · TẬP N", "THỊ TRƯỜNG PHIÊN", "TIN NÓNG TỐI NAY", "HỌC NẾN NHẬT", "PRICE ACTION"). Đã có trên kênh nào thì không đăng lại kênh đó.
2. Kiểm tra mọi link ảnh `https://raw.githubusercontent.com/sallytovy-sys/marketpulse-assets/main/<đường dẫn>` trả HTTP 200 (404 thì chờ 3 phút, thử tối đa 3 lần; vẫn lỗi thì báo, không đăng).
3. Bài feed, cả 2 kênh: create_post mode=shareNow, schedulingType=automatic, ảnh theo thứ tự (url + altText), text = caption_ig.txt (Instagram) / caption_fb.txt (Facebook) NGUYÊN VĂN. Instagram metadata {"instagram":{"type":"post","shouldShareToFeed":true}}; Facebook {"facebook":{"type":"post"}}. Sau ~30 giây get_post xác nhận "sent".
4. `sleep 300` (5 phút), rồi story ở các kênh có bài feed "sent": create_post mode=shareNow, không text, ảnh story.jpg; Instagram {"instagram":{"type":"story","shouldShareToFeed":false}}; Facebook {"facebook":{"type":"story"}}. get_post xác nhận.
5. Bài lỗi ở kênh nào: không đăng lại, không đăng story kênh đó, báo Sally.

## 4. Lịch
| Giờ | Ngày | Việc | Slot |
|---|---|---|---|
| 7:43 | T2–T6 | ĐĂNG bài sáng đã chuẩn bị (thiếu thì dựng gấp theo §5.1 rồi đăng) | sang |
| 8:43 | T7–CN | ĐĂNG bài nến (thiếu thì dựng gấp §5.4) | nen |
| 11:43 | Hằng ngày | ĐĂNG Chuyện F0 theo queue.json | F0 |
| 16:03 | T7–CN | ĐĂNG bài price action (thiếu thì dựng gấp §5.4) | pa |
| 16:05 | T2–T6 | DỰNG + ĐĂNG bài phiên (dữ liệu chỉ có sau giờ đóng cửa) | chieu |
| 17:47 | Hằng ngày | CHUẨN BỊ tin tối hôm nay (§5.3), không đụng Buffer | toi |
| 18:58 | Hằng ngày | ĐĂNG tin tối đã chuẩn bị | toi |
| 20:43 | CN–T5 | CHUẨN BỊ bài sáng của phiên kế tiếp (§5.1), không đụng Buffer | sang |
| 20:13 | T6 | CHUẨN BỊ 4 bài kỹ thuật T7 + CN (§5.4), không đụng Buffer | nen, pa |
Mỗi lần CHUẨN BỊ xong: báo Sally (tiêu đề, nội dung chính, đường dẫn thư mục) để Sally xem trước; Sally muốn sửa thì sửa trong repo trước giờ đăng.

## 5. Cách dựng từng loại bài
### 5.1 Bài sáng "💼 DOANH NGHIỆP SÁNG NAY" (XANH DƯƠNG, `tools/render.py --kind sang`)
- Chủ đề theo thứ của NGÀY ĐĂNG: T2 lịch sự kiện tuần (marketdata_list_corporate_actions, 3–5 DN); T3 soi lợi nhuận quý gần nhất (fundamental_list_income_summary); T4 định giá (fundamental_list_financial_ratios, fundamental_list_valuation_history); T5 sức khỏe tài chính (balance sheet, cash flow, ratios); T6 so sánh cùng ngành (research_list_ssi100_stocks + ratios).
- 1 mã VN30/SSI100, ưu tiên mã nóng phiên gần nhất (top_stocks, daily_stock_infor) hoặc vừa ra BCTC; không lặp mã đã làm trong 10 ngày (xem */sang/data.json).
- Đọc số: length_report 1–4 quý, 5 cả năm, 6/9 lũy kế; ROE/biên là phân số, quý là TTM; tự tính lại mọi %. Điểm SSI Research là thứ hạng tương đối, ghi "không phải khuyến nghị". Không giá mục tiêu, không "nên mua", không suy đoán nguyên nhân dữ liệu không nêu.
- data.json theo tools/examples/morning_FPT.json (4 slide, "kind":"sang", source BCTC quý). Chạy `python3 tools/render.py <data.json> <YYYY-MM-DD>/sang --kind sang`; xóa *.html; mở ảnh 1 kiểm tra màu xanh dương, không tràn.
- story.json theo tools/examples/story_sang_FPT.json → `python3 tools/story.py <story.json> <YYYY-MM-DD>/sang/story.jpg --kind sang`.
- Caption (lưu caption_ig.txt / caption_fb.txt): "💼 DOANH NGHIỆP SÁNG NAY: <MÃ>" (FB thêm " – <TIÊU ĐỀ IN HOA>") · hook · 📊 3 gạch số liệu · 🔎 Điểm đáng chú ý · 📉/📈 định giá/chỉ số · ⭐ điểm SSI Research · 👉 "Vuốt để xem chi tiết 4 biểu đồ." (FB "Xem chi tiết trong 4 hình.") · 💬 câu hỏi · 🔔 Theo dõi @marketpulse.vn (FB MarketPulse.Vn) · 📊 Nguồn: SSI · BCTC quý X/2026 | Nội dung chỉ mang tính thông tin, không phải khuyến nghị đầu tư. · #<MÃ> #chungkhoan #baocaotaichinh #phantichcoban #dautu #marketpulse.
- Chuẩn bị tối hôm trước dùng dữ liệu phiên vừa đóng cửa; ghi rõ "phiên DD/MM" khi nhắc giá.

### 5.2 Bài chiều "📉📈 THỊ TRƯỜNG PHIÊN" (CAM, `tools/render.py --kind chieu`)
- Dữ liệu SSI hôm nay: VNINDEX, VN30 (index_daily_data, includeToday); không có dòng hôm nay thì chờ 20 phút, thử tối đa 2 lần, vẫn không có thì DỪNG, báo "Không có dữ liệu phiên hôm nay". Đếm chuỗi phiên tăng/giảm liên tiếp từng phiên trước khi viết "N phiên liên tiếp".
- top_stocks (HOSE, topbytradingamount, range=1d, toDate=hôm nay, limit=24); daily_stock_infor tuần tự 8–10 mã lớn (net_buy_sell_value = khối ngoại ròng).
- data_phien.json theo tools/examples/afternoon_1811.json (4 slide: tổng quan + trụ; 5 mã tăng mạnh; 5 mã giảm mạnh; khối ngoại "tính trên các mã lớn marketpulse theo dõi"). `python3 tools/render.py <data_phien.json> <YYYY-MM-DD> --kind chieu`; kiểm tra màu cam.
- story.json theo tools/examples/story_chieu_1911.json → `tools/story.py ... <YYYY-MM-DD>/story.jpg --kind chieu`.
- Caption: "📉/📈 THỊ TRƯỜNG PHIÊN DD/MM: <TIÊU ĐỀ IN HOA>" · đoạn chỉ số · đoạn độ rộng/trụ · đoạn khối ngoại · 👉 Vuốt để xem đầy đủ… (FB "Xem đầy đủ trong 4 hình: …") · 💬 · 🔔 · 📊 Nguồn: SSI | … · #chungkhoan #vnindex #thitruongchungkhoan #khoingoai #dautu #marketpulse. Lưu caption_ig.txt/caption_fb.txt trong `<YYYY-MM-DD>/`, rồi ĐĂNG ngay (§3).

### 5.3 Tin tối "🔥 TIN NÓNG TỐI NAY" (ĐỎ trên nền tối, `tools/render_toi.py`)
- Tìm tin 24–48 giờ (WebSearch/WebFetch các báo tài chính chính thống + SSI company_news): mã/DN được nhắc nhiều nhất; câu chuyện DN/lãnh đạo; giao dịch nội bộ/cổ đông lớn ĐÃ ĐĂNG KÝ còn trong thời gian thực hiện; sự kiện ảnh hưởng giá. Mở bài gốc xác minh từng số, tên, chức vụ, thời gian. Vụ án/tranh chấp chỉ nêu đúng như cơ quan chức năng/DN công bố ("theo …"). Không tin đồn, không suy đoán, không khuyến nghị. Không lặp câu chuyện chính của 3 ngày gần nhất trừ khi có diễn biến mới.
- `<YYYY-MM-DD>/toi/data.json` theo tools/examples/toi_2111.json (cover / timeline / table / deals [/ deals]). `python3 tools/render_toi.py <data.json> <YYYY-MM-DD>/toi`; overflow True thì rút gọn. story.json theo tools/examples/story_toi_2111.json → `tools/story.py ... --kind toi`.
- Caption theo mẫu 2026-11-21/toi/caption_ig.txt và caption_fb.txt.
- Không chắc thông tin → không dùng tin đó; không đủ tin chắc chắn → báo Sally, không đăng.

### 5.4 Kỹ thuật cuối tuần (XANH NGỌC, `tools/render_ta.py`)
- Bài tiếp theo trong tools/ta_curriculum.json (nen / pa) chưa có trong done; thêm "<YYYY-MM-DD>: <tên>" vào done khi chuẩn bị xong.
- Ví dụ THẬT từ SSI (VNINDEX/VN30 hoặc mã VN30, 3–6 tháng), kiểm tra điều kiện bằng script Python trên OHLC; nêu diễn biến sau đó kể cả khi tín hiệu thất bại.
- data.json theo tools/examples/nen_2211.json hoặc pa_2111.json (5 slide). `python3 tools/render_ta.py <data.json> <YYYY-MM-DD>/<nen|pa>`. story.json theo tools/examples/story_ta_pa.json ("series" nen/pa) → `tools/story.py ... --kind ta`.
- Caption theo mẫu 2026-11-22/nen/caption_*.txt và 2026-11-21/pa/caption_*.txt.

### 5.5 Chuyện F0
- Chỉ đăng tập trong chuyen-f0/queue.json có date = hôm nay, status = pending; caption ig/fb và alt lấy nguyên văn; story là chuyen-f0/tap<N>/story.jpg (thiếu thì `tools/story.py chuyen-f0/tap<N>/tap<N>_1.png chuyen-f0/tap<N>/story.jpg --kind f0`). Đăng xong đổi status = posted, push.
- Không tự viết tập mới. Hàng chờ còn ≤ 2 ngày thì nhắc Sally duyệt tập mới.
