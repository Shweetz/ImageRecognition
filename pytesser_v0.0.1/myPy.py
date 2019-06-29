
def conv(pilImage):
#[python]
  from PIL import Image
  import wx

#pilImage = Image.open('my.png')
  image = wx.EmptyImage(pilImage.size[0],pilImage.size[1])
  image.setData(pil.convert("RGB").tostring())
  image.setAlphaData(pil.convert("RGBA").tostring()[3::4])

## use the wx.Image or convert it to wx.Bitmap
  bitmap = wx.BitmapFromImage(image)

  return bitmap

#####

import lxml.etree
# xmlstr is your xml in a string
root = lxml.etree.fromstring(xmlstr)
textelem = root.find('result/field/value/text')
print textelem.tex

import urllib
urllib.urlretrieve ("http://www.s0urce.io/client/img/words/hard/n3b55.png", "tmp.tif")

#http://www.s0urce.io/
#../client/img/words/hard/n3b55.png

# get image
import sys
imageName = 'phototest.tif'
imageName = 'tmp.tif'
#image = sys.argv[1]
#print sys.argv[1] # prints 1st arg


# Img2Text
from pytesser import *
image = Image.open(imageName)

#data = [image.getpixel((x, y)) for x in range(image.width) for y in range(image.height)]
#text = image_to_string(data)

#image.tobitmap()
#newIm = conv(image)
#image = image.convert('1')
bg = Image.new("RGB", image.size, (255,255,255))
bg.paste(image,image)
print image_to_string(bg)

text = image_to_string(bg)

# Print
print text