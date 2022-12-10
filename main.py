from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

kontak = ["GILANG"]
message = "Tes kata Dzul"

def click_search_name(nama):
    x1, y1 = [226,285]
    moveTo(x1,y1)
    click()
    typewrite(nama, interval=0.2)
    sleep(2)
    press('enter')

def tombol_kirim_pesan(pesan):
    x3, y3 = [743, 728]
    moveTo(x3, y3)
    click()
    sleep(2)
    typewrite(pesan)
    press('enter')


try:
    click_search_name(kontak[0])
    for i in range(10):
        try:
            message = message
            tombol_kirim_pesan(message)
        except:
            print("bar pesan tidak ditemukan")
except:
    print(f"Ada Masalah nama = {kontak[0]}, pesan = {message}")

