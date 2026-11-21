# QUY TẮC VẬN HÀNH MARKETPULSE (bắt buộc đọc trước khi dựng ảnh và đăng bài)

Chủ kênh: Sally. Chốt ngày 19/11/2026. Chỉ chủ kênh được thay đổi các quy tắc này.

## 0. Lưu trữ và Buffer (Sally chốt 21/11/2026) – chi tiết trong OPS.md
- Bài được chuẩn bị trước 1–2 ngày (riêng bài phiên chiều và tin tối dựng trong ngày) và lưu trong repo này.
- Buffer chỉ nhận bài đúng lúc đăng (shareNow); KHÔNG hẹn giờ trước trên Buffer. Story đăng 5 phút sau bài feed (đợi rồi shareNow). Giữ gói Buffer Free.

## 1. Thiết kế đã duyệt (KHÓA)
| Giờ | Bài | Màu nhấn | Template | Lệnh dựng |
|---|---|---|---|---|
| 7h45 T2–T6 | Doanh nghiệp sáng nay | XANH DƯƠNG #1D5FD1 | Trắng 1080×1080, Inter Tight, 4 slide | `tools/render.py ... --kind sang` |
| 11h45 hằng ngày | Chuyện F0 | Tím #6A4CF5, nền kem | Truyện tranh 1080×1350, 6 slide | Chỉ đăng tập đã duyệt trong `chuyen-f0/queue.json` |
| 19h00 T2–CN | 🔥 Tin nóng tối nay | ĐỎ #E5484D trên nền tối #0F1115 | 1080×1350, Inter Tight, 4–5 slide (cover / timeline / table / deals) | `tools/render_toi.py <data.json> <thư mục>` (mẫu tools/examples/toi_2111.json) |
| 8h45 T7–CN | 🕯️ Học nến Nhật | XANH NGỌC #0D9488 trên nền trắng | 1080×1350, 5 slide (cover/explain/list/chart/list) | `tools/render_ta.py` series "nen" (mẫu tools/examples/nen_2211.json) |
| 16h05 T7–CN | 📐 Price Action | XANH NGỌC #0D9488 trên nền trắng | 1080×1350, 5 slide | `tools/render_ta.py` series "pa" (mẫu tools/examples/pa_2111.json) |
| 16h05 T2–T6 | Thị trường phiên | CAM #E85D00 | Trắng 1080×1080, Inter Tight, 4 slide | `tools/render.py ... --kind chieu` |

### Story sau mỗi bài (Sally duyệt 19/11/2026)
- Mỗi bài feed (sáng, F0, chiều) có 1 story đăng **5 phút sau** bài feed, lên cả Instagram và Facebook.
- Thiết kế story đã duyệt = "kiểu đầu tiên" 1080×1920: dựng bằng `tools/story.py` (mẫu: `tools/examples/story_*.json`).
  - Sáng: `--kind sang` (xanh dương), Chiều: `--kind chieu` (cam), số liệu lấy đúng từ bài feed cùng ngày.
  - F0: `--kind f0` từ ảnh bìa `tapN_1.png`, lưu `chuyen-f0/tapN/story.jpg`.
- Buffer: Instagram metadata {"instagram":{"type":"story","shouldShareToFeed":false}}, Facebook {"facebook":{"type":"story"}}, không caption.
- ĐĂNG 1 LẦN DUY NHẤT (Sally yêu cầu 20/11/2026): mỗi bài feed và story chỉ create_post 1 lần trên mỗi kênh. Lỗi (kể cả "flagged as potential spam", "unknown error") thì KHÔNG đăng lại, không tạo bài trùng; báo Sally ngay. Bài feed của kênh nào lỗi thì story của kênh đó lưu nháp.

### Tin nóng tối nay (Sally duyệt 21/11/2026)
- Chủ đề: mã/doanh nghiệp được báo tài chính nhắc nhiều nhất trong ngày; câu chuyện doanh nghiệp, lãnh đạo; giao dịch người nội bộ/cổ đông lớn ĐÃ ĐĂNG KÝ nhưng chưa thực hiện; sự kiện ảnh hưởng giá.
- CHỈ dùng thông tin đã công bố chính thức (CBTT HoSE/HNX/UPCoM, cơ quan chức năng, doanh nghiệp) hoặc báo chí chính thống; ghi nguồn trên slide. Vụ án/tranh chấp: chỉ nêu đúng như cơ quan chức năng và doanh nghiệp công bố, ghi rõ "theo ...", không suy đoán, không kết luận thay cơ quan chức năng, không dùng từ xúc phạm. Không đăng tin đồn, không nêu thông tin đời tư không liên quan đến doanh nghiệp.
- Không khuyến nghị mua/bán, không giá mục tiêu. Story: `tools/story.py --kind toi`, đăng 19h05.

### Kỹ thuật cuối tuần (Sally duyệt 21/11/2026)
- T7–CN: 8h45 Học nến Nhật, 16h05 Price Action, story 5 phút sau (`tools/story.py --kind ta`). Thứ tự bài theo tools/ta_curriculum.json.
- Mỗi bài có ví dụ THẬT từ dữ liệu SSI (VN-Index hoặc cổ phiếu VN30), kiểm tra đúng điều kiện mô hình bằng số OHLC; nêu cả kết quả sau đó (kể cả khi tín hiệu thất bại). Kiến thức tham khảo, không khuyến nghị mua/bán, không nói "nên mua/bán".

## 2. Quy tắc thay đổi: PHẢI XÁC NHẬN TRƯỚC KHI TỰ ĐỘNG ĐĂNG
- Mọi thay đổi về thiết kế (màu, font, bố cục, số slide, kích thước), cấu trúc nội dung, mẫu caption, giờ đăng hay kênh đăng
  đều phải được Sally xem bản mẫu và XÁC NHẬN trước. Chưa xác nhận thì lịch tự động vẫn dùng thiết kế đã khóa ở mục 1.
- Lịch tự động KHÔNG được tự ý thay đổi thiết kế. Nếu trong lúc chạy thấy cần làm khác thiết kế đã khóa
  (ví dụ dữ liệu không vừa template, thiếu số liệu phải đổi bố cục, công cụ dựng ảnh lỗi):
  → KHÔNG đăng thẳng. Lưu bài ở dạng NHÁP trong Buffer (saveToDraft=true) và báo rõ lý do để Sally duyệt.
- Trước khi đăng, mở ảnh 1 kiểm tra: đúng màu theo loại bài, chữ không tràn. Sai thì dựng lại; vẫn sai thì lưu nháp và báo.

## 3. Nội dung
- Mọi bài ghi nguồn (SSI) và dòng "Không phải khuyến nghị đầu tư". Không giá mục tiêu, không khuyến nghị mua/bán.
- Chỉ dùng số liệu lấy được, tự tính lại %; không suy đoán nguyên nhân dữ liệu không nêu.
- Chuyện F0: nhân vật hư cấu, ghi "Câu chuyện minh họa"; không tự viết tập mới khi chưa được duyệt.
