import asyncio, sys, re
from chars import *
from playwright.async_api import async_playwright
def person(kind, mood, scale, shirt, hair='#1E1A26', phone=True):
    svg = hung(mood, phone, scale, shirt) if kind=='m' else lan(mood if mood!='cool' else 'happy', phone, scale)
    if kind=='f': svg = svg.replace(PUR, shirt, 1).replace('#2B2238', hair)
    else: svg = svg.replace('#1E1A26', hair)
    return svg
def bub(text, pos, color='#fff', w=360, fs=34):
    return bubble(text,'right',color=color,w=w).replace('class="bub"', f'class="bub" style="{pos};font-size:{fs}px"')
def ep(tag, total=6):
    head=f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page"><div class="top"><div class="tag">{tag}</div><div class="brand"><img src="file:///home/claude/story/icon.png">marketpulse.vn</div></div>'
    foot=lambda n: f'<div class="foot"><div>Câu chuyện minh họa · Không phải khuyến nghị đầu tư</div><div>{n}/{total}{" · Vuốt ➜" if n==1 else ""}</div></div></div></body></html>'
    pg=lambda n,panel,cap: page(n,total,panel,cap).replace('CHUYỆN F0 · TẬP 2',tag)
    return head,foot,pg
def checklist(items, color):
    return ''.join(f'<div style="display:flex;gap:18px;align-items:center;font-size:34px;font-weight:700;padding:14px 0;border-bottom:3px dashed #DDD4C4"><span style="background:{color};color:#fff;border-radius:50%;width:54px;height:54px;display:flex;align-items:center;justify-content:center;flex:none">✓</span>{t}</div>' for t in items)
