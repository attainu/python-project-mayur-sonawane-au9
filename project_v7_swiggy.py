print("\n" * 5)                                           
import threading                            # to process the multiple task
import time                                 # used for decrementing processing capacity after a defined period of time
restaurent_dict = {"HOTEL THE TAJ":0, "THE HERITAGE":0, "JW CAFE":0,"BOMBAY DHABA":0,"ABBC":0}  #dict for restaurant name and processing capacity

def mainMenu():                              
    while True:
        print("\n")
        print("#"*35,"WELCOME TO SWIGGY","#"*35)
        print("\n"*2)
        print("#"*39,"MAIN MENU","#"*39)     #Design for Main Menu
        print("(O) ORDER FOOD" + "\n"
            "(J) JOIN SERVICES\n"
            "(E) EXIT\n")
        print("-"*89)
        mm_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
        if (mm_input == "O"):
            orderFood()                      #Calling orderFood() function
            break
        elif (mm_input == "J"):
            joinServices()                   #Calling joinServices()
            break
        elif (mm_input == "E"):
            print("#"*39,"THANK YOU","#"*39)        
            exit()                           #exiting main function and terminating the code
            break
        else:
            print("\n" + "ERROR: Invalid Input (" + str(mm_input) + "). Try again!")            #Invalid input

def orderFood():                            #Order food menu
    while True:
        print("\n"*1)
        print("#"*39,"ORDER FOOD","#"*39)
        print("PLEASE SELECT THE RESTAURENT OF YOUR CHOICE FROM BELOW OPTIONS: \n")
        for i in range (0,len(restaurent_dict)):            #itterating over the restaurants names with referrence to count
            print("(",i+1,")"," ",(list(restaurent_dict.keys())[i]),sep='')   #converting restaurant names into list and printing them along with count which increases with each itteration         
            print()
        print()
        print("(M) BACK TO MAIN MENU","\t"*5,"(S) SEARCH FOR DISH / RESTAURENT")
        print("-"*89)
        of_input = input("PLEASE SELECT YOUR OPERATION: ")      #input for operation to be performed in orderFood function
        num_input_check = []
        if of_input.upper() == "M":
            mainMenu()                                      #calling mainMenu function and breaking the current function loop
            break
        elif of_input.upper() == "S":
            search_Menu()                                   #calling search_Menu() function and breaking the current function loop
            break    
        elif of_input != "M" or of_input != "S":
            for i in of_input:
                if ord(i) >= 48 and ord(i) <= 57:           #checking for the input whether integer or not
                    num_input_check.append("True")
                else:
                    num_input_check.append("False")
        if "False" in num_input_check:
            print("\n" + "ERROR: Invalid Input (",of_input,"). Try again!",sep='')
        else:
            of_input = int(of_input)
            if of_input <= len(restaurent_dict): 
                restaurent_Menu(list(restaurent_dict.keys())[of_input-1])          #Calling restaurant_Menu function with argument as user defined restaurant name and breaking the current function loop
                break       
            else:
                print("\n" + "ERROR: Invalid Input (",of_input,"). Try again!",sep='')

auth = {"HOTEL THE TAJ" : {"mayur":123},\
    "THE HERITAGE" : {"manasa":123},\
    "JW CAFE" : {"chandra":123},\
    "BOMBAY DHABA" : {"amit":123},\
    "ABBC" : {"rakesh":123}}                                #dict ot maintain the records of username and password with reference to restaurant name

menu_restaurent = {
    "HOTEL THE TAJ" : {"CEASER SALAD":835, "SPAGHETTI   ":940, "ROAST CHICKEN": 850,\
    "RISOTTO       ":885, "LAMPRAISE   ":985},\
    "THE HERITAGE" : {"CLUB SANDWICH" : 350,"PANEER TIKKA" : 370, "ROAST CHICKEN" : 450,\
    "GRILLED PANEER" : 390, "BUTTER CHICKEN" : 540},\
    "JW CAFE" : {"SOUPS         ":695, "BURGER      ":650, "SPAGHETTI   ":1150, "MAKI ROLLS  ":1095,\
    "CLUB SANDWICH":750},\
    "BOMBAY DHABA" : {"VEG PLATTER  ":1190, "ROAST CHICKEN":560, "PANEER TIKKA":350, "SOYA CHAAP    ":850,\
    "CHICKEN LOLLIPOP":350},\
    "ABBC" : {"SAMPLE 1    ": 50, "SAMPLE 2    ":55}        #dict to maintain the records of food_item and food_price with reference to restaurant name
}

