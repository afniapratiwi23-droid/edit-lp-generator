import requests
import json

API_KEY = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"
HTML_INPUT = "<h1>Test</h1>"

url = "http://127.0.0.1:8080/generate"

payload = {
    "html": HTML_INPUT,
    "api_key": API_KEY,
    "style": "pink_curhat",
    "copywriting_style": "original",
    "generate_variants": False
}

print("Testing /generate endpoint...")
try:
    response = requests.post(url, json=payload, timeout=60)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        html = data.get('html', '')
        print(f"HTML Length: {len(html)}")
        print("First 200 chars:")
        print(html[:200])
        print("Last 200 chars:")
        print(html[-200:])
        
        with open('debug_output.html', 'w') as f:
            f.write(html)
            
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Error: {e}")
