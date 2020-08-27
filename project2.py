import os
from csv import DictWriter
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Ramu")
#create lebel
name_label = ttk.Label(window,text='Enter your name: ')  #pack() it's written in middle
name_label.grid(row=0,column=0,sticky = tkinter.W)

age_label = ttk.Label(window,text="Enter your age: ")
age_label.grid(row =1,column=0,sticky=tkinter.W) #sticky = it remove the indentention

email_label = ttk.Label(window,text='Enter your email: ')
email_label.grid(row=2,column=0,sticky=tkinter.W)

gender_label = ttk.Label(window,text="Choose your gender: ")
gender_label.grid(row=3,column=0)

#crete entry box
name_var = tkinter.StringVar()
name_entrybox = ttk.Entry(window,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var = tkinter.StringVar()
age_entrybox = ttk.Entry(window,width = 16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var = tkinter.StringVar()
email_entrybox = ttk.Entry(window,width = 16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

# create combobox
gender_var = tkinter.StringVar()
gender_cobobox = ttk.Combobox(window,width=13,textvariable=gender_var,state='readonly')
gender_cobobox['values']=('Gender','Male','Female','Other','Noobde')
gender_cobobox.current(0)
gender_cobobox.grid(row=3,column=1,sticky=tkinter.W)

#radio button
user_type = tkinter.StringVar()
radiobtn1 = ttk.Radiobutton(window,text="Student",value='Student',variable=user_type)
radiobtn1.grid(row=4,column=0,sticky=tkinter.W)

radiobtn2 = ttk.Radiobutton(window,text='Teacher',value='Teacher',variable=user_type)
radiobtn2.grid(row=4,column=1,sticky=tkinter.W)

#checkbutton
checkbtn_var= tkinter.IntVar()
chkbtn = ttk.Checkbutton(window,text='check if you are subcribe my channel: ',variable=checkbtn_var)
chkbtn.grid(row=5,columnspan=3)





# def action():
#     username = name_var.get()
#     useremail = email_var.get()
#     userage = age_var.get()
#     usergender=gender_var.get()
#     usertype = user_type.get()
#     if checkbtn_var.get()==0:
#         subscribed = "No"
#     else:
#         subscribed="Yes"
#     print(f'{username},{useremail},{userage},{usergender},{usertype},subscribed={subscribed}')
#     with open('file4.txt','a') as f:
#         f.write(f'{username},{userage},{usergender},{usertype},{useremail},{subscribed}\n')
#     name_entrybox.delete(0,tkinter.END)
#     age_entrybox.delete(0,tkinter.END)
#     email_entrybox.delete(0,tkinter.END)
#     name_label.configure(foreground='Blue')
#     submit_button.configure(foreground='Red')
    # print(f'{usertype},Username: {username},user emailid: {useremail}, and user age: {userage} gender of user {usergender}')
    
#write to csv file 
def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    usergender=gender_var.get()
    usertype = user_type.get()
    if checkbtn_var.get()==0:
        subscribed = "No"
    else:
        subscribed="Yes"
    #write to csv file
    with open('file1.csv','a',newline='') as f:
        dict_Writer = DictWriter(f,fieldnames=['User Name','User Email Adress','User Age','User Gender',
        'User Type','Subscribed'])
        if os.stat('file1.csv').st_size == 0:
            dict_Writer.writeheader()


        dict_Writer.writerow({
            'User Name' : username,'User Email Adress' : useremail,
            'User Age' : userage,'User Gender' : usergender,
            'User Type' : usertype,'Subscribed' : subscribed
        })

    name_entrybox.delete(0,tkinter.END)
    age_entrybox.delete(0,tkinter.END)
    email_entrybox.delete(0,tkinter.END)
    name_label.configure(foreground='Blue')


#creae button
submit_button = tkinter.Button(window,text='Submit',command=action)
submit_button.grid(row=6,columnspan=2)








window.mainloop()
