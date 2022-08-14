from cProfile import label
from tkinter import *

window= Tk()
window.title('BMI CALCULATOR')
window.geometry('400x400')

window.configure(bg='blue')

heading_label= Label(window, text='BMI CALCULATOR', fg='yellow', bg='red', font=('Calbri',20) , bd=5)
heading_label.place(x=50, y=20)

name_label= Label(window, text='Enter you name', fg='black' , font=('Calbri',10))
name_label.place(x=50, y=90)

user_name= Entry(window, text='', bd=2, width=22)
user_name.place(x=180, y=90)

height_label= Label(window, text='Enter you height', fg='black' , font=('Calbri',10))
height_value= Entry(window, text='', bd=2, width=22)
height_label.place(x=50, y=160)
height_value.place(x=180, y=160)

weight_label= Label(window, text='Enter you weight', fg='black' , font=('Calbri',10))
weight_value= Entry(window, text='', bd=2, width=22)
weight_label.place(x=50, y=230)
weight_value.place(x=180, y=230)

result_frame= LabelFrame(window, text='RESULT', bg= 'black',fg='white',font=('Calbri',20))
result_frame.place(x=50, y=330)
result_frame.pack(padx=20,pady=20)

result_label= Label(result_frame, text='RESULT', bg='white', fg='black',font=('Calbri',15))
result_label.place(x=10, y=20)
result_label.pack()
window.mainloop()