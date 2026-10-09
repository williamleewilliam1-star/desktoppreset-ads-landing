from pathlib import Path
from html import escape
from urllib.parse import urlencode
import json

root=Path.home()/'Desktop/DesktopPreset-ChatGPT-Ads-Landing'
guides=root/'guides'
guides.mkdir(exist_ok=True)
base='https://williamleewilliam1-star.github.io/desktoppreset-ads-landing/guides/'
shop='https://www.etsy.com/shop/DesktopPreset'
products={'obs':'https://www.etsy.com/listing/4368054532','luma':'https://www.etsy.com/listing/4355306048'}
source={'obs':'https://obsproject.com/kb/apply-lut-filter','luma':'https://luma-touch.com/wp-content/uploads/2020/07/LumaFusion-Reference-Guide.pdf'}
content={
'en':{
'obs':('How to Add .CUBE LUTs in OBS Studio: Natural Webcam Color',
'Learn how to apply a creative .cube LUT to an OBS camera source without losing natural skin tones. This guide is for streamers and creators who want repeatable results rather than one-click miracles.',
['Prepare a well-exposed webcam image first. Lock white balance and exposure when possible, and position a soft light so skin tones are not dominated by an RGB accent lamp.','Open OBS Studio. In Sources, select the webcam or video capture source, then choose Filters. Under Effect Filters, add Apply LUT.','Use Browse beside the Path setting to select a compatible .cube file. OBS also supports LUTs supplied as .png files, but a conventional image is not itself a valid LUT.','Start with a subtle strength using the Amount slider, then examine skin, white objects, highlights, and dark backgrounds. Compare against the unfiltered camera before you commit.','If the image becomes orange, green, crushed, or washed out, turn off the LUT and check the camera input and color space before increasing intensity.'],
'What a LUT can and cannot fix',
'A look-up table maps input colors to output colors. It is useful for creative contrast and palette adjustments, but it does not replace correct lighting, exposure, or camera color management. A Rec.709-oriented creative LUT should be tested against an appropriate Rec.709 input, not blindly placed on log-encoded footage.',
'DesktopPreset offers an OBS-focused set of Rec.709 .CUBE looks for webcam, LED, and neon-light setups. Verify the product details and your camera workflow before purchasing.'),
'luma':('How to Import .CUBE LUTs into LumaFusion on iPad or iPhone',
'This step-by-step guide explains importing a custom color LUT into LumaFusion and applying it gently to mobile footage. The exact layout can differ across app versions.',
['Download your purchased or free LUT pack, unzip it in the Files app if needed, and locate the .cube file. Keep the original file in a folder you can find again.','In LumaFusion, open the project, select a clip on the timeline, and enter its Color & Effects editor. Find the LUT section or User LUT category.','Choose Import LUT, select the storage location, select your .cube file and confirm Import. LumaFusion documentation also describes .3dl as a supported import format.','Select the newly imported LUT. Use the Blend control to reduce the effect if it is too strong, then compare skin tones and exposure with the untreated clip.','Export a short test clip and inspect it on the intended display. If a camera records Log, normalize that footage appropriately before applying a creative Rec.709 look.'],
'Why a cinematic LUT sometimes looks wrong',
'Creative LUTs assume particular input colors and exposure. A LUT built for standard Rec.709 video may produce excessive contrast or inaccurate colors on Apple Log or other log footage unless the color space is transformed first. Use a technical conversion when required and a creative LUT afterward.',
'DesktopPreset has cinematic .CUBE LUT packs aimed at LumaFusion workflows. Check the exact format, footage requirements, and current product description before buying.')
},
'ja':{
'obs':('OBS Studioに.CUBE LUTを追加する方法｜自然なウェブカメラの色調整',
'OBSの「Apply LUT」フィルターでウェブカメラの色を整える基本手順です。フィルターだけで照明や露出の問題をすべて解決できるわけではありません。',
['まず照明、露出、ホワイトバランスを調整し、肌色が不自然にならない状態を作ります。','OBSの「ソース」でカメラを選択し「フィルタ」を開きます。「エフェクトフィルタ」に「Apply LUT」を追加します。','「Path」で対応する.cubeファイルを選択します。OBSは.png形式のLUTにも対応しています。','「Amount」で適用量を下げ、肌色・白い部分・暗部を比較しながら調整します。','色が極端に変わる場合は、カメラの設定や入力の色空間を先に確認してください。'],
'LUTを使う前に知っておきたいこと',
'LUTは色の変換表です。照明や露出の修正を完全に代行するものではありません。Rec.709向けのクリエイティブLUTは、適切な入力映像で試してください。',
'DesktopPresetではOBS向けのRec.709 .CUBE LUTを提供しています。ご購入前に対応条件を確認してください。'),
'luma':('LumaFusionで.CUBE LUTを読み込む方法｜iPad・iPhone',
'LumaFusionでカスタムLUTを読み込んで、動画の色調を調整するためのガイドです。アプリのバージョンによって画面の名称が異なる場合があります。',
['LUTファイルをダウンロードし、必要なら「ファイル」アプリでZIPを解凍します。','LumaFusionでクリップを選び、「Color & Effects」の編集画面を開きます。','LUTの「Import」機能で保存先を選び、.cubeファイルを指定して読み込みます。','読み込んだLUTを選択し、「Blend」で強さを調整します。','短い動画を書き出し、肌色やコントラストを確認します。Log映像の場合は事前の正しい色空間変換が重要です。'],
'色が不自然に見える理由',
'クリエイティブLUTには想定する入力色空間があります。Apple Logなどの映像にRec.709向けLUTを直接適用すると、色やコントラストが崩れることがあります。',
'DesktopPresetではLumaFusionで使用できるシネマティックな.CUBE LUTパックを販売しています。商品説明で互換性をご確認ください。')
},
'de':{
'obs':('CUBE-LUTs in OBS Studio importieren: natürliche Webcam-Farben',
'Eine praktische Anleitung für Streamer: Mit dem OBS-Filter „Apply LUT“ lässt sich die Farbwirkung einer Kamera gezielt verändern. Eine LUT ersetzt jedoch keine gute Beleuchtung.',
['Zuerst Belichtung, Weißabgleich und Licht der Webcam sauber einstellen.','In OBS die Kameraquelle auswählen, „Filter“ öffnen und unter Effektfiltern „Apply LUT“ hinzufügen.','Unter „Path“ eine passende .cube-Datei auswählen. OBS unterstützt auch LUT-Dateien im .png-Format.','Mit „Amount“ die Stärke reduzieren und Hauttöne, Weiß und Schatten kontrollieren.','Bei unnatürlichen Farben den Filter deaktivieren und Eingangsfarbraum sowie Kameraeinstellungen prüfen.'],
'Was eine LUT leisten kann',
'Eine Lookup-Tabelle bildet Farbwerte auf andere Farbwerte ab. Sie kann einen kreativen Look hinzufügen, aber weder falsche Belichtung noch ungeeignetes Licht vollständig reparieren.',
'DesktopPreset bietet .CUBE-LUTs für OBS und Rec.709-Webcam-Workflows. Bitte vor dem Kauf die Produktanforderungen prüfen.'),
'luma':('Eigene .CUBE-LUTs in LumaFusion auf iPad und iPhone importieren',
'So importierst du eine eigene Farb-LUT in LumaFusion und wendest sie kontrolliert an. Menünamen können sich mit App-Versionen ändern.',
['Die LUT-Datei herunterladen, ZIP-Dateien gegebenenfalls in der Dateien-App entpacken.','.cube-Datei auf dem Gerät oder in einem erreichbaren Speicherordner ablegen.','In LumaFusion einen Timeline-Clip und anschließend „Color & Effects“ öffnen.','Über „Import LUT“ die .cube-Datei auswählen und importieren.','LUT anwenden und mit dem Blend-Regler dosieren. Danach einen kurzen Testclip exportieren.'],
'Wichtig: Log-Material und Rec.709',
'Eine kreative Rec.709-LUT kann direkt auf Log-Aufnahmen zu falschen Kontrasten und Farben führen. Falls nötig zuerst technisch nach Rec.709 transformieren und anschließend den kreativen Look anwenden.',
'DesktopPreset bietet passende .CUBE-Look-Pakete für LumaFusion. Die individuellen Kompatibilitätsangaben stehen im Etsy-Angebot.')
},
'fr':{
'obs':('Installer un LUT .CUBE dans OBS Studio : corriger les couleurs de webcam',
'Guide pour appliquer un look colorimétrique dans OBS sans exagérer les couleurs de peau. Un LUT ne remplace pas un éclairage correct.',
['Réglez d’abord la lumière, l’exposition et la balance des blancs de la caméra.','Dans OBS, sélectionnez la source vidéo, ouvrez « Filtres » puis ajoutez « Apply LUT » aux filtres d’effet.','Choisissez un fichier .cube compatible dans le champ du chemin. OBS accepte également les LUT au format .png.','Diminuez « Amount » si le résultat est trop intense ; comparez la peau, les blancs et les ombres.','Si les couleurs deviennent étranges, vérifiez les réglages et l’espace colorimétrique du signal source.'],
'Ce qu’un LUT peut faire',
'Une table de correspondance transforme des valeurs de couleur. Elle apporte un style, mais ne corrige pas entièrement une mauvaise exposition ou un éclairage inadapté.',
'DesktopPreset propose des LUT .CUBE pour les workflows webcam OBS en Rec.709. Vérifiez les caractéristiques avant achat.'),
'luma':('Importer un LUT .CUBE dans LumaFusion sur iPad ou iPhone',
'Découvrez comment importer puis doser un LUT personnalisé dans LumaFusion. Les intitulés peuvent varier selon la version.',
['Téléchargez et décompressez votre pack dans l’application Fichiers si nécessaire.','Dans LumaFusion, sélectionnez un plan sur la timeline et ouvrez « Color & Effects ».','Dans la section LUT, utilisez « Import LUT » et choisissez le fichier .cube.','Appliquez le LUT puis ajustez l’intensité avec le contrôle Blend.','Exportez un court essai et contrôlez les teintes de peau et le contraste.'],
'Attention aux vidéos Log',
'Un LUT créatif prévu pour du Rec.709 peut dégrader une image Apple Log appliqué directement. Effectuez d’abord, si nécessaire, la conversion colorimétrique technique.',
'DesktopPreset vend des packs de LUT cinématiques .CUBE adaptés à LumaFusion. Consultez la fiche produit pour les conditions exactes.')
},
'it':{
'obs':('Come applicare LUT .CUBE in OBS Studio per una webcam naturale',
'Una guida pratica per usare il filtro Apply LUT di OBS senza alterare eccessivamente l’incarnato. Una LUT non sostituisce una buona illuminazione.',
['Prima imposta esposizione, bilanciamento del bianco e luce della webcam.','In OBS seleziona la sorgente video, apri Filtri e aggiungi Apply LUT tra i filtri effetti.','Nel campo Path seleziona un file .cube compatibile. OBS supporta anche LUT in formato .png.','Riduci Amount quando l’effetto è troppo intenso; controlla pelle, bianchi e ombre.','Se i colori sono innaturali, verifica prima le impostazioni della videocamera e lo spazio colore.'],
'Cosa può fare una LUT',
'Una lookup table rimappa i valori cromatici e permette un look creativo. Non può compensare del tutto illuminazione o esposizione sbagliate.',
'DesktopPreset propone LUT .CUBE Rec.709 pensate per la webcam in OBS. Verifica i requisiti prima dell’acquisto.'),
'luma':('Come importare LUT .CUBE in LumaFusion su iPad e iPhone',
'Guida per importare LUT personalizzate in LumaFusion e regolarne l’intensità. Le voci dell’interfaccia possono variare con la versione.',
['Scarica il pacchetto LUT e, se necessario, estrai lo ZIP nell’app File.','Seleziona un clip nella timeline di LumaFusion e apri Color & Effects.','Nella sezione LUT usa Import LUT per scegliere il file .cube.','Applica la LUT e regola l’intensità con Blend.','Esporta una clip di prova e controlla l’incarnato e il contrasto.'],
'Log e Rec.709 non sono la stessa cosa',
'Una LUT creativa per Rec.709 applicata direttamente a un video Apple Log può creare colori errati. Prima effettua, se necessaria, una conversione tecnica dello spazio colore.',
'DesktopPreset offre pacchetti di LUT cinematiche .CUBE per LumaFusion. Controlla i dettagli di compatibilità nella scheda Etsy.')
}
}

