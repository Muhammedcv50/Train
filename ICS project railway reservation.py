from tkinter import *
from PIL import ImageTk, Image
import os
import random


w = Tk()
img = ImageTk.PhotoImage(Image.open("irctc.png"))
panel = Label(w, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
w.after(2000,lambda:w.destroy())
w.mainloop()


def checkid(a):
    f=open("users.txt","r")
    for i in f:
        k=i.split(",")
        if k[2]==a:
            return False
    return True


        
def form(d):
    a=d.split("/")
    if len(d)!=8 or len(a)!=3:
        return False
    else:
        return True

    
def gettick():
    f=open("ticket.txt","r")
    l=open("temp.txt","a")
    t=random.choice(f.readlines())
    f.seek(0)
    for i in f:
        if i!=t:
           l.write(i) 
    f.close()
    l.close()
    os.remove("ticket.txt")
    os.rename("temp.txt","ticket.txt")
    return (t.strip())


    
def login():
    f=open("users.txt","r")
    u=input("\n  Username : ")
    p=input("\n  Password: ")
    a=f.readlines()
    c=0
    for i in range(len(a)):
        d=a[i]
        name,mob,usn,add,pas=d.split(",")
        if(usn==u and pas.strip()==p):
            print("\n  Login Sucessfull")
            c=1
            break
    if c==0:
        print("\n Invalid username or password !!")
    else:
        print("\n\n\n\n Welcome ",name," ")
        print("","-"*20,end="")
        while True:
            print("\n\n 1.New Booking\n\n 2.Cancel Ticket\n\n 3.My Bookings\n\n 4.Profile\n\n Press any other key to signout ")
            op=int(input("\n Choose any option - "))
            if op==1:
                 f2=open("booking.txt","a")
                 print("\n\n\n","*"*22,"\n *    New Booking     *\n","*"*22)
                 frm=input("\n From : ")
                 to=input("\n To : ")
                 date="000"
                 while len(date)!=8 or form(date)==False:
                     date=input("\n Date (DD/MM/YY) : ")
                     if len(date)!=8 or form(date)==False:
                         print("\n Invalid date format !!")
                 np=input("\n No of passengers - ")    
                 print("\n Trains available :-\n\n 1.Maharajas Express\n\n 2.Antyodaya Express\n\n 3.Janshatabdi\n\n 4.Maveli Express")
                 no=6
                 while no>4:
                     no=int(input("\n Choose any train - "))
                     if no>4:
                         print(" Invalid train !!!")
                 t=gettick()
                 r=usn+","+frm+","+to+","+date+","+str(no)+","+np+","+t
                 f2.write(r+"\n")
                 f2.close()
                 f2=input(" \n Ticket booked ....\n\n Press enter to continue\n\n")
                 
            elif op==3 or op==2:
                 print("\n")
                 f2=open("booking.txt","r")
                 c=0
                 a=f2.readlines()
                 if op==2:
                      print("\n\n\n ","-"*23,"\n|     Cancel Ticket   |\n ","-"*23)
                 else:
                      print("\n\n\n ","-"*22,"\n|       My Booking      |\n ","-"*22)
                 for i in range(len(a)):
                     k=a[i].split(",")
                     if k[0]==usn:
                         c=1
                         d,m,y=k[3].split("/")
                         if m=='01':
                             mo="January"
                         elif m=='02':
                             mo="February"
                         elif m=='03':
                             mo="March"
                         elif m=='04':
                             mo="April"
                         elif m=='05':
                             mo="May"
                         elif m=='06':
                             mo="June"
                         elif m=='07':
                             mo="July"
                         elif m=='08':
                             mo="August"
                         elif m=='09':
                             mo="September"
                         elif m=='10':
                             mo="October"
                         elif m=='11':
                             mo="November"
                         else:
                             mo="December"
                         b=k[4].strip()
                         if b=='1':
                            print("\n Maharajas Express     ",d,end="")
                         elif b=='2':
                             print("\n Antyodaya Express     ",d,end="")
                         elif b=='3':
                             print("\n Janshatabdi Express   ",d,end="")
                         elif b=='4':
                             print("\n Maveli Express        ",d,end="")
                         if op==2:
                             print(" -",m,"-",y,"\n From: ",k[1]," "*(14-len(k[1])),"To:",k[2],"\n Ticket No: ",k[6].strip(),"       No of passengers - ",k[5])
                         if op==3:
                              print(",",mo," 20",end="")
                              print(y,"\n ",k[1]," ->",k[2]," "*(16-len(k[1]+k[2])),"Ticket no - ",k[6].strip())          
                 f2.close()
                 if c==0:
                     print("\n  Sorry ,No Bookings Yet !!")
                 elif op==2:
                        u=0
                        n=input("\n Enter the ticket number to be cancelled - ")
                        f=open("booking.txt","r")
                        l=open("temp.txt","w")
                        for i in f:
                            a=i.split(",")
                            if a[6].strip()!=n:
                                 l.write(i)
                            else:
                                u=1
                        l.close()
                        f.close()
                        os.remove("booking.txt")
                        os.rename("temp.txt","booking.txt")
                        if u==1:
                            print("\n Ticket Cancelled ..")
                        else:
                            print("\n Ticket Not found ..")
                        
                 p=input("\n Press enter to continue - ")
                
                     
            elif op==4 :
                 print("\n\n\n ","-"*22,"\n|       My Profile      |\n ","-"*22)
                 print("\n\n Name - ",name)
                 print("\n\n Mob - ",mob)
                 print("\n\n Address - ",add)
                 print("\n\n Username - ",usn)
                 print("\n\n Password - ****",end="")
                 print(pas.strip()[4:])
                 p=input("\n Press enter to continue - ")
                
            else:
                break
    f.close() 
    

    

while True:
    print ("\n\n*******************************************************************************")
    print ("*                    RAILWAY TICKET RESERVATION SYSTEM                        *")
    print ("*******************************************************************************")

    print("\n\n\n"," "*23," 1.Login\n\n"," "*23," 2.Sign Up\n\n"," "*23," Press any other key to exit ")

    op=int(input("\n                          Choose any option - "))

    if op==1:
        print("\n\n\n ","-"*22,"\n  |    Login Portal    |\n ","-"*22)
        login()  

    elif op==2:
         print("\n\n\n ","-"*22,"\n  |       Sign Up       |\n ","-"*22)
         f=open("users.txt","a")
         name=input("\n Name : ")
         mob=0
         while len(str(mob))!=10 or mob.isdigit()==False:
             mob=input("\n Mobile : ")
             if len(str(mob))!=10 or mob.isdigit()==False:
                 print("\n Enter a valid mobile no (10 digits)")
         add=input("\n Address : ")
         us=input("\n Enter a Username : ")
         while checkid(us)==False:
             us=input("\n Username already taken, enter a new username\n\n Username: ")
         pas="232"
         while len(pas)<4:
             pas=input("\n Enter a Password (min 4 characters): ")
             if len(pas)<4:
                 print("\n Please enter a valid password with minimum 4 characters ..")
                 pas=input("\n Enter a Password (min 4 characters): ")
         r=name+","+mob+","+us+","+add+","+pas
         f.write(r+"\n")
         print("\n Login with your username and password \n\n")
         f.close()   

    else:
        print("\n                              ___________\n                             /           \\\n                             |   /\\ /\\   |\n                             |     -     |\n                             |   \\___/   |\n                              \\_________/\n\n                         Thanks for using IRCTC App   ")
        break

