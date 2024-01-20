import tkinter
from tkinter import*
from tkinter import ttk,font
from PIL import ImageTk,Image
def customerbank(r,details):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=600,height=450,bg="#de9e4b").place(relx=.33,rely=.2)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="Welcome to Madhan Bank",font=f,bg="#de9e4b").place(relx=.43,rely=.3)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    a="UserName : "+details[0]
    label=Label(frame,text=a,font=f,bg="#de9e4b")
    label.place(relx=.45,rely=.4)
    a="Aadhar No : "+details[1]
    label=Label(frame,text=a,font=f,bg="#de9e4b")
    label.place(relx=.45,rely=.5)
    a="PAN No: "+details[2]
    label=Label(frame,text=a,font=f,bg="#de9e4b")
    label.place(relx=.45,rely=.6)
    a="Phone No : "+details[3]
    label=Label(frame,text=a,font=f,bg="#de9e4b")
    label.place(relx=.45,rely=.67)
    a="Amount : "+details[4]
    label=Label(frame,text=a,font=f,bg="#de9e4b")
    label.place(relx=.45,rely=.74)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()
def reg(a,b,r):
    f=open("registers.txt","r")
    d=f.read()
    d=d.split("\n")
    for x in d:
        x=x.split(" ")
        if (a==x[0] and b==x[3]):
            print(customerbank(r,x))
            break
    else:
        print(customerlog(r))

def customerlog(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=250,bg="#4FD6F7").place(relx=.35,rely=.3)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER LOGIN",font=f,bg="#4FD6F7").place(relx=.45,rely=.3)

    e=font.Font(r,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="Customer ID:",font=e,bg="#4FD6F7").place(relx=.38,rely=.4)
    l=Label(frame,text="Password:",font=e,bg="#4FD6F7").place(relx=.38,rely=.5)

    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    b=Button(frame,text="Login",font=e,bg="red",command=lambda:reg(l1.get(),l2.get(),r))
    b.place(relx=.48,rely=.57)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()
def file(a,b,c,d,r):
    n=a+" "+b+" "+c+" "+d+" "+ " 1000 "+ "\n"
    f=open("registers.txt","a")
    f.write(n)


def customer_reg(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=590,bg="#4FD6F7").place(relx=.33,rely=.1)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="#4FD6F7").place(relx=.40,rely=.12)

    e=font.Font(r,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=e,bg="#4FD6F7").place(relx=.38,rely=.23)
    l=Label(frame,text="Aadhar No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.32)
    l=Label(frame,text="PAN No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.43)
    l=Label(frame,text="Phone No:",font=e,bg="#4FD6F7").place(relx=.38,rely=.54)
    l=Label(frame,text="Rupees:",font=e,bg="#4FD6F7").place(relx=.38,rely=.65)
    l=Label(frame,text="1000/-",font=e,bg="#4FD6F7").place(relx=.50,rely=.65)



    l1=Entry(frame)
    l1.place(relx=.50,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.50,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.50,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.50,rely=.55)

    b=Button(frame,text="Register",font=e,bg="#de9e4b",command=lambda:file(l1.get(),l2.get(),l3.get(),l4.get(),r))
    b1=Button(frame,text="Clear",font=e,bg="#de9e4b",command=lambda:file(l1.delete(0,"end"),l2.delete(0,"end"),l3.delete(0,"end"),l4.delete(0,"end"),r))
    b.place(relx=.47,rely=.75)
    b1.place(relx=.55,rely=.75)


    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()


def adminpage(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=590,bg="#4FD6F7").place(relx=.01,rely=.1)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="#4FD6F7").place(relx=.07,rely=.12)

    e=font.Font(r,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=e,bg="#4FD6F7").place(relx=.05,rely=.23)
    l=Label(frame,text="Aadhar No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.32)
    l=Label(frame,text="PAN No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.43)
    l=Label(frame,text="Phone No:",font=e,bg="#4FD6F7").place(relx=.05,rely=.54)
    def reg1():
        from tkinter import messagebox
        file(l1.get(),l2.get(),l3.get(),l4.get(),r)
        l1.delete(0,"end")
        l2.delete(0,"end")
        l3.delete(0,"end")
        l4.delete(0,"end")
        messagebox.showinfo("success","successfully done")

    l1=Entry(frame)
    l1.place(relx=.17,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.17,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.17,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.17,rely=.55)

    b=Button(frame,text="Register",font=e,bg="#de9e4b",command=lambda:reg1())
    b.place(relx=.14,rely=.80)


    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)


    def read_file():
        try:
            with open("customer.txt","r") as file:
                r=file.readlines()
                for x in r:
                    item=x.split("\t")
                    tree.insert("", "end", values=item)
        except FileNotFoundError:
            tree.insert("", "end", values=("File not found",))


    # Create a Treeview widget
    tree = ttk.Treeview(r, columns=("Name", "Aadhar No", "PAN No", "Phone No","Amount"), show="headings")
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Aadhar No")
    tree.heading("#3", text="PAN No")
    tree.heading("#4", text="Phone No")
    tree.heading("#5", text="Amount")
    tree.column("#1", width=55)
    tree.place(relx=.39,rely=.10,height=500)
    read_button = Button(r, text="Read File", command=lambda :read_file())
    read_button.place(relx=.65,rely=.8)
    r.mainloop()


def admin(a,b,r):
    if(a=="admin" and b=="1234"):
        adminpage(r)
    else:
        adminlog(r)


def adminlog(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x720")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=500,height=250,bg="#4FD6F7").place(relx=.35,rely=.3)
    f=font.Font(r,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="ADMIN LOGIN",font=f,bg="#4FD6F7").place(relx=.45,rely=.3)

    e=font.Font(r,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="Admin ID:",font=e,bg="#4FD6F7").place(relx=.38,rely=.4)
    l=Label(frame,text="Password:",font=e,bg="#4FD6F7").place(relx=.38,rely=.5)

    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    b=Button(frame,text="Login",font=e,bg="red",command=lambda:admin(l1.get(),l2.get(),r)).place(relx=.48,rely=.57)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()


def Home():
    #Home page
    r=Tk()
    r.geometry("1500x900")
    r.title("Bank")
    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="times new roman",size=25)
    x=Label(frame,text="Madhan Bank",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.45,rely=.1)

    frame=Frame(r,width=100,height=100)
    frame.place(anchor="s",relx=.05,rely=.3)
    # img=ImageTk.PhotoImage(Image.open("bank1.jpg"))
    # label=Label(frame,image=img)
    # label.pack()

    f=font.Font(weight="bold",family="times new roman",size=20)
    t="""A bank is a financial institution that accepts deposits from the public
    and creates a demand deposit while simultaneously making loans.
    Lending activities can be directly performed by the bank or indirectly through capital markets."""
    l=Label(r,text=t,font=f).place(relx=.13,rely=.2)

    b=Button(r,text="Customer Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customerlog(r)).place(relx=.10,rely=.5)
    c=Button(r,text="Customer Register",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customer_reg(r)).place(relx=.40,rely=.5)
    d=Button(r,text="Admin Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:adminlog(r)).place(relx=.71,rely=.5)

    frame=Frame(r,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(r,weight="bold",family="times new roman",size=15)
    x=Label(frame,text=" © CopyRight 2024 Madhan",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=.40,rely=.1)
    r.mainloop()
Home()










