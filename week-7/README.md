# Back Up dan Restore

# Overview

Pertemuan tujuh membahas tentang bagaimana cara mengarchivekan file atau direktori menggunakan command `tar`, kemudian kita juga belajar bagaimana menzipkan suatu file atau direktori dengan menggunakan command `gzip`, terakhir kita juga belajar mengekstraks file atau direktori yang telah di archive dan di zip kan dengan command `ungzip` atau dengan options `-z` di command `tar`.

## tar 

`tar` merupakan singkatan dari tape archive, yang merupakan perintah yang paling umum digunakan oleh sistem Linux/Unix untuk backup.  Ini memungkinkan Anda untuk dengan cepat mengakses kumpulan file dan menempatkannya ke dalam file arsip yang sangat terkompresi yang biasa disebut tarball, atau tar, gzip, dan bzip di Linux.  Algoritma yang digunakan untuk mengompresi .tar.gz dan .tar.bz2 masing-masing adalah algoritma gzip atau bzip.

** File atau direktori yang telah di archive dan di zip kan memiliki ukuran file yang sangat kecil **

### Pola command tar

```bash
# untuk mengarchivekan direktori
tar options path-ke-file/direktori

# untuk mengarchivekan file
tar options .
```
