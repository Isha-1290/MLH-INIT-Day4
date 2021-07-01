from tkinter import *
from tkcalender import *

root = Tk()
root.title('calender')
root.minisize(800, 600)
root.configure(backgroung="#A1CDEC")

def selectDate():
    myDate = myCal.get_date()
    selectedDate = Label(text = myDate)
    selectedDate.place(x=425, y=350)

myCal = Calender(root, setmode = 'day' , date_pattern = 'd/m/yy')
myCal.place(x=350, y=100)

openCal = Button(root, text = 'select done', command = selectDate)
openCal.place(x=425, y=300)
