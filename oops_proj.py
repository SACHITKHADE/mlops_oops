class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin= False
        self.menu()
    def menu(self):
        user_input=input('''welcome to the chatbot || please select the option you want to proceed with.
                         1. press 1 for signUP
                         2. press 2 for signIN
                         3. press 3 for writing a post
                         4. press 4 for messaging a friend
                         5. Any key to exit ''')
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()
    def signup(self):
        email=input("enter your email ID here->")
        pwd=input("enter your password here->")
        self.username= email
        self.password= pwd
        print("your signup has been done successfully!!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.username=='':
            print("please signup first by pressing 1 in the menu")
            self.menu()
        else:
            uname=input("enter your email adress here ->")
            pwd2=input("enter your password here -> ")
            if uname==self.username and pwd2==self.password:
                print("you have successfully signedIN  ")
                self.loggedin=True
            else:
                print("above entered credentials are wrong , plz write the correct credential")
        print("\n")
        self.menu()
            

obj=chatbook()