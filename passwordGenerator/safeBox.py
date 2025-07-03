import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt
import sys
import subprocess

# SQLite veritabanı bağlantısı
conn = sqlite3.connect('user.db')
c = conn.cursor()

safe_password = None

def main():
    if len(sys.argv) != 2:
        print("Usage: safeBox.py <safe_password>")
        return

    global safe_password
    safe_password = sys.argv[1]  # sys.argv[1] kullanıldı
    print(f"Kasa parolası: {safe_password}")

def check_password():
    entered_password = password_entry.get()

    if entered_password.strip() == '':
        messagebox.showerror("Hata", "Şifre alanı boş bırakılamaz.")
        return

    # Veritabanından kullanıcı bilgilerini alma
    c.execute("SELECT * FROM user WHERE safe_password=?", (safe_password,))
    user = c.fetchone()
    if user is None or not bcrypt.checkpw(entered_password.encode(), user[1].encode()):  # Sorgu ve şifre karşılaştırması düzeltildi
        messagebox.showerror("Hata", "Yanlış kasa parolası.")
        return
    else:
        messagebox.showinfo("Başarılı", "Kasa başarıyla açıldı.")
        open_password_generator()

def open_password_generator():
    try:
        result = subprocess.run([sys.executable, 'passwordGenerator.py'], capture_output=True, text=True)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        if result.returncode != 0:
            messagebox.showerror("Hata", f"Şifre oluşturucu açılırken hata oluştu: {result.stderr}")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen hata: {e}")
    finally:
        root.destroy()

# GUI
root = tk.Tk()
root.title("Kasa")
root.geometry("300x200")

password_label = tk.Label(root, text="Kasa Parolası:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Kiliti Aç", command=check_password)
check_button.pack(pady=5)

# Veritabanı bağlantısını kapat
conn.close()

root.mainloop()

if __name__ == "__main__":
    main()
    conn.close()
