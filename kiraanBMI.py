# Program Mengira BMI  
# oleh: AmirulMukminin

# Mengimport time untuk mengarah program menunggu sebelum mula semula
import time

# Mengisytiharkan pemboleh ubah untuk fungsi
keputusanKiraan = 0
teksKeputusan = ""
cadanganPemakanan = 0
cadanganSenaman = 0

# Ini adalah fungsi kategoriBMI. Fungsi ini akan memangil BMIresult untuk menentukan 
# kategori anda berdasarkan BMI.
def kategoriBMI(BMI, keputusanKiraan):
    if BMI <= 0.0:
        print("RALAT: TINGGI BUKAN DALAM METER.")
        exit(0)
    else:    
        if BMI <= 20.6:
            keputusanKiraan = 0
        elif BMI  <= 26.4:
            keputusanKiraan = 1    
        elif BMI  <= 30.9:
            keputusanKiraan = 2
        elif BMI  <= 45.2:
            keputusanKiraan = 3
    

# Fungsi BMIresult adalah untuk tentukan kategori daripada kategoriBMI
def BMIresult(keputusanKiraan):
    switcher = {
        0: 'Kurus',
        1: 'Normal',
        2: 'Gemuk',
        3: 'Obesiti'
    }  

    return switcher.get(keputusanKiraan)
    
# Fungsi ini adalah untuk memaparkan keputusan di akhir program
def paparKeputusan(BMI):
    print ("")
    print ("KEPUTUSAN PENGIRAAN")
    print ("")
    print ("Nama:",nama)
    print ("Umur:",umur, "tahun")
    print ("Berat:",berat, "kg")
    print ("Tinggi:",tinggi, "m")
    print ("BMI:",BMI)
    print ("Kategori BMI :", BMIresult(keputusanKiraan))
    print ("cadangan pemakanan:", cadanganPemakanan, "kcal")
    print ("cadangan senaman:", cadanganSenaman, "kali")

# Permulaan program
if __name__ == "__main__":
    # Paparkan tajuk program
    print("Program Pengiraan BMI oleh AmirulMukminin")
    time.sleep(3)

    # Pengambilan input pengguna
    nama = input("Nama:")
    umur = input("Umur:")
    berat = float(input("Berat (KG):"))
    tinggi = float(input("Tinggi (M):"))

    # Pengiraan BMI 
    BMI = round(berat/(tinggi*tinggi), 1)

    # Memanggil kategoriBMI untuk mengkategorikan pengguna pada scale BMI
    kategoriBMI(BMI, keputusanKiraan)

    # Perbandingan untuk menentukan cadangan makanan dan senaman
    if keputusanKiraan == 0:
            cadanganPemakanan = 2400
            cadanganSenaman = 2
    elif keputusanKiraan == 1:
            cadanganPemakanan = 2100
            cadanganSenaman = 3
    elif keputusanKiraan == 2:
            cadanganPemakanan = 1800
            cadanganSenaman = 4
    elif keputusanKiraan == 3:
            cadanganPemakanan = 1500
            cadanganSenaman = 5
    
    print("Sedang mengira...")
    time.sleep(5)
    paparKeputusan(BMI)
