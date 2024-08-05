import sys
import time
import colorama
import random
import os
import subprocess
import platform
from colorama import * 
from tkinter import *
import soundfile as sf
import soundcard as sc
from alive_progress import alive_bar
import pyautogui
import keyboard
import json
name = ""
Key = False
try:
    with open ("C:\\Users\\James\\pass\\yes.txt") as file:
        name = file.read()
        print("key found!"+Fore.LIGHTGREEN_EX+"██")
        time.sleep(1)
        Key = True
except:
    Key = False
    print("Key not found!"+Fore.LIGHTRED_EX+"██")
    time.sleep(1)
pyautogui.hotkey("win", "up")
pyautogui.hotkey("F11")
if Key == False:
    try:
        with open ("key.txt") as file:
            name = file.read()
            print(Fore.RESET+"key found!"+Fore.LIGHTGREEN_EX+"██")
            time.sleep(1)
            Key = True
    except:
        Key = False
        print(Fore.RESET+"Key not found!"+Fore.LIGHTRED_EX+"██")
        time.sleep(1)
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2   
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

bang = Fore.WHITE+"""
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""+Fore.RESET
oldJt =Fore.LIGHTCYAN_EX+ """
██████████████████████████████████████████████████████████████████████████████████████████
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                      """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""       ██  █████  ███    ███ ███████ ███████     ████████  ██████   ██████  ██        """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""       ██ ██   ██ ████  ████ ██      ██             ██    ██    ██ ██    ██ ██        """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""       ██ ███████ ██ ████ ██ █████   ███████        ██    ██    ██ ██    ██ ██        """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""  ██   ██ ██   ██ ██  ██  ██ ██           ██        ██    ██    ██ ██    ██ ██        """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""   █████  ██   ██ ██      ██ ███████ ███████        ██     ██████   ██████  ███████   """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                      """+Fore.LIGHTCYAN_EX+"""██
██████████████████████████████████████████████████████████████████████████████████████████
"""

Jt= Fore.LIGHTCYAN_EX+"""
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                                                                                         """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                                                                                         """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████████████  ██████          ██████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████████████  ██████████████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████████████  ██████████████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████  ██████  ██████████████████████  ██████          ██████              ██████      ██████  ██████  ██████  ██████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""         ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+""" ██████  ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+""" ██████  ██████  ██████  ██████  ██████          ██████  ██████                  ██████      ██████      ██████  ██████  ██████  ██████  ██████          """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+""" ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+""" ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+""" ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                                                                                         """+Fore.LIGHTCYAN_EX+"""██
██"""+Fore.LIGHTYELLOW_EX+"""                                                                                                                                                         """+Fore.LIGHTCYAN_EX+"""██
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                                                                                                                        
"""
commands = Fore.LIGHTCYAN_EX+"""
-help
-title
-quit or // or EXIT
-del
-reload
-cer
-time
-bang
-info
-perhak
-py
-plso or plso -s
-plso -f
-piao -s
-piao -f
-load -g
-google
-cal
-winoff
-settings
-resetup
-reup
-bsod
-license() for all licenses
"""+Fore.RESET
info = Fore.LIGHTCYAN_EX+"""

This is JAMES TOOL made by James
If you are using CMD to run fullscreen
and dont run with python use CMD
or some commands will not work
Type help for help with commands
perhak does nothing
this might not work in linux or mac
"""
perhak = (Fore.LIGHTGREEN_EX+"""
101101101101011
011200001010010101
101010101010101000
101000101010101010
101001010100010000
01010101010101010
10101010101010101
10101010101010010
1001010101010101
010101010100101
010101010101101
010101010101010010
10101010101010101
0100101010101010101
010101001010101010
101010101010101010101
01010101010101010101
01010101001010110101
0101101010101011011
5101010101101010101
01010110100101010101011
000101010101010101010
01011010101010100101110
010101010001010101010101
01010101010101010101010
0101010101010101011101010001\n"""+Fore.RESET)

JMAESL=Fore.LIGHTCYAN_EX+"""

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
with open (resource_path("config.json"), "r") as f:
    data = json.load(f)
def off():
    os.system("shutdown -s -t 0 -f")
def compute():
    print(Fore.LIGHTRED_EX+"FULLSCREEN NOW")
    default_speaker = sc.default_speaker()
    samples, samplerate = sf.read(resource_path('done.wav'))
    default_speaker.play(samples, samplerate=samplerate)
