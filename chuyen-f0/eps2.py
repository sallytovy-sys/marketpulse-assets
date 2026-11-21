import asyncio, sys, os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'episodes.py')).read().split('EPS={}')[0]
exec(src)
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/claude/story'
def kv(items):
    out=''
    for k,v,style in items:
        bg={'a':'#F4F1EA','b':'#FFF1D6','d':INK}[style]; c='#fff' if style=='d' else INK
        out+=f'<div style="display:flex;justify-content:space-between;background:{bg};color:{c};border-radius:16px;padding:16px 22px">{"<span>"+k+"</span><span>"+v+"</span>"}</div>'
    return f'<div style="margin-top:22px;display:flex;flex-direction:column;gap:12px;font-size:27px;font-weight:700">{out}</div>'
def left(inner,top=50,w=490): return f'<div style="position:absolute;left:50px;top:{top}px;width:{w}px">{inner}</div>'
def who(kind,mood,shirt,hair='#1E1A26',scale=1.25,phone=True): return f'<div style="position:absolute;right:10px;bottom:0">{person(kind,mood,scale,shirt,hair,phone)}</div>'
def mascot(text,top=40): return f'<div style="position:absolute;right:10px;bottom:10px">{cnd("cool",w=300,h=390)}</div>'+bub(text,f'right:40px;top:{top}px',color='#FFF7CC',w=330,fs=28)
def line(points,marks=''):
    return f'<svg width="520" height="360" viewBox="0 0 520 360"><polyline points="{points}" fill="none" stroke="{INK}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>{marks}</svg>'
def dot(x,y,c,t,ty):
    a='end' if x>400 else ('start' if x<60 else 'middle'); tx=x+16 if a=='end' else x
    return f'<circle cx="{x}" cy="{y}" r="16" fill="{c}"/><text x="{tx}" y="{ty}" text-anchor="{a}" font-family="BVP" font-weight="700" font-size="24" fill="{c}">{t}</text>'
def cover(head,foot,title,figure,card): return head+f'<div class="h1" style="margin-top:50px">{title}</div><div style="position:absolute;left:30px;bottom:80px">{figure}</div><div style="position:absolute;right:60px;bottom:230px;transform:rotate(5deg)">{card}</div>'+foot(1)
def card(top,big,tag,tagc,w=430):
    return f'<div style="width:{w}px;background:#fff;border:6px solid {INK};border-radius:36px;overflow:hidden"><div style="background:{INK};color:#fff;padding:16px 24px;font-size:22px;font-weight:700">{top}</div><div style="padding:24px 28px"><div style="font-family:Anton;font-size:58px;line-height:1.1">{big}</div><div style="display:inline-block;margin-top:10px;background:{tagc};color:#fff;font-weight:700;font-size:28px;padding:8px 16px;border-radius:12px">{tag}</div></div></div>'
EPS={}
# ---------- TẬP 6: BẮT ĐÁY (Khoa) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 6'); S=[]; SH='#B91C1C'
S.append(cover(head,foot,f'GIẢM 50% RỒI,<br>TÔI TƯỞNG LÀ<br><span style="color:{RED}">ĐÁY</span>. HÓA RA<br>CHỈ LÀ <span style="color:{RED}">GIỮA DỐC</span>',person('m','shock',1.55,SH),card('📉 Cổ phiếu Khoa đang giữ','−50%','Mua ở “đáy” 50.000đ',RED)))
S.append(pg(2,left(f'<div style="font-weight:700;font-size:30px">Cổ phiếu X trong 3 tháng</div>{kv([("Đỉnh","100.000đ","a"),("Hiện tại","50.000đ","b"),("Đã giảm","−50%","d")])}<div style="margin-top:22px;font-family:Anton;font-size:52px;color:{GRN}">“RẺ QUÁ RỒI!”</div>')+who('m','excited',SH)+bub('"Giảm một nửa<br>rồi, còn giảm<br>được nữa à?"','right:40px;top:60px',w=300),
 'Khoa thấy cổ phiếu X giảm từ <b>100.000đ xuống 50.000đ</b>. "Giảm một nửa rồi, chắc là đáy." Khoa dồn toàn bộ <b>200 triệu</b> mua vào một lần.'))
