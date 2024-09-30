### Latihan Praktikum 1

### VARIABEL TIPE DATA

# Buat program menampilkan nama dan umur
nama = "Rania"
umur = 20
print(f"Nama : {nama} \nUmur : {umur}")

# Buatlah variabel untuk menyimpan nilai luas dan keliling lingkaran, hitung hasilnya
from math import pi
jari = 14
luas = pi *jari**2
keliling = 2*pi*jari
print(f"Luas Lingkaran : {luas} \nKeliling Lingkaran : {keliling}")

# Tampilkan tipe data dari variabel yang menyimpan angka dan teks
angka = 777
teks = 'ini angka'
print(f"Tipe Data Angka : {type(angka)} \nTipe Data Teks : {type(teks)}")

# Buat program yang mengubah nilai tipe integer menjadi float
nilai = 99
print(f'nilai kamu adalah {nilai} dan tipe datanya adalah {type(nilai)}')
nilai = float(nilai)
print(f'nilai kamu adalah {nilai} dan tipe datanya adalah {type(nilai)}')

# Buat program yang mengubah string menjadi integer dan sebaliknya
a = "789"
print(f"Tipe Data a : {type(a)}")
a = int(a)
print(f"Tipe Data a : {type(a)}")

# Buat Program yang menghasilkan string dengan angka
text = "kembali "
multiplied_text = text * 3
print(multiplied_text)

### PERCABANGAN (IF-ELSE)

# Buat program yang memeriksa apakah angka adalah bilangan genap atau ganjil
number = 2
if number % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

# Buat program yang memeriksa apakah sebuah nilai lebih besar dari 100
value = 270
if value > 100:
    print("lebih dari 100")
else:
    print("100 atau kurang dari")

# Buatlah program yang menerima input imur dan menampilkan kategori umur (anak-anak, remaja, dewasa)
age = 34
if age <= 12:
    print("Anak-anak")
elif 13 <= age <= 17:
    print("Remaja")
else:
    print("Dewasa")

# Buatlah program yang meminta input nama pengguna, jika nama benar tampilkan "Welcome"
username = input("Enter username: ")
if username == "Rania":
    print("Welcome {username}")
elif username == "Jewo":
    print(f"Welcome {username}")
else:
    print("Nama tidak dikenali")

# Buatlah program yang menampilkan apakah suatu tahun adalah tahun kabisat
year = 2024
if (year %4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")

# Buatlah program untuk menentukan apakah seseorang boleh memberikan suara berdasarkan umurnya
age = 21
if age >= 18:
    print("Boleh memberikan suara")
else:
    print("Tidak boleh memberikan suara")

# Buatlah program yang meminta input tiga angka dan menampilkan angka terbesar
a, b, c = 18, 9, 55
largest = max(a, b, c)
print(f"Nilai terbesar {largest}")

# Buatlah program yang mengecek apakah dua string memiliki panjang yang sama
str1 = "dreams"
str2 = "dreaming"
if len(str1) == len(str2):
    print("Memiliki Panjang yang sama")
else:
    print("Memiliki panjang yang berbeda")

### PERULANGAN (LOOPS)

# Buat program yang menampilkan angka 1 sampai 10 menggunakan for loop
for i in range(1, 11):
    print(i)

# Buat program yang menampilkan bilangan genap dari 2 sampai 20 menggunakan while loop
i = 2
while i <= 20:
    print(i)
    i += 2

# Buat program yang menrima input dan menampilkan kalimat tersebut sebanyak 5 kali
sentence = input("Masukan Kalimat: ")
for _ in range(5):
    print(sentence)

# Buat program untuk menghitung jumlah angka dari 1 sampai N
N = 5
total_sum = sum(range(1, N + 1))
print(f"Sum dari 1 to {N} adalah {total_sum}")

# Buat program yang menggunakan break untuk keluar dari loop jika kondisi terterntu terpenuhi
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Buatlah program yang menggunakan continue untuk melewati iterasi tertentu dalam loop
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Buatlah program yang menampilkan tabel perkalian 1 sampai 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# Buatlah program untuk menghitung jumlah bilangan ganjil antara dua bilangan yang diberikan
start = 1
end = 10
sum_odds = sum(i for i in range(start, end + 1) if i % 2 != 0)
print(f"Sum of odd numbers between {start} and {end} is {sum_odds}")

### FUNGSI (FUNGTIONS)

# Buatlah fungsi untuk menghitung luas segitiga
def triangle_area(base, height):
    return 0.5 * base * height

print(triangle_area(15, 5))

# Buat fungsi yang menerima nama dan menampilkan "Halo, [nama]"
def great(name):
    print(f"Halo, {name}")

great("Deva")

# Buat fungsi untuk memeriksa apakah suatu angka adalah bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

# Buat fungsi yang mengembalikan nilai maksimum dari tiga angka
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3, 7, 5))

