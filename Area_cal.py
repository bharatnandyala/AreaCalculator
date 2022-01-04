from tkinter import *

window = Tk()
window.title("Area of Triangle")
window.geometry('300x300')

label1 = Label(window, text='Enter Height')
label1.config(fg='blue')
label1.config(font=('Arial', 14))
label1.grid(row=0, column=0, padx=5, pady=10)
'''Storing the label1 data into data1'''
height = IntVar()
'''First Text box creation'''
textbox1 = Entry(window, textvariable=height)
textbox1.config(fg='black')
textbox1.config(font=('Arial', 10))
textbox1.grid(row=0, column=1)

label2 = Label(window, text='Enter Breadth')
label2.config(fg='blue')
label2.config(font=('Arial', 14))
label2.grid(row=1, column=0, padx=5, pady=10)

'''Storing the label2 data into data2'''
breadth = IntVar()

'''Second Text box creation'''
textbox2 = Entry(window, textvariable=breadth)
textbox2.config(fg='black')
textbox2.config(font=('Arial', 10))
textbox2.grid(row=1, column=1)

'''Button Function'''


def click():
    emptylabel.config(text='Height:' + str(height.get()))
    emptylabel2.config(text='Base:' + str(breadth.get()))
    area = 0.5 * height.get() * breadth.get()
    emptylabel3.config(text='Area : ' + str(area))


'''Function for a Button'''

button = Button(window, text='Calculate')
button.config(fg='black')
button.config(font=('Arial', 10, 'bold'))
button.grid(row=2, column=1, padx=10, pady=20)
button.config(command=click)

'''creating a empty label to show the output'''
emptylabel = Label(window)
emptylabel.config(fg='green')
emptylabel.config(font=('Arial', 10, 'bold'))
emptylabel.grid(row=3, column=1, sticky=W)

'''creating a empty label2 to show the output'''
emptylabel2 = Label(window)
emptylabel2.config(fg='green')
emptylabel2.config(font=('Arial', 10, 'bold'))
emptylabel2.grid(row=4, column=1, sticky=W)

'''creating a empty label2 to show the output'''
emptylabel3 = Label(window)
emptylabel3.config(fg='green')
emptylabel3.config(font=('Arial', 10, 'bold'))
emptylabel3.grid(row=5, column=1, sticky=W)

window.mainloop()
