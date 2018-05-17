import geoip2.database

def lite2city(ip):
    try:
        reader = geoip2.database.Reader("Databases/GeoLite2-City.mmdb")
        try:
            response = reader.city(ip)
        except geoip2.errors.AddressNotFoundError:
            print "The address %s is not in the database."%(ip)
        else:
            print "Country Code","\t\t:",response.country.iso_code
            print "Country Name","\t\t:",response.country.name
            print "Simplified Chinese","\t:",response.country.names['zh-CN']
            print "Location's Major City","\t:",response.city.name
            print "Specific Location","\t:",response.subdivisions.most_specific.name
            print "Specific Location Code","\t:",response.subdivisions.most_specific.iso_code
            print "Location's Postal Code","\t:",response.postal.code
            print "Location's Latitude","\t:",response.location.latitude
            print "Location's Longitude","\t:",response.location.longitude
            reader.close()
    except ValueError:
            print "IP %s Does not appear to be an IPv4 or IPv6 address"%(ip)
