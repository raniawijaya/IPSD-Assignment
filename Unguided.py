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
    if n<= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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
    atm = ATM(pin="111777", saldo=1000000000) # PIN dan saldo awal

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
