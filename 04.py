while True:
    user_name =input("enter your name:")
    password =input("enter your password:")
    if user_name and password=="admin":
        print("welcome",user_name)
        break
    else:
       print("username or password is wrong")
car_list = []
birth_car_list = []
while True:
    print("****menu****")
    print("1.add car name")
    print("2.show list of cars")
    print("3.add birth of car")
    print("4.show list of birth of cars")
    print("5.remove car name")
    print("6.show new list of cars")
    print("0.exit")
    choice = int(input("enter your choice:"))
    if choice == 1 :
        car_name= input("enter your car name:")
        car_list.append(car_name)
        print(15*"*")
    elif choice == 2 :
        print("list of your cars:", car_list)
        print(15*"*")
    elif choice == 3 :
        birth_car = int(input("enter birth of your car:"))
        birth_car_list.append(birth_car)
        print(15*"*")
    elif choice == 4 :
        print("list of  birth of your cars:", birth_car_list)
        print(15*"*")
    elif choice == 5 :
        remove_car = input("remove the car:")
        if remove_car in car_list:
            car_list.remove(remove_car)
            print("car removed successfully")
            print(15*"*")
    elif choice == 6 :
        print("your new car list:" , car_list)
        print(15*"*")
    elif choice == 0 :
        break
    else:
        print("invalid choice")



