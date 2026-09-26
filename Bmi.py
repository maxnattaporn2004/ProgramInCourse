from tkinter import *
from math import *
def resltBmi():
    weight = float(textboxWeight.get())
    height = float(textboxHeight.get())
    result = weight / pow((height / 100),2)
    return round(result,2)
def leftCliclkCalBmi(event):
    Bmi = resltBmi()
    if Bmi > 30:
        labelresult.configure(text="อ้วนมาก")
    elif 25 < Bmi < 30:
        labelresult.configure(text="อ้วน")
    elif 18.6 < Bmi < 22.9:
        labelresult.configure(text="ปกติ")
    elif Bmi < 18.5:
        labelresult.configure(text="ผอมเกินไป")
    labelresultnum.configure(text = Bmi)

main = Tk()
main.title("HealthBMI")
labelHeight = Label(main,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textboxHeight =Entry(main)
textboxHeight.grid(row=0,column=1)
textboxHeight.get()
labelWeight = Label(main,text="น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textboxWeight =Entry(main)
textboxWeight.grid(row=1,column=1)
labelresult = Label(main,text="result")
labelresult.grid(row=2,column=1)
labelresultnum = Label(main,text="result")
labelresultnum.grid(row=2,column=2)
buttonCal = Button(main,text="คำนวณ")
buttonCal.bind("<Button-1>",leftCliclkCalBmi)
buttonCal.grid(row=2,column=0)
main.mainloop()