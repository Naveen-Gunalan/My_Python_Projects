#tkinter are using an gui applicatin toolkit 
from tkinter import *
#this pil module are used in view an pixele image an process to an page images
from PIL import ImageTk,Image
#call an meesage an formate yes or no and savein message an process
from tkinter import messagebox
#ast is normal from of an change an dict fotmate to key and values
import ast
#import an date time us current time
from datetime import datetime
#give an rndom number to give in billing option
import random
#this html only used for an hiperlink of an social median and image can used 
from tkhtmlview import *
#using an subtools of an kinter 
from tkinter import ttk
#mysql are used an store an all data of billing are saveed in database are used in an this module
import mysql.connector as mc



#main window
win=Tk()
win.title("RESTAURANT HOME PAGE")
win.geometry('1200x700')
win.config(bg='#4D0039')
#win.resizable(0,0)
#===============main window home page view=================================================================================
l1=Label(win,text="Mother Indian Restaurant",bg='#4D0039',fg='#ff4a4a',font=('Bodoni MT Black',25,'bold'),relief=RAISED,bd=15)
l1.pack(fill=X)
lbl=Label(win,text='Welcome to Mother restaurant',padx=5,pady=10,font=('Bodoni MT Black',25,'bold'),bg='#4D0039',fg='#ff4a4a')
lbl.place(x=400,y=70)
l2=HTMLLabel(win,html='<a href="https://www.instagram.com/crazy_navin_21/">Instagram</a>')
l2.config(bg='#4D0039',fg='#ff4a4a')
l2.place(x=320,y=630)

l3=HTMLLabel(win,html='<a href="https://youtube.com/channel/UChSDslwfTjaOZXdiUTOq6Iw/">YouTube</a>')
l3.config(bg='#4D0039',fg='#ff4a4a')
l3.place(x=620,y=630)
l4=HTMLLabel(win,html='<a href="https://twitter.com/VedhaNavin/">Twitter</a>')
l4.config(bg='#4D0039',fg='#ff4a4a')
l4.place(x=920,y=630)
#insert images
pic=Image.open("C:/Users/siva/Documents/2img")
resize=pic.resize((1100,500))
img=ImageTk.PhotoImage(resize)
l5=Label(win,image=img,relief=RAISED)
l5.place(x=310,y=120)




