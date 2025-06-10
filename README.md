# Pemisah IP Berdasarkan Subnet 172.16.0.0/12

Aplikasi GUI Python sederhana untuk memisahkan alamat IP berdasarkan apakah mereka berada dalam subnet `172.16.0.0/12` (subnet privat kelas B) atau di luar subnet tersebut. Aplikasi ini berguna untuk keperluan administrasi jaringan atau validasi daftar IP.

## 🖥️ Fitur

- Antarmuka grafis sederhana menggunakan Tkinter.
- Menerima input IP dalam format teks campuran (dipisahkan dengan koma, titik koma, atau baris baru).
- Menyortir dan menampilkan:
  - IP yang berada **dalam** subnet `172.16.0.0/12`.
  - IP yang berada **di luar** subnet tersebut.

## 🚀 Cara Menjalankan

### 1. Prasyarat

Pastikan Python 3.x sudah terpasang. Aplikasi ini hanya menggunakan modul standar, jadi tidak perlu instalasi tambahan.

### 2. Menjalankan Aplikasi

```bash
python subnet_classificationIP.py