S.append(pg(3,left(line('10,40 140,180 260,200 360,280 470,330',dot(140,180,RED,'Khoa mua',230)+dot(470,330,RED,'25.000đ',300)),60,520)+who('m','shock',SH),
 'Nhưng giá tiếp tục giảm, về <b>25.000đ</b>. Từ chỗ Khoa mua, cổ phiếu <b>giảm thêm 50% nữa</b>. 200 triệu còn 100 triệu.'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">Muốn về lại 50.000đ, từ 25.000đ cần:</div><div style="margin-top:24px;font-family:Anton;font-size:120px;color:{RED};line-height:1">+100%</div><div style="margin-top:18px;font-size:30px;font-weight:700;line-height:1.35">Giảm 50% chỉ cần một nhịp xấu.<br>Tăng 100% có khi mất vài năm.</div>')+who('m','sad',SH),
 '“Giá rẻ” không có nghĩa là “đáy”. Một cổ phiếu đã giảm 50% <b>vẫn có thể giảm thêm 50%</b>, và để quay lại điểm mua, Khoa cần cổ phiếu tăng gấp đôi.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Khoa lẽ ra nên:</div>{kv([("Chia nhỏ lệnh mua","3–4 lần","a"),("Chờ giá ngừng giảm","có xác nhận","b"),("Định trước mức sai","cắt lỗ","d")])}')+mascot('"Đừng cố bắt<br>con dao đang rơi.<br>Chờ nó chạm đất<br>rồi hãy nhặt."',60),
 'Bắt đáy giống bắt <b>con dao đang rơi</b>. Thay vì đoán đáy, nhà đầu tư thường chờ giá ngừng giảm, chia nhỏ tiền và đặt trước mức chấp nhận sai.'))
S.append(final(head,foot,'GIÁ RẺ<br><span style="color:'+RED+'">CHƯA CHẮC</span><br>LÀ ĐÁY','Trước khi “bắt đáy”, F0 nên nhớ:',['Giảm 50% vẫn có thể giảm thêm 50%','Không dồn hết tiền vào một lần mua','Chờ giá ngừng giảm rồi mới vào','Luôn định trước mức cắt lỗ'],RED,'Gửi cho người bạn đang<br>“bắt đáy” mỗi ngày 🔪'))
EPS['tap6']=S
# ---------- TẬP 7: TÍM TRẦN / FOMO (Vy) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 7'); S=[]; SH='#7C3AED'
S.append(cover(head,foot,f'3 PHIÊN <span style="color:{PUR}">TÍM TRẦN</span>,<br>TÔI MUA Ở<br>PHIÊN THỨ 4<br>VÀ <span style="color:{RED}">ĐỨNG ĐỈNH</span>',person('f','shock',1.55,'#7C3AED'),card('📈 Bảng điện hôm nay','+7% ×3','Cả nhóm khoe lãi',PUR)))
S.append(pg(2,chat([('Minh','Mã này tím 3 phiên rồi 🚀🚀🚀','o'),('Trang','Tớ lãi 22% rồi nè','o'),('Hải','Ai chưa lên tàu là phí cả đời','o'),('','Thôi mai tớ vào luôn 😤','me')],title='Hội đầu tư cùng nhau',sub='đang hoạt động').replace('class="phone"','class="phone" style="position:absolute;left:40px;top:40px;width:560px;height:520px"')+who('f','excited','#7C3AED',scale=1.2),
 'Cổ phiếu Y <b>tăng trần 3 phiên liền</b> (sàn HOSE cho phép tăng tối đa 7% mỗi phiên). Nhóm chat bạn bè ai cũng khoe lãi. Vy sợ bị bỏ lại.'))
S.append(pg(3,left(f'<div style="font-weight:700;font-size:30px">Phiên thứ 4, Vy mua</div>{kv([("Giá ban đầu","10.000đ","a"),("Sau 3 phiên trần","≈ 12.250đ","b"),("Vy mua tại","12.250đ","d")])}<div style="margin-top:20px;font-size:30px;font-weight:700">Phần lớn mức tăng đã xảy ra trước khi Vy mua.</div>')+who('f','happy','#7C3AED'),
 'Phiên thứ 4, Vy đặt mua ở giá trần <b>12.250đ</b>. Lệnh khớp ngay, vì có rất nhiều người đang <b>bán ra cho Vy</b>.'))
