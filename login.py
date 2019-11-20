#author Alwan Putra
#gataungoding.id
#androsec1337

import requests, json
import time
import os
from getpass import getpass

url = 'URL API KAMU sayang'


def login():
    print("LOGIN")
    print ("-"*31)
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("username ga bole kosong")
        else:
            break
    while True:
        password = getpass("Password: ")
        if not len(password) > 0:
            print("password ga boleh kosong")
        else:
            break
    while True:
        token = input("Token: ")
        if not len(token) > 0:
            print("Token ga bole kosong")
        else:
            break
    if loginauth(username,password,token):
        return True

def loginauth(username, password, token):
    global url
    r = requests.get(url)
    ra = r.json()
    valid = False
    for item in ra:
        if username == item["username"] and password == item["password"] and token == item["token"]:
            valid = True
            break
    if valid:
        print('Sukses Login,Akan diarahkan ke Halaman Selanjutnya')
        time.sleep(2)
        menu()
    else:
        print("Invalid username or password or token")
        back = input("mau login lagi?/exit? [y/n]:")
        if back == 'y':
            login()
        elif back == 'n':
            exit()

def daftar():
    global url
    time.sleep(1)
    print ("-"*31)
    a = input('masukkan username: ')
    b = input('masukkan password: ')
    data = { 'username' : (a), 'password': (b), }
    r = requests.post(url, data = data)
    if r.status_code == 200:
        print('sukses daftar,silahkan kontak admin untuk mendapatkan token(aktivasi akun)')
    elif r.status_code == 404:
        print('gagal daftar')

def ea():
	os.system ('clear')
	time.sleep(1)
	print('selamat datang sobat gatau ngoding')

def menu():
	print("menu login gataungoding.id")
	print("options : 1. login | 2. Register")

	menu = input("pilih angka =>")
	if menu == '1':
		login()
	elif menu == '2':
		daftar()
	else:
		print('yang bener inputnya asw')
menu()
