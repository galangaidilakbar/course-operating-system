
## Manajemen Memori Komputer

<!-- Pengertian manajemen memori -->

**Jadi Manajemen Memori itu apa?**

Manajemen Memori adalah tindakan untuk mengelola memori komputer. 

Tugasnya adalah menyediakan cara untuk mengalokasikan bagian-bagian dari memori kepada program yang berjalan, dan membebaskan untuk digunakan kembali ketika tidak lagi diperlukan.
    
Ini penting untuk dipahami karena setiap komputer memiliki lebih dari satu proses mungkin berlangsung setiap saat.


<!-- Berkenalan dengan hardware -->
**Komponent dasar pada Laptop / PC**

Pada dasarnya laptop / pc terdiri dari tiga komponen:

1. CPU
2. RAM
3. SSD

    ```
    RAM di sebut sebagai Primary Memory, sedangkan ssd disebut Secondary Memory.
    ```
**RAM**

Ram adalah singkatan dari Random Access Memory yang berguna untuk menyimpan data sementara.

Di RAM terdapat dua alamat:

1. Alamat memori mutlak (alamat fisik)

    Sel memori pada memori kerja adalah sumber daya berbentuk fisik, sehingga untuk mencapai sel memori ini digunakan kata pengenal. Maka disebutlah alamat fisik dan karena nomor alamat fisik ini bersifat mutlak (nomor setiap sel adalah tetap), maka disebut juga alamat mutlak.

2. Alamat memori relatif (alamat logika)

    Alamat memori yang digunakan oleh program / data berurutan / berjulat. Jika kita menggunakan alamat 1, maka kitapun menggunakan alamat 2,3, … dan untuk 1 informasi jika alamat awalnya 0 dan alamat lainnya relatif terhadap alamat awal 0 ini, maka dinamakan alamat relatif. Dan alamat tersebut adalah logika dari untaian alamat yang menyimpan informasi maka dikenal alamat memori logika. Contoh : alamat awal relatif 0, alamat awal fisik 14726, maka selisihnya = relokasinya = 14726-0 = 14726.

<!-- Bagaimana cara program bekerja -->
**Cara kerja komputer**

secara gampangnya gini:

1. Pengguna mengklik aplikasi
2. Aplikasi tersebut dimasukkan kedalam ram
3. cpu mengexecute intruksi dari program.

**Gimana kalau memory nya penuh**

Android Studio, Chrome, Netbeans ada contoh Aplikasi yang menggunakan RAM yang banyak.

Cara Sistem Operasi menangani hal tersebut cukup unik, yaitu dengan menggunakan sebagian dari Secondary memory untuk di jadikan tempat menaruh program.

Sebagian dari secondary memory tadi dijadikan sebagai `virtual memory`.

```
RAM: "Eh bro, gua udah mau penuh nih!!"
SSD: "Iya bro, Android Studio Gede banget dah"
RAM: "Gua pinjem sebagian dari elu ya?😖"
SSD: "Iya bro pake aja"
```

Ketika RAM penuh, maka RAM akan memindahkan datanya ke `virtual memory`. prosesnya disebut dengan Paging.

**Berkenalan dengan Paging**

**Berkenalan dengan Digital Storage**

## Link

- [Materi dari bapak](https://utyac-my.sharepoint.com/:w:/g/personal/galangaidil_akbar_student_uty_ac_id/EX8PBnzC3DNDvh-eNfvX1ZoBhpbj61fK-225-AQI5lLLwg?e=ALV5wt)
- [Manajemen Memori | Binus](https://socs.binus.ac.id/2019/02/28/memory-management/)
- [Mengenal tentang Paging di dalam sistem operasi | dari negeri srindavvan](https://youtu.be/pJ6qrCB8pDw)