S.append(pg(4,left(line('10,300 120,230 220,150 300,70 380,170 470,260',dot(300,70,RED,'Vy mua',40)+dot(470,260,RED,'≈ 10.600đ',310)),60,520)+who('f','sad','#7C3AED'),
 'Hai phiên sau, cổ phiếu <b>giảm sàn</b> liên tiếp, còn khoảng <b>10.600đ</b> (−13%). Cổ phiếu mua theo chu kỳ T+2, phải sau 2 ngày làm việc mới về tài khoản để bán, nên Vy <b>không kịp thoát</b>.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">FOMO là gì?</div><div style="margin-top:20px;font-size:32px;font-weight:700;line-height:1.4"><b>F</b>ear <b>O</b>f <b>M</b>issing <b>O</b>ut:<br>sợ bị bỏ lỡ.<br><br>Khi ai cũng khoe lãi,<br>thường là lúc giá đã tăng nhiều.</div>')+mascot('"Khi cả nhóm chat<br>cùng hô mua,<br>hãy hỏi: ai đang<br>bán cho mình?"',60),
 'Mua vì sợ lỡ cơ hội là quyết định <b>dựa trên cảm xúc</b>. Người mua sau cùng thường là người chịu rủi ro lớn nhất.'))
S.append(final(head,foot,'ĐỪNG MUA<br><span style="color:'+PUR+'">VÌ SỢ LỠ</span>','Trước khi đuổi theo mã tăng nóng:',['Tự hỏi: mình mua vì hiểu hay vì sợ lỡ?','Nhớ T+2: mua hôm nay chưa bán được ngay','Mã tăng trần nhiều phiên có thể giảm sàn','Chỉ dùng số tiền chấp nhận được nếu sai'],PUR,'Gửi cho người bạn hay<br>“đu đỉnh” cùng nhóm chat 🎢'))
EPS['tap7']=S
# ---------- TẬP 8: GỒNG LỖ (Bình) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 8'); S=[]; SH='#0369A1'
S.append(cover(head,foot,f'TÔI <span style="color:{RED}">GỒNG LỖ</span><br>TỪ −10% ĐẾN<br><span style="color:{RED}">−50%</span> CHỈ VÌ<br>CHỜ “VỀ BỜ”',person('m','sad',1.55,SH),card('📱 Danh mục của Bình','−50%','Vẫn đang “chờ về bờ”',RED)))
S.append(pg(2,left(f'<div style="font-weight:700;font-size:30px">Bình mua cổ phiếu Z</div>{kv([("Giá mua","50.000đ","a"),("Tuần sau","45.000đ","b"),("Đang lỗ","−10%","d")])}')+who('m','neutral',SH)+bub('"Chưa bán thì<br>chưa lỗ."','right:40px;top:60px',w=300),
 'Bình mua cổ phiếu Z giá <b>50.000đ</b>. Một tuần sau giá còn 45.000đ. Bình tự nhủ: <i>"Chưa bán thì chưa lỗ, chờ về bờ rồi bán."</i>'))
S.append(pg(3,left(line('10,40 120,90 220,160 320,230 470,320',dot(120,90,'#F59E0B','−10%',140)+dot(320,230,RED,'−30%',280)+dot(470,320,RED,'−50%',290)),60,520)+who('m','shock',SH),
 'Giá về 35.000đ (−30%), rồi <b>25.000đ (−50%)</b>. Mỗi lần giảm, Bình lại tắt app và chờ. Tiền bị “kẹt” suốt nhiều tháng, không làm được gì khác.'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">Lỗ bao nhiêu thì cần tăng bao nhiêu để hòa vốn?</div>{kv([("Lỗ 10%","cần +11%","a"),("Lỗ 20%","cần +25%","a"),("Lỗ 30%","cần +43%","b"),("Lỗ 50%","cần +100%","d")])}')+who('m','sad',SH),
 'Lỗ càng sâu, quãng đường quay về càng xa. Từ lỗ 10% chỉ cần tăng 11%, nhưng <b>lỗ 50% thì cần tăng 100%</b> mới hòa vốn.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Cắt lỗ không phải là thua</div><div style="margin-top:20px;font-size:32px;font-weight:700;line-height:1.4">Cắt lỗ là chấp nhận<br>một khoản sai nhỏ<br>để giữ tiền cho<br>cơ hội tiếp theo.</div>')+mascot('"Về bờ không phải<br>chiến lược.<br>Đó là hy vọng."',60),
 'Nhiều nhà đầu tư đặt trước một mức cắt lỗ (ví dụ 7–10% tùy khẩu vị) <b>ngay khi mua</b>, và làm đúng khi giá chạm mức đó, thay vì “chờ về bờ”.'))
