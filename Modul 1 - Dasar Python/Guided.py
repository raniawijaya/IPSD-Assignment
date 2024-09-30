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
    
