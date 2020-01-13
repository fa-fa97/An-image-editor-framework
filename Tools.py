# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:26:13 2018

@author: Fatemeh

"""
from Photo import Photo
import numpy as np
from PIL import Image
from shapely.geometry import Point
from shapely.geometry import Polygon

class Tool:
    
    def __init__(self,toolName,photo):
        self.toolName = toolName
        self.photo = Photo(photo.getPath())
        
    def crop(self,x1,y1,x2,y2): 
        #crop image that specific part of it
        x = self.photo.getPhotoCopy()
        area = (x1,y1,x2,y2)
        x = x.crop(area)
        x.show()
        self.photo.setPhotoCopy(x)
        return x
    
    def rotate(self,degree):
        #rotate image by spcific degree
        r = self.photo.getPhotoCopy().rotate(degree,expand=True)
        r.show()
        self.photo.setPhotoCopy(r)
        return r
    
    def flipLR(self):
        fL = self.photo.getPhotoCopy().transpose(Image.FLIP_LEFT_RIGHT)
        fL.show()
        self.photo.setPhotoCopy(fL)
        return fL
    
    
    def flipTB(self):
        fT = self.photo.getPhotoCopy().transpose(Image.FLIP_TOP_BOTTOM)
        fT.show()
        self.photo.setPhotoCopy(fT)
        return fT
        
    
    def resize(self,x,y):
        s = self.photo.getPhotoCopy().resize((x,y),Image.ANTIALIAS)
        s.show()
        self.photo.setPhotoCopy(s)
        return s
        
    
    def cut(self,x1,y1,x2,y2,x3,y3):
        y = self.photo.getPhotoCopy().convert('RGBA')
        pixels = np.array(y)
        im_copy = np.array(y)
        region = Polygon([(x1, y1), (x2, y2), (x3, y3)])
        
        for index, pixel in np.ndenumerate(pixels):
              # Unpack the index.
              row, col, channel = index
              # We only need to look at spatial pixel data for one of the four channels.
              if channel != 0:
                    continue
              point = Point(row, col)
              if not region.contains(point):
                    im_copy[(row, col, 0)] = 255
                    im_copy[(row, col, 1)] = 255
                    im_copy[(row, col, 2)] = 255
                    im_copy[(row, col, 3)] = 0        
        cut = Image.fromarray(im_copy)
        cut.show()
        self.photo.setPhotoCopy(cut)
        return cut
    
    def getTname(self):
        return self.toolName
    
    def setTname(self,tnew):
        self.toolName = tnew
    

    
    