import requests
from os import system
import path , time
import random
import os
from colorama import Fore
u=Fore.LIGHTRED_EX
y=Fore.LIGHTYELLOW_EX
asd=Fore.LIGHTMAGENTA_EX
acd=Fore.LIGHTGREEN_EX
sd=Fore.LIGHTBLUE_EX
done = 1
reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        os.system("exit")
print("loding")
time.sleep(0.3)
print("10%■□□□□□□□□□")
time.sleep(0.3)
print("20%■■□□□□□□□□")
time.sleep(0.3)
print("30%■■■□□□□□□□")
time.sleep(0.3)
print("40%■■■■□□□□□□")
time.sleep(0.3)
print("50%■■■■■□□□□□")
time.sleep(0.3)
print("60%■■■■■■□□□□")
time.sleep(0.3)
print("70%■■■■■■■□□□")
time.sleep(0.3)
print("80%■■■■■■■■□□")
time.sleep(0.3)
print("90%■■■■■■■■■□")
time.sleep(0.3)
print("100%■■■■■■■■■")
time.sleep(0.4)        
os.system('clear')

print(f"{asd}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

print(f"""{u}


  __                        
[  |                       
 | |.--.   ,--.   _ .--.   
 | '/'`\ \`'_\ : [ `.-. |  
 |  \__/ |// | |, | | | |  
[__;.__.' \'-;__/[___||__] 
------------------------------------
orginal by:6g7r_here
  updated by:343o8
  
  make sure to follow us on instagram
------------------------------------                           
""")
print(f"{asd}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
name = input(' (-) Name > : ')
user = input('(-) User >  : ')
email = input('(-) Email > : ')
phone = int(input("P-N: "))
band = int(input("""how did they kill you : 
[1]: normal
[2]: Plagiarism
[3]: spam
[4]: trade
[5]: sexual 
[6]: 13 years old
[7]: hate
[8]: self
[+] enter chose: """))
print("----------------------------------")
if band == "1":
    band = f"""My account has been disabled by accident, I didn’t broke any instagram rules , and i hope you help me reactive it my account
               Username : @{name}
               register : {email}"""

elif band == "2":
    band = f"""Hello there is someone
They claim that I am publishing racism and my personal account item
But I do not have my personal account, I’m not racist, and you can check that and I will post clips to me personally
Just help me please beg you I wish you a humorous arithmetic band as fast as possible
my email : {email}
user name : {user}
    """

elif band == "3":
    band = """ Hello instagram support my account was disabled by mistake i am sure because I didn t violate any rules people reporting me and bullying me so thay report my account is there anyway you can help them get my account back thank you so much"""

elif band == "4":
    band = ""
    
elif band == "5":
    	band = """
 	Hello Instagram, my account has been deactivated by mistake since I have not posted any porn content. I hope you will reactivate the account."""
 	
elif band == "6":
    	band = """
 	Hello Instagram, my account has been deactivated, as it is an account. I want to submit a report to restore this account. If you want proof, I will provide all proofs on your Tawasul email. Thank you.."""
 	
elif band == "7":
    	band = """
 	Hello Instagram, my account has been canceled for hate speech. I would like to prepare the account and swear not to break any Instagram policy."""

elif band == "8":
    	band = """
 	Hello Instagram, my account has been deactivated by mistake. I have not posted anything about suicide or self-killing."""
 	
def unbanned():
    unbanned = "https://help.instagram.com/ajax/help/contact/submit/page"
    headers = {
                "Host": "help.instagram.com",
                "Accept": "*/*",
                "X-FB-LSD": "AVr_Dx9PS9A",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://help.instagram.com",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                "Connection": "keep-alive",
                "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content",
            }
    data = {
                "jazoest": 2890,
                "lsd": "AVr_Dx9PS9A",
                "name": name,
                "instagram_username": user,
                "email": email,
                "mobile_number": phone,
                "appeal_reason": band,
                "support_form_id": 606967319425038,
               'Field236858559849125_iso2_country_code':'SA',
        'Field236858559849125':'المملكة العربية السعودية',
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": "h",
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 3,
                "__ccg": "EXCELLENT",
                "__rev": 1003521343,
                "__s": "8x0mgw:dal0sr:s5g412",
                "__hsi": "6943937313156005653-0",
                "__comet_req": 0,
                "__spin_r": 1003521343,
                "__spin_b": "trunk",
                "__spin_t": 1616761394,
            }
    while True:
        req = requests.post(unbanned, headers=headers,  data=data)
        print(f"{acd}sent")
 
unbanned()