# Buatlah fungsi yang mengkonversi suhu dari Celcius ke Fahrenheit
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print(celcius_ke_fahrenheit(30))

# Buat fungsi rekrusif untuk menghitung faktorial dari suatu angkka
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Buat fungsi yang menerima dua string dan menggabungkannya
def gabung(str1, str2):
    return str1 + str2

print(gabung("Hello, ", "World!"))

# Buat fungsi untuk menghilangkan total bilangan dalam sebuah list
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2 ,3 ,4 , 5]))

### LIST & TUPLE

# Buatlah program yang membuat list dari 5 nama
names = ["Haruto", "Jolie", "Cornel", "Rasendriya", "Shinta"]
# Buat program untuk mengakses elemen pertama dan terakhir dari sebuah list
print(names[0])
print(names[-1])
#Buat program untuk menambahkan elemen baru ke list
names.append("Asahi")
print(names)
# Buatlah program untuk menghapus elemen tertentu dari list
names.remove("Jolie")
print(names)
# Buat program yang menghitung jumlah elemen dalam list
print(len(names))

# Buat program yang mengurutkan list angka secara ascending
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

# Buat program untuk membuat tuple yang berisi 5 bilangan
numbers_tuple = (1, 2, 3, 4, 5)
# Buat program untuk memeriksa apakah elemen ada dalam tuple
print(3 in numbers_tuple)

### DICTIONARY

# Buat dictionary untuk menyimpan nama dan nilai siswa
students = {"Desta" : 90, "Daniza" : 87, "Ade" : 80}
# Buat program untuk menampilkan nilai seorang siswa dari dictionary
print(students["Daniza"])
# Buat program untuk menambahkan siswa baru ke dictionary
students["Fafa"] = 98
print(students)
# Buat program yang menghapus entri dari dictionary berdasarkan nama siswa
del students["Desta"]
print(students)
# Buat program untuk mengupdate nilai siswa dalam dictionary
students["Ade"] = 78
print(students)
# Buat program yang menampilkan semua nama siswa dari dictionary
print(students.keys())
# Buat program yang menampilkan semua nilai siswa dari dictionary
print(students.values())
# Buat program untuk mengubah nilai menjadi list daari sebuah dictionary
scores_list = list(students.values())
print(scores_list)

### SET

# Buat program untuk membuat set yang berisi angka-angka unik
unique_numbers = {1, 2, 3, 4, 5}
# Buat program yang menambahkan elemen baru ke dalam set
unique_numbers.add(6)
print(unique_numbers)
# Buat program yang menghapus elemen dari set
unique_numbers.remove(3)
print(unique_numbers)

# Buat program yang menampilkan irisan dari dua set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))
# Buat program yang menampilkan gabungan dari dua set
print(set1.union(set2))
# Buat program yang mengecek apakah satu set merupakan subset dari set lain
print(set1.issubset(set2))
# Buat program yang menampilkan perbedaan dari dua set
print(set1.difference(set2))
# Buat program yang menampilkan perbedaan dari dua set
print(set1.difference(set2))
# Buat program untuk menghitung elemen unik dalam sebuah list menggunakan set
numbers = [1, 2, 2, 3, 4 ,4, 4, 5]
unique_numbers = set(numbers)
print(len(unique_numbers))

### FILE HANDLING

# Buat program yang membuat dan menulis teks ke dalam file
with open("example.txt", "w") as file :
    file.write("Hello, world!")

# Buat program yang membaca isi dari file teks
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Buat program untuk menambahkan teks baru ke file yang sudah ada
with open("example.txt", "a") as file:
    file.write("\nNew line addes.")

# Buat program yang menampilkan isi file baris per baris
with open("example.txt", "r") as file:
    for line in file:
        print(line, end="")

