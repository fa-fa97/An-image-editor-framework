# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:45:18 2018

@author: Fatemeh

"""
from PIL import Image
import requests
import io
#from Connection import Connection

class Photo:
    def __init__(self,Path):
        self._path = Path
        self._photo = Image.open(self._path)
        self._height, self._width = self._photo.size
        self._type = self._photo.format
        self._mode = self._photo.mode
        self._copy_photo = self._photo
#        self.con = Connection()
#        sqlcommand = ("IF NOT EXISTS (SELECT * FROM Photo WHERE pathp = '%s')"
#                      "INSERT INTO Photo"
#                      "(pathp,height,width,mode,typep)"
#                      " VALUES ('%s','%s','%s','%s','%s')"
#                       %(self._path,self._path ,self._height ,self._width ,self._mode,self._type))
#                     
#        self.con.cursor.execute(sqlcommand)
#        self.con.connection.commit()
        
    def getPixel(self,i, j):
        if i > self._width or j > self._height:
          return None
        pixel = self._photo.getpixel((i, j))
        return pixel          
    
    def getPhoto(self):
        return self._photo
    
    def getPhotoCopy(self):
        
        return self._copy_photo
    def setPhotoCopy(self,image):
        self._copy_photo =image
    
    def setPath(self,path):
        self._path = path
        
    def getPath(self):
        return self._path
        
    def getWidth(self):
        return self._width
        
    def getHeight(self):
        return self._height 
        
    def getType(self):
        return self._type
    
    def getMode(self):
        return self._mode
        

    
        

    
        
        
