import asyncio, sys
sys.path.insert(0,'/home/claude/story')
from chars import *
from playwright.async_api import async_playwright
ICON='file:///home/claude/story/icon.png'
FONT=f"""@font-face{{font-family:'Inter Tight';src:url('file:///root/.fonts/InterTight.ttf');font-weight:100 900}}
@font-face{{font-family:BVP;src:url(file:///root/.fonts/BeVietnamPro-Medium.ttf);font-weight:500}}
@font-face{{font-family:BVP;src:url(file:///root/.fonts/BeVietnamPro-Bold.ttf);font-weight:700}}
@font-face{{font-family:Anton;src:url(file:///root/.fonts/Anton-Regular.ttf)}}
body{{margin:0}} *{{box-sizing:border-box}}"""
def news_story(acc, label, big, sub, body_rows, cta, extra=''):
    rows=''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:22px 0;border-bottom:2px solid #EEE;font-size:40px;font-weight:700"><span>{a}</span><span style="color:{c}">{b}</span></div>' for a,b,c in body_rows)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT}</style></head><body>
<div style="width:1080px;height:1920px;background:#fff;font-family:'Inter Tight';color:#111;padding:260px 80px 0;position:relative">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="border:3px solid {acc};color:{acc};border-radius:999px;padding:10px 32px;font-weight:600;font-size:34px">@MarketPulse.Vn</div><img src="{ICON}" style="width:84px;height:84px;border-radius:20px"></div>
<div style="margin-top:70px;background:{acc};color:#fff;display:inline-block;padding:14px 28px;border-radius:14px;font-weight:800;font-size:38px;letter-spacing:1px">{label}</div>
<div style="margin-top:40px;font-weight:800;font-size:150px;letter-spacing:-6px;line-height:.95;color:{acc}">{big}</div>
<div style="margin-top:24px;font-weight:700;font-size:52px;line-height:1.2">{sub}</div>
<div style="margin-top:50px">{rows}</div>{extra}
<div style="position:absolute;left:80px;right:80px;bottom:380px;border:4px dashed {acc};border-radius:28px;padding:30px;text-align:center;font-weight:700;font-size:40px;color:{acc}">{cta}</div>
<div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center;font-size:26px;color:#8A8A92">Nguồn: SSI · Không phải khuyến nghị đầu tư</div>
</div></body></html>'''
R='#D93025'; G='#16A34A'
A=news_story('#E85D00','📉 THỊ TRƯỜNG PHIÊN 19/11','1.689,62','VN-Index <span style="color:#D93025">−13,39 điểm (−0,79%)</span><br>Phiên giảm thứ 3 liên tiếp, thủng mốc 1.700',
  [('VN30','−1,00%',R),('FPT','−2,66%',R),('VIC','−2,04%',R),('VNM','−1,73%',R)],'👆 Xem đầy đủ trong bài mới nhất')
B=news_story('#1D5FD1','💼 DOANH NGHIỆP SÁNG NAY','FPT','Doanh thu giảm 20%,<br>lợi nhuận cổ đông mẹ vẫn tăng gần 12%',
  [('Doanh thu thuần Q3','−20,1%',R),('LN cổ đông mẹ Q3','+11,8%',G),('P/E hiện tại','≈ 8,6 lần','#111')],'👆 Xem phân tích đầy đủ<br>trong bài mới nhất')
# C: Chuyện F0 comic
CSSC=CSS.replace('.page{','.pagex{')
C=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div style="width:1080px;height:1920px;background:{CREAM};font-family:BVP;color:{INK};padding:260px 70px 0;position:relative;overflow:hidden">
<div style="display:flex;justify-content:space-between;align-items:center"><div class="tag" style="font-size:30px">CHUYỆN F0 · TẬP 1</div><div class="brand"><img src="{ICON}">marketpulse.vn</div></div>
<div class="h1" style="margin-top:60px;font-size:128px">THÁNG ĐẦU<br>LÃI <span style="color:{GRN}">30%</span>, TÔI<br>TƯỞNG MÌNH LÀ<br><span style="color:{PUR}">THIÊN TÀI</span></div>
<div style="position:absolute;left:40px;top:880px">{hung('cool',True,1.45)}</div>
<div style="position:absolute;right:60px;top:1030px;transform:rotate(5deg);width:440px;background:#fff;border:6px solid {INK};border-radius:36px;overflow:hidden"><div style="background:{INK};color:#fff;padding:16px 24px;font-size:22px;font-weight:700">📱 Tài khoản chứng khoán</div><div style="padding:24px 28px"><div style="font-size:22px;color:#6B6375">Tổng tài sản</div><div style="font-family:Anton;font-size:62px">65.000.000đ</div><div style="display:inline-block;margin-top:8px;background:{GRN};color:#fff;font-weight:700;font-size:28px;padding:8px 16px;border-radius:12px">▲ +30% trong 3 tuần</div></div></div>
<div style="position:absolute;left:70px;right:70px;bottom:380px;border:4px dashed {PUR};border-radius:28px;padding:28px;text-align:center;font-weight:700;font-size:38px;color:{PUR};background:#fff">👆 Đọc trọn câu chuyện<br>trong bài mới nhất</div>
<div style="position:absolute;left:70px;right:70px;bottom:300px;text-align:center;font-size:26px;color:#8A8A92">Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div>
</div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        g=await b.new_page(viewport={'width':1080,'height':1920})
        for n,h in (('story_chieu',A),('story_sang',B),('story_f0',C)):
            fn=f'/home/claude/stories/{n}.html'; open(fn,'w').write(h)
            await g.goto('file://'+fn); await g.wait_for_timeout(300)
            await g.screenshot(path=f'/home/claude/stories/{n}.png')
        await b.close()
asyncio.run(main())