S.append(final(head,foot,'CHỜ VỀ BỜ<br><span style="color:'+RED+'">KHÔNG PHẢI</span><br>CHIẾN LƯỢC','Để không gồng lỗ như Bình:',['Đặt mức cắt lỗ ngay khi mua','Lỗ 50% cần tăng 100% mới hòa vốn','“Chưa bán chưa lỗ” là tự an ủi','Tiền kẹt lâu là mất cơ hội khác'],RED,'Gửi cho người bạn đang<br>“gồng” mã đỏ lòm 🧱'))
EPS['tap8']=S
# ---------- TẬP 9: TIKTOKER ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 9'); S=[]; SH='#DB2777'
tk=lambda t,v,l,h=560,mt=150: f'<div style="width:{360 if h<560 else 400}px;height:{h}px;background:{INK};border-radius:40px;padding:26px;color:#fff;position:relative"><div style="font-size:24px;opacity:.7">@keo.x3.moingay</div><div style="font-family:Anton;font-size:58px;margin-top:{mt}px;line-height:1.05">{t}</div><div style="position:absolute;right:24px;bottom:30px;text-align:center;font-size:24px;font-weight:700">❤️<br>{l}<br><br>👁<br>{v}</div></div>'
S.append(cover(head,foot,f'XEM 1 VIDEO<br><span style="color:#DB2777">TIKTOK</span>, TÔI<br>MUA NGAY.<br>NGƯỜI QUAY ĐÃ <span style="color:{RED}">BÁN</span>',person('m','shock',1.55,SH),tk('KÈO X3<br>TRONG<br>1 THÁNG 🚀','1,2tr','86k',420,70)))
S.append(pg(2,f'<div style="position:absolute;left:60px;top:30px">{tk("MÃ NÀY<br>SẮP X3,<br>VÀO NGAY!","1,2tr","86k")}</div>'+who('m','excited',SH)+bub('"1 triệu view<br>chắc chuẩn!"','right:40px;top:60px',w=300),
 'Đức lướt TikTok, thấy video <b>1,2 triệu lượt xem</b>: "Mã này sắp x3, vào ngay kẻo lỡ!" Người quay video có hàng trăm nghìn người theo dõi.'))
S.append(pg(3,left(line('10,300 140,280 240,160 320,90 400,200 480,300',dot(140,280,GRN,'Người quay mua',330)+dot(320,90,RED,'Đức mua',50)),60,520)+who('m','happy',SH),
 'Sáng hôm sau, rất nhiều người cùng mua, giá tăng mạnh. Đức mua ở vùng giá cao. Điều Đức không biết: <b>người quay video đã mua từ trước</b>, khi giá còn thấp.'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">Ai bán khi đám đông mua?</div>{kv([("Người quay video","mua sớm, giá thấp","a"),("Người xem","mua sau, giá cao","b"),("Kết quả","người xem chịu lỗ","d")])}')+who('m','sad',SH),
 'Khi người xem đổ vào mua, người đã mua sớm có thể <b>bán ra cho chính họ</b>. Vài phiên sau, giá giảm mạnh. Video vẫn còn đó, nhưng không ai nhắc lại “kèo” này nữa.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Trước khi tin một video, hỏi:</div>{kv([("Người nói có chứng chỉ hành nghề?","?","a"),("Họ có đang giữ mã đó?","?","b"),("Có số liệu, nguồn kiểm chứng?","?","d")])}')+mascot('"Lượt xem không<br>phải bằng chứng.<br>Số liệu mới là."',60),
 'Nhiều lượt xem không có nghĩa là đúng. Người nói về cổ phiếu trên mạng <b>có thể đang có lợi ích</b> từ việc bạn mua.'))
