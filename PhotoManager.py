#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:19:17 2019

@author: fatemehf
"""

from PIL import Image
import requests
import io



class PhotoManager:
    
    
    def view(self,photo):
        return photo.getPhotoCopy().show()        
    
    def save(self,photo,path):
        return photo.getPhotoCopy().save(path)
        sqlcommand = ("UPDATE Photo SET pathp=%s WHERE pathp='%s'" %(path,self._path))
        con.cursor.execute(sqlcommand)
        con.connection.commit()
    
    def load(self,photo):
        self.photo.getPhotoCopy().load()
    
    def download(self,url, image_path):
        r = requests.get(url, timeout=4.0)
        if r.status_code != requests.codes.ok:
            assert False, 'Status code error: {}.'.format(r.status_code)
    
        with Image.open(io.BytesIO(r.content)) as im:
            im.save(image_path)

        print('Image downloaded from url: {} and saved to: {}.'.format(url, image_path))
        
    
    def copy(self,photo):
        return photo.getPhotoCopy().copy()
    