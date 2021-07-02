from GPSPhoto import gpsphoto

img_name = 'test.jpg'
# Create GPSInfo Data Object
#info = gpsphoto.GPSInfo((35.104860, -106.628915))
#info = gpsphoto.GPSInfo((35.104860, -106.628915), timeStamp='1970:01:01 09:05:05')
info = gpsphoto.GPSInfo((35.104860, -106.628915), alt=10, timeStamp='1970:01:01 09:05:05')

# Read Photo
photo = gpsphoto.GPSPhoto(img_name)

# Modify GPS Data
photo.modGPSData(info, img_name)


