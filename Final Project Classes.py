# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:49:21 2019

@author: Abhijit
"""
import random
#%% Product

class Product:
    
    def __init__(self, row):
        
        row = row.split(',')
        
        self.name = row[0]
        self.category = row[1]
        self.price = row[2]
        self.units = row[3]
    
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    
    def get_units(self):
        return self.units
    
    def decrement_units(self):
        self.units = str(int(self.units) - 1)
    
    def make_transaction(self):
    
        if int(self.get_units()) > 0:
            self.decrement_units()
    
        else:
            raise Exception
            
            
    def convert_to_string(self):
        
        return f"{self.name},{self.category},{self.price},{self.get_units()}"
#%%
        
def make_recommendation(inventory, titles, name, category):
    
    titles = titles.split(',')
    suggested_products = []
    
    for row in inventory:
        
        row = row.split(',')
        
        if (
                row[titles.index('Product')] != name 
                and row[titles.index('Category')] == category
        ):
                suggested_products.append(row[titles.index('Product')])
                
                
    if len(suggested_products) > 3:
        
        temp = []
        
        for i in range(3):

            temp.append(suggested_products.pop(random.randint(0, len(suggested_products) - 1)))
        
        suggested_products = temp
         
    return f"Here are similar products {suggested_products}"    
#%%
        
def make_recommendation2(inventory, titles, name, category):
    
    titles = titles.split(',')
    suggested_products = []
    
    for row in inventory:
        
        product = Product(row)
        
        if product.get_name() != name and product.get_category() == category:
            
                suggested_products.append(product.get_name())
                
                
    if len(suggested_products) > 3:
        
        temp = ''
        
        for i in range(3):

            temp += str(i+1) + '.' + str(suggested_products.pop(random.randint(0, len(suggested_products) - 1)))
        
        suggested_products = temp
         
    return f"Here are similar products: {suggested_products}"  
    
#%% Function to write inventory to external file
        
def write_inventory_to_file(inventory, file_name):

    try:
        output_file = open(file_name, 'w')
        
        for row in inventory:
            output_file.write(row + '\n')
            
    except IOError as e:
        print(f"{e} error occured")
        
    except Exception as e:
        print(f"{e} error occured")
        
#%%

file_name = 'C:\\Users\\Abhijit\\Desktop\\Inventory.csv'
input_file = open(file_name, 'r')
inventory = input_file.read().splitlines()
input_file.close()

titles = inventory.pop(0)

while True:

    requested_product = input('Please select a product to buy: ')
    found_match = False
    
    for row in inventory:
        
        product = Product(row)
        
        if product.get_name() == requested_product:
            
            found_match = True
            name = product.get_name()
            category = product.get_category()
            
            try:
                product.make_transaction()
                inventory[inventory.index(row)] = product.convert_to_string()
                
            except:
                print(f'Sorry, {name} is out of stock')
                       
    if found_match == False:
        print('We do not sell that product')
        continue
                    
    buy_more = input('Would you like to buy more (y/n): ')
    
    if buy_more == 'n':
        
        print(make_recommendation2(inventory, titles, name, category))   
        buy_more = input(f"Last chance, would you like to buy more (y/n): ")
        
        if buy_more == 'n':
            break
        
        
inventory.insert(0,titles)
      
write_inventory_to_file(inventory, file_name)        
#%%