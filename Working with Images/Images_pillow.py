from PIL import Image

mac = Image.open('example.jpg')

# mac.show()

print(mac.size)

#Outputs the filename
mac.filename

#Outputs the file format
mac.format_description

#CROPPING IMAGES

pencils = Image.open('pencils.jpg')
print(pencils.size)

pencils.crop((0,1100,1950/3,1300)).show()