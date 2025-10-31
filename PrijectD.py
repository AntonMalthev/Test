from customtkinter import *
from PIL import Image
from tkinter import messagebox




win = CTk()
win.geometry('1000x800')
win.title('Тест')




img = Image.open('Nissan.jpg')
img_ctk = CTkImage(light_image=img, size=(200, 200))

label1 = CTkLabel(win, text='Назва проекту ', font=("None", 30, "bold"), text_color="red")
label1.grid(row=0, column=0,columnspan=3)




label2 = CTkLabel (win, text='', image=img_ctk)
label2.grid(row=1, column=1)

frame = CTkFrame(master=win, width=200, height=200)
frame.grid(row=2,column=1)
q1=CTkLabel (frame, text='У якому році засновали Нісан')
q1.grid(row=0, column=1)
radio_var = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame, text="1933",variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(frame, text="1921", variable= radio_var, value=2)
radiobutton_3 = CTkRadioButton(frame, text="1942", variable= radio_var, value=3)
radiobutton_1.grid(row=1,column=1)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)


frame = CTkFrame(master=win, width=200, height=200)
frame.grid(row=2,column=1)
q1=CTkLabel (frame, text='Хто засновав Ніссан')
q1.grid(row=0, column=1)
radio_var = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame, text="Аїкава Йосісуке",variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(frame, text="Ден Кендзіро", variable= radio_var, value=2)
radiobutton_3 = CTkRadioButton(frame, text="William R. Gorham", variable= radio_var, value=3)
radiobutton_1.grid(row=1,column=1)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)


frame = CTkFrame(master=win, width=200, height=200)
frame.grid(row=2,column=1)
q1=CTkLabel (frame, text='Яка найдорожча модель Ніссан')
q1.grid(row=0, column=1)
radio_var = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame, text="Nissan GT-R NISMO Special Edition",variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(frame, text="Nissan N-7", variable= radio_var, value=2)
radiobutton_3 = CTkRadioButton(frame, text="Nissan Leaf", variable= radio_var, value=3)
radiobutton_1.grid(row=1,column=1)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)

win.mainloop()