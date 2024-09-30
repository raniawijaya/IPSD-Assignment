### Soal 1: Memecahkan Masalah Unik dengan Loop dan If-Else
'''
Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya:

1
2 3
5 7 11
13 17 19 23
...
Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan prima.
'''

def bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prima(count):
    prima = []
    num = 2
    while len(prima) < count:
        if bilangan_prima(num):
            prima.append(num)
        num += 1
    return prima


def print_pola_prima(rows):
    total_prima = sum(range(1, rows + 1))
    prima = generate_prima(total_prima)
    index = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(prima[index], end=' ')
            index += 1
        print()


print_pola_prima(7)

'''
Penjelasan :
1. Fungsi bilangan_prima digunakkan untuk memeriksa apakah suatu bilangan merupakan bilangan prima.
    (+) if n <= 1 : Bilangan yang kurang dari atau sama dengan 1 bukan bilangan prima.
    (+) for i in range(2, int(n**0.5) + 1) : Loop dari 2 sampai akar kuadrat dari n, karena faktor bilangan prima tidak akan lebih besar dari akar kuadratnya.
    (+) if n % i == 0 : jika n habis dibagi i, maka n bukan bilangan prima
    (+) Jadi, jika tidak ada pembagi yang didapatkan, maka n adalah bilangan prima.

2. Fungsi generate_prima(count) akan menghasilkan daftar bilangan prima sebanyak count (banyaknya bilangan prima yang perlu dicetak untuk dibuat pola).
    (+) prima = [] : inisialisasi daftar kosong untuk menyimpan bilangan prima
    (+) num = 2 : bilangan prima dimulai dari bilangan 2
    (+) while len(prima) < count: : loop berlanjut hingga jumlah bilangan prima dalam daftar mencapai count
    (+) if bilangan_prima(num): : memeriksa apakah num adalah bilangan prima
    (+) prima.append(num) : jika num adalah bilangan prima, maka akan ditambhakan ke daftar prima
    (+) num += 1 : menambahkan num untuk memeriksa bilangan selanjutnya.

3. Fungsi print_pola_prima(rows) bertujuan mencetak pola bilangan prima sesuai dengan jumlah baris yang diinginkan.
    (+) total_prima = sum(range(1, rows + 1)) : menghitung total bilangan prima yang dibutuhkan. Misalnya untuk 7 baris, jumlah total bilangan prima adalah 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    (+) prima = generate_prima(total_prima) : menghasilkan daftar bilangan prima sebanyak total_prima
    (+) index = 0 : inisialisasi index untuk mengakses elemen dalam daftar prima
    (+) for i in range(1, row + 1): : loop untuk setiap baris dari satu hingga rows
    (+) for j in range(i): : loop untuk mencetak bilangan prima pada setiap baris
    (+) print(prima[index], end=' ') : mencetak bilangan prima pada index 
    (+) index += 1 : tambahan indeks untuk mengakses bilangan prima beirikutnya
    (+) print() : memindahkan ke baris berikutnya setelah mencetak semua bilangan prima pada baris yang sedang dikerjakan
 '''
### Soal 2: Membuat Fungsi dengan Syarat Spesifik
'''
Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.
'''


def combine_and_sort_odd_index_elements(list1, list2):
    # Mengembalikan elemen dengan indeks ganjil dari kedua list
    odd_index_elements = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(1, len(list2), 2)]

    # Mengurutkan elemen secara menurun
    sorted_elements = sorted(odd_index_elements, reverse=True)

    return sorted_elements


list1 = [10, 21, 32, 43, 54, 65]
list2 = [15, 26, 37, 48, 59, 70]
result = combine_and_sort_odd_index_elements(list1, list2)
print(result)
''' 
Penjelasan : 
1. Fungsi odd_index_elemenrs = [list1[i] for i in range(1, len(list1), 2)] + [list2[i] for i in range(1, len(list2), 2)] untuk mengambil elemen dengan indeks ganjil.
2. Menggunakan list comprehension untuk mengambil elemen dengan indeks ganjil dari list1 dan list2.
3. range(1, len(list1), 2) mengahsilkan indeks ganjil (1,3,5,...) dari list1, begitu pula untuk list2.
4. Kemudian kedua list digabungan dengan operator +.
5. Untuk mengurutkan elemen secara menurun, kita menggunakan fungsi sorted() dengan parameter reverse=True.
6. Sedangkan untuk mengembalikkan list yang sudah diurutkan sebagai hasil dan fungsi, kita gunakan return sorted_elements.
'''

