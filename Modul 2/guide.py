import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/rania/OneDrive/Dokumen/Movie_classification.csv')
df.head(10)
df.tail()
df.info()
df.describe()
df.describe().T
df.isna().sum()
df.isnull().sum()

# Melihat ukuran data (baris,kolom)
df.shape
df.dtypes
df.duplicated().sum()
(df.isna().sum()/len(df))*100

a = df.copy(deep=True)
a.dropna(inplace=True)
a.dropna(inplace=True)
a

df = df.dropna()
df.isna().sum()
a.isna().sum()

df.to_excel('Movie_classification_clean.xlsx', index=False)
bebas = pd.read_excel('Movie_classification_clean.xlsx')
bebas.head()

# importing package pandas dan membaca dataset Iris
import pandas as pd
iris_filename = 'C:/Users/rania/OneDrive/Logika Matematika/iris(1).csv'
iris = pd.read_csv(iris_filename, sep=',',
                   decimal='.', header=None,
                   names= ['sepal_length',
                    'sepal_width',
                    'petal_length',
                    'petal_width',
                    'target'])

#untuk mengetahui isi dari dataset iris, melalui row pertama
#Tanpa argumen secara default Alan menampilkan lima baris
iris.head()

#untuk mengetahui isi dari dataset iris, melalui row terakhir
#Tanpa argumen secara default akan menampilkan lima baris
iris.tail()

#untuk mengetahui isi dari dataset iris, melalui row pertama
 #dengan argumen 2 berarti akan menampilkan dua baris
