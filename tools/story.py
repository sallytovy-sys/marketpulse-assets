#!/usr/bin/env python3
"""MarketPulse story renderer (1080x1920) - thiet ke story da duyet 19/11/2026.
  Bai sang/chieu:  python3 tools/story.py <story.json> <out.jpg> --kind sang|chieu
    story.json: {"big":"FPT", "sub":"Doanh thu giam 20%,<br>loi nhuan ...",
                 "rows":[["Doanh thu thuan Q3","-20,1%","down"],["LN co dong me","+11,8%","up"],["P/E","8,6 lan","flat"]],
                 "date":"19/11"}   (rows: 3-4 dong; label tu dong theo kind)
  Tin toi:         python3 tools/story.py <story.json> <out.jpg> --kind toi  (json: date, big, sub, rows)
  Chuyen F0:       python3 tools/story.py <tapN_1.png> <out.jpg> --kind f0
Mau KHOA theo kind: sang=#1D5FD1, chieu=#E85D00 (khong doc accent tu data).
"""
import sys, os, json, asyncio, base64, io
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__)); FD=os.path.expanduser('~/.fonts')
COLORS={'sang':'#1D5FD1','chieu':'#E85D00'}
CTA={'toi':'👆 Xem đầy đủ trong bài mới nhất','sang':'👆 Xem phân tích đầy đủ<br>trong bài mới nhất','chieu':'👆 Xem đầy đủ trong bài mới nhất','f0':'👆 Đọc trọn câu chuyện<br>trong bài mới nhất'}
RC={'up':'#16A34A','down':'#D93025','flat':'#111'}
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
FONT=f"""@font-face{{font-family:'Inter Tight';src:url('file://{FD}/InterTight.ttf');font-weight:100 900}}
@font-face{{font-family:BVP;src:url(file://{FD}/BeVietnamPro-Bold.ttf);font-weight:700}}
body{{margin:0}} *{{box-sizing:border-box}}"""
ICON='data:image/png;base64,'+b64(os.path.join(HERE,'icon.png'))
def news(kind,d):
    acc=COLORS[kind]
    label=d.get('label') or ('💼 DOANH NGHIỆP SÁNG NAY' if kind=='sang' else f"{d.get('emoji','📉')} THỊ TRƯỜNG PHIÊN {d['date']}")
    rows=''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:22px 0;border-bottom:2px solid #EEE;font-size:40px;font-weight:700"><span>{a}</span><span style="color:{RC.get(c,c)}">{b}</span></div>' for a,b,c in d['rows'])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT}</style></head><body>