def restaurent_Menu(res):
    if restaurent_dict[res] > 2:                            #it will check for the processing capacity of that particualr restaurant in restaurant_dict
        print("SORRY WE ARE CURRENTLY NOT ACCEPTING ANY ORDERS FOR THIS RESTAURENT!")
        orderFood()                                         #if the processing capacity is greater than 2, than it wont accept further orders untill processing capacity decreases
    else:
        dish_input_food_list = []                           #for appending only user defined food_item names
        dish_input_price_list = []                          #for appending only user defined food_item prices
        dish_quantity_list = []                             #for keeping the count of every dish selected by user
        while True:
            print("\n"*2)
            print("#"*34,"MENU OF",res,"#"*34)
            print("\n"*2)
            if res in menu_restaurent:
                print("ITEMS","\t"*9,"PRICE")
                print("-"*89)
                i = 0
                for k,v in menu_restaurent[res].items():
                    i += 1
                    print("(",i,")"," ",k,"\t"*7,v,sep="")      #print menu of the restaurent
                print("-"*89)
                print("(V) VIEW CART","\t"*7,"(B) BACK TO ORDER FOOD PAGE")
                print("-"*89)
                dish_input = input("PLEASE SELECT DISH OF YOUR CHOICE: ")
            num_input_check = []
            if dish_input.upper() == "B":
                orderFood()                                     # gets u back to previous menu
                break
            elif dish_input.upper() == "V":
                print("\n"*2)
                print("#"*39,"YOUR CART","#"*39)
                if dish_input_food_list != [] and dish_input_price_list != [] and dish_quantity_list != []:     #if all the list are empty at initial stage then it wont call the cart function
                    cart(dish_input_food_list,dish_input_price_list, dish_quantity_list,res)
                    break
                else:                                           # when cart is empty
                    print("\n"*2)
                    print("\t"*4,"YOUR CART IS EMPTY!!")
                    continue
            elif dish_input != "V" or dish_input != "B":
                for i in dish_input:
                    if ord(i) >= 48 and ord(i) <= 57:           # when input is not either V nor B then it will check if the number is integer
                        num_input_check.append("True")
                    else:
                        num_input_check.append("False")
                if "False" in num_input_check:
                    print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='') #displays error if input is not a number nor either V or B
                else:
                    food_and_price_list = []                    # created a list to add food_item name and food_item price
                    dish_input = int(dish_input)
                    if dish_input <= len(menu_restaurent[res].items()):
                        try:
                            dish_quantity = int(input("PLEASE SELECT THE QUANTITY FOR THE DISH SELECTED: "))
                            dish_quantity_list.append(dish_quantity)
                        except Exception:
                            print("\n" + "ERROR: Invalid Input. Try again!")
                            continue
                        print("\n"*2)
                        for food,price in menu_restaurent[res].items():
                            food_and_price_list.append(food)        #appending the food_item name to the list above defined
                            food_and_price_list.append(price)       #appending the food_item price to the list above defined
                        dish_input_food_list.append(food_and_price_list[(dish_input)*2-2])  #now appending the exact user defined food name from the list to another list
                        dish_input_price_list.append(food_and_price_list[dish_input*2-1])   #now appending the exact user defined food price from the list to another list
                        print("#"*34,"TEST","#"*34)
                        print("\n"*2)     
                    else:
                        print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
            else:
                print("\n" + "ERROR: Invalid Input (",dish_input,"). Try again!",sep='')
                


