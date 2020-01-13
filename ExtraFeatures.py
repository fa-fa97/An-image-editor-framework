#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 09:52:08 2019

@author: fatemeh
"""

from PIL import ImageOps,ImageFont
from Photo import Photo


class ExtraFeatures:
    
    def __init__(self,FeatureName,photo):
        
        self.FeatureName = FeatureName
        self.photo = Photo(photo.getPath())
        
    def anotherPhoto(self,newPhoto):
        
        cphoto = self.photo.getPhotoCopy()
        position = ((cphoto.width - newPhoto.getWidth()), (cphoto.height - newPhoto.getHeight()))
        cphoto.paste(newPhoto.getPhoto(), position)
        cphoto.show()
        self.photo.setPhotoCopy(cphoto)
        return cphoto


    def add_border(self, border, color=0):
     
        if isinstance(border, int) or isinstance(border, tuple):
            bPhoto = ImageOps.expand(self.photo.getPhotoCopy(), border=border, fill=color)
        else:
            raise RuntimeError('Border is not an integer or tuple!')
     
        bPhoto.show()
        self.photo.setPhotoCopy(bPhoto)
        return bPhoto
    
    def add_text(self,text,textX,textY,textTopLeftX,textTopLeftY):
        font = ImageFont.load_default() # load default bitmap font
        (width, height) = font.getsize(text)
        textImage = font.getmask(text)
        pixels = self.photo.getPhotoCopy().load()
        
        for y in range(self.photo.getHeight()):
            by = int(height * (y - textTopLeftY) / textY + 0.5)
            if by >= 0 and by < height:
                for x in range(self.photo.getWidth()):
                    bx = int(width * (x - textTopLeftX) / textX + 0.5)
                    if bx >= 0 and bx < width:
                        if textImage.getpixel((bx, by)) == 0: # text background
                            #background 
                            # pixels[x, y] = textBackgroundColor
                            pixels[x, y] = (255,255,255)
                        else: # text foreground
                            # pixels[x, y] = textColor
                            pixels[x, y] = (0,0,0)
        
        self.photo.setPhotoCopy(self.photo.getPhotoCopy())
        self.photo.getPhotoCopy().show()
        return self.photo.getPhotoCopy()
     
    
    def getFeaturename(self):
        return self.FeatureName
    
    def setFeaturename(self,fnew):
        self.FeatureName = fnew
    

        
        
