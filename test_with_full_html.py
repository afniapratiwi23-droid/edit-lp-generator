import requests
import json
import time

# Test dengan HTML Natural Fresh lengkap dari user
url = "http://localhost:8080/generate"

# HTML Natural Fresh dari user (Step 127)
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
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        luxury: {
                            black: '#121212', 
                            gold: '#D4AF37',
                            lightGold: '#F3E5AB',
                            text: '#333333',
                            red: '#8B0000',
                        }
                    },
                    fontFamily: {
                        serif: ['"Cinzel"', 'serif'],
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                    },
                    boxShadow: {
                        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)',
                        'float': '0 20px 40px -15px rgba(0,0,0,0.1)',
                    },
                }
            }
        }
    </script>

    <style>
        html { scroll-behavior: smooth; }
        body { background-color: #e5e5e5; color: #121212; }
        
        .mobile-wrapper {
            max-width: 480px;
            margin: 0 auto;
            background: #FAFAFA;
            min-height: 100vh;
            position: relative;
            box-shadow: 0 0 60px rgba(0,0,0,0.1);
            overflow-x: hidden;
            /* Padding bawah secukupnya agar bayangan kartu tidak terpotong */
            padding-bottom: 24px; 
        }

        /* Background Noise Texture Halus */
        .bg-texture {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
            z-index: 0;
            pointer-events: none;
            mix-blend-mode: soft-light;
        }

        .card-glass {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Shimmer Effect untuk Tombol Harga */
        .btn-shimmer {
            position: relative;
            overflow: hidden;
        }
        .btn-shimmer::after {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 50%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transform: skewX(-20deg);
            animation: shimmerBtn 3s infinite;
        }
        @keyframes shimmerBtn {
            0% { left: -100%; }
            100% { left: 200%; }
        }
    </style>
</head>
<body class="antialiased font-sans bg-gray-200 sm:py-8 py-0">
    
    <div class="mobile-wrapper relative sm:rounded-3xl overflow-hidden">
        <div class="bg-texture"></div>

        <header class="relative pt-16 pb-12 px-8 text-center z-10">
            <div class="absolute top-0 left-1/2 -translate-x-1/2 w-72 h-72 bg-luxury-gold/10 rounded-full blur-3xl -z-10"></div>

            <div class="mb-8 inline-block">
                <span class="bg-luxury-red/10 text-luxury-red border border-luxury-red/20 text-[10px] tracking-[0.3em] uppercase px-4 py-1.5 font-bold rounded-full">
                    Reality Check
                </span>
            </div>
            
            <h1 class="font-serif text-3xl text-luxury-black leading-tight mb-6 drop-shadow-sm font-bold">
                Percuma Outfit Mahal,<br>
                Kalau Napas Bikin <span class="text-luxury-red italic relative">Ilfeel.</span>
            </h1>

            <p class="text-sm text-gray-600 mb-10 max-w-xs mx-auto leading-relaxed font-medium">
                "Fakta pahit: Orang ngejauh bukan karena lo jahat, tapi karena mereka <b class="text-luxury-black underline decoration-luxury-gold/50">gak tahan</b> sama aroma mulut lo."
            </p>

            <div class="relative w-full max-w-[220px] mx-auto mb-6 group">
                <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-56 h-56 bg-luxury-gold/20 rounded-full blur-2xl group-hover:bg-luxury-gold/30 transition duration-700"></div>
                
                <img src="https://cdn.scalev.id/uploads/1763945565/p88njs9JO_cCjpWUYY-5Wg/1763945564890-Gemini_Generated_Image_isnqc8isnqc8isnq.webp" 
                     class="relative w-full h-auto drop-shadow-2xl transform group-hover:-translate-y-2 transition duration-500 z-10" 
                     alt="Natural Fresh Bottle">
            </div>
        </header>

        <section class="py-8 px-6 relative z-10">
            <div class="flex items-center gap-4 mb-8">
                <div class="h-px bg-gray-300 flex-1"></div>
                <h3 class="font-serif text-sm font-bold text-luxury-black uppercase tracking-widest">Tanda Lo Di-Skip</h3>
                <div class="h-px bg-gray-300 flex-1"></div>
            </div>
            
            <div class="space-y-5">
                <div class="card-glass p-6 rounded-2xl flex gap-5 items-start shadow-sm hover:shadow-float transition-all duration-300 group">
                    <div class="w-12 h-12 shrink-0 bg-red-50 rounded-xl flex items-center justify-center text-2xl shadow-sm border border-red-100 group-hover:scale-110 transition">🤢</div>
                    <div>
                        <h4 class="font-bold text-base text-luxury-black mb-2">Gestur "Tahan Napas"</h4>
                        <p class="text-sm text-gray-600 leading-relaxed">Perhatiin deh. Lawan bicara mundur dikit atau reflek pegang hidung pas lo ngomong? Itu kode keras.</p>
                    </div>
                </div>

                <div class="card-glass p-6 rounded-2xl flex gap-5 items-start shadow-sm hover:shadow-float transition-all duration-300 group">
                    <div class="w-12 h-12 shrink-0 bg-red-50 rounded-xl flex items-center justify-center text-2xl shadow-sm border border-red-100 group-hover:scale-110 transition">💔</div>
                    <div>
                        <h4 class="font-bold text-base text-luxury-black mb-2">Asmara Gagal Total</h4>
                        <p class="text-sm text-gray-600 leading-relaxed">Udah dandan maksimal, pas mau <i>deep talk</i> deket-deket, gebetan malah buang muka secara halus.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-12 px-6 relative z-10">
            <div class="relative w-full rounded-3xl overflow-hidden shadow-2xl border border-white/50 group">
                <div class="absolute inset-0 bg-luxury-black/10 group-hover:bg-transparent transition duration-500 z-10"></div>
                <img src="https://cdn.scalev.id/uploads/1763947063/Qr699udSjTo-lMBQalBMWg/1763947063671-Gemini_Generated_Image_pcwevxpcwevxpcwe.webp" 
                     class="w-full h-auto object-cover transform scale-105 group-hover:scale-100 transition duration-700" 
                     alt="Lifestyle Confidence">
            </div>
            <div class="text-center mt-6 px-4">
                 <p class="font-serif text-lg text-luxury-black">Natural Fresh™</p>
                 <p class="text-xs text-gray-500 tracking-wider uppercase mt-1">Definisi Wibawa Baru</p>
            </div>
        </section>

        <section class="py-8 px-6 relative z-10">
             <div class="flex items-center gap-4 mb-8">
                <div class="h-px bg-gray-300 flex-1"></div>
                <h3 class="font-serif text-sm font-bold text-luxury-black uppercase tracking-widest">Kenapa Ini Beda</h3>
                <div class="h-px bg-gray-300 flex-1"></div>
            </div>

            <div class="grid grid-cols-2 gap-4">
                <div class="p-5 rounded-2xl bg-white border border-gray-100 text-center hover:border-luxury-gold/30 hover:shadow-sm transition group">
                    <div class="text-3xl mb-3 group-hover:-translate-y-1 transition">🌿</div>
                    <h4 class="font-serif text-sm font-bold text-luxury-black mb-1">Gak Bau Obat</h4>
                    <p class="text-xs text-gray-500 font-medium">Aroma Natural</p>
                </div>
                <div class="p-5 rounded-2xl bg-white border border-gray-100 text-center hover:border-luxury-gold/30 hover:shadow-sm transition group">
                    <div class="text-3xl mb-3 group-hover:-translate-y-1 transition">❄️</div>
                    <h4 class="font-serif text-sm font-bold text-luxury-black mb-1">Dingin Seketika</h4>
                    <p class="text-xs text-gray-500 font-medium">Fresh 1 Detik</p>
                </div>
                <div class="p-5 rounded-2xl bg-white border border-gray-100 text-center hover:border-luxury-gold/30 hover:shadow-sm transition group">
                    <div class="text-3xl mb-3 group-hover:-translate-y-1 transition">🛡️</div>
                    <h4 class="font-serif text-sm font-bold text-luxury-black mb-1">Matiin Kuman</h4>
                    <p class="text-xs text-gray-500 font-medium">Sumber Masalah</p>
                </div>
                <div class="p-5 rounded-2xl bg-white border border-gray-100 text-center hover:border-luxury-gold/30 hover:shadow-sm transition group">
                    <div class="text-3xl mb-3 group-hover:-translate-y-1 transition">🧠</div>
                    <h4 class="font-serif text-sm font-bold text-luxury-black mb-1">PD Booster</h4>
                    <p class="text-xs text-gray-500 font-medium">Auto Pede</p>
                </div>
            </div>
        </section>

        <section class="py-12 px-6 bg-gray-50/50 relative z-10 mt-8 border-t border-gray-200">
            <h2 class="font-serif text-xl text-center mb-2 text-luxury-black">Bukti Nyata</h2>
            <p class="text-xs text-center text-gray-500 mb-8 tracking-wider uppercase">Mereka yang terselamatkan</p>
            
            <div class="space-y-6 max-w-sm mx-auto">
                <div class="bg-white p-3 rounded-2xl shadow-sm border border-gray-200">
                    <img src="https://cdn.scalev.id/business_files/S2k0vwHqofW11VSJXwAqHwEg/1752457794030-CYVHOY6qFPGRVj4NDM6xT3hQ.webp" class="w-full h-auto rounded-xl border border-gray-100">
                    <div class="mt-4 px-2 pb-2">
                        <div class="text-[10px] text-luxury-gold uppercase tracking-widest font-bold mb-1">Klien Happy</div>
                        <p class="text-sm leading-relaxed text-gray-600 italic">"Meeting sama klien jadi jauh lebih lancar. Gak khawatir lagi pas ngomong deket."</p>
                    </div>
                </div>
                <div class="bg-white p-3 rounded-2xl shadow-sm border border-gray-200">
                    <img src="https://cdn.scalev.id/business_files/x7ErIkU2m52tTg4LfCYcOUDt/1752457801422-ffUDJJHFlf6CgNffGkP9HqYXTVWLyRbCu0CF0E2qYLQ.webp" class="w-full h-auto rounded-xl border border-gray-100">
                    <div class="mt-4 px-2 pb-2">
                        <div class="text-[10px] text-luxury-gold uppercase tracking-widest font-bold mb-1">First Impression</div>
                        <p class="text-sm leading-relaxed text-gray-600 italic">"Kecil tapi ngefek banget buat first impression pas kencan pertama."</p>
                    </div>
                </div>
                <div class="bg-white p-3 rounded-2xl shadow-sm border border-gray-200">
                    <img src="https://cdn.scalev.id/business_files/k20UD6fOSB4vYztZY-5ZEK3E/1752457824152-LGlMMIb.webp" class="w-full h-auto rounded-xl border border-gray-100">
                     <div class="mt-4 px-2 pb-2">
                        <div class="text-[10px] text-luxury-gold uppercase tracking-widest font-bold mb-1">Repeat Order</div>
                        <p class="text-sm leading-relaxed text-gray-600 italic">"Langsung checkout 3 botol buat stok di kantor."</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="pt-8 px-6 relative z-10">
            <div class="bg-white border border-gray-200 rounded-3xl shadow-xl overflow-hidden max-w-sm mx-auto">
                
                <div class="bg-luxury-black text-white p-5 text-center relative overflow-hidden">
                    <div class="absolute inset-0 bg-luxury-gold opacity-10"></div>
                    <span class="text-[10px] uppercase tracking-[0.2em] font-bold text-luxury-gold">Limited Offer</span>
                    <h2 class="font-serif text-xl mt-2">Paket Anti Minder</h2>
                </div>

                <div class="p-6 text-center">
                    
                    <div class="mb-6">
                        <p class="text-xs text-gray-400 line-through mb-1 font-serif">IDR 155.000</p>
                        <div class="flex justify-center items-baseline gap-1 text-luxury-black">
                            <span class="text-sm font-medium">IDR</span>
                            <span class="text-6xl font-serif font-bold tracking-tighter">99</span>
                            <span class="text-xl font-light">rb</span>
                        </div>
                    </div>

                    <div class="bg-gray-50 border border-luxury-gold/30 rounded-xl p-4 mb-6">
                        <p class="font-serif text-lg text-luxury-black font-bold">Beli 2, Gratis 1</p>
                        <p class="text-[10px] uppercase tracking-wider text-gray-500 mt-1">Investasi Kepercayaan Diri</p>
                    </div>

                    <div class="flex justify-center items-center gap-2 text-luxury-black font-serif mb-8" id="countdown">
                        <div class="bg-gray-100 rounded w-10 py-2 shadow-inner">
                            <span class="block text-sm font-bold time-box">00</span>
                        </div>
                        <span class="text-xs font-bold">:</span>
                        <div class="bg-gray-100 rounded w-10 py-2 shadow-inner">
                            <span class="block text-sm font-bold time-box">14</span>
                        </div>
                        <span class="text-xs font-bold">:</span>
                        <div class="bg-luxury-red text-white rounded w-10 py-2 shadow-lg">
                            <span class="block text-sm font-bold time-box">59</span>
                        </div>
                    </div>

                    <button class="w-full bg-luxury-black text-white py-4 rounded-xl font-bold uppercase tracking-widest text-xs btn-shimmer hover:bg-gray-800 transition mb-4">
                        Ambil Promo Ini
                    </button>

                    <p class="text-[10px] text-gray-400 italic">
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

print("🧪 Testing NEW flexible prompt logic with FULL HTML...")
print("=" * 60)

try:
    start_time = time.time()
    response = requests.post(url, json=payload, timeout=90)
    duration = time.time() - start_time
    
    print(f"⏱️ Request took {duration:.2f} seconds")
    
    if response.status_code == 200:
        result = response.json()
        html_result = result['html']
        
        # Save hasil
        with open('test_full_html_result.html', 'w', encoding='utf-8') as f:
            f.write(html_result)
        
        # Verifikasi konten tetap ada
        print("\n✅ Generation SUCCESSFUL!")
        print(f"📄 HTML Length: {len(html_result)} chars")
        print("\n🔍 Checking if content preserved...")
        
        tests = {
            "4 Feature Cards (grid 2x2)": "Gak Bau Obat" in html_result and "PD Booster" in html_result,
            "3 Testimoni Images": html_result.count("business_files/") >= 3,
            "Countdown Timer Script": "updateTimer" in html_result,
            "Tanda Lo Di-Skip": "Gestur \"Tahan Napas\"" in html_result and "Asmara Gagal Total" in html_result,
            "Natural Fresh™": "Natural Fresh" in html_result,
            "Pricing (IDR 99)": "99" in html_result and ("155" in html_result or "155.000" in html_result),
            "Beli 2 Gratis 1": "Beli 2" in html_result or "Gratis 1" in html_result,
            "Script Tag Preserved": "<script>" in html_result
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
            print("⚠️  Some content missing, check test_full_html_result.html")
        
        print(f"\n📂 Saved to: test_full_html_result.html")
        
    else:
        print(f"\n❌ HTTP Error {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"\n❌ EXCEPTION: {str(e)}")
    import traceback
    traceback.print_exc()
