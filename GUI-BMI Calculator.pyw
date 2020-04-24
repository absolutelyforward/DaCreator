from tkinter import *
root = Tk()
root.title('Overweight or not')
root.geometry('300x180')
realweight = IntVar()
realheight = IntVar()
lblweight = Label(root, text="Weight(Kg)").place(x=30,y=30)
askweight = Entry(root, textvariable=realweight).place(x=120,y=30)
lblheight = Label(root, text="Height(Cm)").place(x=30,y=70)
askheight = Entry(root, textvariable=realheight).place(x=120,y=70)

def bmi():
    bmi = realweight.get()/(realheight.get()**2)*10000
    if(bmi > 0 and bmi < 18.5):
        ans = Label(root, text="You are underweight").place(x=120,y=110)
    elif(bmi > 18.5 and bmi < 24.9):
        ans = Label(root, text="You are normal").place(x=120,y=110)
    elif(bmi > 24.9 and bmi < 30):
        ans = Label(root, text="You are overweight").place(x=120,y=110)
    else:
        ans = Label(root, text="You are obese").place(x=120,y=90)
B1 = Button(root,text='Get Result', command=bmi ) .place(x=30,y=100)       
root.mainloop()
