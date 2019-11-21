# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:49:14 2019

@author: Abhijit
"""
#%%

class Shape:
    def __init__(self, name):
        self.name = name
        
class Circle(Shape):
   def __init__(self, name, r):
       super().__init__(name)
       self.r = r

c = Circle('circle 1', 5)
c.name
       

#%%