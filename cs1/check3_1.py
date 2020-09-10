from PIL import Image
import check2_helper as c
import panoramio as pan
address = input('Enter an address => ')
urls = pan.getPhotos(address,4)
if len(urls) < 4:
    print("Could not find sufficient number of pictures.")
else:
    im = Image.new("RGB",(512,512))
    im2 = c.make_square(pan.openphoto(urls[0]))
    im3 = c.make_square(pan.openphoto(urls[1]))
    im4 = c.make_square(pan.openphoto(urls[2]))
    im5 = c.make_square(pan.openphoto(urls[3]))
    im.paste(im2.resize((256,256)),(0,0))
    im.paste(im3.resize((256,256)),(0,256))
    im.paste(im4.resize((256,256)),(256,0))
    im.paste(im5.resize((256,256)),(256,256))
    im.save("check3.jpg")
    im.show()