from GPSPhoto import gpsphoto

img_name = 'test.jpg'

# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData(img_name)

# print(data)

for value in data:
	print (value,'=',data[value])

'''
# For raw Data
rawData = gpsphoto.getRawData(image_name)

for value in rawData:
	print (value,'=',rawData[value])
'''

