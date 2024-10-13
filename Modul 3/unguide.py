import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from imblearn.under_sampling import RandomUnderSampler

'''
1. Pandas dan numpy digunakan untuk memanipulasi data.
2. Matplotlib dan seaborn digunakan untuk visualisasi data.
3. Simplelmputer digunakan untuk menyelesaikan nilai yang hilang.
4. RebustScaler dan MinMaxScaler digunakan untuk skala fitur.
5. RandomUnderSampler digunakan untuk menangani dataset yang tidak optimal.
'''
# Membaca data
data = pd.read_csv("C:/Users/rania/Downloads/diabetes.csv")
data.head(3)

data.info()

### 1. INPUT MISSING VALUES DENGAN MEAN, MEDIAN, DAN MODUS
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')
imputer_mode = SimpleImputer(strategy='most_frequent')

'''
Kode ini akan membuat library SimpleImputer yang menggunakan strategi mean untuk mengimputasi nilai yang hilang. SimpleImputer merupakan bagian dari pustaka sklearn yang digunakan untuk mengisi nilai yang hilang dalam dataset.
Dengan strategy mean, median, dan modus; nilai yang hilang akan digantikan dengan rata-rata, nilai tengah,dan modus dari kolom yang bersangkutan.
'''

data_mean = data.copy()
data_median = data.copy()
data_mode = data.copy()
'''
Fungsi data.copy() digunakan untuk membuat salinan dari DataFrame asli (data). Salinan ini adalah model dari DataFrame asli, yang berarti perubahan yang dilakukan pada salinan tidak akan mempengaruhi DataFrame asli dan sebaliknya.
'''

data_mean.iloc[:, :] = imputer_mean.fit_transform(data)
data_median.iloc[:, :] = imputer_median.fit_transform(data)
data_mode.iloc[:, :] = imputer_mode.fit_transform(data)

'''
fit_transfrom adalah metode yang pertama kali menyesuaikan imputer dengan data dan kemudian mengubah (transform) data dengan strategi yang ditentukan sebelumnya.
iloc adalah atribut dari pandas DatFrame yang memungkinkan akses berdasarkan indeks posisi. [:, :] berarti semua baris dan semua kolom.
Resultnya yaitu hasil dari fit_transform(data) akan disimpan kembali ke data_(mean/median/mode) menjadi data yang telah diimputasi.
'''

# Contohnya kita memanggil data yang diimputasi dengan mean untuk proses selanjutnya
data_imputed = data_mean

### 2. HEATMAP
plt.figure(figsize=(12, 10))
sns.heatmap(data_imputed.corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi Data Diabetes - Heatmap')
plt.show()

'''
* sns.heatmap() = fungsi pustaka seaborn untuk membuat heatmap.
* data_inputed.corr() = menghitung matriks korelasi dari DataFrame data_imputed.
* annot=True = menambahkan anotasi pada setiap sel heatmap, yang berrati nilai korelasi akan ditampilkan pada setiap sel.
'''

### 3. PENANGANAN KETIDAKSEIMBANGAN DENGAN UNDERSAMPLING
X = data_imputed.drop('Outcome', axis=1)
y = data_imputed['Outcome']
rus = RandomUnderSampler(random_state=42)    # untuk mengatasi ketidakseimbangan kelas dengan undersampling kelas mayoritas
X_res, y_res = rus.fit_resample(X, y)

'''
* drop = metode pandas untuk menghapus kolom/baris.
* 'Outcome' = nama kolom yang dihapus.
* axis=1 = menunjukan bahwa kolom yang akan dihapius, bukan baris.
* fit_resample = metode dari RandomUnderSampler yang menyesuaikan model dan kemudian menerapkan undersampling pada data.
* X_res = DataFrame fitur yang telah diundersample.
* Y_res = Series target yang telah diundersample.
Sehingga, kelas mayoritas dalam data telah diundersample untuk mencocokan jumlah sample dari kelas minoritas. Yang akhirnya menciptakan data yang lebih seimbang.
'''

# Menggabungkan fitur yang telah diresample dan target ke dalam DataFrame baru
data_resampled = pd.DataFrame(X_res, columns=X.columns)
data_resampled['Outcome'] = y_res

'''
Kode ini membuat DataFrame baru yang disebut data_resampled dari hasil undersampling fitur (X_res). Kemudian, kode ini menambahkan kolom target 'Outcome' yang telah di-undersample (y_res) ke dalam DataFrame tersebut. Hasilnya adalah DataFrame yang berisi fitur dan target yang telah di-undersample, siap untuk analisis lebih lanjut atau pelatihan model.
'''
### 4. SCALING DATA DENGAN ROBUSTSCALER & MINMAXSCALER
scaler_robust = RobustScaler()
scaler_minmax = MinMaxScaler()

data_resampled_robust_scaled = scaler_robust.fit_transform(data_resampled)
data_resampled_minmax_scaled = scaler_minmax.fit_transform(data_resampled)

'''
Membuat objek sclaer dan menerapkan scaler pada data yang telah diresampe.
'''

# Mengonversi data yang telah diskalakan ke dataframe
data_resampled_robust_scaled = pd.DataFrame(data_resampled_robust_scaled, columns=data_resampled.columns)
data_resampled_minmax_scaled = pd.DataFrame(data_resampled_minmax_scaled, columns=data_resampled.columns)

# Display first few rows of the scaled data
print(data_resampled_robust_scaled.head())
print(data_resampled_minmax_scaled.head())

'''
Pada kode di atas kita mengimputasi nilai menggunakan tiga point, yaitu dengan mean, median, dan  modus. Tiga DataFrame berbeda dibuat untuk menyimpan hasil imputasi dengan masing-masing strategi.
Data yang telah diimputasi dengan mean dipilih untuk digunakan pada langkah-langkah di proses selanjutnya. Untuk visualisasinya, kita menggunakan heatmap dengan membandingkan korelasi antarvariabel dalam dataset yang diimputasi.
Lalu, data yang telah diresample akan dikombinasikan kembali ke dalam DataFrame baru. Selanjutnya, kita menetapkan dua jenis sclaler. Yaitu RobustScaler dan MinMaxScaler. Hasilnya akan dikonversi kembali ke dalam DataFrame panadas.
Untuk menampilkan hasil skala data, akan ditampilkan beberapa baris pertama dari DataFrame yang telah diskalakan akan ditampilkan untuk memeriksa hasilnya.
'''