def cart(dish_input_food_list,dish_input_price_list,dish_quantity_list,res):
    while True:
        total_price = []
        j = 0
        while j < len(dish_input_price_list):
            total_price.append((dish_quantity_list[j])*(dish_input_price_list[j]))      #will append the (dish price x dish quantity) value in the total price list above
            j += 1
        print("\n")
        print("-"*89)
        print("ITEMS","\t"*5,"QUANTITY","\t"*4,"PRICE")
        print("-"*89)
        i = 0
        sr_no = 1
        while i < len(dish_input_food_list):
            print("(",sr_no,")"," ",dish_input_food_list[i],"\t","*","\t"*2, dish_quantity_list[i],\
                "\t"*5,total_price[i],sep="")
            i += 1
            sr_no += 1
        print("-"*89)
        print("TOTAL","\t"*10,sum(total_price))                 #will display the total of the whole cart amount
        if sum(total_price) >= 3500:
            print("DISCOUNT RECEIVED","\t"*3,"15%","\t"*5,"-",(15*(sum(total_price))/100),sep="")
            discount_total_price = float(sum(total_price)) - (15*(sum(total_price))/100)        #created a check if the total cart amount is more than 3500 then it will calculate 15% discount on whole amount
            print("TOTAL","\t"*10,(discount_total_price))
        print("-"*89)
        print("(P) PAYMENT","\t"*8,"(B) BACK TO MENU")
        print("-"*89)    
        cart_input = input("PLEASE SELECT YOUR OPERATION: ")
        if cart_input.upper() == "B":
            restaurent_Menu(res)                                #take your back to the previous menu
            break
        elif cart_input.upper() == "P":
            payment(res)                          #take you to the payment option menu
            break
        else:
            print("\n" + "ERROR: Invalid Input (",cart_input,"). Try again!",sep='')


def payment(res):
    while True:
        print("\n")
        print("#"*39,"PAYMENT","#"*39)
        print("\n")
        print("SR NO","\t"*2,"MODES OF PAYMENT")   #Displays the list of payment modes
        print("-"*89)
        print("(1)","\t"*2,"CREDIT CARD")
        print("(2)","\t"*2,"DEBIT CARD")
        print("(3)","\t"*2,"NET BANKING")
        print("(4)","\t"*2,"UPI PAYMENT")
        print("-"*89)
        print("(C)","\t"*2,"CANCEL PAYMENT")
        print("-"*89)
        payment_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
        if payment_input == "C":
            restaurent_Menu(res)
            break
        elif payment_input == "1" or payment_input == "2" or payment_input == "3" or payment_input == "4":
            restaurent_dict[res] += 1              # here the processing capacity count is incremented for the particular restaurant in restaurant_dict
            payment_Status(res)
            break
        else:
            print("\n" + "ERROR: Invalid Input (",payment_input,"). Try again!",sep='')

queueList = []                                     # queue list will maintain list of thread with reference to the restaurent

def payment_Status(res):
    while True:
        print("\n")
        print("#"*39,"PAYMENT STATUS","#"*39)
        print("\n"*3)
        print("\t"*4,"PAYMENT SUCCESSFUL")
        print("\n"*3)
        print("-"*89)
        print("(M)","\t","BACK TO MAIN MENU")
        print("-"*89)
        def endHotelProcess(res):                       #process of each thread with reference to each restaurant
            while(restaurent_dict[res]!=0):         
                time.sleep(30)                          #processing capacity count will decrement after very 30 sec, unless the count = 0
                restaurent_dict[res] -= 1
        t1 = threading.Thread(target=endHotelProcess,args=(res,))           #thread created for the process(endHotelProcess) 
        queueList.append(t1)                            #appending the thread to queueList
        queueList[-1].start()                           #starting the thread in the queueList
        payment_Status_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
        if payment_Status_input == "M":
            mainMenu()                                  #getting back to mainMenu
            break
        else:
            print("\n" + "ERROR: Invalid Input (",payment_Status_input,"). Try again!",sep='')

def joinServices():
    while True:
        print("\n")
        print("#"*35,"JOIN OUR SERVICES","#"*35)
        print("\n")
        print("-"*89)
        print("(1) NEW USER")
        print("(2) EXSISTING USER")
        print("\n"*2)
        print("-"*89)
        print("(M) BACK TO MAIN MENU")
        print("-"*89)
        joinServices_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
        if joinServices_input == "M":
            mainMenu()
            break
        elif joinServices_input == "1":
            new_User()                      # will call the new_User function which will ask for registration process
            break
        elif joinServices_input == "2":
            exsisting_User()                # will call exisiting_User function which will ask for authentication
            break
        else:
            print("\n" + "ERROR: Invalid Input (",joinServices_input,"). Try again!",sep='')

