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
                         5. Any key to exit
                         
                         ----> ''')
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.my_post()
        elif user_input=='4':
            self.send_msg()
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
    def my_post(self):
        if self.loggedin==True :
            txt=input("whats on your mind lets post it out ")
            print(f"the post has been public--->{txt}")
        else:
            print("plz signup and signin first and proceed further for chatbook exprience")
        print("\n")
        self.menu()
    def send_msg(self):
        if self.loggedin==True :
            txt=input("write the message here---> ")
            frd=input("whom do you want to send this message--->")
            print(f"message sent to--->{frd}")
        else:
            print("plz signup and signin first and proceed further for chatbook exprience")
        print("\n")
        self.menu()

#obj=chatbook()
#just remove the above commment to run this file