langs={'en':'English','ja':'日本語','de':'Deutsch','fr':'Français','it':'Italiano'}
css="""body{font:16px/1.68 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f8f7f3;color:#202322;margin:0}main{max-width:790px;margin:auto;padding:28px 24px 80px}a{color:#225e59}header,footer{padding:20px 0;border-bottom:1px solid #d9d9d2}nav{display:flex;gap:12px;flex-wrap:wrap;font-size:14px}.eyebrow{letter-spacing:.15em;text-transform:uppercase;font-size:12px;color:#667}h1{font-size:clamp(31px,5vw,48px);line-height:1.14;letter-spacing:-.045em;margin:24px 0}h2{font-size:23px;margin-top:40px}li{margin:15px 0;padding-left:6px}.note{background:#eeeee7;border-left:3px solid #536c61;padding:18px 22px;margin:30px 0}.cta{border:1px solid #d7dbd3;border-radius:14px;background:#fff;padding:24px;margin-top:38px}.cta a{font-weight:700}footer{border:0;border-top:1px solid #ddd;color:#666;font-size:13px;margin-top:50px}.meta{color:#677; font-size:14px}.lang{margin:12px 0 24px;display:flex;gap:12px;flex-wrap:wrap}.lang a{text-decoration:none}"""

for language,items in content.items():
 for kind,(title,intro,steps,sub,explanation,ad) in items.items():
  fname=f'{kind}-luts-{language}.html'
  url=base+fname
  alt=''.join(f'<link rel="alternate" hreflang="{code}" href="{base}{kind}-luts-{code}.html">' for code in langs)
  switch=' '.join(f'<a href="{kind}-luts-{code}.html" hreflang="{code}">{label}</a>' for code,label in langs.items())
  params=urlencode({'utm_source':'desktoppreset_guides','utm_medium':'organic_content','utm_campaign':f'{kind}_guide_{language}'})
  etsy=products[kind]+'?'+params
  article=f'''<!doctype html><html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | DesktopPreset Guides</title><meta name="description" content="{escape(intro[:155],quote=True)}">
<link rel="canonical" href="{url}">{alt}<style>{css}</style>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"HowTo","name":title,"description":intro,"inLanguage":language,"author":{"@type":"Organization","name":"DesktopPreset"},"step":[{"@type":"HowToStep","text":x} for x in steps],"url":url},ensure_ascii=False).replace('</','<\\/')}</script></head>
<body><main><header><a href="../">DesktopPreset</a> / <a href="index.html">Guides</a></header>
<p class="eyebrow">DesktopPreset · Creator education</p><h1>{escape(title)}</h1><p class="meta">Updated 9 October 2026 · Independent educational guide</p><div class="lang">{switch}</div>
<p>{escape(intro)}</p><h2>Steps / 手順 / Schritte / Étapes / Passaggi</h2><ol>{''.join('<li>'+escape(step)+'</li>' for step in steps)}</ol>
<h2>{escape(sub)}</h2><p>{escape(explanation)}</p><div class="note"><strong>Reference / Source</strong><p><a href="{source[kind]}" rel="noopener noreferrer">Official {'OBS Studio' if kind=='obs' else 'LumaTouch LumaFusion'} documentation</a>. Consult the current app interface because features and labels can change.</p></div>
<section class="cta"><strong>Explore DesktopPreset</strong><p>{escape(ad)}</p><p><a href="{etsy}" rel="sponsored noopener noreferrer">View relevant DesktopPreset LUTs on Etsy →</a></p><p><a href="{shop}">Visit the full DesktopPreset shop</a></p><small>Products are sold and delivered by Etsy. No affiliation with OBS Studio or LumaTouch is claimed.</small></section>
<footer>© 2026 DesktopPreset · Creator education, not a substitute for product compatibility information.</footer></main></body></html>'''
  (guides/fname).write_text(article,encoding='utf8')

index='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Color Grading Guides — DesktopPreset</title><meta name="description" content="Free practical guides for OBS Studio, LumaFusion and creative .CUBE LUT workflows."><style>'''+css+'''</style></head><body><main><header><a href="../">DesktopPreset</a></header><p class="eyebrow">Free guides</p><h1>Color grading, explained.</h1><p>Practical tutorials for editors and creators. Our articles explain the steps before suggesting an optional product.</p><h2>LumaFusion</h2><p><a href="luma-luts-en.html">Import and adjust .CUBE LUTs in LumaFusion</a></p><h2>OBS Studio</h2><p><a href="obs-luts-en.html">Apply .CUBE LUTs to a webcam source in OBS</a></p><p>Available in English, Japanese, German, French, and Italian.</p><footer><a href="https://www.etsy.com/shop/DesktopPreset">DesktopPreset Etsy store</a></footer></main></body></html>'''
(guides/'index.html').write_text(index,encoding='utf8')
print('created',len(list(guides.glob('*.html'))),'pages')
