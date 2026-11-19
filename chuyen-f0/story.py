import sys, asyncio
sys.path.insert(0,'/home/claude/post')
from mascot import candle
from playwright.async_api import async_playwright
INK='#1F1A2E'; PUR='#6A4CF5'; RED='#E5484D'; CREAM='#FFF4E4'; GRN='#16A34A'; BLUE='#1E88E5'
CDEFS='<defs><linearGradient id="cg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6A4CF5"/><stop offset="1" stop-color="#A68BFF"/></linearGradient></defs>'
def lan(mood='neutral', phone=True, scale=1.0):
    # simple flat girl, viewBox 0 0 300 420
    eyes={'happy':'<path d="M118 150 q12 -12 24 0 M158 150 q12 -12 24 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/>',
          'neutral':'<circle cx="130" cy="150" r="7" fill="#1F1A2E"/><circle cx="170" cy="150" r="7" fill="#1F1A2E"/>',
          'shock':'<circle cx="130" cy="150" r="12" fill="#fff" stroke="#1F1A2E" stroke-width="4"/><circle cx="130" cy="150" r="4" fill="#1F1A2E"/><circle cx="170" cy="150" r="12" fill="#fff" stroke="#1F1A2E" stroke-width="4"/><circle cx="170" cy="150" r="4" fill="#1F1A2E"/>',
          'sad':'<path d="M118 152 q12 8 24 0 M158 152 q12 8 24 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M124 162 q-4 22 2 40" stroke="#7FC8FF" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M176 162 q4 22 -2 40" stroke="#7FC8FF" stroke-width="8" fill="none" stroke-linecap="round"/>',
          'excited':'<path d="M120 146 l10 8 l10 -8 M160 146 l10 8 l10 -8" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'}[mood]
    mouth={'happy':'<path d="M132 182 q18 18 36 0" stroke="#1F1A2E" stroke-width="6" fill="#fff" stroke-linecap="round"/>',
           'neutral':'<path d="M138 186 q12 6 24 0" stroke="#1F1A2E" stroke-width="5" fill="none" stroke-linecap="round"/>',
           'shock':'<ellipse cx="150" cy="190" rx="14" ry="18" fill="#1F1A2E"/>',
           'sad':'<path d="M134 194 q16 -14 32 0" stroke="#1F1A2E" stroke-width="6" fill="none" stroke-linecap="round"/>',
           'excited':'<path d="M128 178 q22 30 44 0 z" fill="#1F1A2E"/>'}[mood]
    ph='<g transform="translate(196 236) rotate(-12)"><rect x="0" y="0" width="56" height="96" rx="12" fill="#1F1A2E"/><rect x="6" y="10" width="44" height="72" rx="6" fill="#B9F2D0"/></g><circle cx="206" cy="300" r="16" fill="#F2C9A0"/>' if phone else ''
    return f'''<svg viewBox="0 0 300 420" width="{300*scale}" height="{420*scale}" xmlns="http://www.w3.org/2000/svg">
<path d="M70 420 q0 -150 80 -150 q80 0 80 150 z" fill="{PUR}"/><path d="M128 270 l22 30 l22 -30 z" fill="#fff"/>
<path d="M78 130 q0 -90 72 -90 q72 0 72 90 l0 80 q-20 10 -30 -10 l-84 0 q-10 20 -30 10 z" fill="#2B2238"/>
<ellipse cx="150" cy="160" rx="62" ry="72" fill="#F7D3AE"/>
<path d="M90 120 q30 -50 120 -20 q-30 -10 -60 10 q-30 -5 -60 10 z" fill="#2B2238"/>
<circle cx="108" cy="180" r="10" fill="#FF9AA8" opacity=".5"/><circle cx="192" cy="180" r="10" fill="#FF9AA8" opacity=".5"/>
{eyes}{mouth}{ph}</svg>'''
def cnd(mood, s=0.42, w=300, h=360):
    return f'<svg viewBox="-160 -320 320 620" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">{CDEFS}{candle(0,0,1,mood)}</svg>'
