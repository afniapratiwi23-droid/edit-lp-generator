import requests
import json

# Test API endpoint langsung
url = "http://localhost:8080/generate"

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>
<body>
    <h1>Percuma Outfit Mahal, Kalau Napas Bikin Ilfeel.</h1>
    <p>Fakta pahit: Orang ngejauh bukan karena lo jahat.</p>
</body>
</html>"""

api_key = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"

payload = {
    "html": html_content,
    "api_key": api_key,
    "style": "pink_curhat",
    "rewrite_copywriting": False
}

print("Sending request to", url)
print("Payload:", json.dumps(payload, indent=2)[:200], "...")

try:
    response = requests.post(url, json=payload, timeout=60)
    print("\n=== RESPONSE ===")
    print("Status Code:", response.status_code)
    print("Headers:", dict(response.headers))
    
    if response.status_code == 200:
        result = response.json()
        print("\n=== RESULT KEYS ===")
        print("Keys:", result.keys())
        
        if 'html' in result:
            html_result = result['html']
            print(f"\n=== HTML RESULT (first 500 chars) ===")
            print(html_result[:500])
            
            # Save to file
            with open('test_api_result.html', 'w', encoding='utf-8') as f:
                f.write(html_result)
            print("\n✅ Saved to test_api_result.html")
        elif 'error' in result:
            print("\n❌ ERROR:", result['error'])
    else:
        print("\n❌ HTTP Error:", response.text)
        
except Exception as e:
    print("\n❌ EXCEPTION:", str(e))
    import traceback
    traceback.print_exc()
