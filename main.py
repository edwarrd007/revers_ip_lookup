"""
Allah <(I)>
Ya Heidar Karar
"""
import sys
from colorama import init,Fore
import requests as req
import pyfiglet as p

red = Fore.RED
bule = Fore.CYAN
green = Fore.GREEN
reset = Fore.RESET
yellow = Fore.YELLOW
init()

print(green + p.figlet_format("Revers_Ip_LookUp",font='small_slant'))
print(bule + p.figlet_format("By Edward",font='digital')+reset)

def main():
    head = {
        'Accept': 'application/vnd.github.v3.text-match+json',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "X-Prototype-Version": 1.6,
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": 30,
        "Origin": "https://www.yougetsignal.com",
        "Connection": "keep-alive",
        "Referer": "https://www.yougetsignal.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }
    def Reverse_ip_lookup(target,key=""):
        res = req.post("https://domains.yougetsignal.com/domains.php",data={"remoteAddress":target,"key":key})
        res = res.json()
        if res.get('status') == "Success":
            #print(res)
            lres = []
            for i in res.get('domainArray'):
                lres.append(i[0])
            with open('CN-output.txt','a') as w:
                for i in lres:
                    w.write(i+"\n")
            print(f"\n{green}[+] Domain IP :{red} {res.get('remoteIpAddress')}{reset}")
            print(f"{green}[+] DomainCount : {red}{res.get('domainCount')}{reset}\n")
        else:
            print("[-] Error",res.get('message'))

    while 1:
        print(f"{green}[1]{bule} Start\n{green}[2] {bule}Exit\n")
        try:
            x = int(input(">"))
        except BaseException as w:
            print(f"{yellow}[!]{bule} Bad Input {w} !!!{reset}")
        if x == 1:
            target = input(f"{green}[?] {bule}Enter Your Url/ip :")
            Reverse_ip_lookup(target)
        elif x == 2:
            sys.exit(1)
        else:
            print(f"{yellow}[!]{bule} Invalid input!!!{reset}")
        key = ""



if __name__=="__main__":
    main()
