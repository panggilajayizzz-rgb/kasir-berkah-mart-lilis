"""Program Kasir Warung Berkah Mart (versi sederhana, berbasis terminal)."""

from datetime import datetime

NAMA_TOKO = "WARUNG BERKAH MART"
DISKON_MINIMAL = 100_000   # belanja minimal untuk mendapat diskon
DISKON_PERSEN = 5          # besar diskon (%)

# Daftar barang: kode -> (nama, harga)
BARANG = {
    "1": ("Beras 1 Kg", 14_000),
    "2": ("Minyak Goreng 1 L", 18_000),
    "3": ("Gula Pasir 1 Kg", 16_000),
    "4": ("Telur 1 Kg", 28_000),
    "5": ("Mie Instan", 3_500),
    "6": ("Kopi Sachet", 2_000),
    "7": ("Air Mineral 600 ml", 4_000),
    "8": ("Sabun Mandi", 5_000),
}

keranjang = {}  # kode -> jumlah


def rupiah(angka):
    return "Rp{:,}".format(angka).replace(",", ".")


def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")
    for kode, (nama, harga) in BARANG.items():
        print(f"{kode}. {nama:<20} {rupiah(harga):>10}")


def input_angka(pesan):
    """Meminta input angka bulat positif; mengembalikan None jika tidak valid."""
    try:
        nilai = int(input(pesan))
        return nilai if nilai > 0 else None
    except ValueError:
        return None


def tambah_barang():
    tampilkan_barang()
    kode = input("Masukkan kode barang: ").strip()
    if kode not in BARANG:
        print("Kode barang tidak ditemukan!")
        return
    jumlah = input_angka("Jumlah: ")
    if jumlah is None:
        print("Jumlah tidak valid!")
        return
    keranjang[kode] = keranjang.get(kode, 0) + jumlah
    print(f"{BARANG[kode][0]} x{jumlah} ditambahkan.")


def hapus_barang():
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    tampilkan_keranjang()
    kode = input("Kode barang yang dihapus: ").strip()
    if kode in keranjang:
        del keranjang[kode]
        print("Barang dihapus dari keranjang.")
    else:
        print("Barang tidak ada di keranjang!")


def hitung_total():
    subtotal = sum(BARANG[k][1] * j for k, j in keranjang.items())
    diskon = subtotal * DISKON_PERSEN // 100 if subtotal >= DISKON_MINIMAL else 0
    return subtotal, diskon, subtotal - diskon


def tampilkan_keranjang():
    print("\n=== KERANJANG BELANJA ===")
    if not keranjang:
        print("(kosong)")
        return
    for kode, jumlah in keranjang.items():
        nama, harga = BARANG[kode]
        print(f"{kode}. {nama:<20} {jumlah:>3} x {rupiah(harga):>9} = {rupiah(harga * jumlah):>10}")
    subtotal, diskon, total = hitung_total()
    print("-" * 52)
    print(f"{'Subtotal':<40}{rupiah(subtotal):>12}")
    if diskon:
        print(f"{'Diskon ' + str(DISKON_PERSEN) + '%':<40}{'-' + rupiah(diskon):>12}")
    print(f"{'TOTAL':<40}{rupiah(total):>12}")


def cetak_struk(subtotal, diskon, total, bayar, kembali):
    print("\n" + "=" * 52)
    print(NAMA_TOKO.center(52))
    print(datetime.now().strftime("%d-%m-%Y %H:%M:%S").center(52))
    print("=" * 52)
    for kode, jumlah in keranjang.items():
        nama, harga = BARANG[kode]
        print(f"{nama:<20} {jumlah:>3} x {rupiah(harga):>9} = {rupiah(harga * jumlah):>10}")
    print("-" * 52)
    print(f"{'Subtotal':<40}{rupiah(subtotal):>12}")
    print(f"{'Diskon':<40}{rupiah(diskon):>12}")
    print(f"{'Total':<40}{rupiah(total):>12}")
    print(f"{'Bayar':<40}{rupiah(bayar):>12}")
    print(f"{'Kembali':<40}{rupiah(kembali):>12}")
    print("=" * 52)
    print("Terima kasih sudah berbelanja!".center(52))


def bayar():
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    tampilkan_keranjang()
    subtotal, diskon, total = hitung_total()
    while True:
        uang = input_angka("\nUang pembayaran: Rp")
        if uang is None:
            print("Nominal tidak valid!")
        elif uang < total:
            print(f"Uang kurang {rupiah(total - uang)}. Coba lagi.")
        else:
            break
    cetak_struk(subtotal, diskon, total, uang, uang - total)
    keranjang.clear()


def main():
    while True:
        print(f"\n===== {NAMA_TOKO} =====")
        print("1. Lihat daftar barang")
        print("2. Tambah barang ke keranjang")
        print("3. Lihat keranjang")
        print("4. Hapus barang dari keranjang")
        print("5. Bayar")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            tampilkan_keranjang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            bayar()
        elif pilihan == "0":
            print("Sampai jumpa!")
            break
        else:
            print("Menu tidak valid!")


if __name__ == "__main__":
    main()
