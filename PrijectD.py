from customtkinter import *
from PIL import Image
from tkinter import messagebox

win = CTk()
win.geometry('1400x800+10+10')
win.title('Тест')

label1 = CTkLabel(win, text='Car Test', font=("None", 30, "bold"), text_color="red")
label1.grid(row=0, column=0,columnspan=3)

img1 = Image.open('Nissan.jpg')
img_ctk1 = CTkImage(light_image=img1, size=(200, 200))


img2 = Image.open('Skoda.jpg')
img_ctk2 = CTkImage(light_image=img2, size=(200, 200))

img3 = Image.open('Volkswagen.jpg')
img_ctk3 = CTkImage(light_image=img3, size=(200, 200))

label2 = CTkLabel (win, text='', image=img_ctk1)
label2.grid(row=1, column=1)

frame1 = CTkFrame(master=win, width=200, height=200)
frame1.grid(row=2,column=1)
q1=CTkLabel (frame1, text='У якому році засновали Нісан')
q1.grid(row=0, column=1,pady=10)
radio_var1 = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame1, text="1933",variable= radio_var1, value=1)
radiobutton_2 = CTkRadioButton(frame1, text="1921", variable= radio_var1, value=2)
radiobutton_3 = CTkRadioButton(frame1, text="1942", variable= radio_var1, value=3)
radiobutton_1.grid(row=1,column=1,pady=10)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)

frame2 = CTkFrame(master=win, width=200, height=200)
frame2.grid(row=3,column=1)
q1=CTkLabel (frame2, text='Хто засновав Ніссан')
q1.grid(row=0, column=1,pady=10)
radio_var2 = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame2, text="Аїкава Йосісуке",variable= radio_var2, value=1)
radiobutton_2 = CTkRadioButton(frame2, text="Ден Кендзіро", variable= radio_var2, value=2)
radiobutton_3 = CTkRadioButton(frame2, text="William R. Gorham", variable= radio_var2, value=3)
radiobutton_1.grid(row=1,column=1,pady=10)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)

frame3 = CTkFrame(master=win, width=200, height=200)
frame3.grid(row=4,column=1)
q1=CTkLabel (frame3, text='Яка найдорожча модель Ніссан')
q1.grid(row=0, column=1,pady=10)
radio_var3 = IntVar(value=0)
radiobutton_1 = CTkRadioButton(frame3, text="Nissan GT-R NISMO Special Edition",variable= radio_var3, value=1)
radiobutton_2 = CTkRadioButton(frame3, text="Nissan N-7", variable= radio_var3, value=2)
radiobutton_3 = CTkRadioButton(frame3, text="Nissan Leaf", variable= radio_var3, value=3)
radiobutton_1.grid(row=1,column=1,pady=10)
radiobutton_2.grid(row=1,column=2)
radiobutton_3.grid(row=1,column=3)

#--------
label3 = CTkLabel (win, text='', image=img_ctk2)
label3.grid(row=1, column=2)
frame4 = CTkFrame(master=win, width=200, height=200)
frame4.grid(row=2,column=2)
q4=CTkLabel (frame4, text='У якому році засновали Škoda')
q4.grid(row=0, column=1,pady=10)
radio_var4 = IntVar(value=0)
radiobutton_12 = CTkRadioButton(frame4, text="1895",variable= radio_var4, value=1)
radiobutton_22 = CTkRadioButton(frame4, text="1890", variable= radio_var4, value=2)
radiobutton_32 = CTkRadioButton(frame4, text="1858", variable= radio_var4, value=3)
radiobutton_12.grid(row=1,column=1,pady=10)
radiobutton_22.grid(row=1,column=2)
radiobutton_32.grid(row=1,column=3)

frame5 = CTkFrame(master=win, width=200, height=200)
frame5.grid(row=3,column=2)
q5=CTkLabel (frame5, text='Хто засновав Škoda')
q5.grid(row=0, column=1,pady=10)
radio_var5 = IntVar(value=0)
radiobutton_13 = CTkRadioButton(frame5, text="Вацлав Лаурин",variable= radio_var5, value=1)
radiobutton_23 = CTkRadioButton(frame5, text="Вацлав Клемент", variable= radio_var5, value=2)
radiobutton_33 = CTkRadioButton(frame5, text="Йосуке Оматоке", variable= radio_var5, value=3)
radiobutton_13.grid(row=1,column=1,pady=10)
radiobutton_23.grid(row=1,column=2)
radiobutton_33.grid(row=1,column=3)

