from pygeoip import *
from time import sleep
import socket, os, pygeoip, geoip2.database

IPDAT1 = GeoIP("databases/GeoLiteCity.dat", MEMORY_CACHE)
IPDAT2 = geoip2.database.Reader("databases/GeoLite2-City.mmdb")
DB = "GeoLiteCity"

class IPGeoLoc:
    def __init__(self):
        ip = raw_input("\nIP Address to GeoLocate: ")
        self.ip = ip
        domain_name=socket.getfqdn(ip)
        print "\n[+] Tracing IP Address","\t\t:",\
              self.ip,"\r\n[+] Hostname/Domain Name","\t:",domain_name


class Lite2City:
    def __init__(self, ip):
        self.ip = ip

        try:
            self.IPDAT2 = geoip2.database.Reader("databases/GeoLite2-City.mmdb")
            try:
                self.response = IPDAT2.city(self.ip)
            except geoip2.errors.AddressNotFoundError:
                print "The Address %s is not in the database"%(self.ip)
            else:
                print "Country Code","\t\t:",self.response.country.iso_code
                print "Country Name","\t\t:",self.response.country.name
                print "Simplified Chinese","\t:",self.response.country.names['zh-CN']
                print "Major City","\t\t:",self.response.city.name
                print "Location of Major City","\t:",self.response.subdivisions.most_specific.name
                print "Major City Code","\t:",self.response.subdivisions.most_specific.iso_code
                print "Location's Postal Code","\t:",self.response.postal.code
                print "Location's Latitude","\t:",self.response.location.latitude
                print "Location's Longitude","\t:",self.response.location.longitude
                IPDAT2.close()
        except ValueError:
            print "IP %s does not appear to be an IPv4 or IPv6 Address"%(self.ip)

#Lite2City("154.123.145.145")
            
class LiteCity:
    def __init__(self, ip):
        self.ip = ip

        try:
            self.hostname = net(self.ip)
            self.c_code = IPDAT1.country_code_by_name(self.hostname)
            self.region = IPDAT1.region_by_name(self.hostname)
            self.org = IPDAT1.org_by_name(self.hostname)
            self.isp = IPDAT1.isp_by_name(self.hostname)
            self.asn = IPDAT1.asn_by_name(self.hostname)
            self.sp = IPDAT1.netspeed_by_name(self.hostname)
        except:
            self.hostname = None
            self.c_code, self.region, self.org = None, None, None
            self.isp, self.asn, self.sp = None, None, None
            pass

        try:
            self.c_code = IPDAT1.country_code_by_addr(ip)
            self.c_name = IPDAT1.country_name_by_addr(ip)
            self.regionaddr = IPDAT1.region_by_addr(ip)
            for i in self.regionaddr:
                print "Country Region By Address","\t:",i,"\t:",regionaddr[i]
        except:
            self.co_code, self.c_name = None, None
            pass

        print "Country Name By Address","\t:",self.c_name
        print "Country Code By Address","\t:",self.co_code
        print "Country Code By Hostname","\t:",self.c_code
        print "Country Region By Hostname","\t:",self.region

        try:
            city = IPDAT1.record_by_addr(self.ip)
            if city != None:
                for i in city:
                    print i, "\t\t\t:",city[i]
            else:
                print "[-] The IP Address %s method \r\n could not be used with"\
                            " the %s database"%(self.ip, DB)
        except:
            print "[-] *_by_addr methods only accepts IP addresses."\
                    "\r\n  Dont Use Hostnames/Domain Names or Gibberish"

        print "Organization Lookup By Hostname",":",self.org
        print "ISP Lookup","\t\t\t:",self.isp
        print "ASN Lookup","\t\t\t:",self.asn
        print "NetSpeed Lookup","\t\t:",self.sp

#LiteCity("154.123.145.145")


class Intro:
    def __init__(self):
        os.system("clear")
        print "\r\n","*"*50+"IP GeoLocation"+"*"*50

        print "\n[+] Checking Internet Connction..."

        try:
            s = socket.gethostbyaddr(ip="216.58.206.228")
            print "[+] Internet Connection Available ... \t Your results will be finer"
        except:
            print "[-] No Internet Connection...\tInternet may be needed for Finer Results"

        sleep(1.8)
        os.system("clear")
        print "\r\n","*"*50+"IP GeoLocation"+"*"*50
        
def run():
    ip = IPGeoLoc().ip
    print "\n","*"*50+"...Using GeoLiteCity Database..."+"*"*52
    LiteCity(ip)
    print "\n","*"*50+"...Using GeoLite2-City Database..."+"*"*50
    Lite2City(ip)
    
if __name__=="__main__":
    Intro()
    try:
        while 1:
            run()
            print "\r\n","*"*50+"IP GeoLocation"+"*"*50
    except KeyboardInterrupt:
        print "\nClosing Down...\nBYE BYE"
