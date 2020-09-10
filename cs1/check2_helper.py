from PIL import Image
def make_square(im):
    w,h = im.size
    if w > h:
        im2 = im.crop((0,0,h,h))
    else:
        im2 = im.crop((0,0,w,w))
    return im2
