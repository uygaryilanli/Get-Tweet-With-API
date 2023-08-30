import requests
import tkinter
from tkinter import messagebox
from user_screen import UserScreen


class Users:
    def __init__(self) -> None:
        self.sheet_url = "YOUR SHEETY URL"
        self.header = {"Authorization" : "YOUR SHEETY BARRIER CODE"}
    
    def post_register(self, country_input, name_input, surname_input, age_input, email_input, password_input):
        country = country_input.get().upper()
        name = name_input.get().capitalize()
        surname = surname_input.get().capitalize()
        age = age_input.get()
        email = email_input.get()
        password = password_input.get()

        if len(country) < 2 or len(name) < 2 or len(surname) < 2 or len(age) < 2 or len(email) < 2 or len(password) < 2:
            messagebox.showinfo(title="OOPSS!", message="Lütfen istenen bilgileri 2 karakterden fazla giriniz!")
        else:
            parameters = {
                "SHEETY URL NİZİN SONUNDAKİ KELİMEYİ GİRİN": {
                    "country": country,
                    "name": name,
                    "surname": surname,
                    "age": age,
                    "email": email,
                    "password": password
                }
            }
            response = requests.post(url=self.sheet_url, json=parameters, headers=self.header)
            country_input.delete(0, tkinter.END)
            name_input.delete(0, tkinter.END)
            surname_input.delete(0, tkinter.END)
            age_input.delete(0, tkinter.END)
            email_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)
            messagebox.showinfo(title="Başarılı!", message="Başarılı bir şekilde kayıt oldunuz!")
            return response
        
        
    def get_login(self, email_input, password_input, window):
        email = email_input.get()
        password = password_input.get()
        response = requests.get(url=self.sheet_url, headers=self.header)
        data = response.json()
        for item in data["SHEETY URL NİZİN SONUNDAKİ KELİMEYİ GİRİN"]:
            data_email = item["email"]
            data_password = item["password"]
            data_name = item["name"]
            if email == data_email and password == data_password:
                messagebox.showinfo(title="Giriş Başarılı!", message=f"Hoşgeldin {data_name}")
                window.destroy()
                UserScreen()
                break
        if len(email) < 2 or len(password) < 2:
            messagebox.showinfo(title="OOPSS!", message="Lütfen istenen bilgileri 2 karakterden fazla giriniz!")
        elif email != data_email or password != data_password:
            messagebox.showinfo(title="Giriş Başarısız!", message="Email veya şifre hatalı!!!")