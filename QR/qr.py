#Has to have qrcode installed, "pip install qrcode"
import qrcode

data = str(input("What data should be encoded? "))

img = qrcode.make(data)

location = str(input("Enter the folder location where you want to save the code: "))
img.save(location)