def bubble(text, side='left', color='#fff', tc=INK, w=520):
    tail='left:60px' if side=='left' else 'right:60px'
    return f'<div class="bub" style="background:{color};color:{tc};max-width:{w}px"><span class="tail" style="{tail};border-top-color:{color}"></span>{text}</div>'
def chat(msgs, title='Cộng đồng đầu tư thông minh 💎', sub='2.847 thành viên'):
    rows=''
    for who,txt,kind in msgs:
        if kind=='admin': rows+=f'<div class="msg a"><b>Thầy Đầu Tư ✅</b><br>{txt}</div>'
        elif kind=='img': rows+=f'<div class="msg a img">{txt}</div>'
        elif kind=='me': rows+=f'<div class="msg me">{txt}</div>'
        elif kind=='sys': rows+=f'<div class="sys">{txt}</div>'
        else: rows+=f'<div class="msg o"><b>{who}</b><br>{txt}</div>'
    return f'<div class="phone"><div class="ph-top"><div class="av">💎</div><div><b>{title}</b><br><span>{sub}</span></div></div><div class="ph-body">{rows}</div></div>'
CSS=f'''@font-face{{font-family:BVP;src:url(file:///root/.fonts/BeVietnamPro-Medium.ttf);font-weight:500}}
@font-face{{font-family:BVP;src:url(file:///root/.fonts/BeVietnamPro-Bold.ttf);font-weight:700}}
@font-face{{font-family:Anton;src:url(file:///root/.fonts/Anton-Regular.ttf)}}
body{{margin:0}} *{{box-sizing:border-box}}
.page{{width:1080px;height:1350px;background:{CREAM};font-family:BVP,sans-serif;color:{INK};position:relative;overflow:hidden;padding:56px 64px}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.tag{{background:{INK};color:#fff;font-weight:700;font-size:24px;letter-spacing:2px;padding:10px 22px;border-radius:999px}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:700;font-size:26px}} .brand img{{width:48px;height:48px;border-radius:11px}}
.panel{{margin-top:36px;background:#fff;border:5px solid {INK};border-radius:36px;box-shadow:10px 10px 0 {INK};height:760px;position:relative;overflow:hidden}}
.cap{{margin-top:44px;font-size:40px;line-height:1.38;font-weight:500}} .cap b{{font-weight:700}}
.foot{{position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-size:20px;color:#6B6375;font-weight:500}}
.bub{{position:absolute;border:5px solid {INK};border-radius:32px;padding:24px 30px;font-size:34px;font-weight:700;line-height:1.3}}
.bub .tail{{position:absolute;bottom:-30px;width:0;height:0;border:16px solid transparent;border-top:24px solid}}
.phone{{position:absolute;background:#ECE9F5;border:6px solid {INK};border-radius:40px;overflow:hidden}}
.ph-top{{background:{INK};color:#fff;display:flex;gap:14px;align-items:center;padding:18px 22px;font-size:24px}} .ph-top span{{font-size:18px;opacity:.7}}
.av{{width:48px;height:48px;border-radius:50%;background:{PUR};display:flex;align-items:center;justify-content:center;font-size:26px}}
.ph-body{{padding:18px;display:flex;flex-direction:column;gap:12px}}
.msg{{background:#fff;border-radius:18px;padding:12px 16px;font-size:22px;max-width:85%;line-height:1.35}} .msg b{{font-size:18px;color:{PUR}}}
.msg.me{{align-self:flex-end;background:#D9F7E3}} .msg.img{{font-family:Anton;font-size:56px;color:{GRN};text-align:center;padding:18px}}
.sys{{align-self:center;background:#fff;border-radius:999px;padding:8px 18px;font-size:20px;color:#6B6375}}
.h1{{font-family:Anton;font-size:116px;line-height:1.08;letter-spacing:.5px}}
'''
def page(n,total,panel,cap):
    return f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
