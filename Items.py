print('The items are T-shirts, Jackets, Hats, Shorts, Backpacks, Scarves')
print("Colors Options: Orange, White, Black, Grey")
print("Size Options: Small, Medium, Large")

tshirt_stock=5
jacket_stock=5
shorts_stock=5
backpack_stock=5
hat_stock=5
scarf_stock=5



purchase_number=0
purchase_number+=1

item=input("What item would you like?")

if item=="T-shirt" or "Jackets" or "Shorts":
    color=input("What color would you like?")
    size=input("What size would you like?")
    if item== "T-shirt": 
        price=20
        tshirt_stock-= 1
    elif item == "Jacket": 
        price=25
        jacket_stock -=1
    elif item == "Shorts": 
        price=15
        shorts_stock-=1
    

if item=="Backpack" or "Hat" or "Scarf": 
    color=input("What color would you like?")
    
    if item=="Backpack": 
        price=30
        backpack_stock -= 1
    elif item=="Hat":
        price=10
        hat_stock -=1
    elif item== "Scarf": 
        price= 12
        scarf_stock -= 1
if purchase_number==5:
    price*=.75
paid=0
coins=0
while coins < price:
    coins=input("Please enter how you will pay for the item.")

    if coins=="20":
        paid+=20.00
    elif coins=="10":
        paid+= 10.00
    elif coins=="5":
        paid+=5.00
    elif coins=="1":
        paid+=1.00
    enough_answer=input('Do you have another bill?')
    
if enough_answer== 'No':
    print("Thank you for your purchase") 
    
        
    
    

    
    
    
    

    