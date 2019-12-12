# Final Project Group 13: Abhijit Ballal, Rifa Maknojia, Saanya Pherwani

#%%
# graphics imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

#%% Prodcut Class to convert rows in 'Inventory.csv' to Product Objects
class Product:

    # constrctor that accepts string to initialize Product Object
    def __init__(self, row):
        
        row = row.split(',')
        
        self.name = row[0]
        self.category = row[1]
        self.price = int(row[2])
        self.units = row[3]
        self.amount_paid = 0
        self.amount_needed = self.price
        
    # getter functions to retrieve data attributes
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category    
    
    def get_price(self):
        return self.price
    
    def get_amount_paid(self):
        return self.amount_paid 
    
    def get_amount_needed(self):
        return self.amount_needed
    
    def get_units(self):
        return int(self.units)    
    
    # setter functions to change data attributes
    def set_amount_paid(self, payment):
        self.amount_paid += payment

    def set_amount_needed(self, payment):
        self.amount_needed -= payment
    
    # return object properties as a string
    def convert_to_string(self):
        return f"{self.name},{self.category},{self.price},{self.units}"
            
    # Decreases purchased product's stock by one
    def make_transaction(self):
        self.units = str(int(self.units) - 1)
        
#%% Writes updated inventory stock balances to 'Inventory.csv' file
        
def write_inventory_to_file(inventory, file_name):

    # try block to handle file reading and writing exceptions
    try:
        output_file = open(file_name, 'w')
        for product in inventory:
            output_file.write(product + '\n')
        output_file.close()
        print('file closed')
            
    except IOError as e:
        print(f"{e} error occured")
    except Exception as e:
        print(f"{e} error occured")
    
#%% makes product suggestions based on the product the user purchased
    
def make_recommendation(inventory, category, name):

    l1 = []
    l2 = []
    
    for product in inventory:
        product = product.split(',')
        
        # suggested products should have the same category as the purchased product
        # but it should not have the same name
        if product[1] == category and product[0] != name:
            l1.append(product[0])
    
    # if statement to produce a maximum of three suggested products
    if len(l1) > 3:
        for i in range(3):
            l2.append(l1[random.randint(0, len(l1) - 1)])
        l1 = l2
    
    return l1
#%% main class
    
