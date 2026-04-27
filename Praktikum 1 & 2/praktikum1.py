import re

RESERVED_WORDS = {
    "if", "else", "for", "while", "do",
    "int", "float", "double", "char", "string",
    "boolean", "true", "false",
    "return", "break", "continue",
    "void", "class", "public", "private",
    "static", "new", "print", "input"
}

TOKEN_REGEX = re.compile(
    r"""
    (?P<RESERVED>\b(?:if|else|for|while|do|int|float|double|char|string|boolean|true|false|return|break|continue|void|class|public|private|static|new|print|input)\b)
    |(?P<NUMBER>\b\d+(\.\d+)?\b)
    |(?P<OPERATOR>==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|[+\-*/%=<>])
    |(?P<PUNCTUATION>[;,.(){}\[\]:])
    |(?P<VARIABLE>\b[a-zA-Z_][a-zA-Z0-9_]*\b)
    """,
    re.VERBOSE
)

MATH_REGEX = re.compile(r"(=|\+|-|\*|/|%|<|>|<=|>=|==|!=)")

def tambah_token(hasil, kategori, token, baris):
    hasil[kategori].append({
        "token": token,
        "baris": baris
    })

def analisis_kode(kode):
    hasil = {
        "Reserve Words": [],
        "Simbol dan Tanda Baca": [],
        "Variabel": [],
        "Angka": [],
        "Kalimat Matematika": []
    }

    for nomor_baris, isi_baris in enumerate(kode.splitlines(), start=1):
        for cocok in TOKEN_REGEX.finditer(isi_baris):
            token = cocok.group()
            jenis = cocok.lastgroup
            if jenis == "RESERVED":
                tambah_token(hasil, "Reserve Words", token, nomor_baris)
            elif jenis == "OPERATOR" or jenis == "PUNCTUATION":
                tambah_token(hasil, "Simbol dan Tanda Baca", token, nomor_baris)
            elif jenis == "VARIABLE":
                tambah_token(hasil, "Variabel", token, nomor_baris)
            elif jenis == "NUMBER":
                tambah_token(hasil, "Angka", token, nomor_baris)

        baris_bersih = isi_baris.strip()
        if baris_bersih and MATH_REGEX.search(baris_bersih):
            hasil["Kalimat Matematika"].append({
                "token": baris_bersih,
                "baris": nomor_baris
            })
    return hasil

def tampilkan_hasil(hasil):
    print("\n===================================")
    print(" HASIL ANALISIS TOKEN")
    print("===================================")

    for kategori, daftar in hasil.items():
        print(f"\n{kategori.upper()}")
        print("-" * len(kategori))

        if not daftar:
            print("Tidak ditemukan.")
        else:
            for item in daftar:
                print(f"Baris {item['baris']:>2} | {item['token']}")
        print(f"Total {kategori}: {len(daftar)}")

print("===================================")
print(" PROGRAM ANALISIS TOKEN SEDERHANA")
print("===================================")
print("Masukkan kode program yang ingin dianalisis.")
print("Ketik SELESAI untuk mengakhiri input.\n")

kode_input = []

while True:
    baris = input()
    if baris.upper() == "SELESAI":
        break
    kode_input.append(baris)
kode = "\n".join(kode_input)

if kode.strip() == "":
    print("Kode masih kosong.")
else:
    hasil = analisis_kode(kode)
    tampilkan_hasil(hasil)