# Buat program yang menghitung jumlah kata dalam sebuah file
with open("example.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(word_count)

# Buat progra, untuk menghapus file
import os
os.remove("example.txt")

# Buat program yang memeriksa apakah sebuah file ada atau tidak
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")

# Buat program yang mengcopy isi file ke file lain
with open("example.txt", "w") as file:
    file.write("Hello, world!")

with open("example.txt", "r") as src:
    with open("copy.txt", "w") as dst:
        dst.write(src.read())

### LIST COMPREHENSION
# Buat program untuk membuat list dari angka 1 sampai 10 menggunakan list comprehension
numbers = [x for x in range(1, 11)]
print(numbers)

# Buat program untuk membuat list bilangan genap dari 1 sampai 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# Buat program untuk membuat list bilangan kuadrat dari 1 sampai 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# Buat program untuk mengubah setiap elemen dalam list menjadi huruf besar
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
print(upper_words)

# Buat program yang menyaring elemen dalam list jika lebih besar dari 5
numbers = [1, 2, 3, 6, 7, 8]
filtered = [x for x in numbers if x > 5]
print(filtered)

# Buat program untuk membuat list huruf vokal dari string
string = "hello world"
vowels = [char for char in string if char in 'aeiou']
print(vowels)

### EXCEPTION HANDLING

result = 10/0
print(result)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")

# Buatlah program yang mengkap kesalahan input yang bukan angka
angka = 'ini angka'
print(int(angka))

angka = 'ini angka'
try:
    angka = int(angka)
except ValueError:
    print("")

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Input is not a valid number")

# Buatlah program yang menangkap kesalah akses elemen list di luar indeks
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range")

# Buat program yang menangani beberapa tipe kesalahan dengan exception yang berbeda
try:
    result = 10 / int(input("Enter a number: "))
except ValueError:
    print("Input is not a valid number")
except ZeroDivisionError:
    print("Cannot devide by zero")

# Buat program yang menggunakan finally untuk menampilkan pesan setelah exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("This will execute regardless of an exception")

### OOP (PBJECT-ORIENTED PROGRAMMING)

# Buat class mahasiswa yang memiliki atribut nama dan umur
from sklearn.linear_model import LinearRegression

LinearRegression().fit()

class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

# Buat method dalam class untuk menampilkan informasi mahasiswaa
class Mahasiswa:
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self.u = umur
        self.jk = jenis_kelamin

    def tampilkan_informasi(self):
        print(f"Nama: {self.nama}, Umur: {self.u}, Jenis Kelamin : {self.jk}")

# Buat program untuk menginisialisasi objek dari class mahasiswa
mahasiswa1 = Mahasiswa("Zayn", 20)
mahasiswa1.tampilkan_informasi()

# Buat program yang menggunakan constructor dalam class
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Ian")
print(person.name)

# Buat proggram menggunakan inheritance untuk class Person dan Mahasiswa
class Person:
    def __init__(self, name):
        self.name = name

class Mahasiswa(Person):
    def __init__(self, name, umur):
        super().__init__(name)
        self.umur = umur

mahasiswa = Mahasiswa("Zayn", 20)
print(mahasiswa.name, mahasiswa.umur)

# Buat program yang menggunakan method overriding dalam inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

# Buat program yang menampilkan jumlah objek yang dibuat dari sebuah class
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
print(Counter.count)

# Buat program yang membuat class dengan method statis
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))

### MODULES & PACKAGES

# Buat program yang meng-import modul matematika dan menggunakan fungsi `sqrt`.
# square.py
def area(side):
    return side * side

def perimeter(side):
    return 4 * side

# cuboid.py
def volume(length, width, height):
    return length * width * height

# sphere.py
import math
def volume(radius):
    return (4/3) * math.pi * radius**3

# Buat package untuk menghitung volume berbagai bangun ruang.
import math
def volume(radius):
    return (4/3) * math.pi * radius**3

# Buat program yang meng-import modul random dan menghasilkan angka acak.
import random
print(random.randint(1, 100))

# Buat program yang menggunakan fungsi waktu untuk menghitung lama eksekusi program.
import time
start_time = time.time()

time.sleep(1)
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")

### LAMDA DAN HIGHER-ORDER FUNCTIONS

# Buat fungsi lambda untuk menghitung kuadrat dari sebuah angka.
square = lambda x: x * x
print(square(5))

# Buat program yang menggunakan `map` untuk menghitung kuadrat dari semua elemen dalam list.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)

# Buat program yang menggunakan `filter` untuk menyaring bilangan ganjil dari list.
numbers = [1, 2, 3, 4, 5, 6]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)

# Buat program yang menggunakan `reduce` untuk menghitung jumlah semua elemen dalam list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)

### MISCELLANEOUS

# Buat program untuk menghitung jumlah huruf vokal dalam sebuah string.
string = "hello world"
vowels = "aeiou"
count = sum(1 for char in string if char in vowels)
print(count)

# Buat program untuk memeriksa apakah string adalah palindrom.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))

# Buat program yang menggunakan nested loop untuk menampilkan pola bintang.
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Buat program untuk menghitung faktorial menggunakan iterasi.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

# Buat program yang meminta input nama dan umur lalu menampilkannya dengan format tertentu.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Name: {name}, Age: {age}")

# Buat program yang membalik urutan elemen dalam list tanpa menggunakan fungsi built-in.
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

# Buat program yang menampilkan hari saat ini menggunakan modul `datetime`.
import datetime
today = datetime.datetime.now()
print(today.strftime("%A"))

# Buat program yang menerima dua angka dari input, lalu menampilkan hasil pembagiannya.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num2 != 0:
    print(num1 / num2)
else:
    print("Cannot divide by zero")


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