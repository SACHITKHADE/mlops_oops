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
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()
obj=chatbook()