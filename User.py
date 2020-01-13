#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:33:46 2019

@author: fatemehf
"""
from Connection import Connection

class User:
    
    def __init__(self,username,password,email):
        
        self._username = username
        self._password = password
        self._email = email
        self.con = Connection()
        sqlcommand = ("IF NOT EXISTS (SELECT * FROM User WHERE username = '%s')"
                      "INSERT INTO User"
                      "(username,password,email)"
                      " VALUES ('%s','%s','%s')"
                       %(self.username,self.password ,self.email))
                     
        self.con.cursor.execute(sqlcommand)
        self.con.connection.commit()
        
    def login(self,user,passw): 
        
        if("SELECT count(username) FROM User WHERE username = '%s', password = '%s' " %(user,passw) > 0):
            print ("Login successful!")
            return True
        
        print ("Wrong username/password")
        return False
    
    def displayPhoto():
        pass
    
    
    def getUsername(self):
        return self._username
    
    def setUsername(self,newUsername):
        self._username = newUsername
    
    def getPassword(self):
        return self._password
    
    def setPassword(self,newPassword):
        self._password = newPassword
        
    def getEmail(self):
        return self._email
    
    def setEmail(self,newEmail):
        self._email = newEmail
        
        
    
    
    
    
    
        
        