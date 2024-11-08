import time
import os.path
from subprocess import call


print('Keys are being processed/? ')
time.sleep(2)
f = open('master recoil.py', 'r+')
lines = 0
words = 0
characters = 0
for line in f:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)
TotalLWC = lines + words + characters
print("LWC set ammout is",TotalLWC)

if TotalLWC == 2382:
   print ("input - Got a true expression value")
   print("Code being sent Through anti-cheat")
   #reverse code here
   try:
    infile=open("master recoil.py","r").readlines() #read file as list
    while os.path.isfile("master recoil.exe"):
      file2=input("File Exists! Enter new name for output file: ")
    ofile=open("master recoil.exe", "w")
    ofile.writelines(infile[::-1])#infile is a list, this will reverse it
    ofile.close()
    print('File Finished!')

    time.sleep(2)
    print("Code breached anti-cheat system")
    print("Keys being Reversed?/")
   #back to original code here
    ofile=open("master recoil.exe", "w")
    ofile.writelines(infile[::1])#infile is a list, this will reverse it back to original
    ofile.close()
    os.remove("master recoil.exe")
    print("File Removed!")
    call(["python", "master recoil.py"])
   except IOError:
    print("Error")