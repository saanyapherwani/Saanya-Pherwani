# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:49:21 2019

@author: Abhijit
"""
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
            category = product.get_categroy()
            
            try:
                product.make_transaction()
                inventory[inventory.index(row)] = product.convert_to_string()
                
            except ValueError:
                print('Sorry, the item is out of stock')
                       
    if not found_match:
        print('We do not sell that product')
        continue
                
    
    buy_more = input('Would you like to buy more (y/n): ')
    
    if buy_more != 'y':
        
        print(make_recommendation(inventory, name, category))   
        buy_more = input(f"Last chance, would you like to buy more (y/n): ")
        
        if buy_more != 'y':
            break
        
        
inventory.insert(0,titles)
      
write_to_file(inventory, file_name)        

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
    
    def get_categroy(self):
        return self.category
    
    def get_units(self):
        return self.units
    
    def set_units(self):
        self.units = str(int(self.units) - 1)
    
    def make_transaction(self):
    
        if int(self.get_units()) > 0:
            self.set_units()
    
        else:
            raise ValueError
            
    def convert_to_string(self):
        
        return f"{self.name},{self.category},{self.price},{self.get_units()}"
#%%
        
def make_recommendation(inventory, name, category):
    
    similar_products = []
    
    for product in inventory:
        
        product = product.split(',')
        
        if product[0] != name and product[1] == category:
            
            similar_products.append(product[0])
            
    return f"Here are similar products {similar_products}"    
    
#%% Function to write inventory to external file
        
def write_to_file(inventory, file_name):

    output_file = open(file_name, 'w')
    
    for row in inventory:
        output_file.write(row + '\n')
        
    output_file.close()
    
#%%