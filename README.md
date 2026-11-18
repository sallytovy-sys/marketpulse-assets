# marketpulse-assets
Ảnh post hằng ngày của MarketPulse.Vn (mỗi ngày một thư mục YYYY-MM-DD) và công cụ dựng ảnh.

## Dựng ảnh
1. Font: `mkdir -p ~/.fonts && curl -sSLf -o ~/.fonts/InterTight.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/intertight/InterTight%5Bwght%5D.ttf" && fc-cache -f`
2. Tạo file dữ liệu theo mẫu `tools/sample_data.json` (4 slide: tổng quan, top tăng, top giảm, khối ngoại).
3. `python3 tools/render.py <data.json> <thư mục ra>` (cần playwright + /usr/bin/google-chrome).
Ảnh công khai: `https://raw.githubusercontent.com/sallytovy-sys/marketpulse-assets/main/<YYYY-MM-DD>/<file>.png`
