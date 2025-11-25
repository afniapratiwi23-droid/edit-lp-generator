import google.generativeai as genai
import os

# User provided API Key
API_KEY = "AIzaSyAuMHWCs216ym-Y6J1ihK4ZBwUfdJf7Q_o"

# User provided HTML Input
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ebook Seni Mempengaruhi Atasan</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * {
        word-wrap: break-word;
        overflow-wrap: break-word;
        -webkit-hyphens: auto;
        hyphens: auto;
      }

      body {
        font-size: 16px;
        line-height: 1.6;
      }

      h1, h2, h3 {
        word-break: keep-all;
        overflow-wrap: normal;
      }

      @media (max-width: 768px) {
        h1 {
          font-size: 1.5rem !important; /* 24px */
          line-height: 1.3 !important;
        }

        h2 {
          font-size: 1.25rem !important; /* 20px */
          line-height: 1.4 !important;
        }

        p {
          font-size: 1rem !important; /* 16px */
          line-height: 1.625 !important;
          margin-bottom: 1rem !important;
        }

        /* JARAK MINIMAL KIRI/KANAN - 2px */
        body {
          padding-left: 2px !important;
          padding-right: 2px !important;
          margin: 0 !important;
        }

        .container, section, div {
          padding-left: 2px !important;
          padding-right: 2px !important;
        }
      }
    </style>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-white text-gray-700">
    <div class="container max-w-7xl mx-auto">
        <section class="py-6">
            <h1 class="text-2xl font-semibold text-gray-900 text-center">Capek Jadi Karyawan Biasa? Saatnya Pengaruhi Atasan Tanpa Harus Menjilat!</h1>
            <img src="https://cdn.scalev.id/uploads/1763953046/2gsVVm_xXxgy2BJ7m9ryKA/1763953045667-Gemini_Generated_Image_xptms1xptms1xptm.webp" class="w-full max-w-lg mx-auto rounded-2xl shadow-xl my-8" alt="Hero">
        </section>

        <section class="py-6">
            <p class="mb-3">Pernah gak sih ngerasa gini:</p>
            <p class="mb-3">Kerja udah kayak kuda, lembur tiap malem, tapi kok yang naik jabatan malah si A yang hobinya ngopi bareng bos?</p>
            <p class="mb-3">Bukannya iri, tapi nyesek kan? Kamu tau kamu lebih capable, tapi kenapa dia yang dilihat?</p>
            <p class="mb-3">Di kantor, kerja keras itu penting, itu modal dasar.</p>
            <p class="mb-3">Tapi, setelah itu, yang dinilai adalah siapa yang bisa bikin atasan nyaman, paham visinya, dan bisa diajak diskusi.</p>
            <p class="mb-3">Kalau kamu cuma fokus ngerjain tugas, tanpa nunjukkin kalau kamu punya value lebih, ya siap-siap aja terus jadi pelengkap.</p>
        </section>

        <section class="py-6">
            <h2 class="text-xl font-medium text-gray-900">Solusi: Ebook Seni Mempengaruhi Atasan Tanpa Terlihat Menjilat</h2>
            <img src="https://cdn.scalev.id/uploads/1763952610/5psaX8A6Uysyk2pokL1A9A/1763952610225-Gemini_Generated_Image_9lgf3o9lgf3o9lgf.webp" class="w-full max-w-md mx-auto rounded-2xl shadow-lg my-6" alt="Product">
            <p class="mb-3">Ebook ini BUKAN ngajarin kamu buat cari muka atau menjilat.</p>
            <p class="mb-3">Tapi, ebook ini akan ngajarin kamu gimana caranya bikin atasan mulai MELIHAT, MENGHARGAI, dan BERGANTUNG sama cara berpikir kamu.</p>
            <p class="mb-3">Kamu akan belajar strategi komunikasi yang halus tapi nancep, teknik membangun pengaruh tanpa harus jadi penjilat, dan cara memainkan persepsi agar kamu terlihat menonjol tanpa terkesan caper.</p>
        </section>

        <section class="py-6">
            <h2 class="text-xl font-medium text-gray-900">Yang Bakal Kamu Pelajari:</h2>
            <ul class="list-disc pl-5">
                <li>Cara ngomong yang bikin atasan mikir: “Orang ini bisa gue andalkan”</li>
                <li>Teknik membangun pengaruh tanpa harus sok akrab</li>
                <li>Strategi komunikasi yang bikin bos mulai nurut, bukan nyuruh</li>
                <li>Cara mainkan persepsi tanpa terkesan caper</li>
            </ul>
        </section>

        <section class="py-6">
            <h2 class="text-xl font-medium text-gray-900">Kenapa Ini Penting?</h2>
            <p class="mb-3">Kalau kamu terus-terusan ngandelin kerja keras doang, kamu bakal jadi orang yang disayang karena loyal, tapi gak pernah diajak naik karena gak dianggap punya potensi lebih.</p>
            <p class="mb-3">Sakitnya pelan-pelan, gak meledak, tapi ngikis kepercayaan diri tiap bulan.</p>
            <p class="mb-3">Saatnya berhenti ngandelin kerja keras doang. Saatnya bikin diri kamu TERLIHAT LAYAK dikasih posisi yang lebih tinggi.</p>
        </section>

        <section class="py-6">
            <h2 class="text-xl font-medium text-gray-900 mb-4 text-center">Dapatkan Bonus Eksklusif Ini:</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-200">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-900 mb-2">📚 Ebook Seni Bertahan Hidup di Antara Rekan Kerja Toxic</h3>
                        <p class="text-gray-700">Pelajari cara jitu menghadapi rekan kerja yang penjilat, tukang gosip, dan pengganggu, agar kamu tetap waras dan fokus pada kariermu.</p>
                    </div>
                </div>
                <div class="bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-200">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-900 mb-2">🎬 E-COURSE VIDEO : PERSONAL BRANDING</h3>
                        <p class="text-gray-700">Biar menjadi karyawan yang diincar PERUSAHAAN TOP! Biasanya, e-course sekelas ini hanya diajarkan di seminar-seminar eksklusif yang harganya jutaan.</p>
                    </div>
                </div>
                                <div class="bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-200">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-900 mb-2">📝 Template Ajukan Kenaikan Gaji</h3>
                        <p class="text-gray-700">Dapatkan template profesional untuk mengajukan kenaikan gaji yang efektif dan meyakinkan. Raih apresiasi yang pantas atas kontribusimu.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-6">
        <div class="w-[90%] max-w-md mx-auto bg-white rounded-3xl shadow-2xl overflow-hidden border-2 border-blue-100 relative mt-8">
            <!-- Header Card -->
            <div class="bg-gradient-to-r from-blue-600 to-indigo-700 py-4 px-6 text-center">
                <span class="text-white font-bold tracking-wider text-sm uppercase">✨ Penawaran Spesial Terbatas</span>
            </div>

            <!-- Body Card -->
            <div class="p-8 text-center">
                <!-- Harga Coret -->
                <p class="text-gray-400 text-lg mb-1">Harga Normal</p>
                <p class="text-2xl text-gray-400 line-through font-medium mb-4">Rp 1.150.000</p>

                <!-- Harga Jual -->
                <div class="mb-6">
                    <span class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm font-bold mb-2 inline-block">HEMAT 90% HARI INI</span>
                    <p class="text-5xl font-extrabold text-gray-900 mt-2 tracking-tight">Rp 99.000</p>
                </div>

                <!-- Value Comparison -->
                <p class="text-gray-600 text-sm mb-6 italic border-t border-gray-100 pt-4">
                    "Cuma seharga 2 gelas kopi, tapi ilmunya bisa dipakai seumur hidup untuk karirmu!"
                </p>

                <!-- Garansi Badge -->
                <div class="flex items-center justify-center gap-2 text-green-600 font-semibold bg-green-50 py-3 rounded-xl">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    <span>Garansi 30 Hari Uang Kembali</span>
                </div>
            </div>
        </div>
    </section>
