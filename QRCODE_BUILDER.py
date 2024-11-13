#QRCODE BUILDER
import qrcode

link = input("enter your link:")
image = qrcode.make(link)
#image.save("Downloads/qr.png")
print = (image) 

