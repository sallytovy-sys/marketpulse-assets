import asyncio
from storylib import *
from playwright.async_api import async_playwright
def hung(mood='neutral', phone=True, scale=1.0, shirt='#2563EB'):
    eyes={'happy':'<path d="M118 150 q12 -12 24 0 M158 150 q12 -12 24 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/>',
          'neutral':'<circle cx="130" cy="150" r="7" fill="#1F1A2E"/><circle cx="170" cy="150" r="7" fill="#1F1A2E"/>',
          'shock':'<circle cx="130" cy="150" r="12" fill="#fff" stroke="#1F1A2E" stroke-width="4"/><circle cx="130" cy="150" r="4" fill="#1F1A2E"/><circle cx="170" cy="150" r="12" fill="#fff" stroke="#1F1A2E" stroke-width="4"/><circle cx="170" cy="150" r="4" fill="#1F1A2E"/>',
          'sad':'<path d="M118 152 q12 8 24 0 M158 152 q12 8 24 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M124 162 q-4 22 2 40" stroke="#7FC8FF" stroke-width="8" fill="none" stroke-linecap="round"/>',
          'cool':'<rect x="112" y="138" width="34" height="22" rx="8" fill="#1F1A2E"/><rect x="154" y="138" width="34" height="22" rx="8" fill="#1F1A2E"/><rect x="144" y="144" width="12" height="5" fill="#1F1A2E"/>',
          'excited':'<path d="M120 146 l10 8 l10 -8 M160 146 l10 8 l10 -8" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'}[mood]
    mouth={'happy':'<path d="M132 182 q18 18 36 0" stroke="#1F1A2E" stroke-width="6" fill="#fff" stroke-linecap="round"/>',
           'neutral':'<path d="M138 186 q12 6 24 0" stroke="#1F1A2E" stroke-width="5" fill="none" stroke-linecap="round"/>',
           'shock':'<ellipse cx="150" cy="192" rx="14" ry="18" fill="#1F1A2E"/>',
           'sad':'<path d="M134 196 q16 -14 32 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/>',
           'cool':'<path d="M134 184 q20 14 34 -4" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/>',
           'excited':'<path d="M128 178 q22 30 44 0 z" fill="#1F1A2E"/>'}[mood]
    sweat='<path d="M214 110 q14 22 0 32 q-14 -10 0 -32 z" fill="#7FC8FF"/>' if mood in ('shock','sad') else ''
    ph='<g transform="translate(196 236) rotate(-12)"><rect x="0" y="0" width="56" height="96" rx="12" fill="#1F1A2E"/><rect x="6" y="10" width="44" height="72" rx="6" fill="#B9F2D0"/></g><circle cx="206" cy="300" r="16" fill="#E9BE95"/>' if phone else ''
    return f'''<svg viewBox="0 0 300 420" width="{300*scale}" height="{420*scale}" xmlns="http://www.w3.org/2000/svg">
<path d="M66 420 q0 -150 84 -150 q84 0 84 150 z" fill="{shirt}"/><path d="M130 270 l20 26 l20 -26 z" fill="#fff"/>
<ellipse cx="150" cy="162" rx="60" ry="70" fill="#F0C8A0"/>
<path d="M88 140 q-6 -84 66 -88 q70 -2 60 84 q-14 -40 -40 -46 q-30 14 -86 50 z" fill="#1E1A26"/>
<circle cx="110" cy="182" r="9" fill="#FF9AA8" opacity=".45"/><circle cx="190" cy="182" r="9" fill="#FF9AA8" opacity=".45"/>
{eyes}{mouth}{sweat}{ph}</svg>'''
def app(value, change, color, label='Tổng tài sản', w=420):
    return f'''<div style="width:{w}px;background:#fff;border:6px solid {INK};border-radius:36px;overflow:hidden">
<div style="background:{INK};color:#fff;padding:16px 24px;font-size:22px;font-weight:700">📱 Tài khoản chứng khoán</div>
<div style="padding:26px 28px"><div style="font-size:22px;color:#6B6375">{label}</div>
<div style="font-family:Anton;font-size:64px;margin-top:4px">{value}</div>
<div style="display:inline-block;margin-top:10px;background:{color};color:#fff;font-weight:700;font-size:30px;padding:8px 18px;border-radius:12px">{change}</div></div></div>'''
TAG='CHUYỆN F0 · TẬP 1'
def pg(n,total,panel,cap): return page(n,total,panel,cap).replace('CHUYỆN F0 · TẬP 2',TAG)
T=6; S=[]
head=f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page"><div class="top"><div class="tag">{TAG}</div><div class="brand"><img src="file:///home/claude/story/icon.png">marketpulse.vn</div></div>'
# 1 cover
S.append(head+f'''<div class="h1" style="margin-top:50px">THÁNG ĐẦU<br>LÃI <span style="color:{GRN}">30%</span>, TÔI<br>TƯỞNG MÌNH LÀ<br><span style="color:{PUR}">THIÊN TÀI</span></div>
<div style="position:absolute;left:30px;bottom:80px">{hung('cool',True,1.55)}</div>
<div style="position:absolute;right:70px;bottom:200px;transform:rotate(5deg)">{app('65.000.000đ','▲ +30% trong 3 tuần',GRN,w=440)}</div>
<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>1/{T} · Vuốt ➜</div></div></div></body></html>''')
# 2
p=f'''<div style="position:absolute;left:50px;top:60px">{app('50.000.000đ','Vốn ban đầu','#6B6375',label='Tháng 1 · Mở tài khoản',w=420)}</div>
<div style="position:absolute;left:250px;top:330px;font-size:60px">⬇</div>
<div style="position:absolute;left:50px;top:420px">{app('65.000.000đ','▲ +30%',GRN,label='3 tuần sau',w=420)}</div>
<div style="position:absolute;right:10px;bottom:0">{hung('excited',True,1.3)}</div>
{bubble('"Chứng khoán<br>dễ vậy mà!"','right',w=360).replace('class="bub"','class="bub" style="right:40px;top:70px"')}'''
S.append(pg(2,T,p,'Tháng 1, Hùng mở tài khoản với <b>50 triệu</b>. Mua vài mã bạn bè giới thiệu, không cần tìm hiểu. Ba tuần sau, tài khoản báo <b style="color:#16A34A">+30%</b>.'))
# 3
p=f'''<div style="position:absolute;left:40px;top:40px">{chat([('','+30% 🚀','img'),('','Chứng khoán dễ mà, sao giờ mới biết 😎','me'),('Đức','Đỉnh vậy! Chỉ tao với','o'),('','Tháng sau tao nạp thêm 150 triệu, cả tiền định cưới vợ 💍','me')],title='Hội bạn thân 🍻',sub='6 thành viên').replace('class="phone"','class="phone" style="width:560px;height:520px"')}</div>
<div style="position:absolute;left:60px;bottom:40px;background:#FFF7CC;border:5px solid {INK};border-radius:24px;padding:18px 26px;font-size:32px;font-weight:700">💸 Nạp thêm: <span style="color:{RED}">150.000.000đ</span></div>
<div style="position:absolute;right:10px;bottom:0">{hung('happy',True,1.3)}</div>'''
S.append(pg(3,T,p,'Hùng chụp màn hình khoe nhóm bạn. Tháng sau, Hùng <b>nạp thêm 150 triệu</b>, trong đó có cả tiền định để cưới vợ. Tổng vốn đã bỏ vào: <b>200 triệu</b>.'))
# 4
bars=[('Tuần 1','−10%',90),('Tuần 2','−17%',150),('Tuần 3','−25%',220)]
bh=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="font-family:Anton;font-size:36px;color:{RED}">{v}</div><div style="width:90px;height:{h}px;background:{RED};border-radius:12px 12px 0 0"></div><div style="font-weight:700;font-size:24px">{l}</div></div>' for l,v,h in bars)
p=f'''<div style="position:absolute;left:60px;top:60px;font-weight:700;font-size:30px">Rồi thị trường quay đầu…<div style="font-size:22px;color:#6B6375;font-weight:500;margin-top:6px">Tài khoản của Hùng, giảm cộng dồn</div></div>
<div style="position:absolute;left:60px;bottom:50px;display:flex;gap:30px;align-items:flex-end">{bh}</div>
<div style="position:absolute;right:10px;bottom:0">{hung('shock',True,1.3)}</div>
{bubble('"Chắc chỉnh<br>nhẹ thôi mà…"','right',w=360).replace('class="bub"','class="bub" style="right:40px;top:70px"')}'''
S.append(pg(4,T,p,'Tuần đầu −10%, Hùng nghĩ "chỉnh nhẹ thôi". Tuần thứ ba −25%, Hùng <b>không dám mở app</b>. Hùng không có kế hoạch nào cho lúc thị trường giảm.'))
# 5
tiles=''.join(f'<div style="width:62px;height:62px;border-radius:10px;background:{GRN if i not in (7,13) else "#C9C2D6"}"></div>' for i in range(20))
p=f'''<div style="position:absolute;left:50px;top:50px;width:470px">
<div style="display:flex;justify-content:space-between;font-size:30px;font-weight:700;padding:12px 0;border-bottom:3px dashed #DDD4C4"><span>Tổng tiền đã nạp</span><span>200 triệu</span></div>
<div style="display:flex;justify-content:space-between;font-size:30px;font-weight:700;padding:12px 0;border-bottom:3px dashed #DDD4C4"><span>Còn lại sau 3 tháng</span><span>130 triệu</span></div>
<div style="display:flex;justify-content:space-between;font-family:Anton;font-size:48px;padding:12px 0;color:{RED}"><span>LỖ</span><span>−70 TRIỆU</span></div>
<div style="font-size:24px;font-weight:700;margin-top:22px">Tháng đầu tiên của Hùng: gần như mã nào cũng xanh</div>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;width:400px">{tiles}</div></div>
<div style="position:absolute;right:10px;bottom:10px">{cnd('cool',w=300,h=390)}</div>
{bubble('"Khi cả chợ<br>đều lên giá,<br>ai bán cũng<br>thấy mình giỏi."','right',color='#FFF7CC',w=330).replace('class="bub"','class="bub" style="right:40px;top:40px;font-size:30px"')}'''
S.append(pg(5,T,p,'Ba tháng sau, Hùng mất sạch khoản lãi và thêm <b>70 triệu tiền gốc</b>. Điều Hùng không biết: tháng đầu tiên, <b>gần như cổ phiếu nào cũng tăng</b>. Hùng không giỏi, Hùng chỉ vào đúng lúc.'))
# 6
items=['Ghi lại lý do trước mỗi lần mua','Không nạp thêm tiền chỉ vì vừa lãi','Không dùng tiền đã có kế hoạch: cưới, mua nhà, học phí','So kết quả với VN-Index, không so với bạn bè']
lst=''.join(f'<div style="display:flex;gap:18px;align-items:center;font-size:34px;font-weight:700;padding:14px 0;border-bottom:3px dashed #DDD4C4"><span style="background:{GRN};color:#fff;border-radius:50%;width:54px;height:54px;display:flex;align-items:center;justify-content:center;flex:none">✓</span>{t}</div>' for t in items)
S.append(head+f'''<div class="h1" style="font-size:84px;margin-top:40px">KHOẢN LÃI ĐẦU TIÊN<br>LÀ KHOẢN LÃI<br><span style="color:{RED}">NGUY HIỂM NHẤT</span></div>
<div style="font-size:30px;font-weight:700;margin-top:18px;color:#6B6375">4 điều giúp bạn không thành "Hùng":</div>
<div>{lst}</div>
<div style="position:absolute;left:64px;right:64px;bottom:96px;background:{PUR};color:#fff;border-radius:28px;padding:26px 34px;display:flex;justify-content:space-between;align-items:center">
<div style="font-size:32px;font-weight:700;line-height:1.3">Gửi cho người bạn vừa<br>khoe lãi tháng đầu 😅</div><div style="font-family:Anton;font-size:40px">FOLLOW<br>MARKETPULSE</div></div>
<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>6/{T}</div></div></div></body></html>''')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        g=await b.new_page(viewport={'width':1080,'height':1350})
        for i,h in enumerate(S,1):
            fn=f'/home/claude/story/t1_{i}.html'; open(fn,'w').write(h)
            await g.goto('file://'+fn); await g.wait_for_timeout(300)
            over=await g.evaluate("()=>{const p=document.querySelector('.page');return p.scrollHeight>p.clientHeight}")
            if over: print('overflow',i)
            await g.screenshot(path=f'/home/claude/story/tap1_{i}.png')
        await b.close()
asyncio.run(main())
