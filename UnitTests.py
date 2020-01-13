# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:04:12 2018

@author: fatemeh

"""
#from Photo import Photo
#from Album import Album
#from Tools import Tool
#from Effect import Effect
#from User import User
from ExtraFeatures import ExtraFeatures 
#from PhotoManager import PhotoManager


if __name__ == '__main__':
    
    
    
    #-----create Photo ------
    pic = Photo("p2.jpg")
#    picManager = PhotoManager()
#    
#    
#    
#    eft = Effect("effect1",pic)    
        
#    picManager.view(pic)
#    picManager.load(pic)
#    picManager.save("p2new.jpg")
#    picManager.copy(pic)
#    
#    print(pic.getPixel(4,5))
#    print(pic.getPath())
#    print(pic.getHeight())
#    print(pic.getWidth())
#    print(pic.getMode())
#    print(pic.getType())
#    
#    eft.brightness(50)
#    eft.grayscale()
#    eft.blur()
#    eft.colorized()
#    eft.posterized()

    
    
    
    pic2 = Photo("p1.jpg")
#    to4 = Tool("tool1",pic2)

#     picManager.view(pic2)
#    to4.crop(0,0,250,250)
#    to4.cut(20,20,100,302,150,150)
#    to4.rotate(45)
#    to4.flipLR()
#    to4.flipTB()
#    to4.resize(70,60)
    
    extraFeature1 = ExtraFeatures("pasteAnotherPhoto",pic2)
    extraFeature1.anotherPhoto(pic)
    extraFeature1.add_text("Hello word!",400,100,400,100)
    extraFeature1.add_border(border=(10, 30, 20, 50),color='white')
    
    
    
    
#    
#    al1 = Album("album1","24/9/97","family")
#    al1.addPhoto(pic2)
#    al1.addPhoto(pic)
#    print(al1.listPhotos)
#    
#    print(al1.getNumOfPhotos())
#    
#    al1.removePhoto(pic2)
#    print(al1.listPhotos)
#    
    
    

    
    
    
    
