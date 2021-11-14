# Back Up dan Restore

# Overview

Pertemuan tujuh membahas tentang bagaimana cara mengarchivekan file atau direktori menggunakan command `tar`, kemudian kita juga belajar bagaimana menzipkan suatu file atau direktori dengan menggunakan command `gzip`, terakhir kita juga belajar mengekstraks file atau direktori yang telah di archive dan di zip kan dengan command `ungzip` atau dengan options `-z` di command `tar`.

## tar 

`tar` adalah suatu perintah yang digunakan untuk membuat suatu arsip dari file ataupun direktori.

arsip itu artinya kan kumpulan-kumpulan dokumen ya. jadi pada dasarnya, perintah `tar` ini berguna untuk mengumpulkan banyak file ke satu file.

`tar` merupakan singkatan dari tape archive, yang merupakan perintah yang paling umum digunakan oleh sistem Linux/Unix untuk backup.

contoh perintah `tar`

```bash
tar -cf arsip.tar file1 file2 file3
```
Options `-c` digunakan untuk membuat tar, lalu options `-f` digunakan untuk memberikan nama file tarnya.

### Options

| No   | options |                     kegunaan |
| :--- | :-----: | ---------------------------: |
| 1    |   -c    |                  membuat tar |
| 2    |   -f    |         memberikan nama file |
| 3    |   -v    |               melihat proses |
| 4    |   -z    | mengkompres file kedalam zip |
| 5    |   -x    |   untuk mengekstrak file tar |

Contoh lain
```bash
tar -zvcf arsip.tar.gz file1 file2 file3
```

Options `-z` digunakan untuk mengkompres file dengan zip, supaya nanti ukuran file tar nya itu bisa kecil. lalu options `-v` digunakan untuk melihat proses atau status pentaran suatu file.

Gimana cara mengekstrak file tar? gampang yah, tinggal masukkan command tar dengan options `-x` dan `-f` seperti berikut:
```bash
tar -xf arsip.tar.gz
```

Options `-x` digunakan untuk mengekstrak file tar, dan options `-f` itu untuk nama file tar yang mana yang mau di ekstrak.
