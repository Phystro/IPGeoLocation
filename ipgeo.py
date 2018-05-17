from pygeoip import *
import socket,sys,iplitecity,iplite2city

def run():
    print "\r\n\t    ","*"*10,"""IP GeoLocation Tracer""","*"*10
    print ("[+] Loading Databases into Memory...Please wait...")
    ipdat = GeoIP("Databases/GeoLiteCity.dat", MEMORY_CACHE)
    print ("[+] Checking Internet Connection...")
    
    try:
        s = socket.gethostbyaddr(ip="192.168.1.1")
        hostname = s[0]
        print("[+] Internet Connection Available.\r\n    Your Results will be finer")
    except:
        print ("[-] No Internet Connection...")
        print ("    Internet may be needed for finer results\r\n")
    
    ip = raw_input("[?] Enter IPv4/IPv6 Address :- ")
    def net(ip):
        s = socket.gethostbyaddr(ip)
        hostname = s[0]
        return hostname

    print "\r\n","*"*20,"""...Using GeoLiteCity Database...""","*"*20
    iplitecity.litecity(ip,ipdat)
    print "\r\n","*"*20,"""...Using GeoLite2-City Database...""","*"*20
    iplite2city.lite2city(ip)
    
if __name__=="__main__":
    run()
    while 1:
        res=raw_input("\r\nPress Enter to Continue/Restart or 'q' to Close :- ")
        if res.lower() == 'q':
            sys.exit()
            #quit(1)
        else:
            run()
