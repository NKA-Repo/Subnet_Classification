import tkinter as tk
from tkinter import ttk
import ipaddress
import re

def proses_ip():
    input_text = input_textbox.get("1.0", tk.END)
    baris_input = re.split(r'[,\n;]+', input_text.strip())  # Pisahkan dengan koma, titik koma, atau newline

    subnet = ipaddress.ip_network('172.16.0.0/12')
    dalam_subnet = []
    luar_subnet = []

    # Regex: menangkap semua IP 4 oktet dalam bentuk apapun
    pola_ip = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')

    for item in baris_input:
        item = item.strip()
        ditemukan_ip = pola_ip.findall(item)
        ada_dalam_subnet = False

        for ip_str in ditemukan_ip:
            try:
                ip = ipaddress.ip_address(ip_str)
                if ip in subnet:
                    ada_dalam_subnet = True
                    break  # Cukup satu IP cocok
            except ValueError:
                continue

        if ada_dalam_subnet:
            dalam_subnet.append(item)
        else:
            luar_subnet.append(item)

    output_dalam.delete("1.0", tk.END)
    output_dalam.insert(tk.END, "\n".join(dalam_subnet))

    output_luar.delete("1.0", tk.END)
    output_luar.insert(tk.END, "\n".join(luar_subnet))

# GUI Setup
root = tk.Tk()
root.title("Pemisah IP Subnet 172.16.0.0/12")
root.geometry("900x700")

# Input
ttk.Label(root, text="Masukkan IP Address (campuran, pisahkan dengan koma, titik koma, atau baris):").pack(anchor="w", padx=10, pady=(10, 0))
input_textbox = tk.Text(root, height=10)
input_textbox.pack(fill="both", padx=10)

# Tombol Proses
ttk.Button(root, text="Proses", command=proses_ip).pack(pady=10)

# Output Dalam Subnet
ttk.Label(root, text="IP dalam subnet 172.16.0.0/12:").pack(anchor="w", padx=10)
output_dalam = tk.Text(root, height=10, bg="#e8ffe8")
output_dalam.pack(fill="both", padx=10)

# Output Luar Subnet
ttk.Label(root, text="IP di luar subnet 172.16.0.0/12:").pack(anchor="w", padx=10)
output_luar = tk.Text(root, height=10, bg="#ffe8e8")
output_luar.pack(fill="both", padx=10, pady=(0, 10))

root.mainloop()