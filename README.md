# Soal Ujian Python Data Science Fundamental

![Lintang_Purwadhika](https://static.wixstatic.com/media/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png/v1/fill/w_246,h_39,al_c,usm_0.66_1.00_0.01/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png)

<hr>

### **Soal 3 - 🛵 Jarak Dilan & Milea**

Selepas SMA, Dilan & Milea memutuskan untuk berpisah & fokus belajar _coding_ di [Purwadhika Startup & Coding School](https://www.purwadhika.com/). Dilan mengambil program _Job Connector Web & Mobile_ di Purwadhika BSD, sementara Milea mengikuti program _Job Connector Data Science_ di Purwadhika Bandung.

Sehari-hari Dilan beraktivitas di [Purwadhika BSD](https://www.google.com/maps/place/Purwadhika+Startup+%26+Coding+School+BSD/@-6.302403,106.652248,15z/data=!4m2!3m1!1s0x0:0xa3d17293fd1fcd?sa=X&ved=2ahUKEwi-tJTH_s_nAhUH4jgGHeptAfkQ_BIwCnoECA8QCA) yang terletak di Green Office Park 9, Kelurahan __SAMPORA__, Kecamatan __CISAUK__, Kabupaten __TANGERANG__, Provinsi __BANTEN__. Milea pun sibuk belajar di [Purwadhika Bandung](https://www.google.com/maps/place/Purwadhika+Startup+and+Coding+School+Bandung/@-6.9049166,107.6133146,15z/data=!4m5!3m4!1s0x0:0x5dcb022ab9f2b9c6!8m2!3d-6.9049166!4d107.6133146) yang berlokasi di NextSPACE by UnionSPACE, Kelurahan __CITARUM__, Kecamatan __BANDUNG WETAN__, Kota __BANDUNG__, Provinsi __JAWA BARAT__.

<hr>

Buatlah __sebuah file python__ (*.py*) yang dapat menghitung jarak (dalam _km_) antara Dilan (Purwadhika BSD) & Milea (Purwadhika Bandung). Untuk menghitungnya, Anda dapat memanfaatkan 3 buah REST API berikut.

- Disediakan API untuk mengakses daftar __Provinsi__ & __kode Provinsi__ di Indonesia. Untuk mengakses data tersebut, lakukan HTTP GET request ke URL endpoint berikut.

    ```bash
    http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json
    ```

- Disediakan API untuk mengakses daftar kode Provinsi di Indonesia beserta seluruh __Kelurahan__ (_urban_), __Kecamatan__ (_sub district_), __Kota/Kabupaten__ (_city_) & __Kode Pos__ (_postal code_) yang ada dalam Provinsi tersebut. Untuk mengakses data, lakukan HTTP GET request ke URL endpoint berikut.

    ```bash
    http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json
    ```

- [ZipCodeAPI.com](https://www.zipcodeapi.com/API) memberikan fasilitas untuk melakukan perhitungan jarak, radius & lokasi-lokasi di __Amerika Serikat__ berdasarkan kode posnya. [ZipCodeAPI.com](https://www.zipcodeapi.com/API) memungkinkan user untuk menghitung jarak antara 2 atau lebih lokasi berdasarkan kode posnya. Di soal ini kita __abaikan__ fakta bahwa [ZipCodeAPI.com](https://www.zipcodeapi.com/API) hanya berlaku untuk kode pos di Amerika Serikat, sehingga kita dapat menggunakan kode pos di Indonesia. 

    Lakukan registrasi secara gratis untuk mendapatkan __API key__. Perlu diperhatikan, akun gratis ZipCodeAPI layanannya dibatasi hanya __10 API call/jam__ plus _free trial period_ __50 API call/jam selama 2 minggu__. Untuk menghitung jarak antara 2 kode pos dalam _km_, lakukan HTTP GET request ke URL endpoint berikut.

    ```bash
    http://www.zipcodeapi.com/rest/{APIkeyAnda}/distance.json/{kodepos1}/{kodepos2}/km
    ```

<hr>

Pastikan Anda melakukan GET request API secara efektif & efisien, supaya tidak melampaui _limit API call_. Output yang diharapkan berupa informasi kode pos lokasi beserta jarak antara Dilan & Milea menurut [ZipCodeAPI.com](https://www.zipcodeapi.com/API).

```bash
Kode Pos lokasi Dilan adalah XXXXX 
Kode Pos lokasi Milea adalah YYYYY
Jarak Dilan & Milea adalah ZZZZZ km
```

_**Catatan:**_ 

✅ Commit & push source code jawaban soal ini ke __Github__ Anda, buatlah repo dengan nama __Ujian_DilanMilea__, kemudian lampirkan __url link repo Github__ Anda via email ke _lintang@purwadhika.com!_
