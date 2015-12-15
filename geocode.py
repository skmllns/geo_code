import csv

from geopy.geocoders import Nominatim

file_name = "FA2015.csv"

''' 
headers = id, prog, class, major, sex, age, addr_line1, addr_line2, addr_line3, 
          city, st, zip, country, race, hispanic
'''

with open(file_name) as f:
   reader = csv.reader(f)
   #skip headers
   reader.next()
   for row in reader:
      if "UNITED STATES" in row[12]:
         address = row[6] + " " + row[7] + " " + row[8] + " " + row[9] + " " + row[10] + " " + row[11]
         geolocator = Nominatim()
         location = geolocator.geocode(address)
         if location:
            print((location.latitude, location.longitude))     
      else:
         print "other country"