def new_User():
    while True:
        print("\n")
        print("#"*32,"COMPLETE YOUR REGISTRATION PROCESS","#"*32)
        print("\n")
        print("-"*89)
        print("(J) BACK TO JOIN SERVICES PAGE")
        print("-"*89)
        new_user_id = input("PLEASE ENTER YOUR USERNAME: ")
        new_user_pwd = int(input("PLEASE ENTER YOUR PASSWORD: "))
        new_user_restaurant = input("PLEASE ENTER NAME OF YOUR RESTAURANT OR OPERATION TO BE PERFORMED: ").upper()       
        if new_user_restaurant == "J":
            joinServices()              #if user wants to go back to previosu menu
            break
        elif new_user_restaurant not in restaurent_dict:        # will check and proceed only if the entered restaurent already esist in dict
            id_pwd = {}
            id_pwd.setdefault(new_user_id,new_user_pwd)
            auth[new_user_restaurant] = id_pwd                  #have added new restaurent name along with usename and passwordas its value in auth_Dict
            restaurent_dict[new_user_restaurant] = 0
            dish_price = {}
            while True:                  # this loop will keep on asking user about the dish to be added in menu
                dish = (input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
                price = int(input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
                print("-"*89)
                print("(A) ADD MORE ITEMS","\t"*7,"(D) DONE ADDING ITEMS")
                new_user_add_menu = input("PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
                dish_price.setdefault(dish,price)
                menu_restaurent[new_user_restaurant] = dish_price
                if new_user_add_menu == "D":        #if user is done with adding items, he will be directed to main menu then
                    print("\n"*2)
                    print("\t"*3,"DETAILS ADDED SUCCESSFULLY!!")
                    print("\n"*2)
                    mainMenu()
                    break
                elif new_user_add_menu != "A":      #if any other input other than D or A then it will display error and the loop will run again
                    print("PLEASE ENTER VALID INPUT!!")        
        elif new_user_restaurant in restaurent_dict:
            print("THE ENTERED RESTAURANT NAME ",new_user_restaurant," ALREADY EXSIST")
        else:
            print("\n" + "ERROR: Invalid Input (",new_user_restaurant,"). Try again!",sep='')

        
def exsisting_User():
    while True:
        print("\n"*2)
        print("#"*32,"WELCOME TO SWIGGY SERVICES","#"*32)
        print("\n"*3)
        print("-"*89)
        print("(T) TRY AGAIN","\t"*4,"(M) BACK TO MAIN MENU")
        print("-"*89)
        exsisting_user_id = input("PLEASE ENTER USERNAME: ")
        exsisting_user_pwd = int(input("PLEASE ENTER PASSWORD: "))
        # exsisting_user_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ")
        for k,v in auth.items():
            if exsisting_user_id in v and exsisting_user_pwd in v.values():     #check if the username and password in auth_dict
                update_Menu(k)
                break
        print("\n" + "ERROR: Incorrect Username or Password entered. Try again!",sep='')
        print("-"*89)
        exsisting_user_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()   #if user want to go back hence taking another input
        if exsisting_user_input == "M":
            mainMenu()              #back to main menu
            break
        elif exsisting_user_input == "T":
            continue
        else:
            print("\n" + "ERROR: Invalid Input (",exsisting_user_input,"). Try again!",sep='')



def update_Menu(k):
    while True:
        if k in menu_restaurent:
            print("#"*35,"MENU OF",k,"#"*35)
            print("\n")
            print("-"*89)
            print("ITEMS","\t"*9,"PRICE")
            print("-"*89)
            i = 0
            for r,v in menu_restaurent[k].items():      # itterate over food_name and food_price with reference to restaurant name(k)
                i += 1
                print("(",i,")"," ",r,"\t"*7,v,sep="")      #displays menu of restaurant k
            print("-"*89)
            print("(A) ADD NEW DISH","\t"*2,"(M) BACK TO MAIN MENU","\t"*2,"(R) REMOVE DISH")
            print("-"*89)
            update_menu_input = input("PLEASE ENTER DISH NAME TO BE UPDATED OR SELECT ANY OPERATION TO BE PERFORMED: ").upper()                      
            if update_menu_input in menu_restaurent[k]:
                price = input("PLEASE ENTER THE NEW PRICE: ")
                menu_restaurent[k][update_menu_input]=price     #updates the price of the dish which is alreayd present in menu
            elif update_menu_input == "M":
                mainMenu()                              # back to main menu
                break
            elif update_menu_input == "A":
                add_Dish(k)                             # for adding new dish
                break
            elif update_menu_input == "R":
                remove_Dish(k)                          # for removing existing dish
                break
            else:
                print("\n" + "ERROR: Invalid Input (",update_menu_input,"). Try again!",sep='')
        else:
            print("\n" + "ERROR: Incorrect Username or Password entered. Try again!",sep='')


def add_Dish(k):
    while True:
        print("\n")
        print("#"*20,"PLEASE ENTER DETAILS OF YOUR DISH TO BE ADDED","#"*20)
        print("\n"*2)
        print("-"*89)
        dish = (input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
        price = int(input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
        if dish not in menu_restaurent[k]:                  #check if the input dish name is in menu
            menu_restaurent[k][dish]=price
        print("-"*89)
        print("(A) ADD MORE ITEMS","\t"*6,"(D) DONE ADDING ITEMS")
        add_dish_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
        if add_dish_input == "D":                       # will end the current function loop and take back to main menu once all dishes are added
            print("\n"*2)
            print("\t"*3,"DETAILS ADDED SUCCESSFULLY!!")
            print("\n"*2)
            update_Menu(k)
            break
        elif add_dish_input != "A":                     # unless user dont select either of valid inputs A or D, the loop will run continously
            print("PLEASE ENTER VALID INPUT!!")

def remove_Dish(k):
    while True:
        print("\n")
        print("#"*20,"PLEASE ENTER NAME OF THE DISH TO BE REMOVED","#"*20)
        print("\n"*2)
        print("-"*89)
        print("(T) TRY AGAIN","\t"*5,"(B) BACK TO UPDATE MENU PAGE")
        print("-"*89)
        dish = (input("PLEASE ENTER YOUR DISH NAME TO BE REMOVED: ").upper())
        if dish in menu_restaurent[k]:                  #check if the dish is present in menu
            del menu_restaurent[k][dish]                # deleted the dish from the menu
            update_Menu(k)                              # going back to previous menu
            break
        else:
            print("\n" + "ERROR: (",dish,"). not found in Menu. Try again!",sep='')
        print("-"*89)
        remove_dish_input = input("ENTER OPERATION TO BE PERFORMED: ").upper()
        if remove_dish_input == "B":                    # if user wishes to go back to previous menu without removing any dish
            update_Menu(k)
            break
        elif remove_dish_input != "T":                  
            print("\n" + "ERROR: Invalid Input (",remove_dish_input,"). Try again!",sep='')

def search_Menu():
    l = []
    flag = 0
    while True:
        print("\n")
        print("#"*35,"SEARCH MENU","#"*35)
        print("\n"*2)
        print("-"*89)
        print("(B) BACK TO ORDER FOOD PAGE")
        print("-"*89)
        dish = (input("PLEASE ENTER DISH NAME : ").upper())
        sr_no = 1
        for i,j in menu_restaurent.items():
            for k,v in j.items():               #for dish and price in restaurant
                if k.startswith(dish):          # if dish starts with user input
                    print("\n")
                    print("-"*89)
                    print("(",sr_no,")"," ",i,sep="")
                    sr_no += 1
                    flag += 1
                    l.append(i)
                    print("DISH NAME: ",k,"\t"*6,"PRICE: ",v)
                    print("-"*89)
        if flag == 0:
            print("\n" + "ENTERED DISH (",dish,") NOT FOUND. TRY AGAIN!",sep='')
            continue  
        else:                  
            while True:                              #loop will run again until user inputs valid option
                try:                                  # exceptional error handling for if the input entered is not integer
                    search_menu_input = input("PLEASE SELECT RESTAURANT: ")
                    search_menu_input = int(search_menu_input)
                    break
                except ValueError:
                    print("NO VALID INPUT!! PLEASE TRY AGAIN ...")
            if l != []:
                try:                                  
                    restaurent_Menu(l[search_menu_input-1])     # if list of the search result is not empty, this will call restaurent_Menu function with reference to user defined choice
                    break
                except IndexError:
                    print("NO VALID INPUT!! PLEASE TRY AGAIN ...")
                    search_Menu() 
                    break
            else:
                print("\n" + "ENTERED DISH (",dish,") NOT FOUND. TRY AGAIN!",sep='')
        
if __name__ == "__main__":
    mainMenu()
