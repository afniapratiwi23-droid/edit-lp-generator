import requests
import json
import re

API_KEY = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ebook Seni Mempengaruhi Atasan</title>
</head>
<body>
    <h1>Capek Jadi Karyawan Biasa? Saatnya Pengaruhi Atasan Tanpa Harus Menjilat!</h1>
    <img src="https://example.com/image.jpg" alt="Hero">
    <p>Pernah gak sih ngerasa gini: Kerja udah kayak kuda, lembur tiap malem.</p>
    <h2>Solusi: Ebook Seni Mempengaruhi Atasan</h2>
    <p>Ebook ini akan ngajarin kamu gimana caranya bikin atasan mulai MELIHAT.</p>
    <ul>
        <li>Cara ngomong yang bikin atasan mikir</li>
        <li>Teknik membangun pengaruh</li>
    </ul>
    <p>Harga Normal: Rp 1.150.000</p>
    <p>Harga Diskon: Rp 99.000</p>
</body>
</html>"""

url = "http://127.0.0.1:8080/generate"
payload = {
    "html": HTML_CONTENT,
    "api_key": API_KEY,
    "style": "pink_curhat"
}

print("Sending request...")
try:
    response = requests.post(url, json=payload, timeout=30)
    print(f"✓ Status Code: {response.status_code}\n")
    
    if response.status_code == 200:
        data = response.json()
        html = data.get('html', '')
        
        # Save full HTML
        with open('output_test.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("✓ Full HTML saved to output_test.html\n")
        
        # Check for remaining placeholders
        placeholders = re.findall(r'\[AMBIL[^\]]*\]', html)
        
        if placeholders:
            print("❌ MASIH ADA PLACEHOLDER yang belum diganti:")
            for p in placeholders[:5]:  # Show first 5
                print(f"   - {p}")
        else:
            print("✅ SUKSES! Tidak ada placeholder [AMBIL...] yang tersisa.")
            
        # Show snippet of headline area
        headline_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
        if headline_match:
            print(f"\n📌 Headline: {headline_match.group(1)[:100]}...")
            
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")