frame6 = CTkFrame(master=win, width=200, height=200)
frame6.grid(row=4,column=2)
q6=CTkLabel (frame6, text='Яка найдорожча модель Škoda')
q6.grid(row=0, column=1,pady=10)
radio_var6 = IntVar(value=0)
radiobutton_14 = CTkRadioButton(frame6, text="Škoda Fabia",variable= radio_var6, value=1)
radiobutton_24 = CTkRadioButton(frame6, text="Skoda Enyaq Coupe vRS iV", variable= radio_var6, value=2)
radiobutton_34 = CTkRadioButton(frame6, text="Skoda Karoq", variable= radio_var6, value=3)
radiobutton_14.grid(row=1,column=1,pady=10)
radiobutton_24.grid(row=1,column=2)
radiobutton_34.grid(row=1,column=3)



#-----
#--------
label4 = CTkLabel (win, text='', image=img_ctk3)
label4.grid(row=1, column=3)
frame7 = CTkFrame(master=win, width=200, height=200)
frame7.grid(row=2,column=3)
q7=CTkLabel (frame7, text='У якому році засновали Volkswagen')
q7.grid(row=0, column=1,pady=10)
radio_var7 = IntVar(value=0)
radiobutton_12 = CTkRadioButton(frame7, text="1940",variable= radio_var7, value=1)
radiobutton_22 = CTkRadioButton(frame7, text="1937", variable= radio_var7, value=2)
radiobutton_32 = CTkRadioButton(frame7, text="1935", variable= radio_var7, value=3)
radiobutton_12.grid(row=1,column=1,pady=10)
radiobutton_22.grid(row=1,column=2)
radiobutton_32.grid(row=1,column=3)

frame8 = CTkFrame(master=win, width=200, height=200)
frame8.grid(row=3,column=3)
q8=CTkLabel (frame8, text='Хто засновав Volkswagen')
q8.grid(row=0, column=1,pady=10)
radio_var8 = IntVar(value=0)
radiobutton_14 = CTkRadioButton(frame8, text="Фердинандо Порше",variable= radio_var8, value=1)
radiobutton_24 = CTkRadioButton(frame8, text="Карл Фрідріхо", variable= radio_var8, value=2)
radiobutton_34 = CTkRadioButton(frame8, text="Камілло Кастільйоні", variable= radio_var8, value=3)
radiobutton_14.grid(row=1,column=1,pady=10)
radiobutton_24.grid(row=1,column=2)
radiobutton_34.grid(row=1,column=3)

frame9 = CTkFrame(master=win, width=200, height=200)
frame9.grid(row=4,column=3)
q9=CTkLabel (frame9, text='Яка найдорожча модель Volkswagen')
q9.grid(row=0, column=1,pady=10)
radio_var9 = IntVar(value=0)
radiobutton_15 = CTkRadioButton(frame9, text="Volkswagen Touareg",variable= radio_var9, value=1)
radiobutton_25 = CTkRadioButton(frame9, text="Volkswagen Jetta", variable= radio_var9, value=2)
radiobutton_35 = CTkRadioButton(frame9, text="Volkswagen Talagon", variable= radio_var9, value=3)
radiobutton_15.grid(row=1,column=1,pady=10)
radiobutton_25.grid(row=1,column=2)
radiobutton_35.grid(row=1,column=3)

def button_click():
    rez=0
    if radio_var1.get()==1:
        rez=rez+1
    if radio_var2.get()==1:
        rez=rez+1
    if radio_var3.get()==1:
        rez=rez+1
    if radio_var4.get()==2:
        rez=rez+1
    if radio_var5.get()==2:
        rez=rez+1
    if radio_var6.get()==3:
        rez=rez+1
    if radio_var7.get()==2:
        rez=rez+1
    if radio_var8.get()==1:
        rez=rez+1
    if radio_var9.get()==3:
        rez=rez+1
    messagebox.showinfo("Результат  ",str(rez))
    

button = CTkButton (win, text="Відповісти",command=button_click)
button.grid(row=5, column=2)

win.mainloop()