(iris.head(2)

#untuk mengetahui nama kolom
iris.columns

iris['target']
iris.target

# To extract the target column, for example, you can simply do the following:
y = iris['target']
y

#Akses kolom tertentu dari dataset Iris, ambil dan tampilkan kolom "sepal_length" (panjang sepal).
sepal_length = iris['sepal_length']
print(sepal_length)

#Mengatur kolom "target" sebagai indeks  Ubah kolom "target" menjadi indeks dari DataFrame.
iris.set_index('target', inplace=True)
print(iris.head())

#menghapus indeks yang sudah dibuat
iris.reset_index(drop=True, inplace=True)

#membaca dataset Iris
iris_filename = 'C:/Users/rania/OneDrive/Logika Matematika/iris(1).csv'
iris = pd.read_csv(iris_filename)

#mengecek tipe data kolom numerik atau tidak
iris_array.dtype

#untuk mengetahui isi dari dataset iris, melalui row pertama
#Tanpa argumen secara default Alan menampilkan lima baris
iris.head()

#Memastikan tipe data numerik sebelum operasi aritmatika
#Saat melakukan operasi aritmatika seperti menghitung perbandingan panjang dan lebar sepal, kita harus memastikan bahwa kolom yang terlibat
#dalam operasi memiliki tipe data numerik. Kita dapat memeriksa dan mengubah tipe data jika diperlukan.
#Memeriksa tipe data kolom periksa tipe data untuk setiap kolom di dataset Iris untuk memastikan
#bahwa kolom seperti sepal_length dan sepal_width memiliki tipe numerik.
#Hasil ini akan menunjukkan apakah kolom seperti sepal_length dan sepal_width adalah numerik atau tidak.
print(iris.dtypes)

iris.info()

#Mengubah tipe data kolom yang diperlukan
#Jika kolom tersebut tidak memiliki tipe numerik (misalnya berupa object), kita dapat mengonversinya ke tipe numerik menggunakan pd.to_numeric().
iris['SepalLengthCm'] = pd.to_numeric(iris[1], errors='coerce')
iris['SepalWidthCm'] = pd.to_numeric(iris[2], errors='coerce')
iris['PetalLengthCm'] = pd.to_numeric(iris[3], errors='coerce')
iris['PetalWidthCm'] = pd.to_numeric(iris[4], errors='coerce')

#Melakukan operasi aritmatika
#Hitung perbandingan antara panjang dan lebar sepal untuk setiap target, dan simpan hasilnya sebagai kolom baru "sepal_ratio".
iris['sepal_ratio'] = iris['SepalLengthCm'] / iris['SepalWidthCm']
print(iris.head())

#Menggunakan .apply() untuk operasi kustom  Hitung luas petal (panjang petal × lebar petal) untuk setiap target,
#dan tambahkan hasilnya ke DataFrame sebagai kolom baru "petal_area".
iris['petal_area'] = iris.apply(lambda row: row['PetalLengthCm'] * row['PetalWidthCm'], axis=1)
print(iris.head())

#Mengisi nilai yang hilang*
#Jika ada nilai yang hilang pada kolom numerik seperti sepal_length, kita bisa mengisinya dengan rata-rata kolom tersebut.
# Mengisi nilai yang hilang di kolom sepal_length
iris['SepalWidthCm'].fillna(iris['SepalWidthCm'].mean(), inplace=True)
print(iris.head())

#Menggabungkan dataset Iris dengan dataset tambahan*
#Gabungkan dataset Iris dengan dataset tambahan, seperti dataset yang berisi informasi tambahan tentang spesies bunga, berdasarkan kolom species.
# Misalnya kita punya dataset tambahan dengan informasi spesies

data_spesies = pd.read_csv('species_info.csv')

# Menggabungkan kedua dataset
iris_merged = pd.merge(iris, data_spesies, on='species')
print(iris_merged.head())

#Normalisasi Data (Min-Max Scaling)*
#Normalisasi kolom sepal_length agar nilainya berada dalam rentang [0, 1].

import pandas as pd
import numpy as np

# Normalisasi manual menggunakan min dan max
iris['sepal_length_normalized'] = (iris['SepalLengthCm'] - iris['SepalLengthCm'].min()) / (iris['SepalLengthCm'].max() - iris['SepalLengthCm'].min())

# Tampilkan hasil
print(iris[['SepalLengthCm', 'sepal_length_normalized']].head())

# pengubahan Format Data (One-Hot Encoding)
# Ubah kolom species menjadi one-hot encoding.
# Menggunakan pd.get_dummies untuk melakukan one-hot encoding
iris_data_encoded = pd.get_dummies(iris, columns=[5])

# Tampilkan data hasil transformasi
print(iris_data_encoded.head())

# Mengubah tipe data kolom yang diperlukan
# Jika kolom tersebut tidak memiliki tipe numerik (misalnya berupa object), kita dapat mengonversinya ke tipe numerik menggunakan pd.to_numeric().
iris['sepal_length'] = pd.to_numeric(iris['sepal_length'], errors='coerce')
# iris['SepalWidthCm'] = pd.to_numeric(iris[2], errors='coerce')
# iris['PetalLengthCm'] = pd.to_numeric(iris[3], errors='coerce')
# iris['PetalWidthCm'] = pd.to_numeric(iris[4], errors='coerce')
# '', 'sepal_width', 'petal_length', 'petal_width', 'target'

# Dengan Pandas, kita bisa menggunakan pivot_table() untuk membuat ringkasan data berdasarkan pengelompokan.
# Misal membuat pivot table untuk merangkum rata-rata panjang sepal per spesies
# sebelumnya create index terlebih dahulu --> iris.set_index('target', inplace=True)
# pastikan tipe kolom sudah dalam numerik (jika masih object ubah ke numerik terlebih dulu)
# misal : iris['sepal_length'] = pd.to_numeric(iris['sepal_length'], errors='coerce')

# Membuat pivot table untuk merangkum rata-rata panjang sepal per spesies
pivot_table = iris.pivot_table(values='sepal_length', index='target', aggfunc='mean')

# Tampilkan pivot table
print(pivot_table)

# Pandas menyediakan metode stack() dan unstack() untuk transformasi data dari bentuk wide ke long.
# Ubah dataset dari format lebar menjadi format panjang menggunakan stack().
# Hanya ambil beberapa kolom yang ingin kita ubah formatnya

iris_subset = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

# Mengubah format lebar menjadi format panjang menggunakan stack()
iris_long = iris_subset.stack()

# Tampilkan hasil
print(iris_long.head(10))  # Menampilkan 10 baris pertama

# NumPy fast operation and computations
# When arrays need to be manipulated by mathematical operations, you just need to apply
# the operation on the array with respect to a numerical constant (a scalar), or an array of the same shape:
import numpy as np
a = np.arange(5).reshape(1,5)
a += 1
a*a

a = np.arange(5).reshape(1,5) + 1
b = np.arange(5).reshape(5,1) + 1
a * b

# ekivalen dgn operasi sebelumnya
a2 = np.array([1,2,3,4,5] * 5).reshape(5,5)
b2 = a2.T
a2 * b2