def final(head,foot,title_html,sub,items,color,cta):
    return head+f'''<div class="h1" style="font-size:84px;margin-top:40px">{title_html}</div>
<div style="font-size:30px;font-weight:700;margin-top:18px;color:#6B6375">{sub}</div><div>{checklist(items,color)}</div>
<div style="position:absolute;left:64px;right:64px;bottom:96px;background:{PUR};color:#fff;border-radius:28px;padding:26px 34px;display:flex;justify-content:space-between;align-items:center">
<div style="font-size:32px;font-weight:700;line-height:1.3">{cta}</div><div style="font-family:Anton;font-size:40px">FOLLOW<br>MARKETPULSE</div></div>'''+foot(6)
EPS={}
# ---------------- TẬP 3: MARGIN (Tuấn) ----------------
head,foot,pg=ep('CHUYỆN F0 · TẬP 3'); S=[]; SH='#0F766E'
S.append(head+f'''<div class="h1" style="margin-top:50px">CUỘC GỌI LÚC<br><span style="color:{RED}">10 GIỜ SÁNG</span><br>KHIẾN TÔI MẤT<br><span style="color:{RED}">60%</span> TÀI KHOẢN</div>
<div style="position:absolute;left:30px;bottom:80px">{person('m','shock',1.55,SH)}</div>
<div style="position:absolute;right:70px;bottom:230px;transform:rotate(5deg);width:420px;background:{INK};color:#fff;border:6px solid {INK};border-radius:40px;padding:34px;text-align:center">
<div style="font-size:26px;opacity:.7">Cuộc gọi đến · 10:02</div><div style="font-family:Anton;font-size:52px;margin:14px 0">CÔNG TY CK</div>
<div style="display:flex;justify-content:center;gap:60px;margin-top:20px"><div style="width:84px;height:84px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;font-size:40px">📞</div><div style="width:84px;height:84px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center;font-size:40px">📞</div></div></div>'''+foot(1))
p=f'''<div style="position:absolute;left:50px;top:60px;width:540px">
<div style="display:flex;gap:16px;align-items:flex-end">
<div style="text-align:center"><div style="width:150px;height:220px;background:{GRN};border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:Anton;font-size:40px">100tr</div><div style="font-weight:700;font-size:24px;margin-top:8px">Tiền của Tuấn</div></div>
<div style="font-family:Anton;font-size:60px;padding-bottom:110px">+</div>
<div style="text-align:center"><div style="width:150px;height:220px;background:#F59E0B;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:Anton;font-size:40px">100tr</div><div style="font-weight:700;font-size:24px;margin-top:8px">Tiền đi vay</div></div></div>
<div style="margin-top:28px;background:{INK};color:#fff;border-radius:20px;padding:18px 24px;font-size:32px;font-weight:700">= Mua <span style="font-family:Anton;font-size:44px">200 TRIỆU</span> cổ phiếu</div></div>
<div style="position:absolute;right:10px;bottom:0">{person('m','happy',1.25,SH)}</div>
{bub('"Lãi sẽ<br>gấp đôi!"','right:40px;top:70px',w=300)}'''
S.append(pg(2,p,'Tuấn có <b>100 triệu</b>. Môi giới gợi ý: <i>"Anh dùng margin đi, có thêm 100 triệu nữa."</i> Margin là <b>vay tiền công ty chứng khoán để mua thêm cổ phiếu</b>, và tiền vay phải trả lãi mỗi ngày.'))
p=f'''<div style="position:absolute;left:50px;top:50px;width:560px">
<div style="font-weight:700;font-size:30px">Cổ phiếu giảm <span style="color:{RED}">30%</span></div>
<div style="margin-top:22px;display:flex;flex-direction:column;gap:14px;font-size:30px;font-weight:700">
<div style="display:flex;justify-content:space-between;background:#F4F1EA;border-radius:16px;padding:16px 22px"><span>Giá trị cổ phiếu</span><span>200 → 140 triệu</span></div>
<div style="display:flex;justify-content:space-between;background:#FFF1D6;border-radius:16px;padding:16px 22px"><span>Nợ phải trả</span><span>100 triệu</span></div>
<div style="display:flex;justify-content:space-between;background:{INK};color:#fff;border-radius:16px;padding:16px 22px"><span>Tiền thật của Tuấn</span><span style="color:#FF8A8A">40 triệu</span></div></div>
<div style="margin-top:22px;font-family:Anton;font-size:56px;color:{RED}">MẤT 60% TIỀN GỐC</div></div>
<div style="position:absolute;right:10px;bottom:0">{person('m','shock',1.25,SH)}</div>'''
S.append(pg(3,p,'Cổ phiếu chỉ giảm 30%, nhưng vì một nửa là tiền vay, <b>tiền thật của Tuấn mất tới 60%</b>. Margin nhân đôi lãi, và cũng <b>nhân đôi lỗ</b>.'))
p=f'''<div style="position:absolute;left:40px;top:40px">{chat([('','Chào anh Tuấn, tỷ lệ ký quỹ tài khoản anh đã xuống dưới ngưỡng duy trì.','admin'),('','Anh vui lòng nộp thêm tiền trước 14h hôm nay, nếu không bên em buộc phải bán bớt cổ phiếu.','admin'),('','Em ơi cho anh thêm vài hôm được không 😰','me')],title='Môi giới · Công ty CK',sub='đang hoạt động').replace('Thầy Đầu Tư ✅','Môi giới').replace('class="phone"','class="phone" style="width:560px;height:520px"')}</div>
<div style="position:absolute;right:10px;bottom:0">{person('m','sad',1.25,SH)}</div>'''
S.append(pg(4,p,'10 giờ sáng, điện thoại reo. Đó là <b>call margin</b>: nộp thêm tiền, hoặc cổ phiếu sẽ bị bán. Tuấn không có tiền nộp, cổ phiếu bị <b>bán đúng lúc giá đang thấp</b>.'))
p=f'''<div style="position:absolute;left:60px;top:60px;width:520px">
<svg width="520" height="360" viewBox="0 0 520 360"><polyline points="10,60 120,120 220,200 300,300 380,230 470,150 510,110" fill="none" stroke="{INK}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="300" cy="300" r="18" fill="{RED}"/><text x="300" y="350" text-anchor="middle" font-family="BVP" font-weight="700" font-size="24" fill="{RED}">Bị bán ở đây</text>
<circle cx="470" cy="150" r="14" fill="{GRN}"/><text x="440" y="120" text-anchor="middle" font-family="BVP" font-weight="700" font-size="24" fill="{GRN}">1 tuần sau</text></svg></div>
<div style="position:absolute;right:10px;bottom:10px">{cnd('cool',w=300,h=390)}</div>
{bub('"Margin không<br>làm bạn giàu<br>nhanh hơn. Nó làm<br>mọi thứ xảy ra<br>nhanh hơn."','right:40px;top:40px',color='#FFF7CC',w=330,fs=28)}'''
S.append(pg(5,p,'Một tuần sau giá hồi lại, nhưng <b>Tuấn không còn cổ phiếu nào</b> để hưởng. Khi dùng vốn vay, bạn không còn quyền chờ đợi.'))
S.append(final(head,foot,'MARGIN<br><span style="color:'+RED+'">NHÂN ĐÔI CẢ LỖ</span>','Trước khi dùng margin, F0 nên nhớ:',['Lỗ gấp đôi khi giá giảm, lãi vay tính mỗi ngày','Bị call margin thì phải nộp tiền hoặc bị bán','Người mới: chưa hiểu rõ thì đừng dùng margin','Luôn biết ngưỡng ký quỹ của tài khoản mình'],RED,'Gửi cho người bạn đang<br>"vay thêm cho nhanh giàu" 😬'))
EPS['tap3']=S
# ---------------- TẬP 4: LÙA BỐ MẸ (Nam) ----------------
head,foot,pg=ep('CHUYỆN F0 · TẬP 4'); S=[]; SH='#B45309'
S.append(head+f'''<div class="h1" style="margin-top:50px">TÔI <span style="color:{RED}">LÙA</span> CẢ<br>BỐ MẸ VÀO<br>CHỨNG KHOÁN</div>
<div style="position:absolute;left:10px;bottom:80px;display:flex;align-items:flex-end">
<div style="margin-right:-70px">{person('m','sad',1.15,'#4B5563',hair='#C9C5CE',phone=False)}</div>
<div style="margin-right:-60px;z-index:2">{person('m','shock',1.45,SH)}</div>
<div>{person('f','sad',1.15,'#9D174D',hair='#C9C5CE',phone=False)}</div></div>
<div style="position:absolute;right:60px;top:600px;transform:rotate(6deg);background:#FFF7CC;border:6px solid {INK};border-radius:24px;padding:24px 30px;text-align:center">
<div style="font-size:24px;font-weight:700">SỔ TIẾT KIỆM</div><div style="font-family:Anton;font-size:56px">300.000.000đ</div><div style="font-size:22px;color:{RED};font-weight:700">ĐÃ RÚT</div></div>'''+foot(1))
p=f'''<div style="position:absolute;left:30px;bottom:0;display:flex;align-items:flex-end">
<div style="margin-right:-50px">{person('m','neutral',1.05,'#4B5563',hair='#C9C5CE',phone=False)}</div>
<div style="margin-right:-50px;z-index:2">{person('m','excited',1.25,SH)}</div>
<div>{person('f','neutral',1.05,'#9D174D',hair='#C9C5CE',phone=False)}</div></div>
{bub('"Gửi ngân hàng<br>lãi có mấy phần trăm,<br>để con đầu tư cho!"','right:40px;top:50px',w=440,fs=32)}'''
S.append(pg(2,p,'Năm đó Nam lãi đậm. Về quê, Nam thuyết phục bố mẹ rút <b>sổ tiết kiệm 300 triệu</b>, khoản tiền bố mẹ để dành cho tuổi già.'))
p=f'''<div style="position:absolute;left:50px;top:60px;width:560px">
{bub('"Hôm nay tài khoản<br>thế nào con?"','left:0;top:0;position:relative',w=420,fs=32)}
<div style="margin-top:70px;margin-left:120px">{bub('"Vẫn lãi mà mẹ…"','left:0;top:0;position:relative',color='#E8E2FF',w=360,fs=32)}</div></div>
<div style="position:absolute;right:10px;bottom:0">{person('m','sad',1.3,SH)}</div>'''
S.append(pg(3,p,'Bữa cơm nào bố mẹ cũng hỏi về tài khoản. Khi thị trường giảm, Nam bắt đầu <b>giấu và nói dối "vẫn lãi"</b>. Đêm nào Nam cũng mở bảng điện tới 2 giờ sáng.'))
p=f'''<div style="position:absolute;left:50px;top:60px">{app('170.000.000đ','▼ −130 triệu',RED,label='Tài khoản của bố mẹ',w=460)}</div>
<div style="position:absolute;left:50px;bottom:50px;background:#FFE6E6;border:5px solid {INK};border-radius:24px;padding:18px 26px;font-size:30px;font-weight:700">🏥 Mẹ cần tiền chữa bệnh</div>
<div style="position:absolute;right:10px;bottom:0">{person('m','sad',1.3,SH)}</div>'''
S.append(pg(4,p,'Đến khi mẹ cần tiền chữa bệnh, tài khoản chỉ còn <b>170 triệu</b>. Nam buộc phải nói thật: đã mất <b>130 triệu</b> tiền dưỡng già của bố mẹ.'))
p=f'''<div style="position:absolute;left:60px;top:70px;width:520px;font-size:32px;font-weight:700;line-height:1.5">
<div style="background:#E8F7EE;border-radius:18px;padding:18px 24px">✅ Tiền nhàn rỗi: mất đi không ảnh hưởng cuộc sống</div>
<div style="background:#FFE6E6;border-radius:18px;padding:18px 24px;margin-top:20px">❌ Tiền dưỡng già, chữa bệnh, học phí, tiền đi vay</div></div>
<div style="position:absolute;right:10px;bottom:10px">{cnd('cool',w=300,h=390)}</div>
{bub('"Mất tiền có thể<br>kiếm lại. Mất<br>niềm tin của<br>bố mẹ thì khó."','right:40px;top:40px',color='#FFF7CC',w=330,fs=28)}'''
S.append(pg(5,p,'Điều đau nhất với Nam không phải 130 triệu, mà là <b>ánh mắt của bố</b>. Chứng khoán luôn có rủi ro, nên tiền bỏ vào phải là tiền <b>có thể chấp nhận mất</b>.'))
S.append(final(head,foot,'TIỀN DƯỠNG GIÀ<br><span style="color:'+RED+'">KHÔNG PHẢI</span><br>TIỀN NHÀN RỖI','Trước khi rủ người thân đầu tư:',['Chỉ dùng tiền mất đi không ảnh hưởng cuộc sống','Không quản lý tiền của người khác khi chưa có kinh nghiệm','Nói thật về rủi ro ngay từ đầu','Không giấu lỗ, càng giấu càng nặng'],GRN,'Gửi cho người đang định<br>"đầu tư hộ" bố mẹ 🙏'))
EPS['tap4']=S
# ---------------- TẬP 5: VN-INDEX (Mai) ----------------
head,foot,pg=ep('CHUYỆN F0 · TẬP 5'); S=[]; SH='#0E7490'
S.append(head+f'''<div class="h1" style="margin-top:50px">VN-INDEX <span style="color:{GRN}">TĂNG</span><br>MÀ TÀI KHOẢN<br>TÔI VẪN <span style="color:{RED}">ĐỎ LÒM</span></div>
<div style="position:absolute;left:30px;bottom:80px">{person('f','shock',1.55,SH)}</div>
<div style="position:absolute;right:60px;bottom:560px;transform:rotate(-4deg);background:#fff;border:6px solid {INK};border-radius:24px;padding:20px 28px"><div style="font-size:24px;font-weight:700">📰 Tin sáng nay</div><div style="font-family:Anton;font-size:46px;color:{GRN}">VN-INDEX ▲ TĂNG ĐIỂM</div></div>
<div style="position:absolute;right:80px;bottom:130px;transform:rotate(4deg)">{app('−8,5%','▼ Danh mục của Mai',RED,label='Lãi/lỗ tuần này',w=380)}</div>'''+foot(1))
p=f'''<div style="position:absolute;left:50px;top:60px;width:560px;display:flex;flex-direction:column;gap:18px">
<div style="background:#E8F7EE;border:5px solid {INK};border-radius:20px;padding:20px 26px;font-size:32px;font-weight:700">📰 VN-Index <span style="color:{GRN}">▲ tăng điểm</span></div>
<div style="background:#FFE6E6;border:5px solid {INK};border-radius:20px;padding:20px 26px;font-size:32px;font-weight:700">📱 Danh mục của Mai <span style="color:{RED}">▼ đỏ</span></div></div>
<div style="position:absolute;right:10px;bottom:0">{person('f','shock',1.3,SH)}</div>
{bub('"Mình bị<br>lừa à?!"','left:80px;bottom:80px',w=280)}'''
S.append(pg(2,p,'Sáng nào Mai cũng thấy tin <b>"VN-Index tăng điểm"</b>. Nhưng mở tài khoản ra, các mã Mai đang giữ <b>vẫn đỏ</b>. Mai bắt đầu nghi ngờ mọi tin tức.'))
students=[('A',9,'#16A34A',150),('B',9,'#16A34A',150),('C',4,RED,70),('D',4,RED,70),('E',3,RED,60),('F',4,RED,70)]
st=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><div style="font-family:Anton;font-size:30px;color:{c}">{s}đ</div><div style="width:{w}px;height:{w}px;border-radius:50%;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:{int(w/3)}px">{n}</div></div>' for n,s,c,w in students)
p=f'''<div style="position:absolute;left:40px;top:50px;font-weight:700;font-size:30px">Lớp học có 6 bạn, bạn to thì điểm nhân hệ số cao</div>
<div style="position:absolute;left:40px;top:150px;display:flex;gap:16px;align-items:flex-end">{st}</div>
<div style="position:absolute;left:40px;bottom:50px;background:{INK};color:#fff;border-radius:20px;padding:18px 26px;font-size:30px;font-weight:700">Điểm trung bình cả lớp vẫn <span style="color:#7CF0A8">TĂNG</span> nhờ A và B</div>'''
S.append(pg(3,p,'Chú nến giải thích: VN-Index giống <b>điểm trung bình của cả lớp</b>, nhưng mỗi bạn có "hệ số" khác nhau, tính theo <b>vốn hóa</b>. Chỉ vài bạn "to" điểm cao là trung bình đã tăng.'))
p=f'''<div style="position:absolute;left:50px;top:60px;width:540px;font-size:30px;font-weight:700;line-height:1.5">
<div style="background:#E8F7EE;border-radius:18px;padding:18px 24px">🐘 Vài cổ phiếu vốn hóa lớn tăng<br>→ VN-Index tăng</div>
<div style="background:#FFE6E6;border-radius:18px;padding:18px 24px;margin-top:20px">🐭 Phần lớn cổ phiếu nhỏ giảm<br>→ danh mục của Mai giảm</div></div>
<div style="position:absolute;right:10px;bottom:0">{person('f','neutral',1.25,SH)}</div>'''
S.append(pg(4,p,'Mai toàn mua cổ phiếu nhỏ, đúng nhóm "các bạn khác" trong lớp. Nên <b>VN-Index tăng không có nghĩa cổ phiếu của Mai tăng</b>.'))
p=f'''<div style="position:absolute;left:60px;top:70px;width:520px">
<div style="font-weight:700;font-size:30px;margin-bottom:16px">Thay vì chỉ nhìn điểm số, hãy xem:</div>
<div style="display:flex;height:80px;border-radius:16px;overflow:hidden;border:4px solid {INK}"><div style="flex:1;background:{GRN};color:#fff;display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:34px">TĂNG</div><div style="flex:3;background:{RED};color:#fff;display:flex;align-items:center;justify-content:center;font-family:Anton;font-size:34px">GIẢM</div></div>
<div style="font-size:26px;font-weight:700;margin-top:14px;color:#6B6375">Bao nhiêu mã tăng, bao nhiêu mã giảm = "độ rộng thị trường"</div></div>
<div style="position:absolute;right:10px;bottom:10px">{cnd('cool',w=300,h=390)}</div>
{bub('"VN-Index là<br>điểm trung bình,<br>không phải<br>điểm của bạn."','right:40px;top:200px',color='#FFF7CC',w=330,fs=28)}'''
S.append(pg(5,p,'Muốn biết thị trường thật sự khỏe hay yếu, hãy xem <b>có bao nhiêu mã tăng, bao nhiêu mã giảm</b>, chứ đừng chỉ nhìn điểm số VN-Index.'))
S.append(final(head,foot,'VN-INDEX<br><span style="color:'+PUR+'">KHÔNG PHẢI</span><br>TÀI KHOẢN CỦA BẠN','3 điều F0 nên nhớ:',['VN-Index tính theo vốn hóa, vài mã lớn chi phối','Xem độ rộng: số mã tăng so với số mã giảm','So danh mục với nhóm cổ phiếu tương tự, không chỉ với chỉ số'],PUR,'Gửi cho người bạn hay than<br>"index xanh mà mình đỏ" 😅'))
EPS['tap5']=S
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        g=await b.new_page(viewport={'width':1080,'height':1350})
        for name,S in EPS.items():
            for i,h in enumerate(S,1):
                fn=f'/home/claude/story/{name}_{i}.html'; open(fn,'w').write(h)
                await g.goto('file://'+fn); await g.wait_for_timeout(250)
                await g.screenshot(path=f'/home/claude/story/{name}_{i}.png')
        await b.close()
asyncio.run(main())
