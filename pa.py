
from tkinter import * #Import tkinter library
import tkinter.font as tkFont

#options for  choosing the states
options=['Andaman and Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu and Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telengana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

#Defining a function to calculate imr
def IMR():
    valinp.delete(first=0,last= 100)
    inf=infinp.get()
    inf=int(inf)
    decr=decinp.get()
    decr=int(decr)
    state1=variable.get()
    res=((decr/inf)*1000)
    mystr=str(res)
    valinp.insert(0,mystr)
    infinp.delete(first=1,last=100)
    decinp.delete(first=1,last=100)

#Defining a function to calculate cmr
def CMR():
    valinp.delete(first=1,last=100)
    reck=recinp.get()
    reck=int(reck)
    decr=decinp.get()
    decr=int(decr)
    state1=variable.get()
    res=((decr/(reck+decr))*100)
    mystr="CMR Result of "+state1+" is "+str(res)
    valinp.insert(0,mystr)
    recinp.delete(first=1,last=100)
    decinp.delete(first=1,last=100)

#For initialisation
win = Tk()

#Window title
win.title("Pandemic Calculator")

#dimensions of window
win.geometry('600x400')
win.configure(bg="OliveDrab2")

#font declaration
fontStyle = tkFont.Font(family="Arial", size=40)
fontStyle1 = tkFont.Font(family="Arial", size=20)
fontStyle2=tkFont.Font(family="Arial", size=20)

#Title of analyzer
titlepan = Label(win,text="Pandemic Calculator",font=fontStyle)
titlepan.place(x=250, y=25, anchor="center")

#State  List
state = Label(win,text="Choose State",font=fontStyle1)
state.place(x=125, y=85, anchor="center")
variable = StringVar(win)
variable.set(options[0])
states = OptionMenu(win, variable, *options)
states.place(x=300, y=85, anchor="center")

#Confirmed Label
confirmed = Label(win,text="Confirmed",font=fontStyle1,fg="green")
confirmed.place(x=125, y=120, anchor="center")
infinp= Entry(win,bd=1,bg="white")
infinp.place(x=300, y=120, anchor="center")

#Recovered Label
recovered = Label(win,text="Recovered",font=fontStyle1,fg="orange")
recovered.place(x=125, y=155, anchor="center")
recinp=Entry(win,bd=1,bg="white")
recinp.place(x=300,y=155,anchor="center")

#Death Label
Death  = Label(win,text="Deaths",font=fontStyle1,fg="red")
Death.place(x=125, y=190, anchor="center")
decinp = Entry(win,bd=1,bg="white")
decinp.place(x=300,y=190,anchor="center")

#IMR & CMR Buttons
imrbtn=Button(win,text="IMR",width=5,height=1,command=IMR)
imrbtn.place(x=200,y=220,anchor="center")
cmrbtn=Button(win,text="CMR",width=5,height=1,command=CMR)
cmrbtn.place(x=300,y=220,anchor="center")

#Result
Result = Label(win,text="Result",font=fontStyle1)
Result.place(x=125, y=250, anchor="center")
valinp = Entry(win,bd=1,width=25)
valinp.place(x=300, y=250, anchor="center")
win.mainloop()
