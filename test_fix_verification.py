import requests
import json

# Test dengan HTML Natural Fresh lengkap
url = "http://localhost:8080/generate"

# HTML Natural Fresh dari user
html_content_natural_fresh = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natural Fresh - Reality Check</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;800&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,600;1,400&display=swap" rel="stylesheet">
    
    <style>
        html { scroll-behavior: smooth; }
        body { background-color: #e5e5e5; color: #121212; }
        
        .mobile-wrapper {
            max-width: 480px;
            margin: 0 auto;
            background: #FAFAFA;
            min-height: 100vh;
        }
    </style>
</head>
<body class="antialiased font-sans">
    
    <div class="mobile-wrapper">
        <header class="pt-16 pb-12 px-8 text-center">
            <div class="mb-8">
                <span class="bg-red-100 text-red-600 px-4 py-1.5 rounded-full">Reality Check</span>
            </div>
            
            <h1 class="text-3xl font-bold mb-6">
                Percuma Outfit Mahal,<br>
                Kalau Napas Bikin Ilfeel.
            </h1>

            <p class="text-sm mb-10">
                "Fakta pahit: Orang ngejauh bukan karena lo jahat, tapi karena mereka gak tahan sama aroma mulut lo."
            </p>

            <div class="mb-6">
                <img src="https://cdn.scalev.id/uploads/1763945565/p88njs9JO_cCjpWUYY-5Wg/1763945564890-Gemini_Generated_Image_isnqc8isnqc8isnq.webp" alt="Natural Fresh Bottle">
            </div>
        </header>

        <section class="py-8 px-6">
            <h3 class="text-sm font-bold mb-8">Tanda Lo Di-Skip</h3>
            
            <div>
                <div class="mb-5">
                    <div>🤢</div>
                    <h4 class="font-bold">Gestur "Tahan Napas"</h4>
                    <p>Perhatiin deh. Lawan bicara mundur dikit atau reflek pegang hidung pas lo ngomong? Itu kode keras.</p>
                </div>

                <div>
                    <div>💔</div>
                    <h4 class="font-bold">Asmara Gagal Total</h4>
                    <p>Udah dandan maksimal, pas mau deep talk deket-deket, gebetan malah buang muka secara halus.</p>
                </div>
            </div>
        </section>

        <section class="py-12 px-6">
            <div>
                <img src="https://cdn.scalev.id/uploads/1763947063/Qr699udSjTo-lMBQalBMWg/1763947063671-Gemini_Generated_Image_pcwevxpcwevxpcwe.webp" alt="Lifestyle">
            </div>
            <div class="text-center mt-6">
                 <p>Natural Fresh™</p>
                 <p>Definisi Wibawa Baru</p>
            </div>
        </section>

        <section class="py-8 px-6">
             <h3 class="font-bold mb-8">Kenapa Ini Beda</h3>

            <div class="grid grid-cols-2 gap-4">
                <div class="p-5 text-center">
                    <div>🌿</div>
                    <h4 class="font-bold">Gak Bau Obat</h4>
                    <p>Aroma Natural</p>
                </div>
                <div class="p-5 text-center">
                    <div>❄️</div>
                    <h4 class="font-bold">Dingin Seketika</h4>
                    <p>Fresh 1 Detik</p>
                </div>
                <div class="p-5 text-center">
                    <div>🛡️</div>
                    <h4 class="font-bold">Matiin Kuman</h4>
                    <p>Sumber Masalah</p>
                </div>
                <div class="p-5 text-center">
                    <div>🧠</div>
                    <h4 class="font-bold">PD Booster</h4>
                    <p>Auto Pede</p>
                </div>
            </div>
        </section>

        <section class="py-12 px-6">
            <h2 class="text-xl text-center mb-2">Bukti Nyata</h2>
            <p class="text-xs text-center mb-8">Mereka yang terselamatkan</p>
            
            <div>
                <div class="mb-6">
                    <img src="https://cdn.scalev.id/business_files/S2k0vwHqofW11VSJXwAqHwEg/1752457794030-CYVHOY6qFPGRVj4NDM6xT3hQ.webp">
                    <div class="mt-4">
                        <div class="text-xs font-bold mb-1">Klien Happy</div>
                        <p>"Meeting sama klien jadi jauh lebih lancar. Gak khawatir lagi pas ngomong deket."</p>
                    </div>
                </div>
                <div class="mb-6">
                    <img src="https://cdn.scalev.id/business_files/x7ErIkU2m52tTg4LfCYcOUDt/1752457801422-ffUDJJHFlf6CgNffGkP9HqYXTVWLyRbCu0CF0E2qYLQ.webp">
                    <div class="mt-4">
                        <div class="text-xs font-bold mb-1">First Impression</div>
                        <p>"Kecil tapi ngefek banget buat first impression pas kencan pertama."</p>
                    </div>
                </div>
                <div class="mb-6">
                    <img src="https://cdn.scalev.id/business_files/k20UD6fOSB4vYztZY-5ZEK3E/1752457824152-LGlMMIb.webp">
                     <div class="mt-4">
                        <div class="text-xs font-bold mb-1">Repeat Order</div>
                        <p>"Langsung checkout 3 botol buat stok di kantor."</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="pt-8 px-6">
            <div class="bg-white border rounded-3xl overflow-hidden">
                
                <div class="bg-black text-white p5 text-center">
                    <span class="text-xs uppercase">Limited Offer</span>
                    <h2 class="text-xl mt-2">Paket Anti Minder</h2>
                </div>

                <div class="p-6 text-center">
                    
                    <div class="mb-6">
                        <p class="text-xs line-through mb-1">IDR 155.000</p>
                        <div class="flex justify-center items-baseline gap-1">
                            <span class="text-sm">IDR</span>
                            <span class="text-6xl font-bold">99</span>
                            <span class="text-xl">rb</span>
                        </div>
                    </div>

                    <div class="border rounded-xl p-4 mb-6">
                        <p class="text-lg font-bold">Beli 2, Gratis 1</p>
                        <p class="text-xs uppercase mt-1">Investasi Kepercayaan Diri</p>
                    </div>

                    <div class="flex justify-center items-center gap-2 mb-8" id="countdown">
                        <div class="rounded w-10 py-2">
                            <span class="block text-sm font-bold time-box">00</span>
                        </div>
                        <span class="text-xs font-bold">:</span>
                        <div class="rounded w-10 py-2">
                            <span class="block text-sm font-bold time-box">14</span>
                        </div>
                        <span class="text-xs font-bold">:</span>
                        <div class="rounded w-10 py-2">
                            <span class="block text-sm font-bold time-box">59</span>
                        </div>
                    </div>

                    <button class="w-full bg-black text-white py-4 rounded-xl font-bold uppercase text-xs mb-4">
                        Ambil Promo Ini
                    </button>

                    <p class="text-xs italic">
                        *Garansi uang kembali jika tidak ada perubahan.
                    </p>
                </div>
            </div>
        </section>

    </div>

    <script>
        let minutes = 15; 
        let seconds = 0;
        function updateTimer() {
            const timerContainer = document.getElementById('countdown');
            if (seconds === 0) {
                if (minutes === 0) { clearInterval(interval); return; }
                minutes--; seconds = 59;
            } else { seconds--; }
            
            const m = minutes < 10 ? "0" + minutes : minutes;
            const s = seconds < 10 ? "0" + seconds : seconds;
            
            const boxes = timerContainer.querySelectorAll('.time-box');
            boxes[0].innerText = '00'; 
            boxes[1].innerText = m;    
            boxes[2].innerText = s;    
        }
        let interval = setInterval(updateTimer, 1000);
    </script>
</body>
</html>"""

api_key = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"

payload = {
    "html": html_content_natural_fresh,
    "api_key": api_key,
    "style": "pink_curhat",
    "rewrite_copywriting": False
}

print("🧪 Testing NEW flexible prompt logic...")
print("=" * 60)

try:
    response = requests.post(url, json=payload, timeout=60)
    
    if response.status_code == 200:
        result = response.json()
        html_result = result['html']
        
        # Save hasil
        with open('test_fix_result.html', 'w', encoding='utf-8') as f:
            f.write(html_result)
        
        # Verifikasi konten tetap ada
        print("\n✅ Generation SUCCESSFUL!")
        print(f"📄 HTML Length: {len(html_result)} chars")
        print("\n🔍 Checking if content preserved...")
        
        tests = {
            "4 Feature Cards (grid 2x2)": "Gak Bau Obat" in html_result and "PD Booster" in html_result,
            "3 Testimoni Images": html_result.count("business_files/") >= 3,
            "Countdown Timer": "countdown" in html_result and "updateTimer" in html_result,
            "Tanda Lo Di-Skip": "Gestur \"Tahan Napas\"" in html_result and "Asmara Gagal Total" in html_result,
            "Natural Fresh™": "Natural Fresh" in html_result,
            "Pricing (IDR 99)": "99" in html_result and ("155" in html_result or "155.000" in html_result),
            "Beli 2 Gratis 1": "Beli 2" in html_result or "Gratis 1" in html_result
        }
        
        print()
        for test_name, passed in tests.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"   {status}: {test_name}")
        
        all_passed = all(tests.values())
        print()
        if all_passed:
            print("🎉 ALL TESTS PASSED! Konten tetap lengkap!")
        else:
            print("⚠️  Some content missing, check test_fix_result.html")
        
        print(f"\n📂 Saved to: test_fix_result.html")
        
    else:
        print(f"\n❌ HTTP Error {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"\n❌ EXCEPTION: {str(e)}")
    import traceback
    traceback.print_exc()