#===========login page===================================================================================
def login():
    #this login are uesd an one device are alredy are login to created on accont this login function are execute an other set ofa an process an program
    newwin=Toplevel(win)
    newwin.geometry('500x500')
    newwin.title('Sign In')
    newwin.config(bg='#4D0039')
    newwin.resizable(0,0)
    head1=Label(newwin,text='Welcome To Restaurant Signin',font=('Algerian',20,'bold'),relief=RAISED,bd=10,fg='#ff4a4a',bg='#4D0039')
    head1.pack(fill=X)

    #frame created and user name create
    f1=Frame(newwin,width=350,height=350,bg='lightgreen',relief=RAISED,bd=20)
    f1.place(x=80,y=90)
    head=Label(f1,text='Sign in',font=('Microsoft Yahei UI Light',23,'bold'),fg='#57a1f8',bg='lightgreen')
    head.place(x=100,y=5)
    #this enter function are work in an any of un can write this can delete an alredy text are delete us text view as new enter
    def enter(e):
        user.delete(0,'end')
    #this leave function are anything are not writing any sentence are give space is written an alredy is given are view    
    def leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(f1,width=25,fg='black',bg='white',font=('Microsoft Yahei UI Light',11,'bold'),border=1,relief=RAISED,bd=10)
    user.place(x=35,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',enter)
    user.bind('<FocusOut>',leave)
    #password create
    #this enter function are work in an any of un can write this can delete an alredy text are delete us text view as new enter
    def enter(e):
        passwd.delete(0,END)
    #this leave function are anything are not writing any sentence are give space is written an alredy is given are view            
    def leave(e):
        name=passwd.get()
        if name=='':
            user.insert(0,'password')
    passwd=Entry(f1,width=25,fg='black',bg='white',font=('Microsoft Yahei UI Light',11,'bold'),border=1,relief=RAISED,bd=10)
    passwd.place(x=35,y=150)
    passwd.insert(0,'password')
    passwd.bind('<FocusIn>',enter)
    passwd.bind('<FocusOut>',leave)
    def signin():
        #this sign in process are used an, i am an new worker of an restarant i don't have any of an account so i have cretaed an acoount and can save an id name and an password of an given account
        username=user.get()
        password=passwd.get()
        #this an given user name and password are alredy store an data.txt in file of dict formate
        #can used this file an excute an process of an next to us an line
        file=open(r"C:\\Users\\siva\\Documents\\data.txt.txt",'r')
        d=file.read()
        #this ast foramte are used in change an formate of noraml type of data can change an dict 
        r=ast.literal_eval(d)
        file.close()
        #print(r.keys())
        #print(r.values())

        #this are given user and password are equal to process an next procewss          
        if username in r.keys() and password==r[username]:
#=========================================BILLING option create=======================================            
            w=Toplevel(win)
            w.geometry('1300x800')
            w.config(bg='orange')
            f1=Frame(w,width=1370,height=70,bg='#6f6f6f',relief=RAISED,bd=20)
            f1.pack(fill=BOTH)
            l=Label(f1,text='Restaurant Billing',bg='#6F6F6F',fg='cyan',width=1370,font=('Algerian',30,'bold'))
            l.pack()
            #customer frame
            f2=Frame(w,width=1370,height=50,bg='pink',relief=RIDGE,bd=5)
            f2.pack(fill=X)
            ls=Label(f2,text='Menu And Billing Formate',bg='pink',fg='black',font=('Algerian',30,'bold'))
            ls.pack()

            f3=Frame(w,width=500,height=700,bg='yellow',relief=RIDGE,bd=5)
            f3.place(x=0,y=150)

            f4=Frame(w,width=450,height=450,bg='lavender',relief=RIDGE,bd=10,padx=10,pady=10)

            now = datetime.now()
            localtime=now.strftime("%d/%m/%Y %H:%M:%S")
            #is store an given billing of an customer are store an data in database of given mysql data
            #are store an sql database,using an sql query are store an data of databases
            #first can coonect an python to mysql are usedd connect method and
            #to use an cursor execute an given query in database change an data
            def save_bill(*args):
                e=str(rand.get())
                e1=str(date.get())
                e2=str(tax.get())
                e3=str(Total.get())
                e4=str(cost.get())
                e5=str(servicescharge.get())
                con=mc.connect(host="localhost",user="root",passwd='',db='siva')
                c=con.cursor()
                c.execute("insert into billing(rand, date, tax, tot, cost, ser) values('"+e+"','"+e1+"','"+e2+"','"+e3+"','"+e4+"','"+e5+"')")
                con.close()
            #is store an given proudct are save of an customer are store an data in database of given mysql data
            #are store an sql database,using an sql query are store an data of databases
            #first can coonect an python to mysql are usedd connect method and
            #to use an cursor execute an given query in database change an data                
           
            def save(*args):
                e1=str(veg_briyani.get())
                e2=str(egg_briyani.get())
                e3=str(chiken_briyani.get())
                e4=str(mutton_briyani.get())
                e5=str(beef_briyani.get())
                e6=str(chiken_65.get())
                e7=str(bounless.get())
                e8=str(chiken_gril_full.get())
                e9=str(chiken_thandoori_full.get())
                e10=str(lime_soda.get())
                e11=str(lime_jucie.get())
                e12=str(blueberry.get())
                con=mc.connect(host="localhost",user="root",passwd='',db='siva')
                c=con.cursor()
                c.execute("insert into detalis4(chbriyani, vegbr, eggbr, mubr, bebr, ch65, bouless, gril, than, soda, limeju, blue) values('"+e1+"','"+e2+"','"+e3+"','"+e4+"','"+e5+"','"+e6+"','"+e7+"','"+e8+"','"+e9+"','"+e10+"','"+e11+"','"+e12+"')")
                con.close()
                #this function are using an exit
            def qexit():
                w.destroy()
            #this function are using an any of an change an billing process example any of an customer
            #are add an any off an product add or cancell of item and add an new item can using an this process    
            def reset():
                veg_briyani.set('')
                egg_briyani.set('')
                chiken_briyani.set('')
                mutton_briyani.set('')
                beef_briyani.set('')
                chiken_65.set('')
                bounless.set('')
                chiken_gril_full.set('')
                chiken_thandoori_full.set('')
                lime_soda.set('')
                lime_jucie.set('')
                blueberry.set('')
                f4.pack_forget()
            #this funtion are execute an bill of custiomer are gives as an count of an product item and
            #show an billing an current date ant random bill no and gst and tax of an product are print an bill to an customer to pay an process
            def gentrate():
                bill_no=str(random.randint(15000,50000))
                rand.set(bill_no)
                date.set(localtime)
                #using expction in billing genrate
                #this exception are used an any of single produt are an empty can execute and process an others
                #process an try and catch are used in entry an tax and proces an given customers are
                #print an bill us process an action to us taxx
                try:
                    vegb=int(veg_briyani.get())
                except:
                    vegb=0
                try:
                    egb=int(egg_briyani.get())
                except:
                    egb=0
                try:
                    chb=int(chiken_briyani.get())
                except:
                    chb=0
                try:
                    mub=int(mutton_briyani.get())
                except:
                    mub=0
                try:
                    beb=int(beef_briyani.get())
                except:
                    beb=0
                try:
                    c65=int(chiken_65.get())
                except:
                    c65=0
                try:
                    less=int(bounless.get())
                except:
                    less=0
                try:
                    gril=int(chiken_gril_full.get())
                except:
                    gril=0
                try:
                    th=int(chiken_thandoori_full.get())
                except:
                    th=0
                try:
                    so=int(lime_soda.get())
                except:
                    so=0
                try:
                    lim=int(lime_jucie.get())
                except:
                    lim=0
                try:
                    blu=int(blueberry.get())
                except:
                    blu=0

                costofvegbri=vegb*100
                costofegg=egb*120
                costofchibr=chb*150
                costofmunbri=mub*200
                costofbeefbri=beb*150
                costofch65=c65*100
                costofbouns=less*100
                costofchgril=gril*400
                costofthandori=th*450
                costofsoda=so*40
                costoflime=lim*50
                costofblue=blu*50

                f4.place(x=750,y=300)
                f4.config(bg='cyan')

                f5=Frame(f4,width=400,height=40,relief=RAISED,bd=10,bg='#4D0049')
                f5.grid(row=6,column=1)
                l=Label(f5,text='Gentrate Bill',font=('aria',20,'bold'),fg='#ff4a4a',bg='#4D0049')
                l.pack()
                
                bill=Label(f4,text='Bill no',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                bill.grid(row=0,column=0)
                e6=Entry(f4,textvar=rand,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e6.grid(row=0,column=1)
                
                date1=Label(f4,text='Date',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                date1.grid(row=1,column=0)
                e7=Entry(f4,textvar=date,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e7.grid(row=1,column=1)
                
                cost1=Label(f4,text='Cost',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                cost1.grid(row=2,column=0)
                e4=Entry(f4,textvar=cost,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e4.grid(row=2,column=1)
                
                charge=Label(f4,text='serivce charge',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                charge.grid(row=3,column=0)
                e2=Entry(f4,textvar=servicescharge,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e2.grid(row=3,column=1)

                tax1=Label(f4,text='Tax',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                tax1.grid(row=4,column=0)
                e3=Entry(f4,textvar=tax,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e3.grid(row=4,column=1)

                total1=Label(f4,text='Total',padx=5,font=('aria',10,'bold'),fg='blue4',bg='cyan',width=17,bd=6)
                total1.grid(row=5,column=0)
                e1=Entry(f4,textvar=Total,bd=3,width=20,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
                e1.grid(row=5,column=1)


                #this section are customer tax and product tax and an gst process of an calulatiion are an ised
                totalcost=costofvegbri+costofchibr+costofegg+costofmunbri+costofbeefbri+costofch65+costofbouns+costofchgril+costofthandori+costofsoda+costoflime+costofblue
                costmeal=str("Rs.%2f" % totalcost)

                paytax=(totalcost*0.05)
                paidtax=str("Rs.%2f" % paytax)

                servicechrage=(totalcost * 0.01)
                service=str("Rs.%2f" % servicechrage)

                overall=paytax+servicechrage+totalcost
                total=str("RS.%2f" % overall)

                servicescharge.set(service)
                cost.set(costmeal)
                tax.set(paidtax)
                Total.set(total)
    
            rand=StringVar()
            date=StringVar()
            tax=StringVar()
            Total=StringVar()
            cost=StringVar()
            servicescharge=StringVar()
            veg_briyani=StringVar()
            egg_briyani=StringVar()
            chiken_briyani=StringVar()
            mutton_briyani=StringVar()
            beef_briyani=StringVar()
            chiken_65=StringVar()
            bounless=StringVar()
            chiken_gril_full=StringVar()
            chiken_thandoori_full=StringVar()
            lime_soda=StringVar()
            lime_jucie=StringVar()
            blueberry=StringVar()
            
            l=Label(f3,text='VegBriyani Rs 100',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l.grid(row=0,column=0)
            e1=Entry(f3,textvar=veg_briyani,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e1.grid(row=0,column=1)

            l1=Label(f3,text='EggBriyani Rs 120',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l1.grid(row=1,column=0)
            e2=Entry(f3,textvar=egg_briyani,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e2.grid(row=1,column=1)

            l2=Label(f3,text='ChikenBriyani Rs 150',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l2.grid(row=2,column=0)
            e3=Entry(f3,textvar=chiken_briyani,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e3.grid(row=2,column=1)

            l4=Label(f3,text='MuttonBriyani Rs 200',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l4.grid(row=3,column=0)
            e4=Entry(f3,textvar=mutton_briyani,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e4.grid(row=3,column=1)

            l5=Label(f3,text='BeefBriyani Rs 150',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l5.grid(row=4,column=0)
            e5=Entry(f3,textvar=beef_briyani,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e5.grid(row=4,column=1)

            l6=Label(f3,text='Chikengril(full) Rs 400',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l6.grid(row=5,column=0)
            e6=Entry(f3,textvar=chiken_gril_full,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e6.grid(row=5,column=1)
            
            l7=Label(f3,text='Thandoori(ful) Rs 450',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l7.grid(row=6,column=0)
            e7=Entry(f3,textvar=chiken_thandoori_full,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e7.grid(row=6,column=1)
            
            l8=Label(f3,text='Chiken65 Rs 100',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l8.grid(row=7,column=0)
            e8=Entry(f3,textvar=chiken_65,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e8.grid(row=7,column=1)
            
            l9=Label(f3,text='Bounless Rs 100',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l9.grid(row=8,column=0)
            e9=Entry(f3,textvar=bounless,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e9.grid(row=8,column=1)
            
            l10=Label(f3,text='Limesoda Rs 40',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l10.grid(row=9,column=0)
            e10=Entry(f3,textvar=lime_soda,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e10.grid(row=9,column=1)
            
            l11=Label(f3,text='Limejucie Rs 50',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l11.grid(row=10,column=0)
            e11=Entry(f3,textvar=lime_jucie,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e11.grid(row=10,column=1)
            
            l12=Label(f3,text='Blueberry Rs 50',padx=5,font=('aria',10,'bold'),fg='blue4',bg='yellow',width=15,bd=10)
            l12.grid(row=11,column=0)
            e12=Entry(f3,textvar=blueberry,bd=6,width=12,fg='blue4',bg='misty rose',font=('aria',20,'bold'))
            e12.grid(row=11,column=1)
            
            b=Button(w,text='Gentrate',bd=5,command=gentrate,padx=10,pady=10,fg='black',bg='green',width=14,font=('arial',15,'bold'))
            b.place(x=400,y=180)

            b1=Button(w,text='Reset',command=reset,bd=5,padx=10,pady=10,fg='black',bg='orange',width=14,font=('arial',15,'bold'))
            b1.place(x=400,y=300)

            b2=Button(w,text='Exit',command=qexit,bd=5,padx=10,pady=10,fg='black',bg='red',width=14,font=('arial',15,'bold'))
            b2.place(x=400,y=420)

            b3=Button(w,text='Save',command=save,bd=5,padx=10,pady=10,fg='black',bg='pink',width=14,font=('arial',15,'bold'))
            b3.place(x=400,y=520)

            b4=Button(w,text='Billing',command=save_bill,bd=5,padx=10,pady=10,fg='black',bg='purple',width=14,font=('arial',15,'bold'))
            b4.place(x=400,y=610)


            
            
            
            w.mainloop()
                
        else:
            messagebox.showerror('Invalid','Invalid username and password')
#=====================sign up page======================================================================            
    #this function are if not any of an account in us worker create an new account and store an worker id
    def signcommand():
        newwin2=Tk()
        newwin2.geometry('500x500')
        newwin2.title('Sign up')
        newwin2.config(bg='#4D0039')
        newwin2.resizable(0,0)
        head1=Label(newwin2,text='Welcome To Restaurant Signup',font=('Algerian',20,'bold'),relief=RAISED,bd=10,fg='#ff4a4a',bg='#4D0039')
        head1.pack(fill=X)
        #frame created and user name create
        f1=Frame(newwin2,width=350,height=430,bg='lightgreen',relief=RAISED,bd=20)
        f1.place(x=80,y=60)
        head=Label(f1,text='Sign up',font=('Microsoft Yahei UI Light',23,'bold'),fg='#57a1f8',bg='lightgreen')
        head.place(x=100,y=5)
        

        def enter(e):
            user.delete(0,END)
        def leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')
        
        user=Entry(f1,width=25,fg='black',bg='white',font=('Microsoft Yahei UI Light',11,'bold'),border=1,relief=RAISED,bd=10)
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>',enter)
        user.bind('<FocusOut>',leave)
          #password create
        def enter(e):           
            password.delete(0,END)
        def leave(e):
            name=password.get()
            if name=='':
                user.insert(0,'password')
        password=Entry(f1,width=25,fg='black',bg='white',font=('Microsoft Yahei UI Light',11,'bold'),border=1,bd=10,relief=RAISED)
        password.place(x=30,y=150)
        password.insert(0,'password')
        password.bind('<FocusIn>',enter)
        password.bind('<FocusOut>',leave)
          #confirm password
        def enter(e):           
            conform_passwd.delete(0,END)
        def leave(e):
            name=conform_passwd.get()
            if name=='':
                user.insert(0,'conform password')
        conform_passwd=Entry(f1,width=25,fg='black',bg='white',font=('Microsoft Yahei UI Light',11,'bold'),border=1,bd=10,relief=RAISED)
        conform_passwd.place(x=35,y=220)
        conform_passwd.insert(0,'conform password')
        conform_passwd.bind('<FocusIn>',enter)
        conform_passwd.bind('<FocusOut>',leave)

        def signup():
            name=user.get()
            passwd=password.get()
            cnpass=conform_passwd.get()
            #this an given user name and password are created sucessfully can sote an worker id in
            #given file formate
            if passwd==cnpass:
                try:
                    #this file are can change an normal text of user and password are change to dict formate and
                    #sotore an key values
                    file=open(r"C:\\Users\\siva\\Documents\\data.txt.txt",'r+')
                    d=file.read()
                    r=ast.literal_eval(d)

                    dict2={name:passwd}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()
                    #create an new account is sucess given an message and save an data.txt file us user and password
                    file=open(r"C:\\Users\\siva\\Documents\\data.txt.txt",'w')
                    w=file.write(str(r))
                    messagebox.showinfo('sign up','sucessfully sign up')
                    newwin2.destroy()

                except:
                    file=open(r"C:\\Users\\siva\\Documents\\data.txt.txt",'w')
                    pp=str({'username':'password'})
                    file.write(pp)
                    file.close()
            else:
                messagebox.showerror('Invalid','Both Password should not matched')

        def signin():
            newwin2.destroy()
            

        b1=Button(f1,text='Sign up',command=signup,relief=RIDGE,bd=10,width=27,pady=7,font=('Microsoft Yahei UI Light',9,'bold'),bg='purple',fg='white')
        b1.place(x=35,y=280)
        l2=Label(f1,text="I Have An Account?",bg='white',fg='black',font=('Microsoft Yahei UI Light',9,'bold'))
        l2.place(x=55,y=340)
        singin=Button(f1,text='Sign in',command=signin,bg='white',fg='lightgreen',font=('Microsoft Yahei UI Light',9,'bold'),cursor='hand2',width=6)
        singin.place(x=220,y=340)
        newwin.mainloop()            
#======================================================================================================
#login page balnce button section        
    b1=Button(f1,text='Sign in',command=signin,relief=GROOVE,bd=10,width=27,pady=7,font=('Microsoft Yahei UI Light',9,'bold'),bg='purple',fg='white')
    b1.place(x=35,y=204)
    l2=Label(f1,text="Don't have an account?",bg='white',fg='black',font=('Microsoft Yahei UI Light',9,'bold'))
    l2.place(x=55,y=270)
    singup=Button(f1,text='Sign up',command=signcommand,bg='lightgreen',fg='#57a1f8',font=('Microsoft Yahei UI Light',9,'bold'),cursor='hand2',width=6)
    singup.place(x=220,y=270)
#=====================home page main windows================================================================    
b=Button(win,text='Login',command=login,font=('Perpetua Titling MT',10,'bold'),pady=5,width=15,bg='green',fg='white',activebackground='#009432',activeforeground='black')
b.place(x=1000,y=75)
#side part frame f1
f1=LabelFrame(win,relief=RAISED,bd=20,bg='lavender')
f1.place(x=10,y=70,width=300,height=600)
l20=Label(f1,text='WELCOME TO EVERYONE!',font=('Goudy Old Style',15,'bold'),bg='lavender',fg='#ff4a4a')
l20.place(x=0,y=20)
l5=Label(f1,text='Home',font=('Goudy Old Style',20,'bold'),bg='lavender',fg='#000053')
l5.pack(pady=60,fill=X)
l6=Label(f1,text='Address',font=('Goudy Old Style',20,'bold'),bg='lavender',fg='#000053',padx=10)
l6.place(x=75,y=100)
l7=Label(f1,text='Ottagapalayam 99th Street,',font=('Goudy Old Style',10,'bold'),bg='lavender',fg='#ff4a4a')
l7.place(x=20,y=140)
l8=Label(f1,text='Vadaplani',font=('Goudy Old Style',10,'bold'),bg='lavender',fg='#ff4a4a')
l8.place(x=170,y=140)
l9=Label(f1,text='Chennai',font=('Goudy Old Style',15,'bold'),bg='lavender',fg='#ff4a4a',padx=25)
l9.place(x=60,y=160)
l10=Label(f1,text='Timing',font=('Goudy Old Style',20,'bold'),bg='lavender',fg='#000053',padx=10)
l10.pack(pady=35)
l11=Label(f1,text="Week Day's",font=('Goudy Old Style',15,'bold'),bg='lavender',fg='purple')
l11.place(x=80,y=235)
l13=Label(f1,text="[Monday-Saturday]",font=('Goudy Old Style',15,'bold'),bg='lavender',fg='purple')
l13.place(x=50,y=265)
l12=Label(f1,text='9:00AM TO 10:00PM',font=('Goudy Old Style',10,'bold'),bg='lavender',fg='#ff4a4a')
l12.place(x=70,y=295)
l14=Label(f1,text='Sunday Only',font=('Goudy Old Style',15,'bold'),bg='lavender',fg='purple')
l14.place(x=80,y=320)
l15=Label(f1,text='9:00AM TO 6:00PM',font=('Goudy Old Style',10,'bold'),bg='lavender',fg='#ff4a4a')
l15.place(x=75,y=350)
l16=Label(f1,text="'Food's Your",font=('Goudy Old Style',15,'bold'),bg='lavender',fg='blue')
l16.place(x=80,y=380)
l17=Label(f1,text="Common Ground",font=('Goudy Old Style',15,'bold'),bg='lavender',fg='blue')
l17.place(x=60,y=410)
l18=Label(f1,text="A Universal Experience!'",font=('Goudy Old Style',15,'bold'),bg='lavender',fg='blue')
l18.place(x=30,y=440)
l18=Label(f1,text="🍨 🔁 🍽 🔁 😴",font=('Goudy Old Style',20,'bold'),bg='lavender',fg='blue')
l18.place(x=40,y=470)
#======================================================================================================
#=====================Menu section child window========================================================
#this menu bar are used menu bar is show an window and windows of an formate are an used
#can is only us show us one windows to child windows are an shows
def menulist():
    newwin=Toplevel(win)
    newwin.geometry('1100x600')
    newwin.title("Menu Details")
    newwin.config(bg='#4D0039')
    newwin.resizable(0,0)
    l=Label(newwin,text='Mother Indian Food Menu',width=1600,relief=RAISED,bd=20,font=('Algerian',20,'bold'),fg='#ff4a4a',bg='#4D0039',pady=5)
    l.pack()
    f=LabelFrame(newwin,width=330,height=450,relief=RAISED,bd=20,bg='#474778')
    f.place(x=10,y=80)
    l1=Label(f,text='VEG STARTER',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),pady=10,padx=30)
    l1.grid(row=0,column=0)
    l2=Label(f,text='💥 Samosa Rs 20',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l2.grid(row=1,column=0)
    l3=Label(f,text='💥 Veg.Spring rolls Rs 50',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l3.grid(row=2,column=0)
    l4=Label(f,text='💥 Veg.Momos Rs 70',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l4.grid(row=3,column=0)
    l5=Label(f,text='💥 Veg.Manchurian  Rs 100',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l5.grid(row=4,column=0)
    l6=Label(f,text='💥 Mushroom 65 Rs 70',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l6.grid(row=5,column=0)
    l7=Label(f,text='NON-VEG STARTER',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),padx=30,pady=10)
    l7.grid(row=6,column=0)
    l8=Label(f,text='💥 Chicken.Momos Rs 99',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l8.grid(row=7,column=0)
    l9=Label(f,text='💥 Chicken.Shwarma Rs 99',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l9.grid(row=8,column=0)
    l10=Label(f,text='💥 Chicken 65 Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l10.grid(row=9,column=0)
    l11=Label(f,text='💥 Chicken.Manchurian Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l11.grid(row=10,column=0)
    l12=Label(f,text='💥 Chicken.Lollipop Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l12.grid(row=11,column=0)     
    f1=LabelFrame(newwin,width=330,height=450,relief=RAISED,bd=20,bg='#474778')
    f1.place(x=385,y=80)
    l1=Label(f1,text='INDIAN CURRIES',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),pady=10,padx=30)
    l1.grid(row=0,column=0)
    l2=Label(f1,text='💥 Chicken Curry Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l2.grid(row=1,column=0)
    l3=Label(f1,text='💥 Chicken Masala Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l3.grid(row=2,column=0)
    l4=Label(f1,text='💥 Butter Chicken Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l4.grid(row=3,column=0)
    l5=Label(f1,text='💥 Kadhai Chiken  Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l5.grid(row=4,column=0)
    l6=Label(f1,text='💥 Chicken Korma Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l6.grid(row=5,column=0)
    l7=Label(f1,text='INDIAN BREADS',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),padx=30,pady=10)
    l7.grid(row=6,column=0)
    l8=Label(f1,text='💥 Tawa Roti Rs 30',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l8.grid(row=7,column=0)
    l9=Label(f1,text='💥 Plain Naan Rs 40',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l9.grid(row=8,column=0)
    l10=Label(f1,text='💥 Butter Naan Rs 45',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l10.grid(row=9,column=0)
    l11=Label(f1,text='💥 Rumali Roti Rs 45',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l11.grid(row=10,column=0)
    l12=Label(f1,text='💥 Chapathi Rs 30',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l12.grid(row=11,column=0)      
    f2=LabelFrame(newwin,width=330,height=450,relief=RAISED,bd=20,bg='#474778')
    f2.place(x=730,y=80)
    l1=Label(f2,text='BRIYANI',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),pady=10,padx=30)
    l1.grid(row=0,column=0)
    l2=Label(f2,text='💥 Chicken.Briyani Rs 120',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l2.grid(row=1,column=0)
    l3=Label(f2,text='💥 Mutton.Briyani Rs 150',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l3.grid(row=2,column=0)
    l4=Label(f2,text='💥 Beef.Briyani Rs 120',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l4.grid(row=3,column=0)
    l5=Label(f2,text='💥 Egg.Briyani Rs 80',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l5.grid(row=4,column=0)
    l6=Label(f2,text='💥 Veg.Briyani Rs 60',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l6.grid(row=5,column=0)
    l7=Label(f2,text='DRINKS&ICECREAM',fg='#ff4a4a',bg='#474778',font=('Algerian',15,'bold'),padx=30,pady=10)
    l7.grid(row=6,column=0)
    l8=Label(f2,text='💥 Lime.Juice Rs 30',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l8.grid(row=7,column=0)
    l9=Label(f2,text='💥 Lime.Soda Rs 40',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l9.grid(row=8,column=0)
    l10=Label(f2,text='💥 Blueberry Rs 40',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l10.grid(row=9,column=0)
    l11=Label(f2,text='💥 Vennila Rs 50',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l11.grid(row=10,column=0)
    l12=Label(f2,text='💥 Choloate Rs 50',fg='white',bg='#474778',font=('aria',15,'bold'),padx=5)
    l12.grid(row=11,column=0)      
 
    b1=Button(newwin,text='Exit',bg='red',fg='white',command=newwin.destroy,width=20,pady=10,activebackground='red',activeforeground='pink')
    b1.pack(side=BOTTOM)
menubar=Menu(win)
filename=Menu(menubar,tearoff=0)
filename.add_command(label='Menu Details',command=menulist)
filename.add_separator()
filename.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='Menu',menu=filename)
win.config(menu=menubar)
#========================about child window==============================================================
def carrier():
    newwin5=Toplevel(win)
    newwin5.geometry('1100x500')
    newwin5.title('About Company')
    newwin5.resizable(0,0)
    l=HTMLLabel(newwin5,html='<img src="C:\\Users\\siva\\Pictures\\1223.png">')
    l.place(x=330,y=10,width=450,height=300)
    l1=Label(newwin5,text="☑️Mother Indian is a Indian themed Restaurant located in the heart of Chennai,Vadaplani.")
    l1.place(x=250,y=230)
    l3=Label(newwin5,text="☑️We are the leading food chain that is famous for its exotic spices, delicate herbs, and a fun dining experience")
    l3.place(x=250,y=250)
    l2=Label(newwin5,text="☑️We have a wide menu list that includes Briyani , Indian Curries, Indian Breads , Jucies & Icecream.")
    l2.place(x=250,y=270)
    l4=Label(newwin5,text="☑️We serve quality western food at fair prices and are the highest rated restaurant on google in Chennai")
    l4.place(x=250,y=290)
    l5=Label(newwin5,text="☑️For serving delicious and lip smacking dishes, Mother Indian has become the first choice for foodies in Chennai.")
    l5.place(x=250,y=310)
    l5=Label(newwin5,text="☑️Mother will spread its aroma all over Tamil Nadu in the near future,All the food on the Mother menu is cooked to order.")
    l5.place(x=250,y=330)
    l5=Label(newwin5,text="☑️He finest ingredients are delivered to the restaurants daily to maintain the highest quality and hygiene standards.")
    l5.place(x=250,y=350)
    l5=Label(newwin5,text="☑️Being the best restaurant near you, Mother Restaurant is committed to providing excellent food, service.")
    l5.place(x=250,y=370)
    l6=Label(newwin5,text="☑️And an unforgettable dining experience for you and your family")
    l6.place(x=250,y=390)    
    b1=Button(newwin5,text='Exit',bg='red',fg='white',command=newwin5.destroy,width=20,activebackground='red',activeforeground='pink')
    b1.pack(side=BOTTOM,pady=5)
    newwin5.mainloop()
aboutname=Menu(menubar,tearoff=0)
aboutname.add_command(label='About Restarunt',command=carrier)
aboutname.add_separator()
aboutname.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='About',menu=aboutname)
win.config(menu=menubar)
#==========================gallery child win===========================================================
def TableBooking():
    newwin=Toplevel(win)
    newwin.geometry('1100x500')
    newwin.title('Tables View')
    newwin.config(bg='pink')
    newwin.resizable(0,0)
    #images create
    l=HTMLLabel(newwin,html='<img src="C:\\Users\\siva\\Documents\\table11">')
    l.config(bg='pink')
    l.place(x=0,y=0,width=300,height=200)
    l5=Label(newwin,text='Table 1',bg='pink',font=('times',15,'bold'))
    l5.place(x=100,y=340)
    l1=HTMLLabel(newwin,html='<img src="C:\\Users\\siva\\Documents\\table6">')
    l1.config(bg='pink')
    l1.place(x=320,y=0,width=350,height=200)
    l2=HTMLLabel(newwin,html='<img src="C:\\Users\\siva\Documents\\table5">')
    l2.config(bg='pink')
    l2.place(x=700,y=0,width=350,height=200)
    l3=HTMLLabel(newwin,html='<img src="C:\\Users\\siva\\Documents\\table3">')
    l3.config(bg='pink')
    l3.place(x=0,y=250,width=350,height=200)
    l4=HTMLLabel(newwin,html='<img src="C:\\Users\\siva\\Documents\\table2">')
    l4.config(bg='pink')
    l4.place(x=400,y=250,width=350,height=200)




    #b2=Button(newwin,text="Table Booking",bg='gold',fg='black',font=('times',15,'bold'),padx=5,pady=5)
    #b2.place(x=850,y=300)
    b1=Button(newwin,text='EXIT',bg='red',fg='white',command=newwin.destroy,width=20,activebackground='red',activeforeground='pink')
    b1.pack(side=BOTTOM)
    newwin.mainloop()
galname=Menu(menubar,tearoff=0)
galname.add_command(label='Tables View',command=TableBooking)
galname.add_separator()
galname.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='Booking',menu=galname)
win.config(menu=menubar)
#=======================================combo child win=================================================
win.mainloop()