### Soal 3: Exception Handling dalam Konteks Nyata
'''
Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus:
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir.
'''

class ATM:
    def __init__(self, pin, saldo):
        self.pin = pin
        self.saldo = saldo
        self.attempts = 0

    def verify_pin(self):
        while self.attempts < 3:
            masukkan_pin = input("Masukkan PIN Anda: ")
            if masukkan_pin == self.pin:
                return True
            else:
                self.attempts += 1
                print(f"PIN salah. Anda memiliki {3 - self.attempts} percobaan lagi.")
        return False

    def penarikan(self, jumlah):
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak mencukupi.")
        self.saldo -= jumlah
        return self.saldo


def main():
    atm = ATM(pin="111777", saldo=1000000000)  # PIN dan saldo awal

    if atm.verify_pin():
        try:
            jumlah = int(input("Masukkan jumlah penarikan: "))
            sisa_saldo = atm.penarikan(jumlah)
            print(f"Penarikan berhasil. Saldo akhir : {sisa_saldo}")
        except ValueError as e:
            print(e)
    else:
        print("PIN salah 3 kali. Kartu ATM diblokir.")

if __name__ == "__main__":
    main()
'''
Penjelasan :
1. class ATM mendefinisikan objek ATM dan metode yang diperlukan untuk mensimulasikan transaksi ATM.
2. Metode __init__ digunakkan untuk menginisialisasi objek ATM dengan PIN dan saldo awal.
3. self.pin untuk menyimpan PIN yang benar.
4. self.saldo untuk menyimpan informasi saldo awal.
5. self.attempts untuk menyimpan jumlah percobaan memasukkan PIN yang salah.
6. verify_pin berfungsi meminta pengguna memasukkan PIN sebanyak 3x.
    (+) Jika PIN salah, jumlah percobaan (self.attempts) bertambah dan pesan kesalahan ditampilkan.
    (+) Jika pengguna salah memasukkan PIN 3x, program mengembalikkan False.
7. Fungsi penarikkan bertujuan menerima jumlah penarikan sebagai parameter.
    (+) Jika jumlah penarikan lebih besar dari saldo, program memberikan ValueError dengan pesan "Saldo tidak mencukupi."
    (+) Jika saldo mencukupi, jumlah penarikan dikurangi dari saldo dan saldo yang tersisa akan dikembalikan.
8. Fungsi main() akan menginisialisasi objek ATM dengan PIN "111777" dengan saldo awal 1M.
9. Memverifikasi PIN dengan fungsi verify_pin.
    (+) Jika PIN benar, meminta jumlah penarikan dan mencoba melakukan penarikan.
    (+) Kemudian jika penarikan berhasil, saldo akan ditampilkan.
    (+) Jika saldo tidak mencukupi, pesan kesalahan ditampilkan.
    (+) Jika PIN salah 3x, pesan bahwa "Kartu ATM diblokir." ditampilkan.
10. Blok if __name__ == "__main__" akan memastikan bahwa fungsi main hanya dijalankan jika skrip dijalankan secara langsung, bukan diimpor sebagai modul.
'''

### Soal 4: Studi Kasus Pengelolaan Data
''' Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.
'''
import csv

def baca_csv(file_path):
    data_mahasiswa = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nama = row['Nama Siswa']
            nilai = int(row['Nilai'])
            if nama in data_mahasiswa:
                data_mahasiswa[nama].append(nilai)
            else:
                data_mahasiswa[nama] = [nilai]
    return data_mahasiswa

def hitung_rata_rata(data_mahasiswa):
    rata_rata = {}
    for nama, nilai in data_mahasiswa.items():
        rata_rata[nama] = sum(nilai) / len(nilai)
    return rata_rata

def nilai_tertinggi_terendah(rata_rata):
    mahasiswa_tertinggi = max(rata_rata, key=rata_rata.get)
    mahasiswa_terendah = min(rata_rata, key=rata_rata.get)
    print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_tertinggi} dengan rata-rata nilai {rata_rata[mahasiswa_tertinggi]:.2f}")
    print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terendah} dengan rata-rata nilai {rata_rata[mahasiswa_terendah]:.2f}")

