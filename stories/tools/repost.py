import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F=lambda n,s: ImageFont.truetype(f'/root/.fonts/{n}' if False else __import__('os').path.expanduser(f'~/.fonts/{n}'), s)
BG={'sang':(29,95,209),'chieu':(232,93,0),'f0':(255,244,228)}
def make(src,kind,label,out):
    W,H=1080,1920
    bg=BG[kind]; light=kind!='f0'
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    fg=(255,255,255) if light else (30,30,40)
    # header (inside safe zone, starts ~ y=250)
    logo=Image.open('/home/claude/logo/final/marketpulse_icon_1080.png').convert('RGBA').resize((84,84))
    im.paste(logo,(90,250),logo)
    d.text((192,256),'MarketPulse.Vn',font=F('BeVietnamPro-Bold.ttf',40),fill=fg)
    d.text((192,304),label,font=F('BeVietnamPro-Medium.ttf',30),fill=fg)
    pill='BÀI MỚI'; pf=F('BeVietnamPro-Bold.ttf',30)
    tw=d.textlength(pill,font=pf)
    pc=(255,255,255) if light else (29,95,209); tc=bg if light else (255,255,255)
    d.rounded_rectangle((W-90-tw-48,262,W-90,322),radius=30,fill=pc)
    d.text((W-90-tw-24,270),pill,font=pf,fill=tc)
    # card
    card=Image.open(src).convert('RGB'); cw=900; ch=round(card.height*cw/card.width)
    card=card.resize((cw,ch),Image.LANCZOS)
    x=(W-cw)//2; y=400+(1150-ch)//2
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((x,y+18,x+cw,y+ch+18),36,fill=110)
    sh=sh.filter(ImageFilter.GaussianBlur(28))
    im.paste(Image.new('RGB',(W,H),(0,0,0)),(0,0),sh)
    m=Image.new('L',(cw,ch),0); ImageDraw.Draw(m).rounded_rectangle((0,0,cw,ch),36,fill=255)
    im.paste(card,(x,y),m)
    # CTA
    cf=F('BeVietnamPro-Bold.ttf',38); cta='Xem đầy đủ trong bài viết mới nhất'
    tw=d.textlength(cta,font=cf)
    d.rounded_rectangle(((W-tw)//2-40,1600,(W+tw)//2+40,1690),radius=45,fill=(255,255,255) if light else (30,30,40))
    d.text(((W-tw)//2,1620),cta,font=cf,fill=bg if light else (255,255,255))
    im.save(out,quality=92)
make(*sys.argv[1:])
