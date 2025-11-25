import requests
import json

API_KEY = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ebook Seni Mempengaruhi Atasan</title>
</head>
<body class="bg-white text-gray-700">
    <div class="container max-w-7xl mx-auto">
        <section class="py-6">
            <h1 class="text-2xl font-semibold text-gray-900 text-center">Capek Jadi Karyawan Biasa? Saatnya Pengaruhi Atasan Tanpa Harus Menjilat!</h1>
            <p>Contoh paragraf pendek untuk testing.</p>
        </section>
    </div>
</body>
</html>"""

url = "http://127.0.0.1:8080/generate"
payload = {
    "html": HTML_CONTENT,
    "api_key": API_KEY,
    "style": "pink_curhat"
}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    print(response.text[:500]) # Print first 500 chars
except Exception as e:
    print(f"Error: {e}")
