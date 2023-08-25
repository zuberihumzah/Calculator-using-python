#Calculator:- I am building a basic calculator using python.....
from tkinter import *
GUI_root = Tk()
#GUI logic here

#width X height
GUI_root.geometry("500x590")
#for max and min size we use , as a differentitater between width and height
GUI_root.minsize(500,590)
GUI_root.maxsize(500,590)

#lets add label to this program
humzah=Label(text="MADE BY ZUBERI HUMZAH",bg="black",
fg="white",font="timesnewroman 18 bold italic",borderwidth=5,relief=GROOVE)

#lets also pack this label in the GUI
humzah.pack(fill=X)

#lets add title to our calculator
GUI_root.title("CALCULATOR")

#lets add icon to the calculator
GUI_root.wm_iconbitmap("1.ico")

#lets define what will hapen when we click the buttons
def click(event):
    global entry
    text=event.widget.cget("text")

    if text=="=":
        if entry.get().isdigit():
            value=int(entry.get())
        else:
            #we are trying to handle exceptions also and update the screen to an Error message, also the exception will be printed if occured
            try:
                value=eval(entry.get())   
            except Exception as e:
                print(e)
                value="ERROR"  

                  
        entry.set(value)
        screen.update()
        
    elif text=="C":
        entry.set("")
        screen.update()
    
    else:
        entry.set(entry.get() + text)
        screen.update()
    

entry=StringVar()
entry.set("")
screen=Entry(GUI_root,textvar=entry,font="timesnewroman 30 bold").pack(fill=X,ipadx=8,padx=10,pady=10)

#lets add frames
f1=Frame(GUI_root,bg="grey")
f1.pack(padx=10,pady=0,fill=X)

#lets add buttons to the frame
b=Button(f1,text="9",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="8",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="7",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="+",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)


#lets add more frames
f1=Frame(GUI_root,bg="grey")
f1.pack(padx=10,pady=0,fill=X)

#lets add more buttons to the frame
b=Button(f1,text="6",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="5",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="4",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="-",font="lucida 33 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)


#lets add more frames
f1=Frame(GUI_root,bg="grey")
f1.pack(padx=10,pady=0,fill=X)

#lets add more buttons to the frame
b=Button(f1,text="3",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="2",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="1",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="*",font="lucida 33 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)


#lets add more frames
f1=Frame(GUI_root,bg="grey")
f1.pack(padx=10,pady=0,fill=X)

#lets add more buttons to the frame
b=Button(f1,text="=",font="lucida 33 bold")
b.pack(side=RIGHT,padx=25,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="C",font="lucida 30 bold")
b.pack(side=RIGHT,padx=25,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text="0",font="lucida 30 bold")
b.pack(side=RIGHT,padx=30,pady=15)
b.bind("<Button-1>",click)

b=Button(f1,text=" / ",font="lucida 30 bold")
b.pack(side=RIGHT,padx=25,pady=15)
b.bind("<Button-1>",click)

#now lets finish our program
GUI_root.mainloop()

