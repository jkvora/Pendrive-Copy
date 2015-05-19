
import string
from ctypes import windll
import time
import os
import shutil
import ctypes

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives
delta=0

while (delta==0):
        if __name__ == '__main__':
            before = set(get_drives())
            #pause = raw_input("Please insert the USB device, then press ENTER")
            #print ('Please wait...')
            time.sleep(2)
            after = set(get_drives())
            drives = after - before
            delta = len(drives)

if (delta):
        for drive in drives:
            if os.system("cd " + drive + ":") == 0:
                newly_mounted = drive
                print "There were %d drives added: %s. Newly mounted drive letter is %s" % (delta, drives, newly_mounted)
                ctypes.windll.user32.MessageBoxA(0, "There were %d drives added: %s. Newly mounted drive letter is %s" % (delta, drives, newly_mounted), "Pen-drive Connected...!!!", 0)

else:
        print "Sorry, I couldn't find any newly mounted drives."
        ctypes.windll.user32.MessageBoxA(0, "Sorry, I couldn't find any newly mounted drives.", "NO Pen-drive Connected...!!!", 0)



a=ctypes.windll.user32.MessageBoxA(0, "Do You Wish To Copy All Data From Your Pen-drive ?", "Answer Me.....!!!", 3)
for folderName in os.listdir(newly_mounted+":\\"):
     print folderName
if a==6:
    #ctypes.windll.user32.MessageBoxA(0, "Data Tranfer is taking place....!!!!", "Its Happening...!!!", 0)
    shutil.move(newly_mounted+":\\","D:\\contents\\")
    ctypes.windll.user32.MessageBoxA(0, "Hurray...!!!! Data Transfered to Your disk Drive.", "Success Indeed....", 0)