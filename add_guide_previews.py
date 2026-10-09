from pathlib import Path
from html import escape
import re
root=Path.home()/'Desktop/DesktopPreset-ChatGPT-Ads-Landing'
guides=root/'guides'
labels={
 'en':('Product preview (not an interface screenshot)','See the relevant product'),
 'ja':('製品プレビュー（操作画面のスクリーンショットではありません）','関連する製品を見る'),
 'de':('Produktvorschau (kein Screenshot der Bedienoberfläche)','Passendes Produkt ansehen'),
 'fr':('Aperçu du produit (pas une capture de l’interface)','Voir le produit correspondant'),
 'it':('Anteprima prodotto (non è uno screenshot dell’interfaccia)','Vedi il prodotto')
}
count=0
for kind in ('obs','luma'):
 for p in guides.glob(f'{kind}-luts-*.html'):
  lang=p.stem.rsplit('-',1)[1]
  img='obs.jpg' if kind=='obs' else 'lumafusion.jpg'
  caption,link=labels[lang]
  s=p.read_text()
  anchor='<ol class="steps">'
  if 'class="product-preview"' in s:continue
  insertion=f'<figure class="product-preview"><img src="../assets/{img}" width="850" height="739" loading="lazy" decoding="async" alt="{escape(caption,quote=True)}"><figcaption>{escape(caption)}</figcaption></figure>'
  assert anchor in s,p
  s=s.replace(anchor,insertion+anchor,1)
  s=s.replace('</style>','.product-preview{margin:25px 0}.product-preview img{width:100%;height:auto;max-height:430px;object-fit:cover;border-radius:14px;display:block}.product-preview figcaption{font-size:13px;color:#68726b;margin-top:9px}</style>',1)
  p.write_text(s);count+=1
print('Updated guide images:',count)
