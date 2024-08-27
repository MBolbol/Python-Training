# Image manipulation with pillow

from PIL import Image

# open image
myImage = Image.open(r"E:\Alex\IMG_20231128_121333_289.jpg")

# show image
myImage.show()

# crop image
myBox = (200,300,500,600)
newImage = myImage.crop(myBox)

# show new image
newImage.show()

# converted mode

myConverted = myImage.convert('L') #gray scall
myConverted.show()

