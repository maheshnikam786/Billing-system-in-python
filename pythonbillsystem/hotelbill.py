
from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    textinn.set(operator)

def btnClear():
    global operator
    operator=" "
    textinn.set("")
 
def insert():
   name1 = textin.get()
   sum = textinn.get()
   conn = sqlite3.connect('abc.db')
   with conn:
      cursor = conn.cursor()
      cursor.execute('INSERT INTO people(name, sum) VALUES(?,?)',(name1, sum,))
     # db.close()
     
#
"""def Plot_graph():
    cursor.execute("SELECT sum FROM people ")
    for row in cursor.fetchall():
        print(dates.append(row))
        
    plt.plot([dates])
   # xlim(0,100)
    plt.show()
        """
        
table=[]      
   
def btnEquals():
    global operator
    sumup=str(eval(operator))
    
    textinn.set(sumup)
    table.append(sumup)
    table.sort()
    plt.plot(table)
    plt.show()
    operator=""

"""def Plot_graph():
    
    plt.ylabel("total bill")
    plt.xlabel("no of tran")
    plt.show()"""
    
    


db = sqlite3.connect('abc.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS people(name TEXT, sum TEXT)")
db.commit()    
    
    
    

cal=Tk()

cal.title("hotel management")

operator=" "

textinn=StringVar()
sumup=IntVar()
Full=StringVar()
textin=StringVar()

txtDisplay=Entry(cal,font=("arial",20,"bold"),textvariable=textinn,bd=20,insertwidth=3,bg="cyan",justify="right").grid(columnspan=1)

button20=Button(cal,padx=45,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="CHEESE FRANKIE 20RS",command=lambda:btnclick(20))
button20.grid(row=1,column=0)

button40=Button(cal,padx=45.1,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="chicken FRANKIE 40RS",command=lambda:btnclick(40))
button40.grid(row=1,column=1)

button15=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text=" veg FRANKIE 15 RS ",command=lambda:btnclick(15))
button15.grid(row=1,column=2)

buttonAdd=Button(cal,padx=190,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda:btnclick("+"))
buttonAdd.grid(row=5,column=0)

buttonClr=Button(cal,padx=150,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="CLEAR",command=btnClear)
buttonClr.grid(row=5,column=1)

buttonEqu1=Button(cal,padx=200,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=btnEquals)

buttonEqu1.grid(row=6,column=1)

button16=Button(cal,padx=45.1,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="CHEESE FRANKIE 30RS",command=lambda:btnclick(30))
button16.grid(row=2,column=0)

button17=Button(cal,padx=45.1,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="EGG FRANKIE 30RS",command=lambda:btnclick(30))
button17.grid(row=2,column=1)

button18=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="      FRIES   30   RS     ",command=lambda:btnclick(30))
button18.grid(row=2,column=2)

button19=Button(cal,padx=80,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="   COKE   12  RS ",command=lambda:btnclick(12))
button19.grid(row=3,column=0)

button20=Button(cal,padx=45.1,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="   MOJJITO 90 RS   ",command=lambda:btnclick(90))
button20.grid(row=3,column=1)

button21=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="MAGERITTA PIZZA 30RS",command=lambda:btnclick(30))
button21.grid(row=3,column=2)

button22=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="CHICKEN BURGER 50RS",command=lambda:btnclick(50))
button22.grid(row=4,column=0)

button23=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="BREAD BUTTER 40RS",command=lambda:btnclick(40))
button23.grid(row=4,column=1)

button24=Button(cal,padx=30,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="MAHARAJA BUR. 100RS",command=lambda:btnclick(100))
button24.grid(row=4,column=2)


buttonSubmit=Button(cal,padx=140,pady=1,bd=8,fg="black",font=("arial",20,"bold"),text="Submit",command=insert)
buttonSubmit.grid(row=5,column=2)

label1=Label(cal,text="Name",width=20,font=("arial",20))
label1.place(x=800,y=0)
entry_1=Entry(cal,textvar=textin,width=20,font=("arial",20))
entry_1.place(x=1000,y=0)


cal.mainloop()
        
#Plot_graph()   
    
