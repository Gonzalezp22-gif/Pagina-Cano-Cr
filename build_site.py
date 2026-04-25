import urllib.request
import re

url = "https://maestraauroradelamor.online/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching: {e}")
    exit(1)

new_html = html

# Replace Name Variations
replacements = {
    "Bruja y Chamana Aurora Maestra Experta": "Brujo y Chamán Maestro Cano De El Amor Experto",
    "La Maestra Aurora es una experta reconocida": "El Maestro Cano De El Amor es un experto reconocido",
    "la Maestra Aurora es la guía": "el Maestro Cano De El Amor es el guía",
    "la Maestra Aurora es la gua": "el Maestro Cano De El Amor es el guía",
    "Aurora ha ayudado a cientos": "El Maestro Cano De El Amor ha ayudado a cientos",
    "Maestra Aurora": "Maestro Cano De El Amor",
    "maestra aurora": "maestro cano de el amor",
    "experta en brujería y chamanismo": "experto en brujería y chamanismo",
    "experta en brujera y chamanismo": "experto en brujería y chamanismo",
    "Chatea Con La Maestra Ya": "Chatea Con El Maestro Ya",
    "Maestra Pactada, bruja santera": "Maestro Pactado, brujo santero",
    "Ella está listo": "Él está listo",
    "Ella est listo": "Él está listo",
    "Maestra Experta en:": "Maestro Experto en:",
    "Chatea Con La Experta": "Chatea Con El Experto",
    "La Maestra": "El Maestro",
    "la Maestra": "el Maestro",
    "la maestra": "el maestro",
    "La maestra": "El maestro",
    "Maestra": "Maestro",
    "maestra": "maestro",
    "MAESTRA": "MAESTRO"
}

for old, new in replacements.items():
    new_html = new_html.replace(old, new)
    
# Replace specific URLs for phone numbers
new_html = new_html.replace("https://maestroauroradelamor.online/conversiones-whatsapp.html", "https://wa.me/5539580291")
new_html = new_html.replace("https://maestroauroradelamor.online/conversiones-llamada.html", "tel:5539580291")

# Replace any found phone numbers
new_html = new_html.replace("11305122142", "5539580291")
new_html = new_html.replace("5215546865327", "525539580291")
new_html = new_html.replace("5546865327", "5539580291")

# Also replace direct wa.me links
new_html = re.sub(r'https://api\.whatsapp\.com/send\?phone=\d+', 'https://api.whatsapp.com/send?phone=525539580291', new_html)
new_html = re.sub(r'https://wa\.me/\+?\d+', 'https://wa.me/525539580291', new_html)

# Since we replaced 'maestra' to 'maestro', the base URL of assets might have broken
# Let's fix the asset URLs back to the true domain
new_html = new_html.replace("https://maestroauroradelamor.online/", "https://maestraauroradelamor.online/")

# Wait, but above I tried to replace the whatsapp links using "maestroauroradelamor.online" which means it WAS changed. So that's correct.
# Let's just make sure all asset URLs keep the original domain so images block/CSS don't break.
new_html = new_html.replace("https://maestroauroradelamor.online", "https://maestraauroradelamor.online")

# Replace header logo images with our new local image
new_html = new_html.replace("https://maestraauroradelamor.online/wp-content/uploads/2025/08/logo-aur.png", "logo_cano.png")
new_html = new_html.replace("https://maestraauroradelamor.online/wp-content/uploads/2025/08/logo-4.png", "logo_cano.png")

# Remove srcset so it doesn't load the old images responsively
new_html = re.sub(r'srcset="[^"]*logo-aur[^"]*"', '', new_html)
new_html = re.sub(r'srcset="[^"]*logo-4[^"]*"', '', new_html)

# Inject Google Tag (gtag.js) for Google Ads tracking (AW-18117498384)
    gtag_script = '''<!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18117498384"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-18117498384');
    </script>'''
    # Insert after <head> tag
    if '<head>' in new_html:
        new_html = new_html.replace('<head>', '<head>\n    ' + gtag_script, 1)
    else:
        print('Warning: <head> tag not found in HTML')
with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Done generating index.html")
