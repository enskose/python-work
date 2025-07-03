import tkinter as tk
from tkinter import messagebox
import re
import sqlite3
import bcrypt
import subprocess
import sys

# SQLite veritabanı bağlantısı
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Tablo oluşturma
c.execute('''CREATE TABLE IF NOT EXISTS users
             (email TEXT PRIMARY KEY,
              name TEXT NOT NULL,
              surname TEXT NOT NULL,
              password TEXT NOT NULL,
              safe_password TEXT NOT NULL)''')
conn.commit()

def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search(r"[\W]", password):
        return False
    return True

def register():
    email = email_entry.get()
    name = name_entry.get()
    surname = surname_entry.get()
    password = password_entry.get()
    safe_password = safe_password_entry.get()

    if email.strip() == '' or password.strip() == '' or name.strip() == '' or surname.strip() == '' or safe_password.strip() == '':
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Hata", "Geçersiz E-posta adresi")
        return

    c.execute("SELECT * FROM users WHERE email=?", (email,))
    if c.fetchone() is not None:
        messagebox.showerror("Hata", "Bu e-posta zaten kayıtlı.")
        return

    if not is_valid_password(password):
        messagebox.showerror("Hata", "Şifre geçerli değil. En az 8 karakter, en az 1 büyük harf, en az 1 küçük harf, en az 1 rakam ve en az 1 özel karakter içermelidir.")
        return

    if not is_valid_password(safe_password):
        messagebox.showerror("Hata", "Kasa parolası geçerli değil. En az 8 karakter, en az 1 büyük harf, en az 1 küçük harf, en az 1 rakam ve en az 1 özel karakter içermelidir.")
        return

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
    hashed_safe_password = bcrypt.hashpw(safe_password.encode(), bcrypt.gensalt()).decode('utf-8')

    try:
        c.execute("INSERT INTO users (email, name, surname, password, safe_password) VALUES (?, ?, ?, ?, ?)",
                  (email, name, surname, hashed_password, hashed_safe_password))
        conn.commit()
        messagebox.showinfo("Başarılı", "Kayıt başarıyla tamamlandı.")
        login_page()
    except sqlite3.Error as e:
        messagebox.showerror("Hata", f"Kayıt yapılırken hata oluştu: {e}")

def login():
    email = email_entry.get()
    password = password_entry.get()

    if email.strip() == '' or password.strip() == '':
        messagebox.showerror("Hata", "E-posta ve şifre alanları boş olamaz.")
        return

    c.execute("SELECT * FROM users WHERE email=?", (email,))
    users = c.fetchone()
    if users is None:
        messagebox.showerror("Hata", "Geçersiz e-posta veya şifre.")
        return

    stored_password = users[5]  # stored_password is in the correct column
    if not bcrypt.checkpw(password.encode(), stored_password.encode()):
        messagebox.showerror("Hata", "Geçersiz e-posta veya şifre.")
        return

    messagebox.showinfo("Başarılı", "Giriş başarıyla tamamlandı.")
    open_safe_box()

def open_safe_box():
    try:
        result = subprocess.run([sys.executable, 'safeBox.py', ], capture_output=True, text=True)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        if result.returncode != 0:
            messagebox.showerror("Hata", f"Kasa açılırken hata oluştu: {result.stderr}")
    except Exception as e:
        messagebox.showerror("Hata", f"Beklenmeyen hata: {e}")
    finally:
        root.destroy()

def register_page():
    clear_screen()
    register_label = tk.Label(root, text="Kayıt Ol", font=("Helvetica", 16))
    register_label.grid(row=0, column=1, pady=10)

    name_label = tk.Label(root, text="Ad:")
    name_label.grid(row=1, column=0)
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1)

    surname_label = tk.Label(root, text="Soyad:")
    surname_label.grid(row=2, column=0)
    global surname_entry
    surname_entry = tk.Entry(root)
    surname_entry.grid(row=2, column=1)

    email_label = tk.Label(root, text="E-posta:")
    email_label.grid(row=3, column=0)
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.grid(row=3, column=1)

    password_label = tk.Label(root, text="Şifre:")
    password_label.grid(row=4, column=0)
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=4, column=1)

    safe_password_label = tk.Label(root, text="Kasa Parolası:")
    safe_password_label.grid(row=5, column=0)
    global safe_password_entry
    safe_password_entry = tk.Entry(root, show="*")
    safe_password_entry.grid(row=5, column=1)

    register_button = tk.Button(root, text="Kayıt Ol", command=register)
    register_button.grid(row=6, column=1, pady=10)

    login_button = tk.Button(root, text="Giriş Yap", command=login)
    login_button.grid(row=7, column=1)

def login_page():
    clear_screen()
    login_label = tk.Label(root, text="Giriş Yap", font=("Helvetica", 16))
    login_label.grid(row=0, column=1, pady=10)

    email_label = tk.Label(root, text="E-posta:")
    email_label.grid(row=1, column=0)
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1)

    password_label = tk.Label(root, text="Şifre:")
    password_label.grid(row=2, column=0)
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=2, column=1)

    login_button = tk.Button(root, text="Giriş Yap", command=login)
    login_button.grid(row=3, column=1, pady=10)

    register_button = tk.Button(root, text="Kayıt Ol", command=register_page)
    register_button.grid(row=4, column=1)

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Giriş Ekranı")
    root.geometry("300x300")
    login_page()
    root.mainloop()
    conn.close()
