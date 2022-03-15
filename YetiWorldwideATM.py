# Start of Yeti ATM GUI Tkinter Code
import tkinter as tk  # python 3
# Imports the Time for the Program
import time
#Holds the Current Balance for the ATM User Account
current_balance=20000


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Containers
        self.shared_data={'Balance':tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Frames to present all Pages
        self.frames = {}
        for F in (LoginPage, ATMMenu, BalanceSlide, DepositSlide, WithdrawSlide):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    # Adds frame on the container frame
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# User Login Page
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#476b6b')
        self.controller = controller

        self.controller.title('Yeti World Wide ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,
                                  tk.PhotoImage(file='yeti.png'))

        # Yeti Worldwide ATM Header Text
        headinglabel = tk.Label(self,
                                 text='YETI WORLD WIDE ATM',
                                 font=('antarctica', 48, 'bold'),
                                 foreground='white',
                                 background='#476b6b')
        headinglabel.pack(pady=20)

        space_label = tk.Label(self, height=4, bg='#476b6b')
        space_label.pack()

        # Password Label
        Pass_label = tk.Label(self,
                              text='Enter Your Secret Password',
                              font=('antarctica', 15),
                              bg='#476b6b',
                              fg='white')
        Pass_label.pack(pady=10)

        # Password entry box and allows text
        my_pass = tk.StringVar()
        Pass_entry_box = tk.Entry(self,
                                  textvariable=my_pass,
                                  font=('antarctica', 12),
                                  width=25)
        Pass_entry_box.focus_set()
        Pass_entry_box.pack(ipady=9)

        #Hide passwod while being typed in the text Box
        def hide_pass(_):
            Pass_entry_box.configure(fg='black',show='$')

        Pass_entry_box.bind('<FocusIn>',hide_pass)

        #Password an Message to Display if Password is Wrong
        def check_password():
            if my_pass.get() == 'riverwalk12':
                my_pass.set('')
                wrong_pass_label['text']=''
                controller.show_frame('ATMMenu')

            else:
                wrong_pass_label['text'] = 'Wrong Password, Please try again!'

        #Enter button to login to account
        Enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_password,
                                 relief='raised',
                                 borderwidth=3,
                                 width=31,
                                 height=3)

        Enter_button.pack(pady=5)

        #Displaying user entered Wrong Password
        wrong_pass_label = tk.Label(self,
                                    text='',
                                    font=('antarctica', 12),
                                    fg='white',
                                    bg='#3d5c5c',
                                    anchor='n')
        wrong_pass_label.pack(fill='both',expand=True)

        bottom_frame=tk.Frame(self,relief='raised', borderwidth=4)
        bottom_frame.pack(fill='x',side='bottom')

        #Visa Card Logo
        visacard_photo=tk.PhotoImage(file='visa.png')
        visacard_label=tk.Label(bottom_frame,image=visacard_photo)
        visacard_label.pack(side='left')
        visacard_label.image=visacard_photo

        #Dicover Card Logo
        discovercard_photo=tk.PhotoImage(file='discover.png')
        discovercard_label=tk.Label(bottom_frame,image=discovercard_photo)
        discovercard_label.pack(side='left')
        discovercard_label.image=discovercard_photo

        #Apple Pay Logo
        applepay_photo=tk.PhotoImage(file='apple-pay.png')
        applepay_label=tk.Label(bottom_frame,image=applepay_photo)
        applepay_label.pack(side='left')
        applepay_label.image=applepay_photo

        #American Express Logo
        americanexpress_photo=tk.PhotoImage(file='americanexpress.png')
        americanexpress_label=tk.Label(bottom_frame,image=americanexpress_photo)
        americanexpress_label.pack(side='left')
        americanexpress_label.image=americanexpress_photo

        #Clock in the Bottom Right hand corner
        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        # Time table to present time at the Bottom Left of each Page
        time_label=tk.Label(bottom_frame,font=('antarctica,12'))
        time_label.pack(side='right')

        tick()

