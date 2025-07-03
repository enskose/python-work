import tkinter as tk
from tkinter import messagebox
import random
import string

password_history = []

def at_least_one_selected():
    if not (letters_var.get() or digits_var.get() or special_var.get()):
        messagebox.showwarning("Uyarı", "En az bir seçenek işaretlenmelidir!")
        return False
    return True

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showwarning("Uyarı", "Geçerli bir şifre uzunluğu giriniz!")
        return

    if length < 4 or length > 99:
        messagebox.showwarning("Uyarı", "Şifre uzunluğu en az 4, en fazla 99 olmalıdır!")
        return

    if not at_least_one_selected():
        return

    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # En az bir harf, bir rakam ve bir özel karakter içeren şifre oluştur
    password = ''
    if use_letters:
        password += random.choice(string.ascii_letters)
    if use_digits:
        password += random.choice(string.digits)
    if use_special:
        password += random.choice(string.punctuation)

    #Geri kalan uzunlukta rasgele karakterler ekleme
    password += ''.join(random.choice(characters) for _ in range(length - len(password)))

    #Karakterleri karıştırma
    password = ''.join(random.sample(password, len(password)))

    password_history.append(password)

    #Son 5 şifreyi gösterme
    update_password_history()

    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')

def update_password_history():
    password_history_text.config(state='normal')
    password_history_text.delete(1.0, tk.END)

    #Son 5 şifreyi gösterir
    start_index = max(0, len(password_history) - 5)
    for password in password_history[start_index:]:
        password_history_text.insert(tk.END, password + "\n")

    password_history_text.config(state='disabled')

def save_passwords():
    with open("password_history.txt", "a") as file:
        file.write("\n".join(password_history) + "\n")
    messagebox.showinfo("Bilgi", "Şifreler başarıyla kaydedildi.")

def clear_history():
    if messagebox.askyesno("Temizle", "Şifre geçmişini temizlemek istiyor musunuz?"):
        password_history.clear()
        update_password_history()

# GUI
root = tk.Tk()
root.title("Şifre Oluşturucu")

length_label = tk.Label(root, text="Şifre Uzunluğu:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Harfler (A-Z, a-z)", variable=letters_var)
letters_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")
letters_checkbox.select()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Rakamlar (0-9)", variable=digits_var)
digits_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")
digits_checkbox.select()

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Özel Karakterler (!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)", variable=special_var)
special_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")
special_checkbox.select()

generate_button = tk.Button(root, text="Şifre Oluştur", command=generate_password)
generate_button.grid(row=4, column=0, padx=10, pady=5)

label2 = tk.Label(root, text="Oluşturulan Şifre:")
label2.grid(row=5, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(root, state="readonly")
password_entry.grid(row=5, column=1, padx=10, pady=5)

password_history_label = tk.Label(root, text="Son 5 Şifre:")
password_history_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

password_history_text = tk.Text(root, height=5, width=40, state="disabled")
password_history_text.grid(row=6, column=1, padx=10, pady=5, columnspan=2)

save_button = tk.Button(root, text="Kaydet", command=save_passwords)
save_button.grid(row=7, column=0, padx=10, pady=5)

clear_button = tk.Button(root, text="Temizle", command=clear_history)
clear_button.grid(row=7, column=1, padx=10, pady=5)

#ilk başta güncel geçmişi gösterir
update_password_history()

root.mainloop()