def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def aum():
    clean()
    print(f"□ □ {Fore.LIGHTRED_EX}■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □ □")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □")
    print(f"{Fore.LIGHTRED_EX}■ ■ {Fore.RESET}□ □ □ □ □ □ □ {Fore.LIGHTRED_EX}■ {Fore.RESET}□ □")
    print(f"{Fore.LIGHTRED_EX}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.LIGHTRED_EX}■ {Fore.RESET}□ □")
    print(f"{Fore.LIGHTRED_EX}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.LIGHTRED_EX}■ ■ ■")
    print(f"{Fore.LIGHTRED_EX}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ ■ {Fore.RESET}□ □ {Fore.LIGHTRED_EX}■ ■ ■ ■ ■")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.LIGHTRED_EX}■ ■ {Fore.RESET}□ □")
    print(f"□ {Fore.LIGHTRED_EX}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.LIGHTRED_EX}■ ■ {Fore.RESET}□ □")
    print_slow("you saw nothing")
    time.sleep(1)
    clean()
    print(bang)
    time.sleep(0.5)
    load()
def bsod():
    from ctypes import windll
    from ctypes import c_int
    from ctypes import c_uint
    from ctypes import c_ulong
    from ctypes import POINTER
    from ctypes import byref

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19), 
        c_uint(1), 
        c_uint(0), 
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), 
        c_ulong(0), 
        nullptr, 
        nullptr, 
        c_uint(6), 
        byref(c_uint())
    )
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
def goto():
    if data["ues-old"] == "no":
        print(Jt)
    elif data["ues-old"]== "yes":
        print(oldJt)
def load():
    clean()
    compute()
    time.sleep(.6)
    clean()
    print(Fore.LIGHTRED_EX+"Type help for help with commands")
    print("FULLSCREEN NOW"+Fore.RESET)
    time.sleep(.9)
    clean()
    print(JMAESL)
    time.sleep(0.03)
    clean()
    goto()
    print(Fore.LIGHTCYAN_EX+time.strftime("%I:%M %p"))
    print(time.strftime("%A"))
    print(time.strftime("%B %d, %Y"))
    print("type info for more info")
    print(Fore.LIGHTRED_EX+"FULLSCREEN NOW"+Fore.RESET)
    default_speaker = sc.default_speaker()
    samples, samplerate = sf.read(resource_path('boot.wav'))
    default_speaker.play(samples, samplerate=samplerate)
    clean()
    goto()
def JT_setup():
    data["setup"] = "no"
    data["off-pass-yn"] = ""
    data["off-pass"] = ""
    data["setup"] = "yes"
    print("winoff password[y]=yes[n]=no")
    while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('y'): 
                    pyautogui.press("backspace")
                    data["off-pass-yn"] = "yes"
                    break
                elif keyboard.is_pressed('n'):
                    pyautogui.press("backspace")
                    data["off-pass-yn"] = "no"
                    break
            finally:
                if data["off-pass-yn"] == "yes":
                    data["off-pass"] = input("password:")
    print("login[y]=yes[n]=no")
    while True:
        try:
            if keyboard.is_pressed('y'):
                pyautogui.press("backspace")
                data["login-yn"] = "yes"
                if data["login-yn"] == "yes":
                    data["login-user"] = input("login user:")
                    data["login-password"] = input("login password:")
                break
            elif keyboard.is_pressed('n'):
                pyautogui.press("backspace")
                data["login-yn"] = "no"
                break
        finally:
            pass
    print("use legacy title[y]=yes[n]=no")
    while True:
        try:
            if keyboard.is_pressed('y'):
                pyautogui.press("backspace")
                data["ues-old"] = "yes"
                break
            elif keyboard.is_pressed('n'):
                pyautogui.press("backspace")
                data["ues-old"] = "no"
                break
        finally:
            pass
    with open(resource_path('config.json'), 'w') as file:
        json.dump(data, file, indent=4)
if data["setup"] == "no":
    JT_setup()
load()
if data["login-yn"] == "yes":
    if data["login-user"] == input("user:"):
        if data["login-password"] == input("password:"):
            RUN = True
else:
    RUN = True