<div class="top"><div class="tag">CHUYỆN F0 · TẬP 2</div><div class="brand"><img src="file:///home/claude/story/icon.png">marketpulse.vn</div></div>
<div class="panel">{panel}</div><div class="cap">{cap}</div>
<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>{n}/{total}</div></div></div></body></html>'''
T=6
slides=[]
# 1 cover
slides.append(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
<div class="top"><div class="tag">CHUYỆN F0 · TẬP 2</div><div class="brand"><img src="file:///home/claude/story/icon.png">marketpulse.vn</div></div>
<div class="h1" style="margin-top:50px">PHÍ ROOM VIP<br><span style="color:{PUR}">3 TRIỆU/THÁNG,</span><br>TÔI MẤT <span style="color:{RED}">120 TRIỆU</span></div>
<div style="position:absolute;left:40px;bottom:90px">{lan('sad',True,1.75)}</div>
<div style="position:absolute;right:70px;bottom:250px;transform:rotate(4deg)">{chat([('','+40% 🚀','img'),('Minh K.','Cảm ơn thầy 🙏🙏','o'),('Hà P.','Về bờ rồi ạ!','o')],sub='VIP · 312 thành viên').replace('class="phone"','class="phone" style="position:relative;width:380px"')}</div>
<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>1/{T} · Vuốt ➜</div></div></div></body></html>''')
# 2 group
p2=f'''<div style="position:absolute;left:40px;top:40px">{chat([('','+20% 📈','img'),('Thầy','Hàng về đúng kèo, chúc mừng anh em đã x2 tài khoản tháng này 💰','admin'),('Tuấn N.','Cảm ơn thầy 🙏','o'),('Linh T.','Lần đầu thấy nhóm uy tín vậy','o'),('','+40% 🚀','img')]).replace('class="phone"','class="phone" style="width:560px;height:680px"')}</div>
<div style="position:absolute;right:20px;bottom:0">{lan('excited',True,1.25)}</div>
{bubble('"Ngày nào<br>cũng lãi á?!"','right',w=360).replace('class="bub"','class="bub" style="right:40px;top:90px"')}'''
slides.append(page(2,T,p2,'Một tối, Lan được kéo vào nhóm Zalo <b>"Cộng đồng đầu tư thông minh"</b>. Ngày nào admin cũng đăng ảnh lãi 20%, 40%, kèm hàng trăm lời cảm ơn "thầy".'))
# 3 VIP fee
p3=f'''<div style="position:absolute;left:60px;top:70px;width:520px;background:{INK};color:#fff;border-radius:28px;padding:36px;transform:rotate(-4deg)">
<div style="font-family:Anton;font-size:64px;color:#FFD54A">ROOM VIP 👑</div><div style="font-size:30px;margin-top:10px">Nhận mã trước khi tăng</div>
<div style="font-family:Anton;font-size:84px;margin-top:20px">3.000.000đ</div><div style="font-size:28px;opacity:.8">/ tháng · Chuyển khoản trước</div></div>
<div style="position:absolute;left:90px;bottom:60px;background:#D9F7E3;border:5px solid {INK};border-radius:24px;padding:20px 28px;font-size:34px;font-weight:700">✅ Mã đầu tiên: <span style="color:{GRN}">+8%</span></div>
<div style="position:absolute;right:20px;bottom:0">{lan('happy',True,1.3)}</div>
{bubble('"Thầy giỏi<br>thật sự!"','right',w=340).replace('class="bub"','class="bub" style="right:50px;top:60px"')}'''
slides.append(page(3,T,p3,'Nhóm miễn phí chỉ cho xem "kết quả". Muốn nhận mã thì phải vào <b>room VIP, 3 triệu/tháng</b>. Lan đóng tiền, và mã đầu tiên tăng thật. <b>Lan bắt đầu tin tuyệt đối.</b>'))
# 4 all-in & crash
bars=''.join(f'<rect x="{40+i*70}" y="{60+i*40}" width="40" height="70" rx="6" fill="{BLUE}"/>' for i in range(3))
p4=f'''<div style="position:absolute;left:40px;top:40px">{chat([('','Mã mới: giữ chặt, mục tiêu x2 🚀 Ai chưa vào thì vào ngay!','admin'),('','Em vừa mua hết 120 triệu thầy ạ 🙏','me'),('','Giảm sàn là rũ hàng thôi, gom thêm!','admin')]).replace('class="phone"','class="phone" style="width:540px;height:410px"')}</div>
<div style="position:absolute;left:60px;bottom:34px;background:#fff;border:5px solid {INK};border-radius:24px;padding:16px 24px">
<div style="font-weight:700;font-size:26px">3 phiên liền <span style="color:{BLUE}">giảm sàn</span></div>
<svg width="300" height="150" viewBox="0 0 300 190">{bars}<path d="M20 40 L270 170" stroke="{RED}" stroke-width="6" stroke-dasharray="10 8"/></svg></div>
<div style="position:absolute;right:20px;bottom:0">{lan('shock',True,1.3)}</div>'''
slides.append(page(4,T,p4,'Lan dồn <b>120 triệu</b> vào mã thứ hai theo lời "thầy". Cổ phiếu giảm sàn 3 phiên liền. Hỏi thì "thầy" bảo: <i>"Rũ hàng thôi, gom thêm."</i>'))
# 5 disappear + candle explains
p5=f'''<div style="position:absolute;left:40px;top:40px">{chat([('','Thầy Đầu Tư đã rời nhóm','sys'),('','Nhóm này không còn tồn tại','sys')],title='VIP 👑',sub='0 thành viên').replace('class="phone"','class="phone" style="width:420px;height:250px"')}</div>
<div style="position:absolute;left:60px;top:320px;width:520px;font-size:28px;font-weight:700;line-height:1.4">
<div style="background:#E8E2FF;border-radius:18px;padding:14px 20px">① Nhóm vào sớm mua giá thấp</div>
<div style="text-align:center;font-size:28px">⬇</div>
<div style="background:#FFE6E6;border-radius:18px;padding:14px 20px">② Hô hào người đến sau mua vào</div>
<div style="text-align:center;font-size:28px">⬇</div>
<div style="background:{INK};color:#fff;border-radius:18px;padding:14px 20px">③ Bán hết cho chính người đến sau</div></div>
<div style="position:absolute;right:10px;bottom:10px">{cnd('cool',w=330,h=420)}</div>
{bubble('"Người đến sau<br>chính là thanh khoản<br>để họ thoát hàng."','right',color='#FFF7CC',w=420).replace('class="bub"','class="bub" style="right:40px;top:50px;font-size:30px"')}'''
slides.append(page(5,T,p5,'Tuần sau, nhóm VIP biến mất. Những người vào sớm đã <b>bán ra đúng lúc Lan mua vào</b>. Lan không thua vì chọn sai mã, Lan thua vì đã đóng vai người mua cuối cùng.'))
# 6 checklist + CTA
items=['Khoe lãi liên tục, không bao giờ thấy lỗ','Thu phí để vào "room VIP"','Cam kết lợi nhuận, "x2 tài khoản"','Thúc giục "mua ngay kẻo lỡ"','Cấm hỏi, cấm nghi ngờ "thầy"']
lst=''.join(f'<div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:700;padding:16px 0;border-bottom:3px dashed #DDD4C4"><span style="background:{RED};color:#fff;border-radius:50%;width:56px;height:56px;display:flex;align-items:center;justify-content:center;flex:none">{i+1}</span>{t}</div>' for i,t in enumerate(items))
slides.append(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
<div class="top"><div class="tag">CHUYỆN F0 · TẬP 2</div><div class="brand"><img src="file:///home/claude/story/icon.png">marketpulse.vn</div></div>
<div class="h1" style="font-size:96px;margin-top:40px">5 DẤU HIỆU<br><span style="color:{RED}">ROOM PHÍM HÀNG</span></div>
<div style="margin-top:24px">{lst}</div>
<div style="position:absolute;left:64px;right:64px;bottom:96px;background:{PUR};color:#fff;border-radius:28px;padding:28px 34px;display:flex;justify-content:space-between;align-items:center">
<div style="font-size:34px;font-weight:700;line-height:1.3">Gửi bài này cho người bạn<br>đang "theo thầy" 👀</div><div style="font-family:Anton;font-size:40px">FOLLOW<br>MARKETPULSE</div></div>
<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>6/{T}</div></div></div></body></html>''')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,h in enumerate(slides,1):
            fn=f'/home/claude/story/t2_{i}.html'; open(fn,'w').write(h)
            await pg.goto('file://'+fn); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'/home/claude/story/tap2_{i}.png')
        await b.close()
asyncio.run(main())
