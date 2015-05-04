import exifread
from geopy import point
import webbrowser

# TODO: option to iterate through folders and generate xml file
# Open image file for reading (binary mode)

user_inpt =  raw_input("Please enter a path to an EXIF geotagged Photo")
f = open(r"user_inpt", 'rb')


# Return Exif tags
tags = exifread.process_file(f)
for tag in tags:
	if "Long" in tag:
		if "Ref" not in tag:
			lon = tags[tag]

		else: lonC = str(tags[tag])
	if "Lat" in tag:
		if "Ref" not in tag:
			lat = tags[tag]
		else: latC = str(tags[tag])

def formatthatshit(cord):
	out = ''
	cord = str(cord)
	DD = 0
	for part in cord[1:-1].replace(",","").replace("."," ").split(' '):
		if "/" in part:
			part = part.split("/")
			part=  str(int(part[0]) / int(part[1])).replace('.', ' ')
		if DD == 1:
			part = part + "m"
		elif DD == 2:
			part = part + "s"

		out = out + str(part) + " "
		DD+=1

	return out

lat= formatthatshit(lat)   + latC 
lon=  formatthatshit(lon)  + lonC


p1  = lat + " " + lon
p2 = point.Point(p1)
lat = p2.latitude
lon = p2.longitude


lat = float("{0:.8f}".format(lat))
lon = float("{0:.8f}".format(lon))


url = 'https://www.google.com/maps/place/'+str(lat)+','+str(lon)


webbrowser.open_new(url)

# exit()
# coords = {'lon' :lon, 'lat':lat}# 'activity':activity}
# # print coords

# coords_ = geoplotlib.utils.DataAccessObject(coords)

# #.head(3)
# print geoplotlib.utils.DataAccessObject(coords_).values()


# geoplotlib.scatter(coords_)
# geoplotlib.tiles_provider('toner')
# # exit()
# geoplotlib.show()


