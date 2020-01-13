# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:06:11 2018

@author: fatemeh

"""
from Photo import Photo
from PIL import ImageFilter,Image
from PIL.ImageOps import colorize,posterize
class Effect:
    
    def __init__(self,Ename,photo):
        self.effectName = Ename
        self.photo = Photo(photo.getPath())
        
    def blur(self):
        b = self.photo.getPhotoCopy() 
        b = b.filter(ImageFilter.BLUR)
        b.show()
        self.photo.setPhotoCopy(b)
        return b
    
    def brightness(self,value):
        x = self.photo.getPhotoCopy()
        data = list(x.getdata())
        data_m = list()
        for pixel in data:
            data_m.append((pixel[0]+value, pixel[1]+value, pixel[2]+value))
        img_m = Image.new(x.mode, x.size)
        img_m.putdata(data_m)
        img_m.show()
        self.photo.setPhotoCopy(img_m)
        return img_m
 
    def grayscale(self):
        g = self.photo.getPhotoCopy()
        g = g.convert('L')
        g.show()
        self.photo.setPhotoCopy(g)
        return g
    
    def colorized(self):
        c = colorize(self.photo.getPhotoCopy(), black='red', white='white')
        c.show()
        self.photo.setPhotoCopy(c)
        return c
        
        
    def posterized(self):
        p = posterize(self.photo.getPhotoCopy(), bits=1)
        p.show()
        self.photo.setPhotoCopy(p)
        return p
        
#    def halftoning(self):
#      width = self.photo.getWidth()
#      height = self.photo.getHeight()
      
    
      # Create new Image and a Pixel Map
#      new = self.photo.getPhotoCopy().create_image(width,height)
#      pixels = new.load()
#    
#      # Transform to half tones
#      for i in range(0, width, 2):
#        for j in range(0, height, 2):
#          # Get Pixels
#          p1 = self.photo.getPixel( i, j)
#          p2 = self.photo.getPixel(i, j + 1)
#          p3 = self.photo.getPixel(i + 1, j)
#          p4 = self.photo.getPixel(i + 1, j + 1)
#    
#          # Transform to grayscale
#          gray1 = (p1[0] * 0.299) + (p1[1] * 0.587) + (p1[2] * 0.114)
#          gray2 = (p2[0] * 0.299) + (p2[1] * 0.587) + (p2[2] * 0.114)
#          gray3 = (p3[0] * 0.299) + (p3[1] * 0.587) + (p3[2] * 0.114)
#          gray4 = (p4[0] * 0.299) + (p4[1] * 0.587) + (p4[2] * 0.114)
#    
          # Saturation Percentage
#          sat = (gray1 + gray2 + gray3 + gray4) / 4
#    
#          # Draw white/black depending on saturation
#          if sat > 223:
#            pixels[i, j]         = (255, 255, 255) # White
#            pixels[i, j + 1]     = (255, 255, 255) # White
#            pixels[i + 1, j]     = (255, 255, 255) # White
#            pixels[i + 1, j + 1] = (255, 255, 255) # White
#          elif sat > 159:
#            pixels[i, j]         = (255, 255, 255) # White
#            pixels[i, j + 1]     = (0, 0, 0)       # Black
#            pixels[i + 1, j]     = (255, 255, 255) # White
#            pixels[i + 1, j + 1] = (255, 255, 255) # White
#          elif sat > 95:
#            pixels[i, j]         = (255, 255, 255) # White
#            pixels[i, j + 1]     = (0, 0, 0)       # Black
#            pixels[i + 1, j]     = (0, 0, 0)       # Black
#            pixels[i + 1, j + 1] = (255, 255, 255) # White
#          elif sat > 32:
#            pixels[i, j]         = (0, 0, 0)       # Black
#            pixels[i, j + 1]     = (255, 255, 255) # White
#            pixels[i + 1, j]     = (0, 0, 0)       # Black
#            pixels[i + 1, j + 1] = (0, 0, 0)       # Black
#          else:
#            pixels[i, j]         = (0, 0, 0)       # Black
#            pixels[i, j + 1]     = (0, 0, 0)       # Black
#            pixels[i + 1, j]     = (0, 0, 0)       # Black
#            pixels[i + 1, j + 1] = (0, 0, 0)       # Black
#    
#        # Return new image
#        new.show()
#        self.photo.setPhotoCopy(new)
#        return new
        
    def getEname(self):
        return self.effectName
    
    def setEname(self,enew):
        self.effectName = enew
  

    






    