class MyApp(App):

    # read in 'Inventory.csv' and stroe to 'product_inventory' list
    file_name = 'Inventory.csv'
    input_file = open(file_name, 'r')
    product_inventory = input_file.read().splitlines()
    input_file.close()      
    
    # initialization of class variables
    money_denominations = ['1', '5', '10', '20']  
    product_titles = []
    listed_products = []    
    suggested_products = []    
    product_index = 0

    # 'MyApp' class constructor
    def build(self):
            
        # initialize three boxlayouts that will be the three columns
        User_Input_Box = BoxLayout(orientation='vertical')   
        Payment_Box = BoxLayout(orientation='vertical') 
        Suggested_Products_Box = BoxLayout(orientation='vertical') 
        
        # initialize and format widgets to be added to three boxlayouts
        
        # 'Choose_Item' boxlayout/column
        self.title1 = Label(text='Choose Item', font_size = 70, size_hint=(1,.30), halign='center')
        User_Input_Box.add_widget(self.title1)                
        self.label1 = Label(text='Enter a product to buy', font_size=30, size_hint=(1,.30))
        User_Input_Box.add_widget(self.label1)
        self.textinput1 = TextInput(text='', font_size=50, size_hint=(1,.20), halign='center')
        User_Input_Box.add_widget(self.textinput1)
        self.button1 = Button(text='Select Product', font_size=30, size_hint=(1,.30), halign='center', background_color = (0,1,0,1))
        self.button1.bind(on_press=self.Product_Input_Button)
        User_Input_Box.add_widget(self.button1)        
        self.blankspace1 = Label()        
        User_Input_Box.add_widget(self.blankspace1)  
        
        # 'Payment' boxlayout/column
        self.title2 = Label(text='Payment', font_size = 70, size_hint=(1,.30), halign='center')      
        Payment_Box.add_widget(self.title2)        
        self.label2 = Label(font_size=30, size_hint=(1,.30), halign='center')
        Payment_Box.add_widget(self.label2)
        self.textinput2 = TextInput(font_size=50, size_hint=(1,.20), halign='center')
        Payment_Box.add_widget(self.textinput2)
        self.button2 = Button(text='Submit Payment', font_size=30, size_hint=(1,.15), halign='center', background_color = (0,1,0,1))
        self.button2.bind(on_press=self.Payment_Input_Button)
        
        Payment_Box.add_widget(self.button2)
        self.button3 = Button(text='Finished Paying', font_size=30, size_hint=(1,.15), halign='center',background_color = (0,1,0,1))
        self.button3.bind(on_press=self.Payment_Finished_Button)
        Payment_Box.add_widget(self.button3)
        self.blankspace2 = Label()        
        Payment_Box.add_widget(self.blankspace2)  
             
        # 'Suggestions' boxlayout/column
        self.title3 = Label(text='Suggestions', font_size = 63, size_hint=(1,.30), halign='center')   
        Suggested_Products_Box.add_widget(self.title3)             
        self.label3 = Label(font_size=30, size_hint=(1,.2), halign='center')
        Suggested_Products_Box.add_widget(self.label3)
        self.label4 = Label(font_size=30, size_hint=(1,.2), halign='center')
        Suggested_Products_Box.add_widget(self.label4)        
        self.label5 = Label(font_size=30, size_hint=(1,.2), halign='center')
        Suggested_Products_Box.add_widget(self.label5)
        self.button4 = Button(font_size=30, size_hint=(1,.2), halign='center', background_color = (0,1,0,1))
        self.button4.bind(on_press=self.More_Purchases_Button)        
        Suggested_Products_Box.add_widget(self.button4)   
        self.blankspace3 = Label()        
        Suggested_Products_Box.add_widget(self.blankspace3)            
        
        # 'Super_Box' boxlayout/column
        Super_Box = BoxLayout(orientation='horizontal')
        Super_Box.add_widget(User_Input_Box)
        Super_Box.add_widget(Payment_Box)
        Super_Box.add_widget(Suggested_Products_Box) 
        
        # return 'Super_Box' boxlayout/column as final GUI
        return Super_Box

    # 'Choose_Item' boxlayout/column button 1
    def Product_Input_Button(self,button):
        
        # remove first row in 'Inventory.csv' b/c it is titles
        MyApp.product_titles = MyApp.product_inventory.pop(0)
        
        # initialize a list of available products
        # [0] is the product name
        for product in MyApp.product_inventory:
            MyApp.listed_products.append(product.split(',')[0])
            
        # if statement to check if the product the user enetered
        # is an available product
        if str(self.textinput1.text) in MyApp.listed_products:
            
            # convert list to Product Object
            MyApp.product_index = MyApp.listed_products.index(str(self.textinput1.text))
            MyApp.user_product = Product(MyApp.product_inventory[MyApp.product_index])            
            
            # if statement to check if selected prduct is in stock
            if MyApp.user_product.get_units() > 0:
                
                self.label1.text = 'Valid, please continue to Payment'
                self.label2.text = ( 
                                     f'Please pay ${MyApp.user_product.get_price()} '  
                                     f'for {MyApp.user_product.get_name()}'
                                   )
                
            # else statement if selected product is out of stock    
            else:
                self.label1.text = 'Out of stock!'
                self.textinput1.text = ''
                MyApp.product_inventory.insert(0, MyApp.product_titles)
                
        # else statement if the product the user entered is not 
        # an available product        
        else:
            self.label1.text = 'Invalid!'
            self.textinput1.text = ''
            MyApp.product_inventory.insert(0, MyApp.product_titles)

    # 'Payment' boxlayout/column button 1         
    def Payment_Input_Button(self, button):
        
        # if statement to check if the denomination the user entered is valid
        if str(self.textinput2.text) in MyApp.money_denominations:
            
            # update 'amount_paid' and 'amount_needed' variables
            MyApp.user_product.set_amount_paid(int(self.textinput2.text))
            MyApp.user_product.set_amount_needed(int(self.textinput2.text))
            
            # user must enter denominations until the 'amount_paid' variable
            # exceeds the product's price
            if MyApp.user_product.get_amount_paid() < MyApp.user_product.get_price():          
                self.label2.text = (
                                     f'Please pay ${MyApp.user_product.get_amount_needed()} '
                                     f'for {MyApp.user_product.name}'
                                   )
                
            # else if 'amount_paid' exceeds 'amount_needed'    
            else:
                self.label2.text = "Press 'Finished Paying' button"
                
        # else if the denomination the user entered is invalid
        else:
            self.label2.text = 'Invalid!'
            
        # clears textinput box so user can enter additional denominations
        self.textinput2.text = ''
        
            
    # 'Payment' boxlayout/column button 2
    def Payment_Finished_Button(self, button):
        
        # if the user presses the 'Finished Paying' Button
        # but 'amount_paid' does not exceed the product's price
        if MyApp.user_product.get_amount_needed() > 0:
            self.label2.text = 'Insufficient Funds!'
        
        # else if the user enters enough money to purchase product
        else:
            
            # compute and print change
            change_due = MyApp.user_product.get_amount_paid() - MyApp.user_product.get_price()
            self.label2.text = f'Your change is ${change_due}'
            
            # call 'make_transaction' to update stock balance
            MyApp.user_product.make_transaction()
            
            # convert the Product Object to string in preperation
            # for external file writeout
            product_index = MyApp.listed_products.index(str(self.textinput1.text))
            MyApp.product_inventory[product_index] = MyApp.user_product.convert_to_string()
            MyApp.product_inventory.insert(0, MyApp.product_titles)
            
            # call 'make_recommendation' and retrieve suggested products
            MyApp.suggested_products = make_recommendation(MyApp.product_inventory, MyApp.user_product.get_category(), MyApp.user_product.get_name())
            self.label3.text = MyApp.suggested_products[0]      
            self.label4.text = MyApp.suggested_products[1]
            self.label5.text = MyApp.suggested_products[2]   
            
            # write out to 'Inventory.csv' the updated stock balance 
            # of the purchased product 
            write_inventory_to_file(MyApp.product_inventory, MyApp.file_name) 
            
            # initialize button with text
            self.button4.text = 'Buy More'
            
    # 'Suggestions' boxlayout/column button 1        
    def More_Purchases_Button(self,button):
        
        # clears all existing textinputs and labels
            self.label1.text = 'Please enter an item to purchase'
            self.label2.text = ''            
            self.label3.text = ''    
            self.label4.text = ''
            self.label5.text = ''              
            self.textinput1.text = ''
            self.textinput2.text = ''     
#%% run app
            
if __name__ == "__main__":
    MyApp().run()
    
#%%