S.append(final(head,foot,'VIEW CAO<br><span style="color:#DB2777">KHÔNG PHẢI</span><br>BẰNG CHỨNG','Trước khi mua theo video mạng xã hội:',['Kiểm tra người nói là ai, có lợi ích gì','Tự xem báo cáo tài chính, không chỉ nghe','Cẩn trọng với lời hứa “x2, x3”','Không mua vì sợ lỡ trend'],'#DB2777','Gửi cho người bạn hay<br>“mua theo TikTok” 📱'))
EPS['tap9']=S
# ---------- TẬP 10: LƯỚT SÓNG, PHÍ VÀ THUẾ (Phúc) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 10'); S=[]; SH='#15803D'
S.append(cover(head,foot,f'LƯỚT SÓNG<br><span style="color:{GRN}">50 LỆNH</span> 1 THÁNG,<br>TIỀN LÃI<br>CHẢY VÀO <span style="color:{RED}">PHÍ</span>',person('m','shock',1.55,SH),card('🧾 Sao kê tháng này','50 lệnh','Lãi thì ít, phí thì nhiều','#F59E0B')))
S.append(pg(2,left(f'<div style="font-weight:700;font-size:30px">Phúc “lướt sóng” mỗi ngày</div>{kv([("Vốn","100 triệu","a"),("Số lần mua + bán/tháng","25 vòng","b"),("Tổng tiền mua trong tháng","≈ 2,5 tỷ","d")])}')+who('m','excited',SH)+bub('"Ăn 1–2%<br>mỗi lệnh là<br>ngon rồi!"','right:40px;top:60px',w=300),
 'Phúc có <b>100 triệu</b>, mua bán gần như mỗi ngày, ăn chênh lệch 1–2% mỗi lần. Một tháng Phúc mua rồi bán <b>25 vòng</b>, tổng số tiền mua vào khoảng 2,5 tỷ đồng.'))
S.append(pg(3,left(f'<div style="font-weight:700;font-size:30px">Mỗi vòng mua + bán 100 triệu (ví dụ):</div>{kv([("Phí mua 0,15%","150.000đ","a"),("Phí bán 0,15%","150.000đ","a"),("Thuế bán 0,1%","100.000đ","b"),("Tổng mỗi vòng","400.000đ","d")])}<div style="margin-top:16px;font-size:24px;color:#6B6375">Mức phí tùy công ty chứng khoán; thuế 0,1% tính trên giá trị bán, kể cả khi lỗ.</div>')+who('m','neutral',SH),
 'Mỗi lần mua và bán đều mất <b>phí giao dịch</b>, và khi bán còn bị trừ <b>thuế 0,1%</b> trên giá trị bán, dù lệnh đó lãi hay lỗ.'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">25 vòng trong một tháng:</div><div style="margin-top:24px;font-family:Anton;font-size:110px;color:{RED};line-height:1">10 TRIỆU</div><div style="margin-top:18px;font-size:30px;font-weight:700;line-height:1.35">= 10% số vốn<br>trả cho phí và thuế</div>')+who('m','shock',SH),
 '25 vòng × 400.000đ = <b>10 triệu đồng</b>, tức 10% số vốn mỗi tháng. Phúc phải lãi hơn 10% mỗi tháng <b>chỉ để hòa</b>. Mà không phải lệnh nào cũng lãi.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Giao dịch càng nhiều…</div>{kv([("Phí và thuế","càng nhiều","a"),("Quyết định cảm xúc","càng nhiều","b"),("Lợi nhuận","chưa chắc nhiều hơn","d")])}')+mascot('"Thị trường không<br>trả lương theo<br>số lệnh bạn đặt."',60),
 'Lướt sóng không sai, nhưng cần <b>tính chi phí trước</b>. Nhiều người lãi trên từng lệnh nhưng cuối tháng vẫn lỗ vì phí và thuế.'))