<div style="width:1080px;height:1920px;background:#fff;font-family:'Inter Tight';color:#111;padding:260px 80px 0;position:relative">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="border:3px solid {acc};color:{acc};border-radius:999px;padding:10px 32px;font-weight:600;font-size:34px">@MarketPulse.Vn</div><img src="{ICON}" style="width:84px;height:84px;border-radius:20px"></div>
<div style="margin-top:70px;background:{acc};color:#fff;display:inline-block;padding:14px 28px;border-radius:14px;font-weight:800;font-size:38px;letter-spacing:1px">{label}</div>
<div id="big" style="margin-top:40px;font-weight:800;font-size:150px;letter-spacing:-6px;line-height:.95;color:{acc};white-space:nowrap">{d['big']}</div>
<div style="margin-top:24px;font-weight:700;font-size:52px;line-height:1.2">{d['sub']}</div>
<div style="margin-top:50px">{rows}</div>
<div style="position:absolute;left:80px;right:80px;bottom:380px;border:4px dashed {acc};border-radius:28px;padding:30px;text-align:center;font-weight:700;font-size:40px;color:{acc}">{CTA[kind]}</div>
<div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center;font-size:26px;color:#8A8A92">Nguồn: SSI · Không phải khuyến nghị đầu tư</div>
</div><script>const b=document.getElementById('big');let s=150;while(b.scrollWidth>920&&s>70){{s-=6;b.style.fontSize=s+'px'}}</script></body></html>'''
def toi(d):
    acc='#E5484D'
    rows=''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:22px 0;border-bottom:2px solid #262A33;font-size:40px;font-weight:700"><span>{a}</span><span style="color:{ {"up":"#22C55E","down":acc}.get(c,"#fff") }">{b}</span></div>' for a,b,c in d['rows'])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT}</style></head><body>
<div style="width:1080px;height:1920px;background:#0F1115;font-family:'Inter Tight';color:#fff;padding:260px 80px 0;position:relative">
<div style="display:flex;justify-content:space-between;align-items:center"><div style="border:3px solid {acc};color:{acc};border-radius:999px;padding:10px 32px;font-weight:600;font-size:34px">@MarketPulse.Vn</div><img src="{ICON}" style="width:84px;height:84px;border-radius:20px"></div>
<div style="margin-top:70px;background:{acc};color:#fff;display:inline-block;padding:14px 28px;border-radius:14px;font-weight:800;font-size:38px;letter-spacing:1px">🔥 TIN NÓNG TỐI NAY · {d['date']}</div>
<div id="big" style="margin-top:40px;font-weight:800;font-size:150px;letter-spacing:-6px;line-height:.95;color:{acc};white-space:nowrap">{d['big']}</div>
<div style="margin-top:24px;font-weight:700;font-size:52px;line-height:1.2">{d['sub']}</div>
<div style="margin-top:50px">{rows}</div>
<div style="position:absolute;left:80px;right:80px;bottom:380px;border:4px dashed {acc};border-radius:28px;padding:30px;text-align:center;font-weight:700;font-size:40px;color:{acc}">{CTA['toi']}</div>
<div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center;font-size:26px;color:#9AA0AA">Tổng hợp từ thông tin công bố · Không phải khuyến nghị đầu tư</div>
</div><script>const b=document.getElementById('big');let s=150;while(b.scrollWidth>920&&s>70){{s-=6;b.style.fontSize=s+'px'}}</script></body></html>'''
def f0(cover):
    im=Image.open(cover).convert('RGB'); bg=im.getpixel((20,20))
    crop=im.crop((0,0,1080,1290)); crop=crop.resize((972,1161),Image.LANCZOS)
    buf=io.BytesIO(); crop.save(buf,'PNG'); src='data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
    hexbg='#%02x%02x%02x'%bg
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT}</style></head><body>
<div style="width:1080px;height:1920px;background:{hexbg};font-family:BVP;position:relative;overflow:hidden">
<img src="{src}" style="position:absolute;left:54px;top:230px;width:972px">
<div style="position:absolute;left:70px;right:70px;bottom:380px;border:4px dashed #6A4CF5;border-radius:28px;padding:28px;text-align:center;font-weight:700;font-size:38px;color:#6A4CF5;background:#fff">{CTA['f0']}</div>
<div style="position:absolute;left:70px;right:70px;bottom:300px;text-align:center;font-size:26px;color:#8A8A92">Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div>
</div></body></html>'''
async def shot(html,out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        ex='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None
        b=await p.chromium.launch(executable_path=ex,args=['--no-sandbox'])
        g=await b.new_page(viewport={'width':1080,'height':1920})
        tmp=out+'.html'; open(tmp,'w').write(html)
        await g.goto('file://'+os.path.abspath(tmp)); await g.wait_for_timeout(500)
        png=out.rsplit('.',1)[0]+'.png'; await g.screenshot(path=png); await b.close(); os.remove(tmp)
    Image.open(png).convert('RGB').save(out,quality=92)
if __name__=='__main__':
    a=sys.argv
    if '--kind' not in a: sys.exit('Thieu --kind sang|chieu|f0')
    kind=a[a.index('--kind')+1]; src,out=a[1],a[2]
    if kind not in ('sang','chieu','f0','toi'): sys.exit('kind sai')
    html=f0(src) if kind=='f0' else (toi(json.load(open(src))) if kind=='toi' else news(kind,json.load(open(src))))
    asyncio.run(shot(html,out)); print('OK',out)
