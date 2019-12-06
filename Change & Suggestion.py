

#change = abs(round(price,2))


if coins > price:
    change = price - coins
    print("Your change due is $", change)
    
def suggest(item):
    if item == "T-shirt":
        suggestion = input("Would you like to buy a jacket?")
        if suggestion = "Yes":
            jacket_stock -= 1
            color = input("What color would you like?")
            size = input("What size would you like?")
            coins = input("Please enter how you will pay for the item")
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
        elif suggestion = "No":
            print("Thank you for your purchase")


    if item == "Hat":
        suggestion = input("Would you like to buy a scarf?")
        if suggestion == "Yes":
            scarf_stock -= 1
            color = input("What color would you like?")
            size = input("What size would you like?")
            coins = input("Please enter how you will pay for the item")
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

        elif suggestion == "No":
            print("Thank you for your purchase")
    