# YETI ATM Menu Screen
class ATMMenu(tk.Frame):
        # Page 2 of Yeti World Wide ATM

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#476b6b')
        self.controller = controller

        #Bank name heading label
        headinglabel = tk.Label(self,
                                text='YETI WORLD WIDE ATM',
                                font=('antarctica', 48, 'bold'),
                                foreground='white',
                                background='#476b6b')
        headinglabel.pack(pady=20)

        #ATM Menu Label
        atm_menu_label = tk.Label(self,
                                  text='ATM Main Menu',
                                  font=('antarctica',14,'bold'),
                                  fg='white',
                                  bg='#476b6b')
        atm_menu_label.pack()

        #Label to tell user to make there selection
        selection_label=tk.Label(self,
                                 text="Please, make your next selection",
                                 font=('antarctica', 12, 'bold'),
                                 fg='white',
                                 bg='#476b6b',
                                 anchor='c')
        selection_label.pack(fill='x',pady=25)

        #Frame for the Buttons

        button_frame=tk.Frame(self, bg='#3d5c5c')
        button_frame.pack(fill='both',expand=True)

        # Withdraw button to take you to Deposit Slide
        def withdraw():
            controller.show_frame('WithdrawSlide')

        withdraw_button=tk.Button(button_frame,
                                  text='Withdraw',
                                  command=withdraw,
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        withdraw_button.grid(row=0,column=0,pady=10)

        # Deposit button to take you to Deposit Slide
        def deposit():
            controller.show_frame('DepositSlide')

        deposit_button=tk.Button(button_frame,
                                  text='Deposit',
                                  command=deposit,
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        deposit_button.grid(row=1,column=0,pady=10)

        # Balance button to take you to the Balance Slide

        def balance():
            controller.show_frame('BalanceSlide')

        balance_button=tk.Button(button_frame,
                                  text='Balance',
                                  command=balance,
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        balance_button.grid(row=0,column=1,pady=10,padx=1100)

        #Exit button to take you to the Balance Slide

        def exit():
            controller.show_frame('LoginPage')

        exit_button=tk.Button(button_frame,
                                  text='Exit',
                                  command=exit,
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)

        exit_button.grid(row=1,column=1,pady=10)


        # Bottom Frame
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=4)
        bottom_frame.pack(fill='x', side='bottom')

        # Visa Card Logo
        visacard_photo = tk.PhotoImage(file='visa.png')
        visacard_label = tk.Label(bottom_frame, image=visacard_photo)
        visacard_label.pack(side='left')
        visacard_label.image = visacard_photo

        # Dicover Card Logo
        discovercard_photo = tk.PhotoImage(file='discover.png')
        discovercard_label = tk.Label(bottom_frame, image=discovercard_photo)
        discovercard_label.pack(side='left')
        discovercard_label.image = discovercard_photo

        # Apple Pay Logo
        applepay_photo = tk.PhotoImage(file='apple-pay.png')
        applepay_label = tk.Label(bottom_frame, image=applepay_photo)
        applepay_label.pack(side='left')
        applepay_label.image = applepay_photo

        # American Express Logo
        americanexpress_photo = tk.PhotoImage(file='americanexpress.png')
        americanexpress_label = tk.Label(bottom_frame, image=americanexpress_photo)
        americanexpress_label.pack(side='left')
        americanexpress_label.image = americanexpress_photo

        # Clock in the Bottom Right hand corner
        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        # Time table to present time at the Bottom Left of each Page

        time_label = tk.Label(bottom_frame, font=('antarctica,12'))
        time_label.pack(side='right')

        tick()

#Balance Page for checking Balance
class BalanceSlide(tk.Frame):

    # Page 3 of Yeti World Wide ATM

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#476b6b')
        self.controller = controller

        # Yeti Worldwide ATM Header
        headinglabel = tk.Label(self,
                            text='YETI WORLD WIDE ATM',
                            font=('antarctica', 48, 'bold'),
                            foreground='white',
                            background='#476b6b')
        headinglabel.pack(pady=20)

        #Current Balance
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        bal_label=tk.Label(self,
                           textvariable=controller.shared_data['Balance'],
                           font=('antarctica', 20),
                           fg='white',
                           bg='#476b6b')
        bal_label.pack(pady=10)

        #Balance Buttom Frame
        bal_button_frame=tk.Frame(self,bg='#3d5c5c')
        bal_button_frame.pack(fill='both',expand=True)

        # Button command to goto ATMMenu
        def menu():
            controller.show_frame('ATMMenu')
        atmmenu_button=tk.Button(bal_button_frame,
                                 command=menu,
                                 text='Menu',
                                 relief='raised',
                                 borderwidth=3,
                                 width=60,
                                 height=6)
        atmmenu_button.grid(row=0,column=0,pady=6)

        # Button command to goto Login Page
        def exit():
            controller.show_frame('LoginPage')

        bal_exit_button=tk.Button(bal_button_frame,
                              text='Exit',
                              command=exit,
                              relief='raised',
                              borderwidth=3,
                              width=60,
                              height=6)
        bal_exit_button.grid(row=0,column=2,pady=6,padx=1100)

        #Bottom Frame
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=4)
        bottom_frame.pack(fill='x', side='bottom')

        # Visa Card Logo
        visacard_photo = tk.PhotoImage(file='visa.png')
        visacard_label = tk.Label(bottom_frame, image=visacard_photo)
        visacard_label.pack(side='left')
        visacard_label.image = visacard_photo

        # Dicover Card Logo
        discovercard_photo = tk.PhotoImage(file='discover.png')
        discovercard_label = tk.Label(bottom_frame, image=discovercard_photo)
        discovercard_label.pack(side='left')
        discovercard_label.image = discovercard_photo

        # Apple Pay Logo
        applepay_photo = tk.PhotoImage(file='apple-pay.png')
        applepay_label = tk.Label(bottom_frame, image=applepay_photo)
        applepay_label.pack(side='left')
        applepay_label.image = applepay_photo

        # American Express Logo
        americanexpress_photo = tk.PhotoImage(file='americanexpress.png')
        americanexpress_label = tk.Label(bottom_frame, image=americanexpress_photo)
        americanexpress_label.pack(side='left')
        americanexpress_label.image = americanexpress_photo

        # Clock in the Bottom Right hand corner
        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        # Time table to present time at the Bottom Left of each Page

        time_label = tk.Label(bottom_frame, font=('antarctica,12'))
        time_label.pack(side='right')

        tick()

class WithdrawSlide(tk.Frame):
    # Page 3 of Yeti World Wide ATM

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#476b6b')
        self.controller = controller

        # Bank name heading label
        headinglabel = tk.Label(self,
                                text='YETI WORLD WIDE ATM',
                                font=('antarctica', 48, 'bold'),
                                foreground='white',
                                background='#476b6b')
        headinglabel.pack(pady=20)

        # ATM Menu Label
        select_withdraw_label = tk.Label(self,
                                  text='Select the amount you would like to withdraw',
                                  font=('antarctica', 14, 'bold'),
                                  fg='white',
                                  bg='#476b6b')
        select_withdraw_label.pack()

        # Frame for Button
        button_frame=tk.Frame(self,bg="#3d5c5c")
        button_frame.pack(fill='both',expand=True)

        #Wiithdraw command
        def withdraw(amount):
            global current_balance
            current_balance-=amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('ATMMenu')

        # Button to withdraw 20
        twenty_button=tk.Button(button_frame,
                                text='$20',
                                command=lambda:withdraw(20),
                                relief='raised',
                                borderwidth=3,
                                width=60,
                                height=6)
        twenty_button.grid(row=0,column=0,pady=10)

        #Button to withdraw 40
        forty_button = tk.Button(button_frame,
                                  text='$40',
                                  command=lambda: withdraw(40),
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        forty_button.grid(row=1, column=0, pady=10)

        # Button to withdraw 60
        sixty_button = tk.Button(button_frame,
                                 text='$60',
                                 command=lambda: withdraw(60),
                                 relief='raised',
                                 borderwidth=3,
                                 width=60,
                                 height=6)
        sixty_button.grid(row=2, column=0, pady=10)

        # Button to Withdraw 80
        eighty_button = tk.Button(button_frame,
                                 text='$80',
                                 command=lambda: withdraw(80),
                                 relief='raised',
                                 borderwidth=3,
                                 width=60,
                                 height=6)
        eighty_button.grid(row=3, column=0, pady=10)

        # Button to withdraw 100
        one_hundred_button = tk.Button(button_frame,
                                  text='$100',
                                  command=lambda: withdraw(100),
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        one_hundred_button.grid(row=0, column=1, pady=10,padx=1050)

        # Button to withdraw 200
        two_hundred_button = tk.Button(button_frame,
                                  text='$200',
                                  command=lambda: withdraw(200),
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        two_hundred_button.grid(row=1, column=1, pady=10)

        #Button to withdraw 300
        three_hundred_button = tk.Button(button_frame,
                                  text='$300',
                                  command=lambda: withdraw(300),
                                  relief='raised',
                                  borderwidth=3,
                                  width=60,
                                  height=6)
        three_hundred_button.grid(row=2, column=1, pady=10)

        def exit():
            controller.show_frame('LoginPage')

        #Exit Button to goto the Login Page
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=60,
                                height=6)
        exit_button.grid(row=3, column=1, pady=10)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,
                                    textvariable=cash,
                                    width=60,
                                    justify='right')
        other_amount_entry.grid(row=4,column=1,pady=10,ipady=20)

        #Other Amount
        other_amount_text=tk.Label(button_frame,
                                    text='Other Amount',
                                    font=('antarctica',14,'bold'),
                                    fg='white',
                                    bg="#3d5c5c")
        other_amount_text.grid(row=5,column=1,pady=10)

        #Command for Current Balance
        def other_amount(_):
            global current_balance
            current_balance -=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('ATMMenu')

        other_amount_entry.bind('<Return>',other_amount)

        #Bottom frame
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=4)
        bottom_frame.pack(fill='x', side='bottom')


        # Visa Card Logo
        visacard_photo = tk.PhotoImage(file='visa.png')
        visacard_label = tk.Label(bottom_frame, image=visacard_photo)
        visacard_label.pack(side='left')
        visacard_label.image = visacard_photo

        # Dicover Card Logo
        discovercard_photo = tk.PhotoImage(file='discover.png')
        discovercard_label = tk.Label(bottom_frame, image=discovercard_photo)
        discovercard_label.pack(side='left')
        discovercard_label.image = discovercard_photo

        # Apple Pay Logo
        applepay_photo = tk.PhotoImage(file='apple-pay.png')
        applepay_label = tk.Label(bottom_frame, image=applepay_photo)
        applepay_label.pack(side='left')
        applepay_label.image = applepay_photo

        # American Express Logo
        americanexpress_photo = tk.PhotoImage(file='americanexpress.png')
        americanexpress_label = tk.Label(bottom_frame, image=americanexpress_photo)
        americanexpress_label.pack(side='left')
        americanexpress_label.image = americanexpress_photo

        # Clock in the Bottom Right hand corner
        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        # Time table to present time at the Bottom Left of each Page

        time_label = tk.Label(bottom_frame, font=('antarctica,12'))
        time_label.pack(side='right')

        tick()

class DepositSlide(tk.Frame):
    # Page 3 of Yeti World Wide ATM

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#476b6b')
        self.controller = controller

        #Heading Label Yeti World Wide ATM
        headinglabel = tk.Label(self,
                                 text='YETI WORLD WIDE ATM',
                                 font=('antarctica', 48, 'bold'),
                                 foreground='white',
                                 background='#476b6b')
        headinglabel.pack(pady=20)

        space_label = tk.Label(self, height=4, bg='#476b6b')
        space_label.pack()

        #Deposit Amount Label
        deposit_amount_label = tk.Label(self,
                              text='Enter Your Deposit Amount Below',
                              font=('antarctica', 15),
                              bg='#476b6b',
                              fg='white')
        deposit_amount_label.pack(pady=10)

        #Command to use cash as a string
        cash=tk.StringVar()
        deposit_entry_box=tk.Entry(self,
                                   textvariable=cash,
                                   font=('antarctica'),
                                   width=25)
        deposit_entry_box.pack(ipady=10)

        #Command for Depositing Money
        def deposit_money():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('ATMMenu')
            cash.set('')
        deposit_enter=tk.Button(self,
                                text='Enter',
                                command=deposit_money,
                                relief='raised',
                                borderwidth=5,
                                width=30,
                                height=2)
        deposit_enter.pack(pady=10)

        #Color layer of the Page
        tone_label=tk.Label(self,bg='#3d5c5c')
        tone_label.pack(fill='both',expand=True)

        #Bottom Frame for Images
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=4)
        bottom_frame.pack(fill='x', side='bottom')

        # Visa Card Logo
        visacard_photo = tk.PhotoImage(file='visa.png')
        visacard_label = tk.Label(bottom_frame, image=visacard_photo)
        visacard_label.pack(side='left')
        visacard_label.image = visacard_photo

        # Dicover Card Logo
        discovercard_photo = tk.PhotoImage(file='discover.png')
        discovercard_label = tk.Label(bottom_frame, image=discovercard_photo)
        discovercard_label.pack(side='left')
        discovercard_label.image = discovercard_photo

        # Apple Pay Logo
        applepay_photo = tk.PhotoImage(file='apple-pay.png')
        applepay_label = tk.Label(bottom_frame, image=applepay_photo)
        applepay_label.pack(side='left')
        applepay_label.image = applepay_photo

        # American Express Logo
        americanexpress_photo = tk.PhotoImage(file='americanexpress.png')
        americanexpress_label = tk.Label(bottom_frame, image=americanexpress_photo)
        americanexpress_label.pack(side='left')
        americanexpress_label.image = americanexpress_photo

        # Clock in the Bottom Right hand corner
        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        # Time table to present time at the Bottom Left of each Page
        time_label = tk.Label(bottom_frame, font=('antarctica,12'))
        time_label.pack(side='right')

        tick()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()