clean()
goto()
while RUN:
    print("\n"+Fore.LIGHTCYAN_EX+platform.system()+"@JAMES TOOL")
    Jt1 = input(Fore.LIGHTRED_EX+"↪ "+Fore.RESET)
    default_speaker = sc.default_speaker()
    samples, samplerate = sf.read(resource_path('done.wav'))
    default_speaker.play(samples, samplerate=samplerate)
    if Jt1 == "help":
        print(commands)
    elif Jt1 == "quit":
        RUN = False
    elif Jt1 == "//":
        RUN = False
    elif Jt1 == "EXIT":
        RUN = False
    elif Jt1 == "title":
        goto()
    elif Jt1 == "del":
        clean()
        goto()
    elif Jt1 == "reload":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('Jt5.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        pyautogui.typewrite("//")
        pyautogui.press("enter")
        pyautogui.press("up")
        pyautogui.press("enter")
    elif Jt1 == "time":
        print(Fore.LIGHTCYAN_EX+time.strftime("%I:%M %p"))
        print(time.strftime("%A"))
        print(time.strftime("%B %d, %Y")+Fore.RESET)
    elif Jt1 == "bang":
        clean()
        print(bang)
        time.sleep(0.6)
        clean()
        goto()
    elif Jt1 == "bsod":
        bsod()
    elif Jt1 == "perhak":
        clean()
        print_slow(perhak)
        clean()
        goto()
    elif Jt1 == "py":
        print(Fore.LIGHTCYAN_EX+"type quit() to exit"+Fore.RESET)
        input(Fore.LIGHTRED_EX+"WARNING I have no control over python press enter"+Fore.LIGHTGREEN_EX)
        subprocess.call("python.exe")
        print(Fore.RESET)
    elif Jt1 == "google":
        input("close google to continue")
        subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif Jt1 == "license()":
        yn = input("""
[1]=JAMES TOOL license
[2]=python license
""")    
        if yn == "1":
            print(JMAESL)
        elif yn == "2":
            print(license())
    elif Jt1 == "plso":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('boot.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -short played successfully!\n")
    elif Jt1 == "plso -s":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('boot.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -short played successfully!\n")
    elif Jt1 == "plso -f":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('Jt2.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -full played successfully!\n")
    elif Jt1 == "piao -s":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('Jt3.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        print("\npiao -full played successfully!\n")
    elif Jt1 == "piao -f":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read(resource_path('Jt4.wav'))
        default_speaker.play(samples, samplerate=samplerate)
        print("\npiao -full played successfully!\n")
    elif Jt1 == "load -g":
        compute()
    elif Jt1 == "cal":
        input("press enter continue")
        subprocess.call("calc.exe")
    elif Jt1 == "reup":
        data["setup"] = "no"
        data["off-pass-yn"] = ""
        data["off-pass"] = ""
        data["login-yn"] = ""
        data["login-user"] = ""
        data["login-password"] = ""
        with open(resource_path('config.json'), 'w') as file:
            json.dump(data, file, indent=4)
    elif Jt1 == "winoff":
        print(Fore.LIGHTRED_EX+"are you sure that you want to turn off your PC [Y]=yes[N]=no")
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('y'): 
                    pyautogui.press("backspace")
                    if data["off-pass-yn"] == "yes":
                        passw = input("password:")
                        if passw == data["off-pass"]:
                            off()
                    else:
                        off()
                    break  # finishing the loop
                elif keyboard.is_pressed('n'):
                    pyautogui.press("backspace")
                    break

            except:
                break
    elif Jt1 == "settings":
        print("setup ",data["setup"])
        print("winoff password yes/no ",data["off-pass-yn"])
        print("winoff password ",data["off-pass"])
    elif Jt1 == "resetup":
        JT_setup()
    elif Jt1 == "info":
        print(info)
        if Key == True:
            print(Fore.LIGHTRED_EX+name)
    elif Jt1 == "cer":
        print(Fore.LIGHTCYAN_EX+"james")
        time.sleep(0.5)
        print("guy from stack over flow")
        time.sleep(0.5)
        print("plso -short made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/4888588518555648")
        time.sleep(0.5)
        print("plso -full made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/6747361310801920")
        time.sleep(0.5)
        print("piao -short made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/6312622758166528")
        time.sleep(0.5)
        print("piao -full made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/5967890429378560"+Fore.RESET)
    elif Jt1 == "au":
        aum()
    elif Jt1 == "command":
        aum()
    elif Jt1 == "":
        print()
    else:
        print(Fore.LIGHTRED_EX + Jt1 +" is a Unknown command\n"+Fore.RESET)
clean()
pyautogui.hotkey("F11")
pyautogui.hotkey("win", "down")
quit()