"""

prompt = f"""Kamu adalah Expert Web Designer. Tugasmu adalah melakukan "Visual Upgrade" pada HTML yang diberikan.

ATURAN UTAMA:
1. GANTI DESAINNYA agar persis seperti struktur "TARGET HTML STRUCTURE" di bawah.
2. JANGAN UBAH TEKS/COPYWRITING ASLINYA. Gunakan teks asli dari "HTML INPUT".
3. Jika ada bagian di HTML INPUT yang tidak ada di TARGET STRUCTURE (misal: testimoni), abaikan saja.
4. Jika ada bagian di TARGET STRUCTURE yang tidak ada di HTML INPUT (misal: bonus), kosongkan atau hapus bagian itu.
5. Return HANYA HTML lengkap.

=== HTML INPUT (Ambil Teks dari sini) ===
```html
{html_content}
```

=== TARGET HTML STRUCTURE (Gunakan Desain ini) ===
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; word-wrap: break-word; }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #fdf2f8; 
            color: #4a4a4a;
            font-size: 16px;
            line-height: 1.6;
            padding-left: 2px !important;
            padding-right: 2px !important;
            padding-top: 0 !important;
            padding-bottom: 40px !important;
            min-height: 100vh;
            display: flex;
            justify-content: center;
        }}
        .main-container {{
            width: 100%;
            max-width: 550px;
            background-color: #ffffff;
            box-shadow: 0 8px 30px rgba(219, 39, 119, 0.08);
            border-bottom-left-radius: 25px;
            border-bottom-right-radius: 25px;
            overflow: hidden;
        }}
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
            color: #db2777;
            line-height: 1.3;
        }}
        .highlight {{
            background: linear-gradient(120deg, #fce7f3 0%, #fce7f3 100%);
            background-repeat: no-repeat;
            background-size: 100% 40%;
            background-position: 0 85%;
            padding: 0 2px;
        }}
        .check-list li {{
            position: relative;
            padding-left: 30px;
            margin-bottom: 12px;
        }}
        .check-list li::before {{
            content: '❤';
            position: absolute;
            left: 0;
            top: 2px;
            width: 22px;
            height: 22px;
            background: #fce7f3;
            color: #db2777;
            border-radius: 50%;
            text-align: center;
            line-height: 24px;
            font-size: 11px;
        }}
        .bonus-card {{
            border: 1px dashed #f9a8d4;
            border-radius: 16px;
            padding: 16px;
            background: #fff;
            transition: transform 0.2s;
            margin-bottom: 12px;
        }}
        .bonus-card:hover {{ transform: translateY(-3px); border-color: #db2777; }}
        .pricing-card {{
            border-radius: 25px;
            border: 2px solid #fce7f3;
            position: relative;
            overflow: hidden;
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <!-- HEADER -->
        <section class="pt-10 pb-6 px-5 text-center bg-gradient-to-b from-pink-50 to-white">
            <span class="inline-block py-1 px-4 rounded-full bg-pink-100 text-pink-600 text-xs font-bold tracking-wider mb-5">
                [AMBIL BADGE/KATEGORI DARI INPUT]
            </span>
            <h1 class="text-2xl font-bold mb-6">
                [AMBIL HEADLINE DARI INPUT]
            </h1>
            <div class="relative px-2">
                <div class="absolute inset-0 bg-pink-200 rounded-3xl transform rotate-2 scale-95 opacity-40"></div>
                <img src="[AMBIL URL GAMBAR UTAMA DARI INPUT]" class="relative w-full rounded-3xl shadow-lg border-4 border-white" alt="Hero">
            </div>
        </section>

        <!-- PROBLEM / STORY -->
        <section class="py-6 px-5">
            <div class="bg-blue-50 p-6 rounded-3xl border border-blue-100 text-left">
                <p class="font-bold text-blue-800 mb-3 text-sm">🥺 Pernah gak sih ngerasa gini:</p>
                <div class="space-y-3 text-gray-600 text-sm leading-relaxed">
                    [AMBIL PARAGRAF MASALAH/STORY DARI INPUT]
                </div>
            </div>
        </section>

        <!-- SOLUTION / PRODUCT -->
        <section class="py-8 px-5 bg-white text-center">
            <h2 class="text-xl font-bold mb-2 text-pink-600">Ini Solusinya Bestie:</h2>
            <p class="text-gray-500 text-sm mb-6">[AMBIL NAMA PRODUK DARI INPUT]</p>
            <div class="relative w-3/4 mx-auto mb-6">
                <div class="absolute -inset-3 bg-pink-100 rounded-full blur-xl opacity-60"></div>
                <img src="[AMBIL GAMBAR PRODUK KEDUA JIKA ADA]" class="relative w-full rounded-2xl shadow-md transform hover:scale-105 transition" alt="Product">
            </div>
            <div class="text-left px-2 space-y-3 text-sm text-gray-600">
                [AMBIL DESKRIPSI SOLUSI DARI INPUT]
            </div>
        </section>

        <!-- BENEFITS -->
        <section class="py-8 px-6 bg-pink-50">
            <h2 class="text-xl font-bold text-center mb-6 text-pink-700">Yang Bakal Kamu Pelajari:</h2>
            <div class="bg-white p-6 rounded-3xl shadow-sm border border-pink-100">
                <ul class="check-list text-sm text-gray-600">
                    [AMBIL LIST BENEFIT DARI INPUT, MASUKKAN KE SINI SEBAGAI LIST ITEM]
                </ul>
            </div>
        </section>

        <!-- WHY IMPORTANT -->
        <section class="py-8 px-6 text-center">
            <h2 class="text-xl font-bold mb-4 text-gray-800">Kenapa Ini Penting?</h2>
            <div class="text-sm text-gray-600 space-y-3">
                [AMBIL TEKS ALASAN PENTING DARI INPUT]
            </div>
        </section>

        <!-- BONUSES -->
        <section class="py-8 px-5 bg-white">
            <h2 class="text-xl font-bold text-center mb-6 text-pink-600">🎁 Dapatkan Bonus Eksklusif:</h2>
            <!-- LOOP UNTUK SETIAP BONUS -->
            <div class="bonus-card">
                <h3 class="text-md font-bold text-gray-800 mb-1">[JUDUL BONUS]</h3>
                <p class="text-xs text-gray-500">[DESKRIPSI BONUS]</p>
            </div>
        </section>

        <!-- PRICING -->
        <section class="pt-4 pb-12 px-4 bg-white">
            <div class="pricing-card shadow-lg">
                <div class="bg-pink-500 py-4 px-6 text-center">
                    <span class="text-white font-bold tracking-wider text-sm uppercase">✨ Penawaran Spesial</span>
                </div>
                <div class="p-8 text-center bg-white">
                    <p class="text-gray-400 text-sm mb-1">Harga Normal</p>
                    <p class="text-lg text-gray-400 line-through font-medium mb-4">[HARGA CORET]</p>
                    <div class="mb-6">
                        <span class="bg-pink-100 text-pink-600 px-4 py-1 rounded-full text-xs font-bold mb-3 inline-block">HEMAT HARI INI</span>
                        <p class="text-5xl font-extrabold text-gray-800 mt-2 tracking-tight">[HARGA DISKON]</p>
                    </div>
                    <p class="text-gray-500 text-xs mb-6 italic">
                        [KALIMAT PENUTUP/CTA]
                    </p>
                    <div class="flex items-center justify-center gap-2 text-gray-500 font-medium text-xs mt-4 bg-gray-50 py-3 rounded-xl">
                        <span class="text-lg">🛡️</span>
                        <span>Garansi 30 Hari Uang Kembali</span>
                    </div>
                </div>
            </div>
        </section>
    </div>
</body>
</html>
```

LAKUKAN SEKARANG: Mapping konten dari HTML INPUT ke TARGET HTML STRUCTURE. Jangan ubah kata-katanya!
"""

try:
    print("Configuring Gemini...")
    genai.configure(api_key=API_KEY)
    
    print("Initializing model gemini-2.0-flash-lite...")
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    
    print("Sending prompt...")
    response = model.generate_content(prompt)
    
    print("\n=== SUCCESS! GENERATED HTML ===")
    print(response.text[:500] + "...") # Print first 500 chars to verify
    print("===============================")
    
except Exception as e:
    print(f"\n=== ERROR ===\n{e}")
