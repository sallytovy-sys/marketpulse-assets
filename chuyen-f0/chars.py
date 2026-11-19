from storylib import *
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