S.append(final(head,foot,'MUA BÁN NHIỀU<br><span style="color:'+GRN+'">KHÔNG CÓ NGHĨA</span><br>LÃI NHIỀU','Trước khi lướt sóng, F0 nên nhớ:',['Mỗi vòng mua bán đều mất phí','Thuế bán 0,1% kể cả khi lỗ','Tính chi phí cả tháng, không chỉ từng lệnh','Biết rõ biểu phí công ty chứng khoán của mình'],GRN,'Gửi cho người bạn<br>“ngày nào cũng lướt” 🏄'))
EPS['tap10']=S
# ---------- TẬP 11: TIẾT KIỆM VS CỔ PHIẾU (chị Thu) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 11'); S=[]; SH='#B45309'
S.append(cover(head,foot,f'RÚT <span style="color:#B45309">SỔ TIẾT KIỆM</span><br>MUA CỔ PHIẾU,<br>ĐÚNG LÚC CẦN<br>TIỀN THÌ <span style="color:{RED}">ĐANG LỖ</span>',person('f','shock',1.55,'#B45309'),card('🏦 Sổ tiết kiệm','200 triệu','Đã rút trước hạn','#B45309')))
S.append(pg(2,left(f'<div style="font-weight:700;font-size:30px">Chị Thu so sánh</div>{kv([("Gửi tiết kiệm (ví dụ)","≈ 5%/năm","a"),("Bạn khoe cổ phiếu","+30% năm qua","b")])}<div style="margin-top:22px;font-family:Anton;font-size:52px;color:#B45309">“GỬI NGÂN HÀNG PHÍ QUÁ!”</div>')+who('f','excited','#B45309')+bub('"Tiền nhà<br>sang năm mới<br>cần mà…"','right:40px;top:60px',w=300),
 'Chị Thu có <b>200 triệu</b> gửi tiết kiệm, dự định dùng để sửa nhà vào năm sau. Thấy bạn khoe lãi cổ phiếu, chị rút sổ trước hạn để mua.'))
S.append(pg(3,left(line('10,200 120,140 220,170 320,240 420,280 500,250',dot(10,200,GRN,'',0)+dot(420,280,RED,'Cần tiền ở đây',330)),60,520)+who('f','sad','#B45309'),
 '6 tháng sau, thị trường điều chỉnh, danh mục của chị <b>đang lỗ 20%</b>, đúng lúc thợ báo giá sửa nhà. Chị phải <b>bán cắt lỗ</b> để có tiền.'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">Kết quả sau 1 năm (ví dụ)</div>{kv([("Nếu giữ sổ tiết kiệm","≈ 210 triệu","a"),("Thực tế của chị Thu","≈ 160 triệu","d")])}<div style="margin-top:20px;font-size:30px;font-weight:700">Chênh lệch khoảng 50 triệu.</div>')+who('f','sad','#B45309'),
 'Cổ phiếu có thể lãi cao hơn tiết kiệm <b>trong dài hạn</b>, nhưng có những năm giảm. Tiền cần dùng trong 1–2 năm tới không có thời gian để chờ giá hồi.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Chia tiền theo thời gian cần dùng</div>{kv([("Quỹ dự phòng 3–6 tháng chi tiêu","tiết kiệm","a"),("Cần dùng trong 1–2 năm","tiết kiệm / an toàn","b"),("Không cần dùng 3–5 năm","có thể đầu tư","d")])}')+mascot('"Tiết kiệm và<br>cổ phiếu không<br>đối đầu. Mỗi loại<br>có việc riêng."',60),
 'Không phải “tiết kiệm hay cổ phiếu”, mà là <b>tiền nào cho việc nào</b>. Tiền sắp dùng nên ở nơi an toàn; tiền dài hạn mới chịu được biến động.'))