def main():
    file_path = "C:/Users/rania/OneDrive/Dokumen/siswa_nilai (1).csv"
    data_mahasiswa = baca_csv(file_path)
    rata_rata = hitung_rata_rata(data_mahasiswa)
    nilai_tertinggi_terendah(rata_rata)

    for nama, rata in rata_rata.items():
        print(f"{nama}: {rata:.2f}")

if __name__ == "__main__":
    main()
'''
Penjelasan : 
1. Import modul csv, kemudian untuk membaca dan menyimpan file csv ke dalam dictionary kita gunakkan fungsi def baca_csv(file_path) ke dalam dictionary data_mahasiswa.
    (+) File csv dibaca dengan mode baca ('r').
    (+) csv.DictReader untuk membaca baris-baris atau row dalam file sebagai dictionary.
    (+) Pada setiap bariis, diambil nilai dari kolom 'Nama Siswa' dan 'Nilai'.
    (+) Menambahkan nilai ke dalam list yang sesuai dengan nama siswa dalam dictionary data_mahasiswa.
2. Fungsi hitung_rata_rata(data_mahasiswa) bertujuan untuk menghitung rata-rata nilai untuk setiap mahasiswa.
    (+) Pertama, kita buat dictionary rata_rata untuk menyimpan rata-rata nilai.
    (+) Setiap mahasiswa dalam data_mahasiswa, akan dihitung rata-rata nilainya dengan membagi jumlah nilai dengan jumlah elemen dalam list nilai.
    (+) Kemudian, hasil rata-rata disimpan ke dalam dictionary rat_rata.
3. Fungsi nilai_tertinggi_terendah(rata_rata) akan menemukan dan mengetahui mahasiswa dengan nilai rata-rata tertinggi dan terendah.
    (+) Menggunakan fungsi max untuk menemukan mahasiswa dengan nilai rata-rata tertinggi.
    (+) Menggunakan fungsi min untuk menemukan mahasiswa dengan nilai rata-rata terendah.
    (+) Kemudian, akan diketahui nilai tertinggi dan terendah, beserta rata-rata nilainya.
4. Fungsi main() akan mengatur alur utama program
    (+) Kita harus memanggil file csv dalam path file csv.
    (+) Kemudian memanggil fungsi baca_csv agar file terbaca.
    (+) Memanggil fungsi hitung_rata_rata untuk mengetahui rata-rata nilai.
    (+) Mencetak rata-rata nilai untuk mahasiswa.
5. Blok if __name__ == "__main__" akan memastikan bahwa fungsi main() hanya dijalankan jika script ini dijalankan secara langsung, bukan diimpor sebagai modul.
'''

### Soal 5: Kombinasi Logika dan Kreativitas
'''
Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, tampilkan apakah pemain menang atau kalah.
'''

import random

def main():
    angka_rahasia = random.randint(1, 100)
    percobaan = 5

    print("Selamat datang di permainan tebak angka!")
    print("Saya telah memilih sebuah angka antara 1 sampai 100.")
    print(f"Kamu memiliki {percobaan} kali percobaan untuk menebak angka tersebut.")

    for i in range(percobaan):
        tebakan = int(input(f"Tebakan {i+1}: "))

        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print("Selamat tebakan kamu benar!")
            break
    else:
        print(f"Maaf, kesempatan percobaan telah habis. Angka yang benar adalah {angka_rahasia}.")

if __name__ == "__main__":
    main()

'''
Penjelasan :
1. Import modul random untuk menghasilkan angka acak.
2. random.randint(1,100) berfungsi untuk mengahsilkan angka acak dari 1 sampai 100.
3. Kemudian loop for akan mengulang proses hingga kesempatan habis. Kondisi if-elif-else akan memberi petunjuk apakah tebakan terlalu kecil, terlalu besar, atau benar. Sedangkan else pada loop for akan menampilkan pesan jika pemain kehabisan percobaan.
'''

### Soal 6: Rekursi yang Tidak Biasa
'''
Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:

Input: n = 4
Output: 1, 1, 2, 6, 24
'''

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

