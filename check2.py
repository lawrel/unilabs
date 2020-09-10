from PIL import Image
import check2_helper as c
im = Image.new("RGB",(512,512))
im2 = c.make_square(Image.open("ca.jpg"))
im3 = c.make_square(Image.open('im.jpg'))
im4 = c.make_square(Image.open('hk.jpg'))
im5 = c.make_square(Image.open('bw.jpg'))
im.paste(im2.resize((256,256)),(0,0))
im.paste(im3.resize((256,256)),(0,256))
im.paste(im4.resize((256,256)),(256,0))
im.paste(im5.resize((256,256)),(256,256))
im.save("avengers.jpg")
im.show()