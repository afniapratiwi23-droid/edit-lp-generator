import requests
import json

API_KEY = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"
HTML_INPUT = """<!DOCTYPE html>
<html><body>
<h1>Belajar Marketing Digital</h1>
<p>Pernah bingung kenapa jualan online ga laku? Padahal produk bagus, harga kompetitif.</p>
<h2>Solusi: Kursus Marketing Digital</h2>
<p>Kursus lengkap dari A-Z, praktek langsung.</p>
<ul>
<li>Strategi konten viral</li>
<li>Copywriting yang jualan</li>
<li>Iklan Facebook & Instagram Ads</li>
</ul>
<p>Harga Normal: Rp 500.000</p>
<p>Harga Diskon: Rp 99.000</p>
</body></html>"""

url = "http://127.0.0.1:8080/generate"

# Test design_fresh mode
payload = {
    "html": HTML_INPUT,
    "api_key": API_KEY,
    "style": "design_fresh",
    "rewrite_copywriting": False
}

print("Testing DESIGN FRESH mode...")
print(f"Sending to: {url}")
print(f"Style: {payload['style']}")
print(f"Rewrite: {payload['rewrite_copywriting']}\n")

try:
    response = requests.post(url, json=payload, timeout=60)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        html_result = data.get('html', '')
        
        # Save to file
        with open('test_design_fresh_output.html', 'w', encoding='utf-8') as f:
            f.write(html_result)
        
        print(f"✓ Generated {len(html_result)} characters")
        print("✓ Saved to: test_design_fresh_output.html")
        
        # Check for template indicators
        if 'pink' in html_result.lower() or 'playfair' in html_result.lower():
            print("\n⚠️  WARNING: Output might still be using Pink Curhat template!")
        if 'slate-900' in html_result or 'slate-50' in html_result:
            print("\n⚠️  WARNING: Output might still be using Minimalist Clean template!")
        if 'bg-gray-900' in html_result or 'bg-black' in html_result:
            print("\n⚠️  WARNING: Output might still be using Bold Dark template!")
            
        print("\n✓ Check the file to see the actual design!")
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")