def urutan_faktorial(n):
    hasil = []
    for i in range(n + 1):
        hasil.append(faktorial(i))
    return hasil

def main():
    n = 4 # Dapat diubah
    hasil = urutan_faktorial(n)
    print(f"Input: n = {n}")
    print("Output:", ", ".join(map(str, hasil)))

if __name__ == "__main__":
    main()

'''
Penjelasan : 
1. Fungsi faktorial(n) merupakan fungsi rekursif yang menghitung faktorial dari bilangan bulat n.
    (+) Jika n adalah 0 atau 1, fungsi akan mengembalikan nilai 1.
    (+) Jika n lebih besar dari 1, fungsi mengembalikan n dikali dengan hasil faktorial n-1.
2. Faktorial dari sebuah bilangan bulat n adalah hasil perkalian semua bilangan bulat positif kurang dari atau sama dengan n.
3. Kemudian loop for digunakan untuk mengulangi proses perhtungan faktorial untuk setiap bilangan dari 0 hingga n. List digunakkan untuk menyimpan hasil faktorial dari setiap bilangan tersebut.
'''

### Soal 7: Pemrograman dengan Algoritma Greedy
'''
Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. Namun, program Anda harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.
'''
def minimum_koin(jumlah, koins):
    koins.sort(reverse=True) #Mengurutkan koin dari nilai terbesar ke terkecil
    result = []
    for koin in koins:
        while jumlah >= koin:
            jumlah -= koin
            result.append(koin)
    if jumlah != 0:
        return "Tidak mencapai jumlah koin yang tersedia."
    return result

