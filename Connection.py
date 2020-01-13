# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:38:16 2018

@author: fatemeh
"""

from pyodbc import *
import pandas as pd

class Connection():
    def __init__(self):
        self.connection = connect(r'Driver={SQL Server};Server=DESKTOP-6MUBM5S\SQL2014;Database=photo;Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()
        self.connection.commit()