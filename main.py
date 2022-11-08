from tkinter import *
from tkinter import  messagebox #message box only imports class  it does not import like messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# --------------------- PASSWORD GENERATOR ------------------------------- #
def search_used():

    website = input_website.get()

    try:
      with open("data.json","r") as data_file:
          data = json.load(data_file)
    except FileNotFoundError:
       messagebox.showinfo(title="Error", message=f"File Not Found !")

    else:


        if website in data:
            email = data[website]["email"]
            pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email} \nPassword : {pw}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")




def generate_used():
    #this is giving us a range
    # l = random.randint(8,10)
    # n = random.randint(2,4)
    # s = random.randint(2,4)

    pw_list = []

    for char in range(random.randint(8,10)):
        pw_list.append(random.choice(letters))

    for char in range(random.randint(2,4)):
        pw_list.append(random.choice(numbers))
    for char in range(random.randint(2,4)):
        pw_list.append(random.choice(symbols))

    random.shuffle(pw_list)

    password = ""
    for char in pw_list:
        password+=char
    input_pw.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_used():

    pw = input_pw.get()
    website = input_website.get()
    email = input_user.get()
    new_data = {
        website:{
            "email" : email,
            "password": pw
        }
    }
    if len(pw) == 0 or len(website) == 0:
        messagebox.showerror(title='Error',message="Please dont leave any fields empty!!")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)  # we are reading the old data

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:

           data.update(new_data)  # updating old data with new data

           with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)  # saving the updated data

        finally:


            input_website.delete(0, END)
            input_pw.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

label_website = Label(text='Website:')
label_website.grid(row=1,column=0)
user_label = Label(text='Email/Username:')
user_label.grid(row=2,column=0)
pw_label = Label(text='Password:')
pw_label.grid(row=3,column=0)

input_website = Entry(width=33)

input_website.grid(row=1,column=1)
input_website.focus()
input_user = Entry(width=52)
input_user.grid(row=2,column=1,columnspan=2)
input_user.insert(0,"rawal.aditi272@gmail.com")
input_pw = Entry(width=33)
input_pw.grid(row=3,column=1,)

button_generate = Button(text="Generate Password",command=generate_used)
button_generate.grid(row=3,column=2)

button_add = Button(text="Add" , width=45,command=add_used)
button_add.grid(row=4,column=1,columnspan=2)

button_search = Button(text="Search",width=15,command=search_used)
button_search.grid(row=1,column=2)






window.mainloop()







