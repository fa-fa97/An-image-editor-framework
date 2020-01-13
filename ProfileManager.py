#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:29:26 2019

@author: fatemehf
"""

from Connection import Connection


class ProfileManager:
    
    def __init(self):
        self.con = Connection()
    
    def changeUsername(self,user,newusername):
        user.setUsername(newusername)
        sqlcommand = ("UPDATE User SET username=%s WHERE username='%s'" %(newusername,user.getUsername()))
        self.con.cursor.execute(sqlcommand)
        self.con.connection.commit()
    
    def changePassword(self,user,newpass):
        user.setPassword(newpass)
        sqlcommand = ("UPDATE User SET password=%s WHERE password='%s'" %(newpass,user.getPassword()))
        self.con.cursor.execute(sqlcommand)
        self.con.connection.commit()
    
    def changeEmail(self,user,newEmail):
        user.setEmail(newEmail)
        sqlcommand = ("UPDATE User SET email=%s WHERE email='%s'" %(newEmail,user.getEmail()))
        self.con.cursor.execute(sqlcommand)
        self.con.connection.commit()
        
    
    
    
        