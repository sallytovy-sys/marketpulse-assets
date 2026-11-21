#!/usr/bin/env python3
"""MarketPulse - KỸ THUẬT CUỐI TUẦN (T7-CN). Nen trang, nhan TEAL #0D9488. 1080x1350.
python3 tools/render_ta.py <data.json> <out_dir>
data: {series:"nen"|"pa", tag, date, source, slides:[...]}
slide types:
 cover   {title, sub, candles:[[o,h,l,c],...]}            (nen minh hoa)
 explain {kicker, headline, candles:[...], points:[...]}  (minh hoa + y chinh)
 chart   {kicker, headline, ohlc:[[date,o,h,l,c],...], hl:[dates], zone:[lo,hi,label], marks:{date:label}, note}
 list    {kicker, headline, items:[...]}
"""
import sys, os, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); FD=os.path.expanduser('~/.fonts')
ACC='#0D9488'; UP='#16A34A'; DN='#DC2626'; INK='#111'; MUTED='#6B7280'
LABEL={'nen':'🕯️ HỌC NẾN NHẬT','pa':'📐 PRICE ACTION'}
ICON='data:image/png;base64,'+base64.b64encode(open(os.path.join(HERE,'icon.png'),'rb').read()).decode()
CSS=f"""@font-face{{font-family:'Inter Tight';src:url('file://{FD}/InterTight.ttf');font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}
.s{{width:1080px;height:1350px;background:#fff;color:{INK};font-family:'Inter Tight';padding:70px 72px;position:relative;overflow:hidden}}
.s:before{{content:'';position:absolute;left:0;top:0;right:0;height:14px;background:{ACC}}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.tag{{background:{ACC};color:#fff;font-weight:800;font-size:30px;letter-spacing:1.5px;padding:12px 24px;border-radius:12px}}
.brand{{display:flex;align-items:center;gap:14px;font-weight:700;font-size:28px}} .brand img{{width:56px;height:56px;border-radius:14px}}
.k{{color:{ACC};font-weight:800;font-size:30px;letter-spacing:2px;margin-top:44px;text-transform:uppercase}}
.h{{font-weight:800;font-size:72px;line-height:1.03;letter-spacing:-2.5px;margin-top:18px}}
.sub{{font-size:40px;line-height:1.3;font-weight:600;color:#374151;margin-top:26px}}
.p{{display:flex;gap:22px;font-size:38px;line-height:1.32;font-weight:600;margin-top:30px}} .p b{{color:#fff;background:{ACC};min-width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px}}
.note{{font-size:29px;line-height:1.38;color:#374151;margin-top:22px}}
.foot{{position:absolute;left:72px;right:72px;bottom:50px;display:flex;justify-content:space-between;font-size:22px;color:{MUTED};border-top:2px solid #E5E7EB;padding-top:18px}}
.ill{{display:flex;justify-content:center;margin-top:30px}}
"""
def ill(candles,W=520,H=420,bw=90):
    hi=max(c[1] for c in candles); lo=min(c[2] for c in candles); pad=(hi-lo)*.08; hi+=pad; lo-=pad
    y=lambda v: H-(v-lo)/(hi-lo)*H; n=len(candles); gap=W/n; s=''
    for i,(o,h,l,c) in enumerate(candles):
        x=gap*i+gap/2; col=UP if c>=o else DN
        s+=f'<line x1="{x}" y1="{y(h)}" x2="{x}" y2="{y(l)}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>'
        top,bot=y(max(o,c)),y(min(o,c)); s+=f'<rect x="{x-bw/2}" y="{top}" width="{bw}" height="{max(6,bot-top)}" rx="8" fill="{col}"/>'
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{s}</svg>'
def chart(sl,W=936,H=640):
    d=sl['ohlc']; hi=max(r[2] for r in d); lo=min(r[3] for r in d)
    if sl.get('zone'): hi=max(hi,sl['zone'][1]); lo=min(lo,sl['zone'][0])
    pad=(hi-lo)*.08; hi+=pad; lo-=pad; L,R,T,B=10,110,20,70; pw,ph=W-L-R,H-T-B
    y=lambda v: T+ph-(v-lo)/(hi-lo)*ph; n=len(d); g=pw/n; bw=max(6,g*.62); s=''
    if sl.get('zone'):
        z0,z1,zl=sl['zone']; s+=f'<rect x="{L}" y="{y(z1)}" width="{pw}" height="{y(z0)-y(z1)}" fill="{ACC}" opacity=".14"/>'
    for k in range(5):
        v=lo+(hi-lo)*k/4; s+=f'<line x1="{L}" x2="{L+pw}" y1="{y(v)}" y2="{y(v)}" stroke="#EEF0F2" stroke-width="2"/><text x="{L+pw+12}" y="{y(v)+8}" font-size="22" fill="{MUTED}">{v:,.0f}</text>'.replace(',','.')
    hl=set(sl.get('hl',[])); marks=sl.get('marks',{})
    for i,(dt,o,h,l,c) in enumerate(d):
        x=L+g*i+g/2; col=UP if c>=o else DN
        if dt in hl: s+=f'<rect x="{x-g/2}" y="{T}" width="{g}" height="{ph}" fill="#FDE68A" opacity=".55"/>'
        s+=f'<line x1="{x}" y1="{y(h)}" x2="{x}" y2="{y(l)}" stroke="{col}" stroke-width="3"/>'
        t,b=y(max(o,c)),y(min(o,c)); s+=f'<rect x="{x-bw/2}" y="{t}" width="{bw}" height="{max(2,b-t)}" fill="{col}"/>'
        if dt in marks: s+=f'<text x="{x}" y="{y(l)+38}" font-size="22" font-weight="800" text-anchor="middle" fill="{INK}">{marks[dt]}</text>'
    for i in (0,n//2,n-1): s+=f'<text x="{L+g*i+g/2}" y="{H-20}" font-size="22" text-anchor="middle" fill="{MUTED}">{d[i][0][:5]}</text>'
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="margin-top:26px">{s}</svg>'
def slide(D,sl,n,t):
    head=f'<div class="top"><div class="tag">{LABEL[D["series"]]}</div><div class="brand"><img src="{ICON}">marketpulse.vn</div></div>'
    ty=sl['type']
    if ty=='cover': b=f'<div class="k">{D["kicker"]}</div><div class="h" style="font-size:96px">{sl["title"]}</div><div class="sub">{sl["sub"]}</div><div class="ill">{ill(sl["candles"],600,520,110)}</div>'
    elif ty=='explain': b=f'<div class="k">{sl["kicker"]}</div><div class="h">{sl["headline"]}</div><div class="ill">{ill(sl["candles"],420,300,80)}</div>'+''.join(f'<div class="p"><b>{i}</b><span>{p}</span></div>' for i,p in enumerate(sl['points'],1))
    elif ty=='chart': b=f'<div class="k">{sl["kicker"]}</div><div class="h" style="font-size:60px">{sl["headline"]}</div>{chart(sl)}<div class="note">{sl.get("note","")}</div>'
    else: b=f'<div class="k">{sl["kicker"]}</div><div class="h">{sl["headline"]}</div>'+''.join(f'<div class="p"><b>{i}</b><span>{p}</span></div>' for i,p in enumerate(sl['items'],1))
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">{head}{b}<div class="foot"><span>{D["source"]}</span><span>{n}/{t} · Kiến thức tham khảo, không phải khuyến nghị đầu tư</span></div></div></body></html>'
async def main(dp,out):
    from playwright.async_api import async_playwright
    D=json.load(open(dp)); os.makedirs(out,exist_ok=True); t=len(D['slides'])
    async with async_playwright() as p:
        ex='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None
        b=await p.chromium.launch(executable_path=ex,args=['--no-sandbox']); g=await b.new_page(viewport={'width':1080,'height':1350})
        for i,sl in enumerate(D['slides'],1):
            fn=os.path.join(out,f'_t{i}.html'); open(fn,'w').write(slide(D,sl,i,t))
            await g.goto('file://'+os.path.abspath(fn)); await g.wait_for_timeout(300)
            over=await g.evaluate("()=>{const r=document.querySelector('.s');const f=document.querySelector('.foot').getBoundingClientRect().top;return [...r.children].filter(e=>!e.classList.contains('foot')).some(e=>e.getBoundingClientRect().bottom>f-8)}")
            await g.screenshot(path=os.path.join(out,f'mp_{D["series"]}_{D["tag"]}_{i}.png')); os.remove(fn); print(i,'overflow',over)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2]))
