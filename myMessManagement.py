from tkinter import *
from tkinter.ttk import Treeview,Combobox
from tkinter import ttk, scrolledtext
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import *
import sqlite3
from PIL import Image, ImageTk


class Login:
    def __init__(self, master):
        print("hello")
        self.r = master
        self.root_window_configure()
        self.login_page()
        self.login_frame()

    def login_frame(self):
        addUserLabel = Button(self.r, image=addNewUser,
                              font="Calibri 15 ",
                              bg="#1A1918",
                              fg="white",
                              bd=0,
                              command=lambda: messagebox.showinfo("Add user", "Add User Is clicked"))
        # addUserLabel.configure(color=4)
        user = StringVar()
        passwd = StringVar()
        addUserLabel.place(x=10, y=30)
        existing_user_label = Label(self.r, text='Existing User', font='algerian 17 bold underline', bg='#0F111A',
                                    fg='white')
        existing_user_label.place(x=260, y=40)
        f = Frame(self.r, height=200, width=300)
        f.configure(bg='#0F111A')
        username = Label(f, text='Username', font='calibri 15 bold ', bg='#0F111A', fg='White')
        username.place(x=0, y=0)
        username_entry = Entry(f, width=15, font='calibri 15', textvariable=user)
        username_entry.place(x=120, y=0)
        password = Label(f, text='Password', font='calibri 15 bold', bg='#0F111A', fg='white')
        password.place(x=0, y=50)
        password_entry = Entry(f, width=15, font='calibri 15', show="*", textvariable=passwd)
        password_entry.place(x=120, y=50)
        submit_button = Button(f, image=proceed, font='calibri 15 bold', bg='#0F111A', bd=0, fg='white',
                               command=lambda: Main_window(self.r),
                               cursor="hand2 ",
                               )
        submit_button.place(x=80, y=95)
        f.place(x=200, y=100)

    ''' def check_user_is_valid(self, username, password):
        conn = sqlite3.connect('mydb.db')
        db = conn.cursor()
        u = username.get()
        p = password.get()
        if u == '' or p == '':
            messagebox.showerror('Empty field', 'Username or Password cannot be left empty')
        else:
         db.execute(f"select * from user where username='{u}' and password='{p}'")
         try:
            x = db.fetchall()
            if not x:
                messagebox.showerror('Invalid', 'Wrong username and password')
            else:
                username.set("")
                password.set("")
                Main_window(self.r)
         except:
            pass '''

    def root_window_configure(self):
        height = self.r.winfo_screenheight()
        width = self.r.winfo_screenwidth()
        self.r.geometry("{}x{}+{}+{}".format(width // 3, height // 3, width // 3, height // 3))
        self.r.configure(bg='#0F111A')
        self.r.title("Mess Manager -by Sk Belal Saheb")

    def login_page(self):
        pass


class Main_window:
    def __init__(self, r1):
        # self.bg2 = "pink"
        self.bg1 = "#0F111A"
        self.bg2 = "white"
        r1.withdraw()
        self.r1 = r1
        self.r = Toplevel()
        self.r.resizable(False, False)
        self.main_window_configure()
        self.buttons()
        self.allExpenses()
        self.r.protocol("WM_DELETE_WINDOW", lambda : self.onClosing (self.r))
        self.databaseTables()

    def databaseTables(self):
        try:
            db.execute(
                "create table expenses (id INTEGER PRIMARY KEY AUTOINCREMENT,boolean int(1) NOT NULL, date date,item varchar(255), price double)")
        except:
            pass

    def reminder_closing(self, b, r1):
        r1.destroy()
        b.configure(state="normal")

    def allExpenses(self):
        bg = "#1F4649"
        frameWidth = width // 4
        frameHeight = height // 3
        r = Frame(self.r, width=frameWidth, height=frameHeight, bg=bg,
                  highlightthickness=1,
                  highlightbackground="yellow",
                  highlightcolor="yellow"
                  )
        label = Label(r, text="All Expenses", font="monospace 18 bold underline",
                      fg="white",
                      bg=bg)
        label.place(x=frameWidth // 4, y=5)
        r.place(x=width // 1.4, y=height // 5.2)

        text = scrolledtext.ScrolledText(r, height=frameHeight // 37, width=frameWidth // 12, font="calibri 15 bold")
        text.place(x=frameWidth // 20, y=frameHeight // 5)
        save = Button(r, image=save1, bd=0, activebackground=bg, bg=bg,
                      cursor="hand2"
                      )

        var=IntVar()
        rb=Radiobutton(r,text='Daily',value=1,variable=var,font="calibri 12 bold")
        rb.place(x=frameWidth//30,y=frameHeight//90)
        rb1 = Radiobutton(r, text='Monthly', value=0, variable=var,font="calibri 12 bold")
        rb1.place(x=frameWidth//1.4, y=frameHeight//90)
        def save_working(event):
            t = text.get('1.0', END)
            print(t)
            try:
                v=var.get()
                for i in t.split("\n"):
                    t1, p = i.split(':')
                    try:
                        db.execute(
                            f"insert into expenses (boolean,date,item,price) values({v},date('now'),'{t1}',{p}) ")
                        db.execute("commit")
                        text.delete("1.0",END)
                    except:
                        messagebox.showerror("Insert Not Possible Check Your Data")
            except:
              pass

        save.bind('<Button-1>', save_working)
        save.place(x=frameWidth // 3.5, y=frameHeight // 1.2)

    def reminder_frame(self, b):
        b.configure(state="disabled")
        r1 = Toplevel()
        r1.attributes("-topmost",True)
        r1.protocol("WM_DELETE_WINDOW", lambda: self.reminder_closing(b, r1))
        r1.resizable(False, False)
        frame_height = height // 2
        frame_width = (width // 2)
        r1.geometry("{}x{}+{}+{}".format(frame_width, frame_height + 50, width // 4, height // 4))
        reminder = Frame(r1, height=frame_height + 50, width=frame_width)
        reminder.configure(bg=self.bg1)
        label = Label(reminder, text="Make A Reminder", font="Helvetica 20 bold", bg=self.bg1,
                      fg="white"
                      )
        label.place(x=frame_width // 3, y=0)
        text = scrolledtext.ScrolledText(reminder, font='calibri 20 bold', height=frame_height // 38,
                                         width=frame_width // 16)
        text.place(x=frame_width / 23, y=frame_height / 10)

        help_button = Button(reminder, text="Help ?",
                             font='calibri 15 bold underline', bg=self.bg1,
                             fg="white",
                             bd=0,
                             activebackground=self.bg1,
                             cursor="hand2 ",
                             )
        help_button.place(x=frame_width // 2, y=frame_height - 15)
        execute_button = Button(reminder, image=execute, bg=self.bg1,
                                command=lambda: self.execute_button_working(text),
                                activebackground=self.bg1, bd=0, cursor="hand2 ", )
        execute_button.place(x=0, y=frame_height - 15)

        save_button = Button(reminder, image=save, bg=self.bg1, activebackground=self.bg1,
                             command=lambda: self.saveWorking(text, reminder),
                             cursor="hand2 ",
                             bd=0)
        save_button.place(x=frame_width - 100, y=frame_height - 15)

        clear_button = Button(reminder, image=clear, bg=self.bg1, activebackground=self.bg1,

                              command=lambda: text.delete("1.0", END),
                              bd=0, cursor="hand2 ",
                              )
        clear_button.place(x=frame_width - 200, y=frame_height - 10)

        reminder.place(x=0, y=0)

    def execute_button_working(self, text):
        t = text.get("1.0", END)
        try:
            cmd1, cmd2 = t.split(" ", 1)
            print(cmd1, cmd2)
            if cmd1.strip() == "delete" and cmd2.strip() == "all":
                try:
                    db.execute("drop table reminder")
                    text.delete("1.0", END)
                    messagebox.showinfo("Deleted", "All The Reminders Has Been Deleted")
                except:
                    messagebox.showinfo("", "Deletion Not Posible Contact Developper")
            elif cmd1.strip() == "show" and cmd2.strip() == "all":
                db.execute("select * from reminder")
                x = db.fetchall()
                if len(x) == 0:
                    text.delete("1.0", END)
                    messagebox.showinfo("", "No reminders found please add some reminders ")
                else:
                    text.delete("1.0", END)
                    for i in x:
                        text.insert("1.0", i[0])
            elif cmd1.strip() == "delete" and len(cmd2.strip()) >= 0:
                try:
                    db.execute(f"delete from reminder where date= date('{cmd2}')")
                    text.delete("1.0", END)
                    messagebox.showinfo("Deleted", f"All The Reminders Has Been Deleted For The Date  {cmd2}")
                except:
                    pass


            elif cmd1.strip() == "show" and len(cmd2.lstrip()):
                db.execute(f"select * from reminder where date = date('{cmd2.lstrip()}')")
                x = db.fetchall()
                if (len(x) == 0):
                    messagebox.showinfo("", f"No data found in database for date {cmd2}")
                else:
                    text.delete("1.0", END)
                    for i in x:
                        text.insert("1.0", i[0])
            else:
                messagebox.showerror("Invalid Command", "The given Command {} not found".format(t))

        except:
            messagebox.showerror("Invalid Command", "The given Command {} not found".format(t))

    def saveWorking(self, text, master):
        try:
            db.execute("create table reminder (text text,date date)")
            messagebox.showinfo("", 'reminder table created')
        except:
            pass
        t = text.get("1.0", END)
        print(len(t))
        if len(t) == 1:
            messagebox.showerror('empty field', 'reminder cannot save if it is empty')
        else:
            db.execute(f"insert into reminder values('{t}',date('now'))")
            db.execute("commit")
            messagebox.showinfo('', 'Your reminder has been saved')
            text.delete('1.0', END)

    def buttons(self):
        payment_button = Button(self.r, image=payment,
                                activebackground=self.bg2,
                                cursor="hand2 ",
                                bd=0, bg=self.bg2)
        payment_button.place(x=width // 30, y=height // 5.2)

        meal_button = Button(self.r, image=meal,
                             activebackground=self.bg2,
                             cursor="hand2 ",
                             bd=0, bg=self.bg2)
        meal_button.place(x=width // 30, y=height // 3.2)

        bill_button = Button(self.r, image=bill,
                             cursor="hand2 ",
                             activebackground=self.bg2,
                             bd=0, bg=self.bg2)
        bill_button.place(x=width // 30, y=height // 2.3)

        expences_button = Button(self.r, image=expences,
                                 cursor="hand2 ",
                                 activebackground=self.bg2,
                                 bd=0, bg=self.bg2, command=lambda: self.manageExpenses(expences_button))
        expences_button.place(x=width // 30, y=height // 1.8)

        member_button = Button(self.r, image=member,
                               cursor="hand2 ",
                               activebackground=self.bg2,
                               bd=0, bg=self.bg2)
        member_button.place(x=width // 30, y=height // 1.5)

        reminder_button = Button(self.r, image=reminder,
                                 cursor="hand2 ",
                                 command=lambda: self.reminder_frame(reminder_button),
                                 activebackground=self.bg2,
                                 bd=0, bg=self.bg2)
        reminder_button.place(x=width // 20, y=height - 150)
    def manageExpenses(self, b):
        bg1="pink"
        today = date.today()
        month=today.month
        if(month<=9):
            self.globalVarforMonth="0"+str(month)
        else:
          self.globalVarforMonth=str(month)

        # ------------------------------------- Inner Functions ------------------------------
        def onClose(r):
            if messagebox.askokcancel('Go Back', "Do you Want To Go Back In Main Window?",parent=r):
                self.r.deiconify()
        def onBack(r):
            r.destroy()
            self.r.deiconify()
        def delete_button(t,r):
            item = t.focus()
            x = t.item(item)
            try:
             db.execute(f'delete from expenses where id={x["values"][0]}')
             t.delete(item)
             t.destroy()
             refresh()
             messagebox.showinfo("Deleted","The selected item has been removed")
            except:
               messagebox.showwarning("X","Select An Item From Below For Delete",parent=r)
        def updateButton(t,r,update):
          def onClose(r):
             update.config(state="normal")
             r.destroy()
          def saveFunc(i,p,r,x):

             try:
               db.execute(f"update expenses set item='{i.get()}', price={float(p.get())} where id ={x['values'][0]}")
               db.execute("commit")
               messagebox.showinfo("updated","The selected item has been updated",parent=r)
               onClose(r)
               t.destroy()
               refresh()
             except:
                 messagebox.showerror("Invalid Value","Updation Not Possible",parent=r)
                 onClose(r)

          item=t.focus()
          x=t.item(item)
          try:
           if(x['values'][0]):
             update.config(state="disabled")
             r=Toplevel()
             r.config(bg="lightgreen")
             r.protocol("WM_DELETE_WINDOW",lambda :onClose(r))
             r.resizable(False,False)
             width1=width//3
             height1=height//5
             r.geometry(f"{width1}x{height1}+{width1}+{height1*2}")
             r.attributes("-topmost",True)
             itemVar=StringVar()
             priceVar=StringVar()
             itemE=Entry(r,width=30,font="calibri 15 bold",textvariable=itemVar)
             priceE = Entry(r,width=30, font="calibri 15 bold", textvariable=priceVar)
             save=Button(r,width=10,font="calibri 20 bold",text="Save",cursor="hand2",command=lambda :saveFunc(itemVar,priceVar,r,x))
             try:
               itemVar.set(x['values'][1])
               priceVar.set(x['values'][2])
             except:
                pass
             itemL=Label(r,text="Item",font="calibri 15 bold",bg="lightgreen")
             priceL=Label(r,text="Price",font="calibri 15 bold",bg="lightgreen")
             itemL.place(x=10,y=height1//10)
             priceL.place(x=10,y=height1//3)
             itemE.place(x=width1//5,y=height1//10)
             priceE.place(x=width1//5,y=height1//3)
             save.place(x=width1//2.8,y=height1//1.7)
          except:
            messagebox.showinfo("Id Missing","Please Select Item Then Proceed With Updation",parent=r)
        def insertFunc(btn,r1,t):
            btn['state']="disabled"
            #--------------------------------- INNER FUNC
            def onClose(r):
                btn["state"]="normal"
                r.destroy()
            def insert(d,i,p,type,r):
                boolean=0
                if(type.get()=="Daily"):
                    boolean=1
                else:
                    boolean=0

                try:
                  db.execute(f"insert into expenses(boolean,item,price,date) values({boolean},'{i.get()}',{float(p.get())},date('{date.get()}'))")
                  db.execute("commit")
                  messagebox.showinfo('Inserted',"Your Data Has Successfully Saved",parent=r)
                  r.destroy()
                  t.destroy()
                  refresh()
                except:
                    messagebox.showerror("Invalid Data","Make Sure That You Have Fill All Entries",parent=r)

            #---------------------------------- End of Inner Func

            r = Toplevel()
            r.resizable(False, False)
            width1 = width // 3
            height1 = height // 5
            r.geometry(f"{width1}x{height//4}+{width1}+{height1 * 2}")
            r.attributes("-topmost", True)

            itemVar = StringVar()
            priceVar = StringVar()

            itemE = Entry(r, width=30, font="calibri 15 bold", textvariable=itemVar)
            priceE = Entry(r, width=30, font="calibri 15 bold", textvariable=priceVar)
            date=DateEntry(r,width=20,font="calibri 15 bold",date_pattern="yyyy-mm-dd")
            typeVar = StringVar()
            type = Combobox(r, width=10, textvariable=typeVar, font="calibri 15 bold")
            type['values'] = ("Daily", "Monthly")
            type['state'] = 'readonly'


            save = Button(r, width=10, font="calibri 20 bold", text="Save", cursor="hand2",
                          command=lambda: insert(date,itemVar, priceVar,typeVar, r))

            type.place(x=width1//1.5,y=height1//10)

            dateL=Label(r,text="Date",font="calibri 15 bold")
            itemL = Label(r, text="Item", font="calibri 15 bold")
            priceL = Label(r, text="Price", font="calibri 15 bold")

            dateL.place(x=10,y=height1//10)
            itemL.place(x=10,y=height1//3)
            priceL.place(x=10,y=height1//1.7)
            date.place(x=width1//5,y=height1//10)

            itemE.place(x=width1 // 5, y=height1 // 3)
            priceE.place(x=width1 // 5, y=height1 // 1.7)
            save.place(x=width1 // 2.8, y=height1 // 1.2)
            r.protocol("WM_DELETE_WINDOW",lambda :onClose(r))
        def getMonth(var,t):
            val=var.get()
            if(val=="January"):
               self.globalVarforMonth="01"
            elif(val=="February"):
                self.globalVarforMonth="02"
            elif (val == "March"):
                self.globalVarforMonth = "03"
            elif (val == "April"):
                self.globalVarforMonth = "04"
            elif (val == "May"):
                self.globalVarforMonth = "05"
            elif (val == "June"):
                self.globalVarforMonth = "06"
            elif (val == "July"):
                self.globalVarforMonth = "07"
            elif (val == "August"):
                self.globalVarforMonth = "08"
            elif (val == "Septembor"):
                self.globalVarforMonth = "09"
            elif (val == "October"):
                self.globalVarforMonth = "10"
            elif (val == "Novembor"):
                self.globalVarforMonth ="11"
            else:
                self.globalVarforMonth = "12"
            print(self.globalVarforMonth)
            t.destroy()
            refresh()

        def refresh():
            style.configure("Treeview", font="calibri 17 bold", rowheight=40, anchor="center", width=200, fill='y')
            style.configure("Treeview.Heading", font="calibri 20 underline")
            t = Treeview(r, height=height // 60, style="Treeview", cursor="hand2")
            t['columns'] = ('Id', 'Item', 'Price')
            t.column('Id', width=width // 9, anchor='center')
            t.column('Item', width=width // 3, anchor="center")
            t.column('Price', width=width // 7, anchor="center")
            t.column('#0', width=width // 5, anchor='center')
            t.heading('Id', text="Id")
            t.heading('Item', text="Items")
            t.heading('Price', text="Price")

            t.insert('', 'end', 'dailyExpenses', text="Daily Expenses")
            t.insert('', 'end', 'monthlyExpenses', text="Monthly Expenses")
            c = ['monthlyExpenses', 'dailyExpenses']
            cbL = Label(r, text="Select Month ", font="calibri 20 bold", bg=bg1, )
            cbL.place(x=width // 2.9, y=height // 15)
            cb = Combobox(r, width=15, font="calibri 20 bold")
            cb.config(state="readonly")
            cb['values'] = (
            "January", "February", "March", "April", "May", "June", "July", "August", "Septembor", "October",
            "Novembor", "Decembor")
            cb.place(x=width // 2.2, y=height // 15)
            cbButton = Button(r, text="Show", font="calibri 15 bold", bd=0, bg='yellow', activebackground=bg1, width=10,
                              command=lambda: getMonth(cb, t),
                              cursor="hand2")
            cbButton.place(x=width // 1.6, y=height // 15)

            for x in range(2):
                db.execute(
                    f"select * from expenses where boolean={x} and instr(date,'{today.year}-{self.globalVarforMonth}')>0")
                a = db.fetchall()
                print(a)
                for i in a:
                    try:
                        t.insert(f'{c[x]}', 'end', f'{i[2] + str(i[1])}', text=f"{i[2]}")
                        db.execute(f"select id,item,price from expenses where boolean={x} and date=date('{i[2]}')")
                        a = db.fetchall()
                        for j in a:
                            t.insert(f'{i[2] + str(i[1])}', 'end', values=(f"{j[0]}", f"{j[1]}", f"{j[2]}"))
                        db.execute(f"select sum(price) from expenses where boolean={x} and date=date('{i[2]}')")
                        total = db.fetchone()
                        t.insert(f'{i[2] + str(i[1])}', 'end', text="Total", values=("", '', total))
                    except:
                        pass
            db.execute(f"select sum(price) from expenses where boolean=1 and instr(date,'{today.year}-{self.globalVarforMonth}')>0")
            total = db.fetchone()
            t.insert('dailyExpenses', 'end', text="Total Daily Expenses", values=("", '', total))
            db.execute(f"select sum(price) from expenses where boolean=0  and instr(date,'{today.year}-{self.globalVarforMonth}')>0")
            total1 = db.fetchone()
            t.insert('monthlyExpenses', 'end', text="Total Monthly Expenses", values=("", '', total1))
            db.execute(f"select sum(price) from expenses where instr(date,'{today.year}-{self.globalVarforMonth}')>0")
            allExpenses=db.fetchall()
            t.insert('','end',text="All Expenses ",values=("","",allExpenses))
            t.place(x=width // 9, y=height // 6)
            delete_button1 = Button(r, text="delete", image=delete, bd=0,
                                    command=lambda: delete_button(t,r),
                                    activebackground=bg1, bg=bg1)
            delete_button1.place(x=width // 40, y=height // 3)

            update = Button(r, image=updateExpenses, bd=0,
                                    activebackground=bg1, bg=bg1,command=lambda : updateButton(t,r,update))
            update.place(x=width //40, y=height // 3.8)

            insert=Button(r, text="delete", image=insertExpenses, bd=0,
                          command=lambda :insertFunc(insert,r,t),
                                    activebackground=bg1, bg=bg1)
            insert.place(x=width//40,y=height//5)



        # ---------------------------End of inner functions------------------------------------
        self.r.withdraw()
        r = Toplevel(self.r)
        r.configure(bg=bg1)
        r.protocol("WM_DELETE_WINDOW",lambda :onClose(r))
        r.geometry(f"{width}x{height}")
        style = ttk.Style()
        back_button=Button(r,image=back,bd=0,bg=bg1,activebackground=bg1,command=lambda :onBack(r))
        back_button.place(x=10,y=0)
        refresh()

    def onClosing(self,r):
        if messagebox.askokcancel("Exit", "Do you want to Exit ?",parent=r):
            self.r.destroy()
            self.r1.destroy()

    def main_window_configure(self):
        self.r.geometry("{}x{}".format(width, height - 50))
        self.r.configure(bg=self.bg2)
        self.r.resizable(True, True)
        label = Label(self.r, image=manger, bd=0, bg=self.bg2)
        label.place(x=width // 4, y=height // 45)
        label1=Label(self.r, image=myBatch, bd=0, bg=self.bg2)
        label1.place(x=width//1.2+50,y=height//1.4)


r = Tk()
width = r.winfo_screenwidth()
height = r.winfo_screenheight()
# ----------------------Database Connection -------------------
conn = sqlite3.connect('mydb.db')
db = conn.cursor()
# -----------------------Image loading ------------------------
delete = ImageTk.PhotoImage(Image.open("images/delete.png"))
proceed = ImageTk.PhotoImage(Image.open("images/proceed.png"))
payment = ImageTk.PhotoImage(Image.open("images/payment.png"))
addNewUser = ImageTk.PhotoImage(Image.open("images/addnewuser.png"))
meal = ImageTk.PhotoImage(Image.open("images/meal.png"))
bill = ImageTk.PhotoImage(Image.open("images/billl.png"))
expences = ImageTk.PhotoImage(Image.open("images/expences.png"))
member = ImageTk.PhotoImage(Image.open("images/member.png"))
execute = ImageTk.PhotoImage(Image.open("images/show.png"))
save = ImageTk.PhotoImage(Image.open("images/save.png"))
reminder = ImageTk.PhotoImage(Image.open("images/reminder.png"))
clear = ImageTk.PhotoImage(Image.open("images/clear.png"))
manger = ImageTk.PhotoImage(Image.open("images/messmanager.png"))
de = ImageTk.PhotoImage(Image.open("images/dailyExpenses.png"))
save1 = ImageTk.PhotoImage(Image.open("images/dailySave.png"))
back=ImageTk.PhotoImage(Image.open("images/back.png"))
updateExpenses=ImageTk.PhotoImage(Image.open("images//update.png"))
insertExpenses=ImageTk.PhotoImage(Image.open("images//insert.png"))
myBatch=ImageTk.PhotoImage(Image.open("images/batch.png"))
# --------------------------------------------------------------
r.iconphoto(True, PhotoImage(file='images/icon.png'))
s = Login(r)
r.mainloop()

# ------------------ remembering sections ---------------------
# command = lambda: self.reminder_frame(meal_button),
