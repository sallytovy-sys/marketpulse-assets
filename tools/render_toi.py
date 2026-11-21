#!/usr/bin/env python3
"""MarketPulse - TIN NÓNG TỐI NAY (19h, T2-CN). Nen toi, nhan DO #E5484D. 1080x1350.
python3 tools/render_toi.py <data.json> <out_dir>
slide types: cover{kicker,headline,bullets[]}, timeline{title,headline,items[[date,text]]},
             table{title,headline,rows[[a,b,c]],note}, deals{title,headline,items[{sym,who,action,qty,time,note}]}
"""
import sys, os, json, asyncio, base64
HERE=os.path.dirname(os.path.abspath(__file__)); FD=os.path.expanduser('~/.fonts')
ACC='#E5484D'; BG='#0F1115'; CARD='#1A1D24'; MUTED='#9AA0AA'; BUY='#22C55E'
ICON='data:image/png;base64,'+base64.b64encode(open(os.path.join(HERE,'icon.png'),'rb').read()).decode()
CSS=f"""@font-face{{font-family:'Inter Tight';src:url('file://{FD}/InterTight.ttf');font-weight:100 900}}
*{{box-sizing:border-box;margin:0}} body{{background:{BG}}}
.s{{width:1080px;height:1350px;background:{BG};color:#fff;font-family:'Inter Tight';padding:70px 72px;position:relative;overflow:hidden}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.tag{{background:{ACC};color:#fff;font-weight:800;font-size:30px;letter-spacing:2px;padding:12px 24px;border-radius:12px}}
.brand{{display:flex;align-items:center;gap:14px;font-weight:700;font-size:28px;color:#fff}} .brand img{{width:56px;height:56px;border-radius:14px}}
.h{{font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-2.5px;margin-top:46px}}
.k{{color:{ACC};font-weight:800;font-size:30px;letter-spacing:2px;margin-top:40px;text-transform:uppercase}}
.foot{{position:absolute;left:72px;right:72px;bottom:54px;display:flex;justify-content:space-between;font-size:22px;color:{MUTED};border-top:2px solid #262A33;padding-top:20px}}
.b{{display:flex;gap:22px;align-items:flex-start;font-size:36px;line-height:1.3;font-weight:600;margin-top:30px}} .b i{{color:{ACC};font-style:normal;font-weight:900}}
.tl{{margin-top:44px;border-left:4px solid {ACC};padding-left:40px}} .tl .it{{position:relative;margin-bottom:34px}}
.tl .it:before{{content:'';position:absolute;left:-54px;top:8px;width:24px;height:24px;border-radius:50%;background:{BG};border:5px solid {ACC}}}
.tl .d{{color:{ACC};font-weight:800;font-size:28px}} .tl .t{{font-size:33px;line-height:1.3;font-weight:600;margin-top:6px}}
table{{width:100%;border-collapse:collapse;margin-top:40px}} td{{padding:24px 6px;border-bottom:2px solid #262A33;font-size:34px;font-weight:600}}
td.r{{text-align:right;font-weight:800}} tr.hd td{{color:{MUTED};font-size:24px;font-weight:700;text-transform:uppercase;letter-spacing:1px}}
.note{{font-size:27px;color:{MUTED};margin-top:28px;line-height:1.35}}
.deal{{background:{CARD};border-radius:24px;padding:28px 32px;margin-top:26px;display:flex;gap:28px;align-items:center}}
.sym{{font-weight:900;font-size:46px;min-width:150px}} .act{{display:inline-block;font-weight:800;font-size:24px;padding:6px 14px;border-radius:8px;margin-bottom:10px}}
.who{{font-size:29px;line-height:1.3;font-weight:600}} .meta{{font-size:24px;color:{MUTED};margin-top:8px}}
"""
def head(): return f'<div class="top"><div class="tag">🔥 TIN NÓNG TỐI NAY</div><div class="brand"><img src="{ICON}">marketpulse.vn</div></div>'
def foot(D,n,t): return f'<div class="foot"><span>{D["source"]}</span><span>{n}/{t} · Không phải khuyến nghị đầu tư</span></div>'
def slide(D,s,n,t):
    ty=s['type']; h=head()
    if ty=='cover':
        body=f'<div class="k">{s["kicker"]}</div><div class="h" style="font-size:88px">{s["headline"]}</div>'+''.join(f'<div class="b"><i>▸</i><span>{b}</span></div>' for b in s['bullets'])
    elif ty=='timeline':
        body=f'<div class="k">{s["title"]}</div><div class="h">{s["headline"]}</div><div class="tl">'+''.join(f'<div class="it"><div class="d">{d}</div><div class="t">{x}</div></div>' for d,x in s['items'])+'</div>'
    elif ty=='table':
        rows=''.join(f'<tr class="{"hd" if i==0 else ""}"><td>{a}</td><td class="r">{b}</td><td class="r">{c}</td></tr>' for i,(a,b,c) in enumerate(s['rows']))
        body=f'<div class="k">{s["title"]}</div><div class="h">{s["headline"]}</div><table>{rows}</table><div class="note">{s.get("note","")}</div>'
    else:
        it=''
        for d in s['items']:
            c=BUY if d['action'].startswith('MUA') else ACC
            it+=f'<div class="deal"><div class="sym">{d["sym"]}</div><div><span class="act" style="background:{c}22;color:{c}">{d["action"]} · {d["qty"]}</span><div class="who">{d["who"]}</div><div class="meta">Thời gian: {d["time"]}{(" · "+d["note"]) if d.get("note") else ""}</div></div></div>'
        body=f'<div class="k">{s["title"]}</div><div class="h" style="font-size:66px">{s["headline"]}</div>{it}'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">{h}{body}{foot(D,n,t)}</div></body></html>'
async def main(dp,out):
    from playwright.async_api import async_playwright
    D=json.load(open(dp)); os.makedirs(out,exist_ok=True); t=len(D['slides'])
    async with async_playwright() as p:
        ex='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None
        b=await p.chromium.launch(executable_path=ex,args=['--no-sandbox']); g=await b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(D['slides'],1):
            fn=os.path.join(out,f'_t{i}.html'); open(fn,'w').write(slide(D,s,i,t))
            await g.goto('file://'+os.path.abspath(fn)); await g.wait_for_timeout(300)
            over=await g.evaluate("()=>{const r=document.querySelector('.s');const f=document.querySelector('.foot').getBoundingClientRect().top;return [...r.children].filter(e=>!e.classList.contains('foot')).some(e=>e.getBoundingClientRect().bottom>f-10)}")
            await g.screenshot(path=os.path.join(out,f'mp_toi_{D["tag"]}_{i}.png')); os.remove(fn); print(i,'overflow',over)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2]))
