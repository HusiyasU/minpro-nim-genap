print("________________________________________")
print("__________HUSAINI IYASTAMA H____________")
print("__PROGRAM KALKULASI TOTAL HARGA BARANG__")
print("________________________________________")

# Membuat Login
def login():
    nama = input("\nMasukkan nama: ") 
    prodi = input("Masukkan program studi: ")
    nim = input("Masukkan NIM: ")  
    print(f"Selamat datang, {nama}, Program Studi: {prodi} (NIM: {nim})!")  

# Menginput dan menghitung total harga barang
def hitung_total():
    harga = float(input("\nMasukkan harga barang (Rp.): "))  
    jumlah = int(input("Masukkan jumlah pembelian: "))  
    total = harga * jumlah  
    
    # Cek apakah total > 250.000 dan output perhitungan
    if total > 250000:
        diskon = total * 0.25  
        total -= diskon  
        print(f"Diskon 25% diberikan! Total yang harus dibayar: Rp. {total:.2f}")
    else:
        print(f"Total pembayaran: Rp. {total:.2f}")

# Memanggil fungsi login
def main():
    login()  
    
    # Looping jika ingin menghitung lagi
    while True:
        hitung_total()
        
        ulang = input("Ingin menghitung lagi? (ya/tidak): ").lower()  
        if ulang != 'ya':  
            print("Terima kasih!")
            break  

# Jalankan program utama
if __name__ == "__main__":
    main() # Memanggil fungsi main untuk menjalankan keseluruhan program
 
