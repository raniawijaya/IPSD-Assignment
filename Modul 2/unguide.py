### PRAKTIKUM 2

import pandas as pd
import os

### 1. LOAD DATA DARI FILE CSV
file_path = r'C:\Users\rania\OneDrive\Dokumen\Movie_classification.csv'
df = pd.read_csv(file_path)

print("Dataframe awal:")
print(df.head())

### 2. CEK NIALI DUPLIKAT
duplicate = df.duplicated().sum()
print(f"\nJumlah baris duplikat: {duplicate}")

### 3. MENEMUKAN NULL VALUES UNTUK PRESENTANSE
null_percentage = (df.isnull().sum() / len(df)) * 100
print("\nPresentase nilai null di setiap kolom:")
print(null_percentage)

### 4. DROP MISSING VALUE BERDASARKAN BARIS, KOLOM, IMPUTASI DENGAN MEAN, MODUS, & MEDIAN
df_operations = {
    'cleaned_rows' : df.dropna(),        # berdasarkan baris
    'cleaned_columns' : df.dropna(axis=1),   # berdasarkan kolom
    'imputed_mean' : df.fillna(df.mean(numeric_only=True)),   # mean untuk kolom numerik
    'imputed_median' : df.fillna(df.median(numeric_only=True)), # median untuk kolom numerik
    'imputed_mode' : df.apply(lambda x: x.fillna(x.mode()[0]), axis=0)  # modus untuk kolom numerik
}

print("\nOperasi drop missing values selesai.")

# Membuat folder output jika belum ada
output_folder = r'C:\Users\rania\OneDrive\Dokumen'
os.makedirs(output_folder, exist_ok=True)

### 5. EXPORT DATA KE CSV & EXEL
for name, df_temp in df_operations.items():
    df_temp.to_csv(os.path.join(output_folder, f'Movie_classification_{name}.csv'), index=False)
    df_temp.to_excel(os.path.join(output_folder, f'Movie_classification_{name}.xlsx'), index=False)

print("\nData berhasil diekspor ke CSV dan Excel.")

'''
Kesimpulannya, kode ini dibuat untuk melakukan proses pembersihan dan imputasi pada datset yang diimpor dari file csv. Kode di atas, kita menggunakan dictionary untuk menyimpan hasil dari berbagai operasi drop missing values, dan loop untuk mengurangi pengulangan saat mengekspor data ke csv dan Excel.
1. Pertama, kita mengimpor file csv ke dalam DataFrame menggunakan pandas. Kemudian menampilkan lima bariis pertama dari data frame untuk verifikasi. 
2. Untuk mengecek jumlah baris yang terdapat duplikat dalam data frame, kita menggunakan fungsi duplicated().sum() dan menampilkannya dengan print.
3. Untuk fungsi null_percentage digunakan untuk menghitung presentase nilai null di setiap kolom, yang kemudian ditampilkan dengan perintah print.
4. Pada operator drop missing value didapatkan ketentuan sebagai berikut :
    a. Menghapus baris yang mengandung nilai null.
    b. Menghapus kolom yang mengandung nilai null.
    c. Mengimputasi nilai null dengan mean untuk kolom numerik.
    d. Mengimputasi nilai null dengan median untuk kolom numerik.
    e. Mengimputasi nilai null dengan modus untuk kolom numerik.
5. Lalu, untuk membuat folder output-nya (jika belum ada) kita menggunakan os.
6. Yang terakhir, kita mengekspor data frame yang sudah diolah ke file csv dan excel menggunakan loop agar meminimalisir pengulangan kode.
'''