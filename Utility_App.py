import os


#Welcome message
print("Welcome to the Utility Application.")

#Initializing the list of menus
balance = int(input("Please Enter you Current Balance to Proceed Further.\n"))
chocolates = [[1,'Galaxy',10,7.00],[2,'Dairymilk',10,10.00],[3,'Ferrero Rocher',10,30.00],[4,'Kitkat',10,12.00],[5,'Flake',10,14.00]]
drinks = [[1,'Hot Chocolate',10,10.00],[2,'Macha',10,12.00],[3,'Americano',10,15.00],[4,'Latte',10,12.00],[5,'Espresso',10,10.00]]
cookies = [[1,'Chocolate Chip',10,15.00],[2,'Oatmeal Cookie',10,20.00],[3,'Macaroni Cookies',10,15.00],[4,'Biscotti',10,10.00],[5,'Sugar Cookies',10,10.00]]
is_buying = True


#Function for clear the console
def clear_console():
    os.system('clear')


#Function to Display Chocolates Menu
def show_choco_menu():
    print("Chocolates.\n")
    for choco in chocolates:
        print(choco[0], choco[1], choco[3],"AED")
    print("6 Main Menu")



#Function to Display Hot drink Menu
def show_drink_menu():
    print("Hot drink.\n")
    for drink in drinks:
        print(drink[0], drink[1], drink[3],"AED")        
    print("6 Main Menu")


#Function to Display cookies Menu
def show_cookies_menu():
    print("Cookies.\n")
    for cookie in cookies:
        print(cookie[0], cookie[1], cookie[3],"AED")        
    print("6 Main Menu")


#Function to ask User if he wants to buy cookies with hot drinks
def ask_for_cookies():
    print("Do you want to buy Cookies with Hot Drinks ?\n")
    choice = input("Enter 'Y' for yes or 'N' for no. ")

    #if user says yes then clear the console and display the cookie menu
    if(choice == "Y" or choice == "y"):
        clear_console()
        show_cookies_menu()
        buy_cookies()

    #else do nothing
    elif(choice == "N" or choice == "n"):
        pass
    else:
        print("Invalid Choice")

#Function to ask User if he wants to add money in case of lower balance
def ask_to_add_money():
    global balance
    print("Do you want to add money ?\n")
    choice = input("Enter 'Y' for yes or 'N' for no. ")

    #if user says yes than ask the amount to deposit and save it to balance variable
    if(choice == "Y" or choice == "y"):
        clear_console()
        amount = int(input("Please enter amount: \n")) 
        balance = balance + amount

    #else do nothing
    elif(choice == "N" or choice == "n"):
        pass
    else:
        print("Invalid Choice")


