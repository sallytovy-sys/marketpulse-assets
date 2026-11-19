import json,sys,asyncio,html,os
HERE=os.path.dirname(os.path.abspath(__file__))
ICON=os.path.join(HERE,'icon.png')
FONT=os.path.expanduser('~/.fonts/InterTight.ttf')
from playwright.async_api import async_playwright
# Usage: python3 render.py <data.json> <out_dir> --kind sang|chieu
# MÀU CỐ ĐỊNH THEO LOẠI BÀI (không lấy từ data.json):
#   sang  = Doanh nghiệp sáng nay 7h45  -> xanh dương #1D5FD1
#   chieu = Thị trường phiên 16h05     -> cam #E85D00
COLORS={'sang':'#1D5FD1','chieu':'#E85D00'}
args=[a for a in sys.argv[1:] if not a.startswith('--kind')]
kind=None
for i,a in enumerate(sys.argv):
    if a.startswith('--kind='): kind=a.split('=',1)[1]
    elif a=='--kind' and i+1<len(sys.argv): kind=sys.argv[i+1]
if kind in COLORS: args=[a for a in args if a!=kind]
if kind not in COLORS: sys.exit('Thiếu hoặc sai --kind (sang|chieu). sang = xanh dương, chieu = cam.')
D=json.load(open(args[0])); OUT=os.path.abspath(args[1] if len(args)>1 else '.')
D['accent']=COLORS[kind]
ACC=D.get('accent','#E85D00')
def bars(rows):
    mx=max(abs(r['val']) for r in rows) or 1; out=''
    for i,r in enumerate(rows):
        w=max(4,100*abs(r['val'])/mx); c=ACC if i==0 else '#B9B9C1'
        out+=f'''<div style="display:flex;align-items:center;gap:20px;height:54px">
<div style="width:150px;text-align:right"><div style="font-weight:800;font-size:28px;line-height:1.1">{r['sym']}</div><div style="font-weight:500;font-size:17px;color:#6B6B73;line-height:1.2">{r.get('sub','')}</div></div>
<div style="flex:1"><div style="width:{w:.0f}%;height:38px;background:{c}"></div></div>
<div style="width:170px;font-weight:800;font-size:34px;letter-spacing:-1px">{r['label']}</div></div>'''
    return out
def page(s):
    return f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Inter Tight';src:url('file://{FONT}');font-weight:100 900}}
body{{margin:0}}</style></head><body>
<div style="width:1080px;height:1080px;box-sizing:border-box;padding:52px 72px 44px;background:#FFFFFF;color:#111111;font-family:'Inter Tight',Arial,sans-serif;display:flex;flex-direction:column;overflow:hidden">
<div style="display:flex;justify-content:center;margin-bottom:24px"><div style="border:2px solid {ACC};color:{ACC};border-radius:999px;padding:6px 26px;font-weight:500;font-size:26px">@MarketPulse.Vn</div></div>
<div style="font-weight:800;font-size:{s.get('hsize',82)}px;line-height:0.98;letter-spacing:-3px;color:{ACC};margin-bottom:20px">{s['headline']}</div>
<div style="font-weight:500;font-size:30px;line-height:1.4;letter-spacing:-0.5px;margin-bottom:28px">{s['body']}</div>
<div style="font-weight:800;font-size:30px;letter-spacing:-0.5px">{s['chart_title']}</div>
<div style="font-weight:500;font-size:20px;color:#6B6B73;margin:2px 0 16px">{s['chart_sub']}</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1">{bars(s['rows'])}</div>
<div style="display:flex;align-items:flex-end;justify-content:space-between;font-weight:500;font-size:18px;color:#6B6B73">
<div style="display:flex;align-items:center;gap:14px"><img src="file://{ICON}" style="width:56px;height:56px;border-radius:13px"><div>{D.get('source','Nguồn: SSI · Phiên '+D['date'])}</div></div>
<div>Không phải khuyến nghị đầu tư</div></div>
</div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1080,'height':1080})
        for i,s in enumerate(D['slides'],1):
            fn=f'{OUT}/mp_{D["tag"]}_{i}.html'; open(fn,'w').write(page(s))
            await pg.goto('file://'+fn); await pg.wait_for_timeout(300)
            # auto-shrink headline/body if overflowing
            over=await pg.evaluate("()=>{const r=document.body.firstElementChild;return r.scrollHeight>r.clientHeight}")
            hs=s.get('hsize',82)
            while over and hs>56:
                hs-=4; s['hsize']=hs; open(fn,'w').write(page(s)); await pg.goto('file://'+fn); await pg.wait_for_timeout(150)
                over=await pg.evaluate("()=>{const r=document.body.firstElementChild;return r.scrollHeight>r.clientHeight}")
            await pg.screenshot(path=f'{OUT}/mp_{D["tag"]}_{i}.png')
            print(i,'hsize',hs,'overflow',over)
        await b.close()
asyncio.run(main())
