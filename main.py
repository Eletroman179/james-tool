import sys
import time
import colorama
import random
import os
import subprocess
from colorama import * 
from tkinter import *
import soundfile as sf
import soundcard as sc
bang = Fore.WHITE+"""████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████"""+Fore.RESET

Jt =Fore.LIGHTCYAN_EX+ """
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
"""+Fore.RESET
info = Fore.LIGHTCYAN_EX+"""

This is JAMES TOOL made by Tames
If you are using CMD to run do NOT fullscreen
or some commands will now work
Type help for help with commands
perhak does nothing

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
def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def aum():
    clean()
    print(f"□ □ {Fore.RED}■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □ □")
    print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □")
    print(f"{Fore.RED}■ ■ {Fore.RESET}□ □ □ □ □ □ □ {Fore.RED}■ {Fore.RESET}□ □")
    print(f"{Fore.RED}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.RED}■ {Fore.RESET}□ □")
    print(f"{Fore.RED}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.RED}■ ■ ■")
    print(f"{Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print(f"□ {Fore.RED}■ ■ ■ ■ {Fore.RESET}□ □ {Fore.RED}■ ■ ■ ■ ■")
    print(f"□ {Fore.RED}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.RED}■ ■ {Fore.RESET}□ □")
    print(f"□ {Fore.RED}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.RED}■ ■ {Fore.RESET}□ □")
    print_slow("you saw nothing")
    time.sleep(1)
    clean()
    print(bang)
    time.sleep(0.5)
    load()

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
def load():
    clean()
    print_slow(Fore.LIGHTGREEN_EX+"######################")
    print_slow("\n|        done!       |\n")
    print_slow(Fore.LIGHTGREEN_EX+"######################"+Fore.RESET)
    time.sleep(.6)
    clean()
    print("Type help for help with commands")
    time.sleep(.9)
    clean()
    print(Jt)
    default_speaker = sc.default_speaker()
    samples, samplerate = sf.read('boot.wav')
    default_speaker.play(samples, samplerate=samplerate)
load()

RUN = True
while RUN:
    Jt1 = input(Fore.RED+"↪ "+Fore.RESET)
    if Jt1 == "help":
        print(commands)
    elif Jt1 == "quit":
        RUN = False
    elif Jt1 == "//":
        RUN = False
    elif Jt1 == "EXIT":
        RUN = False
    elif Jt1 == "title":
        print(Jt)
    elif Jt1 == "del":
        clean()
        print(Jt)
    elif Jt1 == "reload":
        load()
    elif Jt1 == "time":
        print(Fore.LIGHTCYAN_EX+time.strftime("%I:%M %p"))
        print(time.strftime("%A"))
        print(time.strftime("%B %d, %Y")+Fore.RESET)
    elif Jt1 == "bang":
        clean()
        print(bang)
        time.sleep(0.3)
        clean()
        print(Jt)
    elif Jt1 == "perhak":
        clean()
        print_slow(perhak)
        clean()
        print(Jt)
    elif Jt1 == "py":
        print(Fore.LIGHTBLUE_EX+"type quit() to exit"+Fore.RESET)
        input(Fore.LIGHTRED_EX+"WARNING I have no control over python press enter"+Fore.LIGHTGREEN_EX)
        subprocess.call("python.exe")
        print(Fore.RESET)
    elif Jt1 == "plso":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read('boot.wav')
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -short played successfully!\n")
    elif Jt1 == "plso -s":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read('boot.wav')
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -short played successfully!\n")
    elif Jt1 == "plso -f":
        default_speaker = sc.default_speaker()
        samples, samplerate = sf.read('Jt2.wav')
        default_speaker.play(samples, samplerate=samplerate)
        print("\nplso -full played successfully!\n")
    elif Jt1 == "info":
        print(info)
    elif Jt1 == "cer":
        print(Fore.LIGHTCYAN_EX+"james")
        time.sleep(0.5)
        print("guy from stack over flow")
        time.sleep(0.5)
        print("plso -short made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/4888588518555648")
        time.sleep(0.5)
        print("plso -full made by James using https://musiclab.chromeexperiments.com/Song-Maker/song/6747361310801920"+Fore.RESET)
    elif Jt1 == "au":
        aum()
    elif Jt1 == "":
        print()
    else:
        print(Fore.RED + Jt1 +" is a Unknown command\n"+Fore.RESET)
clean()
quit()
