from customtkinter import *
from PIL import Image
import customtkinter
from CTkMessagebox import CTkMessagebox
import mysql.connector
import os

app = CTk()
app.geometry("600x480")
app.title("Queuekie")
app.resizable(0,0)
customtkinter.font = ("Poppins", 12)
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

side_img_data = Image.open("side-img.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

#################################################################################
#Login Frame
#################################################################################

login_frame = CTkFrame(master=app, width=300, height=480, fg_color="#0e1121")
login_frame.pack_propagate(0)
login_frame.pack(expand=True, side="right")

#texts
login_label_data = Image.open("login-label.png")

login_label = CTkImage(dark_image=login_label_data, light_image=login_label_data, size=(151, 45))

CTkLabel(master=login_frame, text="", image=login_label).pack(anchor="w", padx=(53, 0), pady=(105, 15))
CTkLabel(master=login_frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12)).pack(anchor="w", padx=(53, 0))


#LogIn TextBox
employeeid_verify = customtkinter.CTkEntry(master=login_frame, width=201, height=25, placeholder_text="Employee ID")
employeeid_verify.pack(anchor="w", padx=(53, 0))

password_verify = customtkinter.CTkEntry(master=login_frame, width=201, height=25, placeholder_text="Password", show="*")
password_verify.pack(anchor="w", pady=(10, 0), padx=(53, 0))

#create a command for login button
def login():
    print("Login button pressed")
    #check if the employee id and password is in the database
    # Connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    sql = "SELECT employee_id, password FROM users WHERE employee_id = %s AND password = %s"
    val = (employeeid_verify.get(), password_verify.get())
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        print("Login Succesful")
        #update the users table to update bool logged_in to 1 where employee_id = employeeid_verify.get()
        sql = "UPDATE users SET logged_in = 1 WHERE employee_id = %s"
        val = (employeeid_verify.get(),)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Record Updated Succesfully.")
        #destroy the app
        app.destroy()
        #run the main program
        os.system('python main.py')
    else:
        print("Login Failed")
        #show error message
        CTkMessagebox(title="Error", message="You entered incorrect \nEmployee ID or Password!\nPlease try again", icon="cancel")

#create a command for signup button
def signup():
    print("Signup button pressed")
    login_frame.pack_forget()
    signup_frame.pack(expand=True, side="right")
    
Login_button = customtkinter.CTkButton(master=login_frame, text="Login", font=("Poppins Bold", 10), text_color="#ffffff", width=201, height=25, command=login).pack(anchor="w", padx=(53, 0), pady=(10, 0))

CTkLabel(master=login_frame, text="Don't have an account yet?", text_color="#E7F3F3", anchor="center", justify="left", font=("Poppins", 8)).pack(anchor="center")

Signup_button = customtkinter.CTkButton(master=login_frame, text="Create an Account Here!", fg_color="#EEEEEE", hover_color="#7E7E7E", font=("Poppins Bold", 10), text_color="#1F6AA5", width=201, height=25, command=signup).pack(anchor="w", padx=(53, 0), pady=(0, 0))

#################################################################################
#Sign Up Frame
#################################################################################

#make signup frame invisible

signup_frame = CTkFrame(master=app, width=300, height=480, fg_color="#0e1121")
signup_frame.pack_forget()
signup_frame.pack_propagate(0)

signup_label_data = Image.open("signup-label.png")

signup_label = CTkImage(dark_image=signup_label_data, light_image=signup_label_data, size=(149, 50))

CTkLabel(master=signup_frame, text="", image=signup_label).pack(anchor="w", padx=(53, 0), pady=(65, 15))

CTkLabel(master=signup_frame, text="Create an account", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12)).pack(anchor="w", padx=(53, 0))


#Signup TextBox
fname_entry = customtkinter.CTkEntry(master=signup_frame, width=201, height=25, placeholder_text="First Name")
fname_entry.pack(anchor="w", padx=(53, 0))

lname_entry = customtkinter.CTkEntry(master=signup_frame, width=201, height=25, placeholder_text="Last Name")
lname_entry.pack(anchor="w", pady=(10, 0), padx=(53, 0))

employeeid_entry = customtkinter.CTkEntry(master=signup_frame, width=201, height=25, placeholder_text="Employee ID")
employeeid_entry.pack(anchor="w", pady=(10, 0), padx=(53, 0))

password_entry = customtkinter.CTkEntry(master=signup_frame, width=201, height=25, placeholder_text="Password", show="*")
password_entry.pack(anchor="w", pady=(10, 0), padx=(53, 0))

confirmpassword_entry = customtkinter.CTkEntry(master=signup_frame, width=201, height=25, placeholder_text="Confirm Password", show="*")
confirmpassword_entry.pack(anchor="w", pady=(10, 0), padx=(53, 0))

def show_password_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Passwords do not match!\nPlease try again", icon="cancel")

def show_emptyEID_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Employee ID cannot be empty!\nPlease try again", icon="cancel")

def show_existing_error():
    # Show some error message
    CTkMessagebox(title="Error", message="The Employee ID already exists \nPlease try again", icon="cancel")

def create_account():
    if password_entry.get() != confirmpassword_entry.get():
        print("Password does not match")
        show_password_error()
    elif employeeid_entry.get() == "":
        print("Employee ID cannot be empty")
        show_emptyEID_error()
    else:
        # Check if employee ID already exists in database
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM users WHERE employee_id = %s"
        val = (employeeid_entry.get(),)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()

        if len(myresult) > 0:
            # Employee ID already exists in database
            print("The Employee ID already exists")
            show_existing_error()
        else:
            # Insert data into database
            sql = "INSERT INTO users (employee_id, fname, lname, password, logged_in) VALUES (%s, %s, %s, %s, '1')"
            val = (employeeid_entry.get(), fname_entry.get(), lname_entry.get(), password_entry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Record Inserted Succesfully.")
            # Destroy the app
            app.destroy()
            # Run the main program
            os.system('python main.py')

Signup_button = customtkinter.CTkButton(master=signup_frame, text="Sign In", font=("Poppins Bold", 10), text_color="#ffffff", width=201, height=25, command=create_account).pack(anchor="w", padx=(53, 0), pady=(10, 0))

CTkLabel(master=signup_frame, text="Already have an Account?", text_color="#E7F3F3", anchor="center", justify="left", font=("Poppins", 8)).pack(anchor="center")

def backtologin():
    print("Back to login button pressed")
    signup_frame.pack_forget()
    login_frame.pack(expand=True, side="right")

Backtologin_button = customtkinter.CTkButton(master=signup_frame, text="Login Here!", fg_color="#EEEEEE", hover_color="#7E7E7E", font=("Poppins Bold", 10), text_color="#1F6AA5", width=201, height=25, command=backtologin).pack(anchor="w", padx=(53, 0), pady=(0, 0))


app.mainloop()