def main():
    jumlah = int(input("Masukkan jumlah uang: ")) # input jumlah uang dan daftar nilai koin dari pengguna
    koins = list(map(int, input("Masukkan nilai koin yang tersedia (dipisahkan dengan spasi): ").split()))

    result = minimum_koin(jumlah, koins) # Memanggil fungsi kombinasi minimum koin

    if isinstance(result, list): #Hasil
        print(f"Kombinasi minimum koin untuk mencapai jumlah {jumlah} adalah: {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()
'''
Penjelasan : 
1. Fungsi minimum_koin(jumlah, koins) memiliki dua parameter, yaitu jumlah sebagai jumlah uang yang ingin dicapai dan koins sebagai daftar nilai koin yang tersedia.
2. Untuk mengurutkan koin, kita menggunakan koins.sort(reverse=True), koin akan diurutkan dari nilai terbesar ke terkecil untuk meminimalkan jumlah koin yang digunakan.
3. Daftar result akan menyimpan kombinasi koin yang digunakan dengan result = [].
4. Untuk mengurangi jumlah koin, kita menggunakan for koin in koins:. Jika jumlah masih lebih besar atau sama dengan nilai koin. maka jumlah akan dikurangi dengan nilai koin tersebut dan akan ditambhkan koin ke dalam daftar result.
5. Dengan if jumlah != 0: akan mengembalikan pesan kesalahan, jika setelah proses pengurangan masih ada sisa jumlah yang tidak bisa dicapai dengan koin yang tersedia.
6. Jika jumlah berhasil dicapai, fungsi mengembalikan daftar result yang berisi kombinasi koin.
7. Kemudian mendapatkan input jumlah uang dan daftar nilai koin dari pengguna dengan int.
8. Lalu memanggil fungsi minimum_koin.
'''

### Soal 8: Kombinasi String dan Manipulasi List
'''
Buat sebuah program yang menerima string dari pengguna dan mengonversi string tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:

Input: "Saya suka Python"
Output: ["ayaS", "akus", "nohtyP"]
'''
def balik_kata(kalimat):
    kata_list = kalimat.split() # Memisahkan kalimat menjadi list kata-kata
    kata_terbalik = [kata[::-1] for kata in kata_list] # Membalik setiap kata dalam list
    return kata_terbalik

def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    hasil = balik_kata(kalimat) # Fungsi untuk membalik kata-kata
    print(f"List kata-kata terbalik: {hasil}")

if __name__ == "__main__":
    main()

'''
Penjelasan :
1. Fungsi balik_kata akan menerima satu parameter, kalimat yang merupakan string input dari pengguna.
    (+) Kalimat.split() digunakan untuk memisahkan string menjadi list kata-kata berdasarkan spasi.
    (+) Untuk membalik setiap kata dalam list kita memerlukan list comperhension [kata[::-1] for kata in kata_list].
    (+) Kemudian fungsi akan mengenmbalikkan list kata-kata yang telah dibalik.
2. Fungsi main() akan menerima input kalimat dari pengguna melalui input().
3. Lalu memanggil fungsi balik_kata dengan input kalimat dan menyimpan hasilnya dalam variabel hasil.
4. Program dijalankan dengan if __name__ == "__main__" untuk memastikan fungsi main dijalankan.
'''

### Soal 9: Konsep Class dan Object-Oriented Programming
'''
Buat class bernama `Buku` yang memiliki atribut `judul`, `penulis`, dan `tahun_terbit`. Buat method dalam class untuk menampilkan informasi buku, serta method untuk menghitung usia buku berdasarkan tahun saat ini. Buatlah 3 objek dari class `Buku` dan tampilkan informasi serta usia masing-masing buku.
'''
from datetime import datetime

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    def hitung_usia(self):
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - self.tahun_terbit
        return usia

def main():
    # Membuat objek dari class Buku
    buku1 = Buku("Python untuk Pemula", "John Doe", 2015)
    buku2 = Buku("Pemrograman Lanjut dengan Python", "Jane Smith", 2018)
    buku3 = Buku("Data Science dengan Python", "Alice Johnson", 2020)

    # Menampilkan informasi dan usia masing-masing buku
    for buku in [buku1, buku2, buku3]:
        buku.tampilkan_informasi()
        print(f"Usia Buku: {buku.hitung_usia()} tahun\n")

if __name__ == "__main__":
    main()
'''
Penjelasan :
1. Import modul datetime untuk mendapatkan tahun saat ini.
2. Mendefinisikan class buku dengan atribut judul, penulis, dan tahun terbit. Metode _init__ merupakan dasar yang digunakan untuk menginisialisasi objek dengan atribut yang ada.
3. Sedangkan program tampilkan_informasi berfungsi menampilkan informasi buku dari atribut yang terdaftar.
4. Fungsi hitung_usia akan menghitung usia buku berdasarkan tahun saat ini, dengan rumus tahun sekarang dikurangi tahun terbit buku.
5. Dan fungsi main bertugas untuk membuat tiga objek dari class buku dan menampilkan informasi serta usia masing-masing buku.
'''

### Soal 10: Algoritma dengan Persyaratan Logika Khusus
'''
Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa ditemukan.
'''
def binary_search(arr, target):
    if target % 2 != 0: # Memeriksa apakah angka ganjil
        return "Nilai yang dicari adalah angka ganjil, sehingga tidak bisa ditemukan."

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Nilai {target} ditemukan pada indeks {mid}."
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return f"Nilai {target} tidak ditemukan dalam list."

def main():
    # Input list angka genap dari pengguna
    arr = list(map(int, input("Masukkan list angka genap yang sudah diurutkan (dipisahkan dengan spasi): ").split()))
    target = int(input("Masukkan nilai yang ingin dicari: "))

    # Memanggil fungsi binary_search_even
    result = binary_search(arr, target)
    print(result)

if __name__ == "__main__":
    main()
''' 
Penjelasan : 
Fungsi binary_search akan menerima dua parameter yaitu arr (list angka genap yang terurut) dan target (nilai yang ingin dicari).
    (+) Pertama fungsi memeriksa apakah target adalah angka ganjil. Jika ya, fungsi mengembalikan pesan bahwa nilai tersebut tidak bisa ditemukan.
    (+) Jika target adalah bilangan genap, fungsi melanjutkan dengan algoritma pencariann biner standar :
        * Inisialisasi low dan high untuk menentukan batas pencarian.
        * Selama low kurang dari atau sama dengan high, maka menghitung indeks tengah mid.
        * Jika nilai pada indeks tengah sama dengan target, kembalikan pesan bahwa nilai ditemukan beserta indeksnya.
        * Jika nilai pada indeks tengah lebih kecil dari target, perbarui low menjadi mid + 1.
        * Jika nilai pada indeks tengah lebih besar dari target, perbarui high menjadi mid - 1.
        * Jika target tidak ditemukan, fungsi mengembalikan pesan bahwa nilai tidak ditemukan dalam list.
'''
