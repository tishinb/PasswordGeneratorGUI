import customtkinter
import string
import random

length=8
ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
symbols = ''

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.title("Password generator")
app.geometry("400x400")


password_length = customtkinter.CTkLabel(master=app, text='Длина пароля:')
password_length.pack(pady=10)

def upd_length(value):
    global length
    length = int(round(value,0))
    slider_length.configure(text=str(length))

lenght_slider = customtkinter.CTkSlider(master=app, from_=4, to=32, orientation="horizontal", command=upd_length)
lenght_slider.pack(pady=5)

slider_length = customtkinter.CTkLabel(master=app, text=length)
slider_length.pack(pady=5)

check_var_up = customtkinter.StringVar(value="off")
check_var_low = customtkinter.StringVar(value="off")
check_var_dig = customtkinter.StringVar(value="off")
check_var_punc = customtkinter.StringVar(value="off")
def upd_symbols():
    global symbols
    symbols = ''
    if check_var_up.get() == 'on':
        symbols += ascii_uppercase
    if check_var_low.get() == 'on':
        symbols += ascii_lowercase
    if check_var_dig.get() == 'on':
        symbols += digits
    if check_var_punc.get() == 'on':
        symbols += punctuation


def uppercase_letters_sw():
    print("uppercase_letters")
    upd_symbols()


def lowercase_letters_sw():
    print("lowercase_letters")
    upd_symbols()
def digits_set_sw():
    print("digits_set")
    upd_symbols()
def special_symbols_sw():
    print("special_symbols")
    upd_symbols()

uppercase_letters_checkbox = customtkinter.CTkCheckBox(master=app, text="Включить буквы верхнего регистра", command=uppercase_letters_sw, variable=check_var_up, onvalue="on", offvalue="off")
uppercase_letters_checkbox.pack(pady=5)

lowercase_letters_checkbox = customtkinter.CTkCheckBox(master=app, text="Включить буквы нижнего регистра", command=lowercase_letters_sw, variable=check_var_low, onvalue="on", offvalue="off")
lowercase_letters_checkbox.pack(pady=5)

digits_set_checkbox = customtkinter.CTkCheckBox(master=app, text="Включить цифры", command=digits_set_sw, variable=check_var_dig, onvalue="on", offvalue="off")
digits_set_checkbox.pack(pady=5)

special_symbols_checkbox = customtkinter.CTkCheckBox(master=app, text="Включить специальные символы", command=special_symbols_sw, variable=check_var_punc, onvalue="on", offvalue="off")
special_symbols_checkbox.pack(pady=5)

def password_generator():
    global password_length
    if symbols != '':
        password = "".join(random.sample(symbols, length))
        output_passw_label.configure(text=str(password))
    if symbols == '':
        output_passw_label.configure(text=str("Ни один чекбокс не заполнен!"))

gen_button=customtkinter.CTkButton(master=app, text='generate', command=password_generator)
gen_button.pack(pady=5)

output_label = customtkinter.CTkLabel(master=app, text='Вывод: ')
output_label.pack(pady=5)

output_passw_label = customtkinter.CTkLabel(master=app, text='')
output_passw_label.pack(pady=5)

app.mainloop()