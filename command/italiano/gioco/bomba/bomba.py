import time
import os

f = open("ASCII/gioco/bomb_1.txt","r")
line = f.readline()
print("la bomba sta per esplodere, al riparo!!")
print(line)
time.sleep(1)
f = open("ASCII/gioco/bomb_2.txt","r")
line = f.readline()
print("la bomba sta per esplodere, al riparo!!")
print(line)
time.sleep(1)
f = open("ASCII/gioco/bomb_3.txt","r")
line = f.readline()
print("la bomba sta per esplodere, al riparo!!")
print(line)
time.sleep(1)
f = open("ASCII/gioco/bomb_4.txt","r")
line = f.readline()
print("la bomba sta per esplodere, al riparo!!")
print(line)
time.sleep(1)
f = open("ASCII/gioco/explosion.txt","r")
line = f.readline()
print("boooooooooooooooooommmm!!!!!")
print(line)
time.sleep(1)

os.system("python3 language/italiano/console.py")