from code import DBHelper;


def options():
    db = DBHelper()
    while True:
        print("**********WELCOME**********")
        print( )
        print("Press 1 for insert user!")
        print("Press 2 for fetch user!")
        print("Press 3 for delete user!")
        print("Press 4 for update user!")
        print("Press 5 for exit !!")
        print( )

        print("PRESS ANY OPTION U WANT ")
        choice = int(input(  ))
        print("YOU SELECTED NUMBER  : ",choice)
        if choice==1:
            #### insert
            id= int(input("ENTER ID : "))
            name = str(input("ENTER NAME : "))
            phone = int(input("ENTER PHONE :"))

            db.insert_user(id,name,phone)
        elif choice ==2:
            # fetch user
           db.fetch_all()
        elif choice==3:
            # delete user
           id = int(input("ENTER ID "))
           db.delete_user(id)
        elif choice ==4:
            #update user
            i = int(input("ENTER ID : "))
            n = str(input("ENTER NAME : "))
            p = int(input("ENTER PHONE :"))
            db.update_user(i,n,p)
        elif choice ==5:
         break
        else:
              print("CHOOSE A VALID OPTION  : ")


options()














