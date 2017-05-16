import urllib
import json
import math

def hav (lat, lng, lat1, lng1):
	la1 = lat*(math.pi/180)
	la = lat1*(math.pi/180)
	lo1 = lng*(math.pi/180)
	lo = lng1*(math.pi/180)
	r = 6371
	h = math.sin((la1-la)/2.0)**2 + math.cos(la)*math.cos(la1)*math.sin((lo1-lo)/2.0)**2
	d = 2*r*math.asin(math.sqrt(h))
	return d
	

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'


address = raw_input('Enter location 1: ')
if len(address) < 1:
	print 'address will be defaulted to Washington DC'
	address = 'washington dc'

address1 = raw_input('Enter location 2: ')
if len(address1)<1:
	print 'address will be defaulted to Chihuahua, Chihuahua\n'
	address1 = 'Chihuahua, chihuahua'
	
	
url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address}) #urlenconde uses the parameters (sensor and address) so it can be put in a correct url. I.E Chihuahua, chihuahua -> chihuahua%2C+Chihuahua
url1 = serviceurl + urllib.urlencode({'sensor':'false', 'address':address1}) 

print url, '\n',  url1, '\n'

opn = urllib.urlopen(url).read()
js = json.loads(opn)

if 'status' not in js or js['status'] != 'OK':
	print 'failed'
	print opn

opn1 = urllib.urlopen(url1).read()
js1 = json.loads(opn1)
	
print opn1
if 'status' not in js1 or js1['status'] != 'OK':
	print 'failed'
	print opn1

lng = js['results'][0]['geometry']['location']['lng']	
lat = js['results'][0]['geometry']['location']['lat']	
loc1 = js['results'][0]['formatted_address']

lng1 = js1['results'][0]['geometry']['location']['lng']	
lat1 = js1['results'][0]['geometry']['location']['lat']	
loc2 = js1['results'][0]['formatted_address']

print 'For', loc1, 'Latitude', lat,'Longitude', lng, '\n'
print 'For', loc2, 'Latitude', lat1,'Longitude', lng1, '\n'
print 'La distancias entre', loc1, 'y ', loc2,'es ', hav(lat, lng, lat1, lng1), 'Km'