def buy_chocos():
    global balance #defining the scope of the balance variable so the global variable can be change in local scope
    choice = int(input("Enter a choice\n")) #ask for the input choice
    if(choice == 1):
        quantity = int(input("Enter the quantity.\n"))
        if(int(chocolates[0][3])*quantity <= balance): #if user balance is greater than the total chocolate bill i.e choco_price x quantity to buy < user balance
            if(quantity <= chocolates[1][2]): #if available quantity in stock is greater than the user demanding quantity
                chocolates[0][2] = int(chocolates[0][2]) - quantity # do minus the quantity from the choco
                balance = balance - (int(chocolates[0][3])*quantity)# do minus the bill from the user balance
                print("Quantity ",quantity)
                print("\nAmount total: ",int(chocolates[0][3])*quantity)
            else:
                print("Please enter the quantity under", chocolates[0][2])  #else demanding quantity is not availabel in stock and show error message
        else:
            print("You don't have enough balance!") #else user don't have enough balance so ask to add money
            ask_to_add_money() # ask to add more money
    elif(choice == 2):
        quantity = int(input("Enter the quantity.\n"))
        if(int(chocolates[1][3])*quantity <= balance):
            if(quantity <= chocolates[1][2]):
                chocolates[1][2] = int(chocolates[1][2]) - quantity
                balance = balance - (int(chocolates[1][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(chocolates[1][3])*quantity)
            else:
                print("Please enter the quantity under", chocolates[1][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 3):
        quantity = int(input("Enter the quantity.\n"))
        if(int(chocolates[2][3])*quantity <= balance):
            if(quantity <= chocolates[2][2]):
                chocolates[2][2] = int(chocolates[2][2]) - quantity
                balance = balance - (int(chocolates[2][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(chocolates[2][3])*quantity)
            else:
                print("Please enter the quantity under", chocolates[2][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 4):
        quantity = int(input("Enter the quantity.\n"))
        if(int(chocolates[3][3])*quantity <= balance):
            if(quantity <= chocolates[3][2]):
                chocolates[3][2] = int(chocolates[3][2]) - quantity
                balance = balance - (int(chocolates[3][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(chocolates[3][3])*quantity)
            else:
                print("Please enter the quantity under", chocolates[3][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 5):
        quantity = int(input("Enter the quantity.\n"))
        if(int(chocolates[4][3])*quantity <= balance):
            if(quantity <= chocolates[4][2]):
                chocolates[4][2] = int(chocolates[4][2]) - quantity
                balance = balance - (int(chocolates[4][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(chocolates[4][3])*quantity)
            else:
                print("Please enter the quantity under", chocolates[4][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 6):
        pass
    else:
        print("Invalid choice!")

def buy_drink():
    global balance  #defining the scope of the balance variable so the global variable can be change in local scope
    choice = int(input("Enter a choice\n")) #ask for the input choice
    if(choice == 1):
        quantity = int(input("Enter the quantity.\n"))
        if(int(drinks[0][3])*quantity <= balance): #if user balance is greater than the total drinks bill i.e drink_price x quantity to buy < user balance
            if(quantity <= drinks[0][2]):  #if available quantity in stock is greater than the user demanding quantity
                drinks[0][2] = int(drinks[0][2]) - quantity # do minus the quantity from the drinks
                balance = balance - (int(drinks[0][3])*quantity) # do minus the bill from the user balance
                print("Quantity ",quantity) 
                print("\nAmount total: ",int(drinks[0][3])*quantity)
            else:
                print("Please enter the quantity under", drinks[0][2]) #else demanding quantity is not availabel in stock and show error message
        else:
            print("You don't have enough balance!") #else user don't have enough balance so ask to add money
            ask_to_add_money() # ask to add more money
    elif(choice == 2):
        quantity = int(input("Enter the quantity.\n"))
        if(int(drinks[1][3])*quantity <= balance):
            if(quantity <= drinks[1][2]):
                drinks[1][2] = int(drinks[1][2]) - quantity
                balance = balance - (int(drinks[1][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(drinks[1][3])*quantity)
            else:
                print("Please enter the quantity under", drinks[1][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 3):
        quantity = int(input("Enter the quantity.\n"))
        if(int(drinks[2][3])*quantity <= balance):
            if(quantity <= drinks[2][2]):
                drinks[2][2] = int(drinks[2][2]) - quantity
                balance = balance - (int(drinks[2][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(drinks[2][3])*quantity)
            else:
                print("Please enter the quantity under", drinks[2][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 4):
        quantity = int(input("Enter the quantity.\n"))
        if(int(drinks[3][3])*quantity <= balance):
            if(quantity <= drinks[3][2]):
                drinks[3][2] = int(drinks[3][2]) - quantity
                balance = balance - (int(drinks[3][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(drinks[3][3])*quantity)
            else:
                print("Please enter the quantity under", drinks[3][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 5):
        quantity = int(input("Enter the quantity.\n"))
        if(int(drinks[4][3])*quantity <= balance):
            if(quantity <= drinks[4][2]):
                drinks[4][2] = int(drinks[4][2]) - quantity
                balance = balance - (int(drinks[4][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(drinks[4][3])*quantity)
            else:
                print("Please enter the quantity under", drinks[4][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 6):
        pass
    else:
        ("Invalid choice!")


def buy_cookies():
    global balance #defining the scope of the balance variable so the global variable can be change in local scope
    choice = int(input("Enter a choice\n")) #ask for the input choice
    if(choice == 1):
        quantity = int(input("Enter the quantity.\n"))
        if(int(cookies[0][3])*quantity <= balance): #if user balance is greater than the total cookies bill i.e cookies_price x quantity to buy < user balance
            if(quantity <= cookies[1][2]): #if available quantity in stock is greater than the user demanding quantity
                cookies[0][2] = int(cookies[0][2]) - quantity # do minus the quantity from the cookies
                balance = balance - (int(cookies[0][3])*quantity) # do minus the bill from the user balance
                print("Quantity ",quantity)
                print("\nAmount total: ",int(cookies[0][3])*quantity)
            else:
                print("Please enter the quantity under", cookies[0][2]) #else demanding quantity is not availabel in stock and show error message
        else:
            print("You don't have enough balance!") #else user don't have enough balance so ask to add money
            ask_to_add_money() # ask to add more money
            
    elif(choice == 2):
        quantity = int(input("Enter the quantity.\n"))
        if(int(cookies[1][3])*quantity <= balance):
            if(quantity <= cookies[1][2]):
                cookies[1][2] = int(cookies[1][2]) - quantity
                balance = balance - (int(cookies[1][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(cookies[1][3])*quantity)
            else:
                print("Please enter the quantity under", cookies[1][2])
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
            
    elif(choice == 3):
        quantity = int(input("Enter the quantity.\n"))
        if(int(cookies[2][3])*quantity <= balance):
            if(quantity <= cookies[2][2]):
                cookies[2][2] = int(cookies[2][2]) - quantity
                balance = balance - (int(cookies[2][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(cookies[2][3])*quantity)
            else:
                print("Please enter the quantity under", cookies[2][2])               
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 4):
        quantity = int(input("Enter the quantity.\n"))
        if(int(cookies[3][3])*quantity <= balance):
            if(quantity <= cookies[3][2]):
                cookies[3][2] = int(cookies[3][2]) - quantity
                balance = balance - (int(cookies[3][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(cookies[3][3])*quantity)
            else:
                print("Please enter the quantity under", cookies[3][2])               
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 5):
        quantity = int(input("Enter the quantity.\n"))
        if(int(cookies[4][3])*quantity <= balance):
            if(quantity <= cookies[4][2]):
                cookies[4][2] = int(cookies[4][2]) - quantity
                balance = balance - (int(cookies[4][3])*quantity)
                print("Quantity ",quantity)
                print("\nAmount total: ",int(cookies[4][3])*quantity)
            else:
                print("Please enter the quantity under", cookies[2][2])               
        else:
            print("You don't have enough balance!")
            ask_to_add_money()
    elif(choice == 6):
        pass
    else:
        print("Invalid choice!")
        


while(is_buying):
    print("What would you like to buy please enter a choice.\n")
    print("Current available balance: ", balance)
    choice = int(input("\n1: Chocolates     2:Hot drink    6: Exit\n"))


    if(choice == 1):
        clear_console()
        show_choco_menu()
        buy_chocos()        
    elif(choice == 2):
        clear_console()
        show_drink_menu()
        buy_drink()
        ask_for_cookies()
    elif(choice == 6):
        exit()
    else:
        print("Invalid choice!")
