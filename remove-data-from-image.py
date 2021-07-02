from GPSPhoto import gpsphoto

img_name = 'test.jpg'

# Read Photo
photo = gpsphoto.GPSPhoto(img_name)

# Strip GPS Data
photo.stripData(img_name)

