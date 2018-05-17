from pygeoip import *
import pygeoip
db = "GeoLiteCity"
def litecity(ip,ipdat):
    try:
        hostname = net(ip)
        c_code = ipdat.country_code_by_name(hostname)
        region = ipdat.region_by_name(hostname)
        org = ipdat.org_by_name(hostname)
        isp = ipdat.isp_by_name(hostname)
        asn = ipdat.asn_by_name(hostname)
        sp = ipdat.netspeed_by_name(hostname)
    except:
        hostname = None
        c_code,region,org,isp,asn,sp = None,None,None,None,None,None
        pass
            
    print "[+] Tracing IP Address","\t\t:",ip,"\r\n[+] Hostname/Domain Name","\t:",hostname
    try:
        co_code = ipdat.country_code_by_addr(ip)
        c_name = ipdat.country_name_by_addr(ip)
        regionaddr = ipdat.region_by_addr(ip)
        for i in regionaddr:
            print "Country Region by Address","\t:",i,"\t:",regionaddr[i]
    except:
        co_code,c_name = None,None
        pass
            
    print "Country Name by Address","\t:",c_name
    print "Country Code by Address","\t:",co_code
    print "Country Code by Hostname","\t:",c_code
    print "Country Region by Hostname","\t:",region
    try:
        city = ipdat.record_by_addr(ip)
        if city != None:
            for i in city:
                print i,"\t\t\t:",city[i]
        else:
            print ("[-] The IP Address %s method \r\n    could not be used with"
                   " the %s database"%(ip,db))
    except:
        print ("[-] *_by_addr methods only accepts IP addresses."
                   "\r\n    Dont Use Hostnames/Domain Names or Gibberish")
    print "Organization Lookup by Hostname",":",org
    print "ISP Lookup","\t\t\t:",isp
    print "ASN Lookup","\t\t\t:",asn
    print "NetSpeed Lookup","\t\t:",sp
