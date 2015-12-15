import csv

from geopy.geocoders import Nominatim

r_file_name = "FA2015.csv"
w_file_name = "LL_FA2015.csv"
''' 
headers = id, prog, class, major, sex, age, addr_line1, addr_line2, addr_line3, 
          city, st, zip, country, race, hispanic
'''

rf = open(r_file_name, 'rb')
wf = open(w_file_name, 'wb')

reader = csv.reader(rf)
writer = csv.writer(wf)

reader.next()

for row in reader:
   for elem in row:
      elem = elem.lstrip().rstrip()
   if "UNITED STATES" in row[12]:
      address = row[6] + " " + row[7] + " " + row[8] + " " + row[9] + " " + row[10] + " " + row[11]
      geolocator = Nominatim()
      location = geolocator.geocode(address)
      if location:
         print location
         new_row = row + [location.latitude, location.longitude]
         writer.writerow(new_row)
   else:
      print "other country"