S.append(final(head,foot,'TIỀN SẮP DÙNG<br><span style="color:#B45309">ĐỪNG</span> ĐƯA VÀO<br>CỔ PHIẾU','Trước khi rút sổ tiết kiệm đầu tư:',['Giữ quỹ dự phòng 3–6 tháng chi tiêu','Tiền cần trong 1–2 năm: để nơi an toàn','Chỉ đầu tư tiền 3–5 năm không cần dùng','Cổ phiếu có năm tăng, có năm giảm'],'#B45309','Gửi cho người đang định<br>“rút sổ” mua cổ phiếu 🏦'))
EPS['tap11']=S
# ---------- TẬP 12: LÃI KỶ LỤC MÀ VẪN LỖ (Hà) ----------
head,foot,pg=ep('CHUYỆN F0 · TẬP 12'); S=[]; SH='#1D4ED8'
news=lambda t: f'<div style="width:440px;background:#fff;border:6px solid {INK};border-radius:30px;padding:24px 28px"><div style="font-size:22px;color:#6B6375;font-weight:700">📰 TIN NÓNG · 8:30</div><div style="font-family:Anton;font-size:46px;line-height:1.15;margin-top:10px">{t}</div></div>'
S.append(cover(head,foot,f'CÔNG TY BÁO<br><span style="color:{GRN}">LÃI KỶ LỤC</span>,<br>TÔI MUA VÀO<br>VÀ <span style="color:{RED}">LỖ 15%</span>',person('f','shock',1.55,SH),news('Công ty K báo lãi quý cao kỷ lục, tăng 80%')))
S.append(pg(2,f'<div style="position:absolute;left:60px;top:60px">{news("Công ty K báo lãi quý cao kỷ lục, tăng 80%")}</div>'+who('f','excited',SH)+bub('"Lãi kỷ lục<br>thì giá phải<br>tăng chứ!"','right:40px;top:60px',w=300),
 'Sáng thứ Hai, Hà đọc tin: công ty K báo <b>lợi nhuận quý cao kỷ lục, tăng 80%</b>. "Tin tốt thế này, giá chắc chắn tăng." Hà mua ngay lúc mở cửa.'))
S.append(pg(3,left(line('10,320 120,250 220,170 300,100 330,90 420,190 500,240',dot(220,170,GRN,'Tin đồn lãi lớn',262)+dot(330,90,RED,'Tin ra, Hà mua',55)),60,520)+who('f','sad',SH),
 'Nhưng ngay trong phiên, giá đảo chiều giảm. Hai tuần sau, cổ phiếu <b>thấp hơn giá Hà mua 15%</b>. Hà không hiểu: “Lãi kỷ lục mà sao giá giảm?”'))
S.append(pg(4,left(f'<div style="font-weight:700;font-size:30px">Giá đã “biết” trước tin</div>{kv([("2 tháng trước","giá tăng 40%","a"),("Thị trường kỳ vọng","lãi tăng 100%","b"),("Thực tế công bố","lãi tăng 80%","d")])}<div style="margin-top:18px;font-size:30px;font-weight:700">Kỷ lục, nhưng thấp hơn kỳ vọng.</div>')+who('f','neutral',SH),
 'Giá cổ phiếu phản ánh <b>kỳ vọng</b>. Trước đó giá đã tăng 40% vì nhiều người đoán lãi sẽ rất lớn. Khi con số thật thấp hơn kỳ vọng, người mua sớm <b>chốt lời</b>.'))
S.append(pg(5,left(f'<div style="font-weight:700;font-size:30px">Trước khi mua theo tin tốt:</div>{kv([("Giá đã tăng bao nhiêu trước tin?","?","a"),("Kết quả so với kỳ vọng?","?","b"),("Định giá (P/E) đang ở đâu?","?","d")])}')+mascot('"Tin tốt ai cũng<br>biết thì thường<br>đã nằm trong giá."',60),
 'Tin tốt không đồng nghĩa với giá tăng. Câu hỏi quan trọng là: <b>tin này đã được phản ánh vào giá chưa</b>, và kết quả có tốt hơn điều thị trường chờ đợi không.'))
S.append(final(head,foot,'TIN TỐT<br><span style="color:'+BLUE+'">CHƯA CHẮC</span><br>GIÁ TĂNG','Khi đọc tin “lãi kỷ lục”, F0 nên nhớ:',['Giá phản ánh kỳ vọng, không chỉ kết quả','Xem giá đã tăng bao nhiêu trước tin','So kết quả với kỳ vọng của thị trường','Đừng mua chỉ vì tiêu đề tin tức'],BLUE,'Gửi cho người bạn hay<br>“mua theo tin” 📰'))
EPS['tap12']=S
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        g=await b.new_page(viewport={'width':1080,'height':1350})
        for name,S in EPS.items():
            n=name[3:]; d=os.path.join(OUT,f'tap{n}'); os.makedirs(d,exist_ok=True)
            for i,h in enumerate(S,1):
                fn=f'/tmp/{name}_{i}.html'; open(fn,'w').write(h)
                await g.goto('file://'+fn); await g.wait_for_timeout(250)
                await g.screenshot(path=os.path.join(d,f'tap{n}_{i}.png'))
        await b.close()
asyncio.run(main())
