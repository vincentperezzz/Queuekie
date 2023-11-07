from customtkinter import *
from PIL import Image
import customtkinter
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
import mysql.connector
from datetime import datetime, timedelta
import threading
import time
import os

#################################################################################
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
mycursor = mydb.cursor()
#retrieve the logged_in value of the user where loggin_in = 1
sql = "SELECT * FROM users WHERE logged_in = '1'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
#put the entire row in their designated variables
for x in myresult:
    loggedin_employee_id = x[0]
    loggedin_fname = x[1]
    loggedin_lname = x[2]

sql = "UPDATE users SET logged_in = '0' WHERE logged_in = '1'"  
mycursor.execute(sql)
mydb.commit()

#################################################################################
app = CTk()
app.geometry("856x645")
app.title("Queuekie - Main Menu")
app.resizable(0,0)
customtkinter.font = ("Poppins", 12)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


#################################################################################
#Side Frame
#################################################################################

sidebar_frame = CTkFrame(master=app, fg_color="#0E1121",  width=176, height=645, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("resources/logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(116, 116))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(30, 0), anchor="center")

greetings_user = "Hi " + loggedin_fname + "!"
CTkLabel(master=sidebar_frame, text=greetings_user, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 20),).pack(anchor="center")

greetings_EID = "    Employee ID: " + loggedin_employee_id
greetingslabel_EID= CTkLabel(master=sidebar_frame, text=greetings_EID, fg_color="#010311", text_color="#7E7E7E", anchor="w", justify="center", font=("Poppins Bold", 12), height=30, width=157, corner_radius=4)
greetingslabel_EID.pack(anchor="center")

def dashboard_command():
    print("Dashboard button pressed")
    dashboard_button.configure(fg_color="#191D32")
    order_button.configure(fg_color="transparent")
    checkout_button.configure(fg_color="transparent")
    inventory_button.configure(fg_color="transparent")
    accountsettings_button.configure(fg_color="transparent")
    logout_button.configure(fg_color="transparent")

    #show and hide frames
    dashboard_frame.pack(fill="both", expand=True, side="left")
    order_frame.pack_forget()
    checkout_frame.pack_forget()
    inventory_frame.pack_forget()
    accountsettings_frame.pack_forget()

    #other functions
    show_dbtable()
    orders_label_command()
    delays_label_command()
    voided_label_command()

dashboard_img_data = Image.open("resources/dashboard_icon.png")
dashboard_img = CTkImage(dark_image=dashboard_img_data, light_image=dashboard_img_data)
dashboard_button = CTkButton(master=sidebar_frame, image=dashboard_img, text="Dashboard", fg_color="#191D32", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=dashboard_command)
dashboard_button.pack(anchor="center", pady=(60, 0))

def order_command():
    print("Order button pressed")
    dashboard_button.configure(fg_color="transparent")
    order_button.configure(fg_color="#191D32")
    checkout_button.configure(fg_color="transparent")
    inventory_button.configure(fg_color="transparent")
    accountsettings_button.configure(fg_color="transparent")
    logout_button.configure(fg_color="transparent")

    #show and hide frames
    dashboard_frame.pack_forget()
    order_frame.pack(fill="both", expand=True, side="left")
    checkout_frame.pack_forget()
    inventory_frame.pack_forget()
    accountsettings_frame.pack_forget()

    #other functions
    

order_img_data = Image.open("resources/order_icon.png")
order_img = CTkImage(dark_image=order_img_data, light_image=order_img_data)
order_button = CTkButton(master=sidebar_frame, image=order_img, text="Order", fg_color="transparent", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=order_command)
order_button.pack(anchor="center", pady=(10, 0))

def checkout_command():
    print("Check Out button pressed")
    dashboard_button.configure(fg_color="transparent")
    order_button.configure(fg_color="transparent")
    checkout_button.configure(fg_color="#191D32")
    inventory_button.configure(fg_color="transparent")
    accountsettings_button.configure(fg_color="transparent")
    logout_button.configure(fg_color="transparent")

    #show and hide frames
    dashboard_frame.pack_forget()
    order_frame.pack_forget()
    checkout_frame.pack(fill="both", expand=True, side="left")
    inventory_frame.pack_forget()
    accountsettings_frame.pack_forget()

    #other functions
    

checkout_img_data = Image.open("resources/checkout_icon.png")
checkout_img = CTkImage(dark_image=checkout_img_data, light_image=checkout_img_data)
checkout_button = CTkButton(master=sidebar_frame, image=checkout_img, text="Check Out", fg_color="transparent", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=checkout_command)
checkout_button.pack(anchor="center", pady=(10, 0))

def inventory_command():
    print("Inventory button pressed")
    dashboard_button.configure(fg_color="transparent")
    order_button.configure(fg_color="transparent")
    checkout_button.configure(fg_color="transparent")
    inventory_button.configure(fg_color="#191D32")
    accountsettings_button.configure(fg_color="transparent")
    logout_button.configure(fg_color="transparent")

    #show and hide frames
    dashboard_frame.pack_forget()
    order_frame.pack_forget()
    checkout_frame.pack_forget()
    inventory_frame.pack(fill="both", expand=True, side="left")
    accountsettings_frame.pack_forget()

    #other functions
    show_InventTable()
    completedOrdersLabel_command()
    totalSalesLabel_command()

inventory_img_data = Image.open("resources/inventory_icon.png")
inventory_img = CTkImage(dark_image=inventory_img_data, light_image=inventory_img_data)
inventory_button = CTkButton(master=sidebar_frame, image=inventory_img, text="Inventory", fg_color="transparent", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=inventory_command)
inventory_button.pack(anchor="center", pady=(10, 0))

def accountsettings_command():
    print("Account Settings button pressed")
    dashboard_button.configure(fg_color="transparent")
    order_button.configure(fg_color="transparent")
    checkout_button.configure(fg_color="transparent")
    inventory_button.configure(fg_color="transparent")
    accountsettings_button.configure(fg_color="#191D32")
    logout_button.configure(fg_color="transparent")

    #show and hide frames
    dashboard_frame.pack_forget()
    order_frame.pack_forget()
    checkout_frame.pack_forget()
    inventory_frame.pack_forget()
    accountsettings_frame.pack(fill="both", expand=True, side="left")

    #other_functions
    

accountsettings_img_data = Image.open("resources/accountsettings_icon.png")
accountsettings_img = CTkImage(dark_image=accountsettings_img_data, light_image=accountsettings_img_data)
accountsettings_button = CTkButton(master=sidebar_frame, image=accountsettings_img, text="Account Settings", fg_color="transparent", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=accountsettings_command)
accountsettings_button.pack(anchor="center", pady=(10, 0))

def logout_command():
    print("Log Out button pressed")
    dashboard_button.configure(fg_color="transparent")
    order_button.configure(fg_color="transparent")
    checkout_button.configure(fg_color="transparent")
    inventory_button.configure(fg_color="transparent")
    accountsettings_button.configure(fg_color="transparent")
    logout_button.configure(fg_color="#191D32")

    msg = CTkMessagebox(title="Logging Out?", message="Do you want to logout this account?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
        app.destroy()
        os.system("python startup.py")       
    else:
        pass

logout_img_data = Image.open("resources/logout_icon.png")
logout_img = CTkImage(dark_image=logout_img_data, light_image=logout_img_data)
logout_button = CTkButton(master=sidebar_frame, image=logout_img, text="Log Out", fg_color="transparent", font=("Poppins Bold", 12), hover_color="#181A27", anchor="w", width=157, height=38, command=logout_command)
logout_button.pack(anchor="center", pady=(95, 0))

#################################################################################
#dashboard Frame
#################################################################################

dashboard_frame = CTkFrame(master=app, fg_color="#020410",  width=680, height=645, corner_radius=0)
dashboard_frame.pack_propagate(0)
dashboard_frame.pack(anchor="w", side='left')

CTkLabel(master=dashboard_frame, text="Dashboard", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="w", padx=(27, 0), pady=(29, 0))

# Rectangle Parent frame of Rectangles
dashbaordRectangle_frame = CTkFrame(master=dashboard_frame, fg_color="transparent", width=680, height=70, corner_radius=4)
dashbaordRectangle_frame.pack(anchor="w", padx=(27, 0), pady=(15, 0))

def orders_label_command():
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #retrieve all the orders from the orders table and count all who have a status of 'Processing'
    sql = "SELECT * FROM orders WHERE status = 'Processing'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #put the number of orders in the label
    numoforders_NUM.configure(text=str(len(myresult)))

def delays_label_command():
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #retrieve all the orders from the orders table and count all who have a status of 'Delayed'
    sql = "SELECT * FROM orders WHERE status = 'Delayed'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #put the number of orders in the label
    numofdelays_NUM.configure(text=str(len(myresult)))

def voided_label_command():
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #retrieve all the orders from the orders table and count all who have a status of 'Voided'
    sql = "SELECT * FROM orders WHERE status = 'Voided'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #put the number of orders in the label
    numofvoided_NUM.configure(text=str(len(myresult)))

# Orders Rectangle
orders_rectangle = CTkFrame(master=dashbaordRectangle_frame, fg_color="#70179A", width=132, height=70, corner_radius=4)
orders_rectangle.pack_propagate(False)
orders_rectangle.pack(side='left')

numoforders_label = CTkLabel(master=orders_rectangle, text="Orders", fg_color="transparent", text_color="#fff", font=("Poppins Bold", 15), anchor="w", width=132)
numoforders_label.pack(anchor="w", padx=(10, 0), pady=(5, 0))

numoforders_NUM = CTkLabel(master=orders_rectangle, text="0", text_color="#fff",fg_color="transparent", font=("Poppins Bold", 25), anchor="w", width=132)
numoforders_NUM.pack(anchor="w" , padx=(10, 0), pady=(0, 0))

# Delays Rectangle
delays_rectangle = CTkFrame(master=dashbaordRectangle_frame, fg_color="#146C63", width=132, height=70, corner_radius=4)
delays_rectangle.pack_propagate(False)
delays_rectangle.pack(side='left', padx=(20, 0))

numofdelays_label = CTkLabel(master=delays_rectangle, text="Delays", fg_color="transparent", text_color="#fff", font=("Poppins Bold", 15), anchor="w", width=132)
numofdelays_label.pack(anchor="w", padx=(10, 0), pady=(5, 0))

numofdelays_NUM = CTkLabel(master=delays_rectangle, text="0", text_color="#fff",fg_color="transparent", font=("Poppins Bold", 25), anchor="w", width=132)
numofdelays_NUM.pack(anchor="w" , padx=(10, 0), pady=(0, 0))

# Voided Rectangle
voided_rectangle = CTkFrame(master=dashbaordRectangle_frame, fg_color="#9A1717", width=132, height=70, corner_radius=4)
voided_rectangle.pack_propagate(False)
voided_rectangle.pack(side='left', padx=(20, 0))

numofvoided_label = CTkLabel(master=voided_rectangle, text="Voided", fg_color="transparent", text_color="#fff", font=("Poppins Bold", 15), anchor="w", width=132)
numofvoided_label.pack(anchor="w", padx=(10, 0), pady=(5, 0))

numofvoided_NUM = CTkLabel(master=voided_rectangle, text="0", text_color="#fff",fg_color="transparent", font=("Poppins Bold", 25), anchor="w", width=132)
numofvoided_NUM.pack(anchor="w" , padx=(10, 0), pady=(0, 0))

orders_label_command()
delays_label_command()
voided_label_command()

InQueue_dashbaordRectangle_frame = CTkFrame(master=dashboard_frame, fg_color="transparent", width=680)
InQueue_dashbaordRectangle_frame.pack(anchor="nw", padx=(27, 0), pady=(20, 0))  


label_button_frame = CTkFrame(master=InQueue_dashbaordRectangle_frame, fg_color="transparent", width=680, height=70, corner_radius=4)
label_button_frame.pack (anchor="w", side='left')

CTkLabel(master=label_button_frame, text="In Queue", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(side='left')

addorder_img_data = Image.open("resources/addorder_icon.png")
addorder_img = CTkImage(dark_image=addorder_img_data, light_image=addorder_img_data)
addorder_button = CTkButton(master=label_button_frame, image=addorder_img, text="Create an Order", fg_color="#1F243E", font=("Poppins Bold", 12), hover_color="#181A27", anchor="e", width=146, height=25, command=order_command, compound="right")
addorder_button.pack(side='left', padx=(355, 0))

search_dashbaordRectangle_frame = CTkFrame(master=dashboard_frame, fg_color="#191D32", width=680)
search_dashbaordRectangle_frame.pack(anchor="w", padx=(27, 0), pady=(10, 0))  

searchORDERID_entry = CTkEntry(master=search_dashbaordRectangle_frame, width=315, placeholder_text="Enter ORDER ID", border_color="#1F6AA5", border_width=2)
searchORDERID_entry.pack(side="left", padx=(13, 0), pady=15)

def view_order_popup():
    #if the searchORDERID_entry.get() is empty
    if searchORDERID_entry.get() == "":
        #show error message
        CTkMessagebox(title="Error", message="Please enter an order ID!", icon="cancel")
        return
    
    viewWindow_title = "Order ID: " + searchORDERID_entry.get()
    viewWindow = customtkinter.CTkToplevel()
    viewWindow.geometry("610x325")
    viewWindow.title(viewWindow_title)
    viewWindow.attributes('-topmost', True)

    viewWindow_frame = CTkFrame(master=viewWindow, fg_color="#020410",  width=610, height=325, corner_radius=0)
    viewWindow_frame.pack(fill="both", expand=True, side="left")
    viewWindow_frame.pack_propagate(0)

    # Create a scrollable frame to contain the table
    viewScrollable_frame = CTkScrollableFrame(master=viewWindow_frame, fg_color="transparent", width=610, height=120)
    viewScrollable_frame.pack(anchor="w", padx=(10, 0), pady=(20, 0))

    #retrieve data from database and put it in the table
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #retrieve the cart table data which only item_name, quantity, price, and amount
    sql = """
        SELECT menu.item, cart.price, cart.quantity, cart.amount 
        FROM cart 
        INNER JOIN menu ON cart.item_code = menu.item_code 
        WHERE cart.order_id = %s
    """
    val = (searchORDERID_entry.get(),)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    #format the data to be put in the table
    def viewtable_data(myresult, header=["Order", "Price", "Quantity", "Amount"]):
        formatted_data = [header]
        for item_name, price, quantity, amount in myresult:
            formatted_data.append([item_name, price, quantity, amount])
        return formatted_data

    # Create a table using CTkTable
    viewtable = CTkTable(master=viewScrollable_frame, values=viewtable_data(myresult), colors=["#010311", "#070b21"], header_color="#1f6aa5", hover_color="#181A27")
    viewtable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    viewtable.pack(expand=True)

    viewBottom_frame = CTkFrame(master=viewWindow_frame, fg_color="#191D32", width=500, height=44)
    viewBottom_frame.pack(anchor="s", padx=(0, 0), pady=(25, 0))  

    CTkLabel(master=viewBottom_frame, text="Sales: ", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0), pady=(10, 10))

    def viewSales_val():
        #sum up the amount column in the cart table where order_id = searchORDERID_entry.get()
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        sql = "SELECT SUM(amount) FROM cart WHERE order_id = %s"
        val = (searchORDERID_entry.get(),)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            return x[0]
        

    viewSales = CTkLabel(master=viewBottom_frame, text="₱ " + str(viewSales_val()), fg_color="#010311", text_color="#fff", anchor="w", justify="left", font=("Poppins Bold", 12), height=30, width=157, corner_radius=4)
    viewSales.pack(side='left', padx=(5, 0), pady=(10, 10))

    # Create a close button
    close_button = CTkButton(master=viewBottom_frame, text="Close", fg_color="#1F6AA5", font=("Poppins Bold", 10), hover_color="#08365A", anchor="center", width=85, height=20, command=viewWindow.destroy)
    close_button.pack(side="right", padx=(40, 10), anchor="e")

    # Start the mainloop
    viewWindow.mainloop()

vieworder_button = CTkButton(master=search_dashbaordRectangle_frame, text="View Order", fg_color="#1F6AA5", font=("Poppins Bold", 10), hover_color="#08365A", anchor="center", width=85, height=20, command = view_order_popup)
vieworder_button.pack(side='left', padx=(10, 0))

def voidorder_command():
    #if the searchORDERID_entry.get() is empty
    if searchORDERID_entry.get() == "":
        #show error message
        CTkMessagebox(title="Error", message="Please enter an order ID!", icon="cancel")
        return
    
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #update the status of the order to 'Voided' where order_id = searchORDERID_entry.get()
    sql = "UPDATE orders SET status = 'Voided' WHERE order_id = %s"
    val = (searchORDERID_entry.get(),)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record Updated Succesfully.")
    #update table
    show_dbtable()
    orders_label_command()
    delays_label_command()
    voided_label_command()
    #show success message
    CTkMessagebox(title="Success", message="Order has been voided!", icon="info")

voidorder_button = CTkButton(master=search_dashbaordRectangle_frame, text="Void", fg_color="#981616", font=("Poppins Bold", 10), hover_color="#480A0A", anchor="center", width=85, height=20, command=voidorder_command)
voidorder_button.pack(side='left', padx=(10, 0))

def doneorder_command():
    #if the searchORDERID_entry.get() is empty
    if searchORDERID_entry.get() == "":
        #show error message
        CTkMessagebox(title="Error", message="Please enter an order ID!", icon="cancel")
        return
    
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    #update the status of the order to 'Completed' where order_id = searchORDERID_entry.get()
    sql = "UPDATE orders SET status = 'Completed' WHERE order_id = %s"
    val = (searchORDERID_entry.get(),)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record Updated Succesfully.")
    #update table
    show_dbtable()
    orders_label_command()
    delays_label_command()
    voided_label_command()
    #show success message
    CTkMessagebox(title="Success", message="Order has been marked as done!", icon="info")


doneorder_button = CTkButton(master=search_dashbaordRectangle_frame, text="Done", fg_color="#158921", font=("Poppins Bold", 10), hover_color="#0A3D0F", anchor="center", width=85, height=20, command=doneorder_command)
doneorder_button.pack(side='left', padx=(10, 15))

#TABLE PART
dbtable_data = [["Order ID", "Time Ordered", "Time Estimate"]]  # Initialize with headers

table_frame = CTkScrollableFrame(master=dashboard_frame, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=21, side='bottom')


def show_dbtable():
    global dbtable
    global dbtable_data
    def retreive_data_for_database():
        #retrieve data from database and put it in the table
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        #retrieve the orders table data which only order_id, time_ordered, time_est
        sql = "SELECT order_id, time_ordered, time_est, time_finished FROM orders WHERE status = %s"
        val = ("Processing",)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult
    
    def sort_result_by_time_est(results):
        return sorted(results, key=lambda row: (get_duration_seconds(row[2]), row[1]))

    def get_duration_seconds(time_est):
        # Extract the number of minutes from the varchar time_est
        if time_est == "Ready for Pickup":
            return 0
        
        minutes = int(time_est.split()[0])
        return minutes * 60  # Convert minutes to seconds for sorting

        
    def format_result_to_table_data(myresult, header=["Order ID", "Time Ordered", "Time Estimate", "Time Finished"]):
        # Sort the results by time_est and time_ordered
        myresult = sort_result_by_time_est(myresult)

        dbtable_data = [header]
        for order_id, time_ordered, time_estimate, time_finished in myresult:
            formatted_time_ordered = time_ordered.strftime("%Y-%m-%d %H:%M:%S")
            formatted_time_estimate = time_estimate
            formatted_time_finished = time_finished.strftime("%Y-%m-%d %H:%M:%S") if time_finished else None
            dbtable_data.append([order_id, formatted_time_ordered, formatted_time_estimate, formatted_time_finished])

        return dbtable_data
    

    dbtable_data = format_result_to_table_data(retreive_data_for_database())

    dbtable.destroy()

    dbtable = CTkTable(master=table_frame, values=dbtable_data, colors=["#010311", "#070b21"], header_color="#1f6aa5", hover_color="#181A27")
    dbtable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    dbtable.pack(expand=True)

dbtable = CTkTable(master=table_frame, values=dbtable_data, colors=["#010311", "#070b21"], header_color="#1f6aa5", hover_color="#181A27")
dbtable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
dbtable.pack(expand=True)

show_dbtable()

## The voided overdues popping out when addInQueue button is created

def show_message(order_id, time_finished):
    print("show_message() is working and it reaches the code here")
    msg = CTkMessagebox(title="Order Follow Up", message=f"Is Order {order_id} ready?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    
    response = msg.get()
    #retrieve data from database and put it in the table
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()
    
    if response=="Yes":
        # Connect to the database and change the status of the order to 'Completed' where order_id = order_id
        sql = "UPDATE orders SET status = 'Completed' WHERE order_id = %s"
        val = (order_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Record Set 'Completed' Successfully.")
        dashboard_command()
        
    elif response=="No":
        # Connect to the database and change the status of the order to 'Delayed' and add 5 minutes to time_finished
        new_time_finished = time_finished + timedelta(minutes=5)
        sql = "UPDATE orders SET status = 'Delayed', time_finished = %s WHERE order_id = %s"
        val = (new_time_finished, order_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Record Set 'Delayed' and added 5mins Successfully.")
        # Schedule the appearance of the messagebox with the new time_finished
        delay = (new_time_finished - datetime.now()).total_seconds()
        notif = threading.Timer(delay, show_message, args=[order_id, new_time_finished])
        notif.start()
        dashboard_command()
    else:
        pass

def delays_popup():
    current_time = datetime.now()

    #retrieve data from database and put it in the table
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()    
    # Query to retrieve orders with 'Processing' status
    sql = "SELECT order_id, time_finished FROM orders WHERE status = 'Processing'"
    mycursor.execute(sql)
    processing_orders = mycursor.fetchall()

    for order_id, time_finished in processing_orders:
        if current_time < time_finished:
            time_difference = time_finished - current_time
            seconds_to_wait = time_difference.total_seconds()
            notif = threading.Timer(seconds_to_wait, show_message, args=[order_id, time_finished])
            notif.start()
            #display the timer in the console
            print(f"Order {order_id} will be ready in {seconds_to_wait} seconds.")

def overdue_popup():
    #retrieve data from database and put it in the table
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()    
    # Query to retrieve orders with 'Processing' status
    sql = "SELECT order_id, time_finished FROM orders WHERE status = 'Processing'"
    mycursor.execute(sql)
    processing_orders = mycursor.fetchall()
    for order_id, time_finished in processing_orders:
        # Handle overdue orders as needed
        # show info ctkmessagebox that says the order is overdue
        CTkMessagebox(title="Order Follow Up", message=f"Order {order_id} is overdue!", icon="info")
        show_dbtable()
        orders_label_command()
            
delays_popup()
overdue_popup() #runs only on startup

#################################################################################
#Order Frame
#################################################################################

order_frame = CTkFrame(master=app, fg_color="#020410",  width=680, height=645, corner_radius=0)
order_frame.pack_forget()
order_frame.pack_propagate(0)
order_frame.pack(side="left")

CTkLabel(master=order_frame, text="Create an Order", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="w", padx=(27, 0), pady=(29, 0))

checkout_dashbaordRectangle_frame = CTkFrame(master=order_frame, fg_color="transparent", width=680)
checkout_dashbaordRectangle_frame.pack(anchor="nw", padx=(27, 0), pady=(0, 0))  

addorder_button = CTkButton(master=checkout_dashbaordRectangle_frame, text="Proceed to Checkout", fg_color="#158921", font=("Poppins Bold", 12), hover_color="#0A3D0F", anchor="e", width=146, height=25, command=checkout_command)
addorder_button.pack(side='right', padx=(485, 0))

###################################
global Total_Amount
Total = {'TA_1': 0, 'TA_2': 0, 'TA_3': 0, 'TA_4': 0, 'TA_5': 0, 'TA_6': 0, 'TA_7': 0, 'TA_8': 0, 'TA_9': 0, 'TA_10': 0, 'TA_11': 0, 'TA_12': 0, 'TA_13': 0, 'TA_14': 0, 'TA_15': 0, 'TA_16': 0, 'TA_17': 0}
Total_Amount = sum(Total.values())

def show_checkoutItem_1():
    global Total_Amount
    if itemNumber_1.get() == 1:
        checkoutItem_1_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_1'] = amountItem_1_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_1_frame.pack_forget()
        Total['TA_1'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")  
        

def show_checkoutItem_2():
    global Total_Amount
    if itemNumber_2.get() == 1:
        checkoutItem_2_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_2'] = amountItem_2_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_2_frame.pack_forget()
        Total['TA_2'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def show_checkoutItem_3():
    global Total_Amount
    if itemNumber_3.get() == 1:
        checkoutItem_3_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_3'] = amountItem_3_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_3_frame.pack_forget()
        Total['TA_3'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 
    
def show_checkoutItem_4():
    global Total_Amount
    if itemNumber_4.get() == 1:
        checkoutItem_4_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_4'] = amountItem_4_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_4_frame.pack_forget()
        Total['TA_4'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_5():
    global Total_Amount
    if itemNumber_5.get() == 1:
        checkoutItem_5_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_5'] = amountItem_5_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_5_frame.pack_forget()
        Total['TA_5'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_6():
    global Total_Amount
    if itemNumber_6.get() == 1:
        checkoutItem_6_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_6'] = amountItem_6_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_6_frame.pack_forget()
        Total['TA_6'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_7():
    global Total_Amount
    if itemNumber_7.get() == 1:
        checkoutItem_7_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_7'] = amountItem_7_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_7_frame.pack_forget()
        Total['TA_7'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_8():
    global Total_Amount
    if itemNumber_8.get() == 1:
        checkoutItem_8_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_8'] = amountItem_8_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_8_frame.pack_forget()
        Total['TA_8'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_9():
    global Total_Amount
    if itemNumber_9.get() == 1:
        checkoutItem_9_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_9'] = amountItem_9_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_9_frame.pack_forget()
        Total['TA_9'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_10():
    global Total_Amount
    if itemNumber_10.get() == 1:
        checkoutItem_10_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_10'] = amountItem_10_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_10_frame.pack_forget()
        Total['TA_10'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_11():
    if itemNumber_11.get() == 1:
        checkoutItem_11_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_11'] = amountItem_11_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_11_frame.pack_forget()
        Total['TA_11'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_12():
    if itemNumber_12.get() == 1:
        checkoutItem_12_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_12'] = amountItem_12_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_12_frame.pack_forget()
        Total['TA_12'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_13():
    if itemNumber_13.get() == 1:
        checkoutItem_13_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_13'] = amountItem_13_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_13_frame.pack_forget()
        Total['TA_13'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_14():
    if itemNumber_14.get() == 1:
        checkoutItem_14_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_14'] = amountItem_14_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_14_frame.pack_forget()
        Total['TA_14'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_15():
    if itemNumber_15.get() == 1:
        checkoutItem_15_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_15'] = amountItem_15_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_15_frame.pack_forget()
        Total['TA_15'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_16():
    if itemNumber_16.get() == 1:
        checkoutItem_16_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_16'] = amountItem_16_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_16_frame.pack_forget()
        Total['TA_16'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

def show_checkoutItem_17():
    if itemNumber_17.get() == 1:
        checkoutItem_17_frame.pack(anchor="nw", pady=(12, 0))
        Total['TA_17'] = amountItem_17_val
        Total_Amount = sum(Total.values())  
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
    else:
        checkoutItem_17_frame.pack_forget()
        Total['TA_17'] = 0
        Total_Amount = sum(Total.values())
        totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 


#create a scrollable frame
orderScrollable_frame = CTkScrollableFrame(master=order_frame, fg_color="transparent", width=621, height=500)
orderScrollable_frame.pack(anchor="w", padx=(17, 0), pady=(20, 0))

CTkLabel(master=orderScrollable_frame, text="Meals                                                                                              Price           Add to Cart", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 17),).pack(anchor="nw")

#Item Number 1
orderItem_1_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_1_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_1_img_data = Image.open("resources/1pc-Chickenjoy-Solo.png")
ordernum_1_img = CTkImage(dark_image=ordernum_1_img_data, light_image=ordernum_1_img_data, size=(90, 59))
CTkLabel(master=orderItem_1_frame, text="", image=ordernum_1_img).pack(side='left')

CTkLabel(master=orderItem_1_frame, text="Fried Chicken w/ Rice", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_1_frame, text="₱ 95.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(105, 0))

itemNumber_1 = customtkinter.CTkCheckBox(master=orderItem_1_frame, text="", width=20, command=show_checkoutItem_1)
itemNumber_1.pack(side='left', padx=(70,38))

#Item Number 2
orderItem_2_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_2_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_2_img_data = Image.open("resources/Jolly-Spaghetti-Solo 1.png")
ordernum_2_img = CTkImage(dark_image=ordernum_2_img_data, light_image=ordernum_2_img_data, size=(90, 59))
CTkLabel(master=orderItem_2_frame, text="", image=ordernum_2_img).pack(side='left')

CTkLabel(master=orderItem_2_frame, text="Jolly Spaghetti", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_2_frame, text="₱ 50.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(165, 0))

itemNumber_2 = customtkinter.CTkCheckBox(master=orderItem_2_frame, text="", width=20, command=show_checkoutItem_2)
itemNumber_2.pack(side='left', padx=(70,38))

#Item Number 3
orderItem_3_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_3_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_3_img_data = Image.open("resources/Palabok-Solo 1.png")
ordernum_3_img = CTkImage(dark_image=ordernum_3_img_data, light_image=ordernum_3_img_data, size=(90, 59))
CTkLabel(master=orderItem_3_frame, text="", image=ordernum_3_img).pack(side='left')

CTkLabel(master=orderItem_3_frame, text="Palabok Fiesta", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_3_frame, text="₱ 160.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(162, 0))

itemNumber_3 = customtkinter.CTkCheckBox(master=orderItem_3_frame, text="", width=20, command=show_checkoutItem_3)
itemNumber_3.pack(side='left', padx=(70,38))

#Item Number 4
orderItem_4_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_4_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_4_img_data = Image.open("resources/Chicken-Sandwich 1.png")
ordernum_4_img = CTkImage(dark_image=ordernum_4_img_data, light_image=ordernum_4_img_data, size=(63, 51))
CTkLabel(master=orderItem_4_frame, text="", image=ordernum_4_img).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_4_frame, text="Chicken Sandwich", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(27, 0))

CTkLabel(master=orderItem_4_frame, text="₱ 65.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(132, 0))

itemNumber_4 = customtkinter.CTkCheckBox(master=orderItem_4_frame, text="", width=20, command=show_checkoutItem_4)
itemNumber_4.pack(side='left', padx=(70,38))

#Item Number 5
orderItem_5_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_5_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_5_img_data = Image.open("resources/Burger 1.png")
ordernum_5_img = CTkImage(dark_image=ordernum_5_img_data, light_image=ordernum_5_img_data, size=(90, 59))
CTkLabel(master=orderItem_5_frame, text="", image=ordernum_5_img).pack(side='left')

CTkLabel(master=orderItem_5_frame, text="Burger", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_5_frame, text="₱ 50.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(246, 0))

itemNumber_5 = customtkinter.CTkCheckBox(master=orderItem_5_frame, text="", width=20, command=show_checkoutItem_5)
itemNumber_5.pack(side='left', padx=(70,38))

#Item Number 6
orderItem_6_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_6_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_6_img_data = Image.open("resources/Burger-Steak 1.png")
ordernum_6_img = CTkImage(dark_image=ordernum_6_img_data, light_image=ordernum_6_img_data, size=(90, 59))
CTkLabel(master=orderItem_6_frame, text="", image=ordernum_6_img).pack(side='left')

CTkLabel(master=orderItem_6_frame, text="Burger Steak", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(10, 0))

CTkLabel(master=orderItem_6_frame, text="₱ 85.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(185, 0))

itemNumber_6 = customtkinter.CTkCheckBox(master=orderItem_6_frame, text="", width=20, command=show_checkoutItem_6)
itemNumber_6.pack(side='left', padx=(70,38))

#Sides
CTkLabel(master=orderScrollable_frame, text="Sides", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 17),).pack(anchor="nw", pady=(20, 0))

#Item Number 7
orderItem_7_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_7_frame.pack(anchor="nw", pady=(12, 0))  

ordernum_7_img_data = Image.open("resources/Fries 1.png")
ordernum_7_img = CTkImage(dark_image=ordernum_7_img_data, light_image=ordernum_7_img_data, size=(45, 45))
CTkLabel(master=orderItem_7_frame, text="", image=ordernum_7_img).pack(side='left', padx=(20, 0), pady=(7, 7))

CTkLabel(master=orderItem_7_frame, text="Fries", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(33, 0))

CTkLabel(master=orderItem_7_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(267, 0))

itemNumber_7 = customtkinter.CTkCheckBox(master=orderItem_7_frame, text="", width=20, command=show_checkoutItem_7)
itemNumber_7.pack(side='left', padx=(70,38))

#Item Number 8
orderItem_8_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_8_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_8_img_data = Image.open("resources/Creamy-Macaroni Soup 1.png")
ordernum_8_img = CTkImage(dark_image=ordernum_8_img_data, light_image=ordernum_8_img_data, size=(98, 60))
CTkLabel(master=orderItem_8_frame, text="", image=ordernum_8_img).pack(side='left')

CTkLabel(master=orderItem_8_frame, text="Creamy Macaroni Soup", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_8_frame, text="₱ 55.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(83, 0))

itemNumber_8 = customtkinter.CTkCheckBox(master=orderItem_8_frame, text="", width=20, command=show_checkoutItem_8)
itemNumber_8.pack(side='left', padx=(70,38))

#Item Number 9
orderItem_9_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_9_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_9_img_data = Image.open("resources/Plain-White-Rice 1.png")
ordernum_9_img = CTkImage(dark_image=ordernum_9_img_data, light_image=ordernum_9_img_data, size=(98, 60))
CTkLabel(master=orderItem_9_frame, text="", image=ordernum_9_img).pack(side='left')

CTkLabel(master=orderItem_9_frame, text="Rice", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_9_frame, text="₱ 20.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(272, 0))

itemNumber_9 = customtkinter.CTkCheckBox(master=orderItem_9_frame, text="", width=20, command=show_checkoutItem_9)
itemNumber_9.pack(side='left', padx=(70,38))

#Item Number 10
orderItem_10_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_10_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_10_img_data = Image.open("resources/Gravy 1.png")
ordernum_10_img = CTkImage(dark_image=ordernum_10_img_data, light_image=ordernum_10_img_data, size=(98, 60))
CTkLabel(master=orderItem_10_frame, text="", image=ordernum_10_img).pack(side='left')

CTkLabel(master=orderItem_10_frame, text="Gravy", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_10_frame, text="₱ 15.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(257, 0))

itemNumber_10 = customtkinter.CTkCheckBox(master=orderItem_10_frame, text="", width=20, command=show_checkoutItem_10)
itemNumber_10.pack(side='left', padx=(70,38))

#Desserts
CTkLabel(master=orderScrollable_frame, text="Desserts", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 17),).pack(anchor="nw", pady=(20, 0))

#Item Number 11
orderItem_11_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_11_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_11_img_data = Image.open("resources/Peach-Mango-Pie 1.png")
ordernum_11_img = CTkImage(dark_image=ordernum_11_img_data, light_image=ordernum_11_img_data, size=(98, 60))
CTkLabel(master=orderItem_11_frame, text="", image=ordernum_11_img).pack(side='left')

CTkLabel(master=orderItem_11_frame, text="Peach Mango Pie", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_11_frame, text="₱ 39.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(145, 0))

itemNumber_11 = customtkinter.CTkCheckBox(master=orderItem_11_frame, text="", width=20, command=show_checkoutItem_11)
itemNumber_11.pack(side='left', padx=(70,38))

#Item Number 12
orderItem_12_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_12_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_12_img_data = Image.open("resources/Chocolate-Sundae-Twirl 1.png")
ordernum_12_img = CTkImage(dark_image=ordernum_12_img_data, light_image=ordernum_12_img_data, size=(98, 60))
CTkLabel(master=orderItem_12_frame, text="", image=ordernum_12_img).pack(side='left')

CTkLabel(master=orderItem_12_frame, text="Chocolate Sundae", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_12_frame, text="₱ 39.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(131, 0))

itemNumber_12 = customtkinter.CTkCheckBox(master=orderItem_12_frame, text="", width=20, command=show_checkoutItem_12)
itemNumber_12.pack(side='left', padx=(70,38))

#Beverages
CTkLabel(master=orderScrollable_frame, text="Beverages", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 17),).pack(anchor="nw", pady=(20, 0))

#Item Number 13
orderItem_13_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_13_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_13_img_data = Image.open("resources/Coke-Regular 1.png")
ordernum_13_img = CTkImage(dark_image=ordernum_13_img_data, light_image=ordernum_13_img_data, size=(98, 60))
CTkLabel(master=orderItem_13_frame, text="", image=ordernum_13_img).pack(side='left')

CTkLabel(master=orderItem_13_frame, text="Coke", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_13_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(262, 0))

itemNumber_13 = customtkinter.CTkCheckBox(master=orderItem_13_frame, text="", width=20, command=show_checkoutItem_13)
itemNumber_13.pack(side='left', padx=(70,38))

#Item Number 14
orderItem_14_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_14_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_14_img_data = Image.open("resources/Sprite-Regular 1.png")
ordernum_14_img = CTkImage(dark_image=ordernum_14_img_data, light_image=ordernum_14_img_data, size=(98, 60))
CTkLabel(master=orderItem_14_frame, text="", image=ordernum_14_img).pack(side='left')

CTkLabel(master=orderItem_14_frame, text="Sprite", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_14_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(252, 0))

itemNumber_14 = customtkinter.CTkCheckBox(master=orderItem_14_frame, text="", width=20, command=show_checkoutItem_14)
itemNumber_14.pack(side='left', padx=(70,38))

#Item Number 15
orderItem_15_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_15_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_15_img_data = Image.open("resources/Pineapple-Juice-Regular 1.png")
ordernum_15_img = CTkImage(dark_image=ordernum_15_img_data, light_image=ordernum_15_img_data, size=(98, 60))
CTkLabel(master=orderItem_15_frame, text="", image=ordernum_15_img).pack(side='left')

CTkLabel(master=orderItem_15_frame, text="Pineapple juice", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_15_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(160, 0))

itemNumber_15 = customtkinter.CTkCheckBox(master=orderItem_15_frame, text="", width=20, command=show_checkoutItem_15)
itemNumber_15.pack(side='left', padx=(70,38))

#Item Number 16
orderItem_16_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_16_frame.pack(anchor="nw", pady=(20, 0))  

ordernum_16_img_data = Image.open("resources/Hot-Choco 1.png")
ordernum_16_img = CTkImage(dark_image=ordernum_16_img_data, light_image=ordernum_16_img_data, size=(98, 60))
CTkLabel(master=orderItem_16_frame, text="", image=ordernum_16_img).pack(side='left')

CTkLabel(master=orderItem_16_frame, text="Hot Chocolate", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_16_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(173, 0))

itemNumber_16 = customtkinter.CTkCheckBox(master=orderItem_16_frame, text="", width=20, command=show_checkoutItem_16)
itemNumber_16.pack(side='left', padx=(70,38))

#Item Number 17
orderItem_17_frame = CTkFrame(master=orderScrollable_frame, fg_color="#191D32", width=621, height=60, corner_radius=4)
orderItem_17_frame.pack(anchor="nw", pady=(20, 20))  

ordernum_17_img_data = Image.open("resources/Ice-Tea-Regular 1.png")
ordernum_17_img = CTkImage(dark_image=ordernum_17_img_data, light_image=ordernum_17_img_data, size=(98, 60))
CTkLabel(master=orderItem_17_frame, text="", image=ordernum_17_img).pack(side='left')

CTkLabel(master=orderItem_17_frame, text="Iced Tea", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left')

CTkLabel(master=orderItem_17_frame, text="₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 19),).pack(side='left', padx=(229, 0))

itemNumber_17 = customtkinter.CTkCheckBox(master=orderItem_17_frame, text="", width=20, command=show_checkoutItem_17)
itemNumber_17.pack(side='left', padx=(70,38))

#################################################################################
#Check Out Frame
#################################################################################

checkout_frame = CTkFrame(master=app, fg_color="#020410",  width=680, height=645, corner_radius=0)
checkout_frame.pack_forget()
checkout_frame.pack_propagate(0)
checkout_frame.pack(side="left")

CTkLabel(master=checkout_frame, text="Check Out", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="w", padx=(27, 0), pady=(29, 0))

checkoutScrollable_frame = CTkScrollableFrame(master=checkout_frame, fg_color="transparent", width=621, height=450)
checkoutScrollable_frame.pack(anchor="w", padx=(17, 0), pady=(20, 0))

#####
def removeItem_1():
    itemNumber_1.deselect()
    checkoutItem_1_frame.forget()
    Total['TA_1'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_2():
    itemNumber_2.deselect()
    checkoutItem_2_frame.forget()
    Total['TA_2'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱" + str(Total_Amount) + ".00")

def removeItem_3():
    itemNumber_3.deselect()
    checkoutItem_3_frame.forget()
    Total['TA_3'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_4():
    itemNumber_4.deselect()
    checkoutItem_4_frame.forget()
    Total['TA_4'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_5():
    itemNumber_5.deselect()
    checkoutItem_5_frame.forget()
    Total['TA_5'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_6():
    itemNumber_6.deselect()
    checkoutItem_6_frame.forget()
    Total['TA_6'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_7():
    itemNumber_7.deselect()
    checkoutItem_7_frame.forget()
    Total['TA_7'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_8():
    itemNumber_8.deselect()
    checkoutItem_8_frame.forget()
    Total['TA_8'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_9():
    itemNumber_9.deselect()
    checkoutItem_9_frame.forget()
    Total['TA_9'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_10():
    itemNumber_10.deselect()
    checkoutItem_10_frame.forget()
    Total['TA_10'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_11():
    itemNumber_11.deselect()
    checkoutItem_11_frame.forget()
    Total['TA_11'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_12():
    itemNumber_12.deselect()
    checkoutItem_12_frame.forget()
    Total['TA_12'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_13():
    itemNumber_13.deselect()
    checkoutItem_13_frame.forget()
    Total['TA_13'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_14():
    itemNumber_14.deselect()
    checkoutItem_14_frame.forget()
    Total['TA_14'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_15():
    itemNumber_15.deselect()
    checkoutItem_15_frame.forget()
    Total['TA_15'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_16():
    itemNumber_16.deselect()
    checkoutItem_16_frame.forget()
    Total['TA_16'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

def removeItem_17():
    itemNumber_17.deselect()
    checkoutItem_17_frame.forget()
    Total['TA_17'] = 0
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

#CHECKOUT LISTS
#remove button
remove_img_data = Image.open("resources/remove.png")
remove_img = CTkImage(dark_image=remove_img_data, light_image=remove_img_data, size=(18, 17))

CTkLabel(master=checkoutScrollable_frame, text="Meals                                     Price               Quantity         Amount", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 17),).pack(anchor="nw", padx=(12, 0))

#item 1

checkoutItem_1_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_1_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_1_frame.forget()

CTkLabel(master=checkoutItem_1_frame, text="Fried Chicken w/ Rice               ₱ 95.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_1(*args):
    amountItem_1_val = 95 * int(quantityItem_1.get())
    amountItem_1.configure(text=amountItem_1_val)
    Total['TA_1'] = 95 * int(quantityItem_1.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_1 = customtkinter.CTkOptionMenu(master=checkoutItem_1_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_1)
quantityItem_1.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_1_val = 95 * int(quantityItem_1.get())
amountItem_1 = CTkLabel(master=checkoutItem_1_frame, text=amountItem_1_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_1.pack(side='left', padx=(49, 0))

removeItem_1_button = CTkButton(master=checkoutItem_1_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_1)
removeItem_1_button.pack(side='left', padx=(60, 49))

#item 2

checkoutItem_2_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_2_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_2_frame.forget()

CTkLabel(master=checkoutItem_2_frame, text="Jolly Spaghetti                             ₱ 50.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_2(*args):
    amountItem_2_val = 50 * int(quantityItem_2.get())
    amountItem_2.configure(text=amountItem_2_val)
    Total['TA_2'] = 50 * int(quantityItem_2.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_2 = customtkinter.CTkOptionMenu(master=checkoutItem_2_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_2)
quantityItem_2.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_2_val = 50 * int(quantityItem_2.get())
amountItem_2 = CTkLabel(master=checkoutItem_2_frame, text=amountItem_2_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_2.pack(side='left', padx=(49, 0))

removeItem_2_button = CTkButton(master=checkoutItem_2_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_2)
removeItem_2_button.pack(side='left', padx=(60, 49))

#item 3

checkoutItem_3_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_3_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_3_frame.forget()

CTkLabel(master=checkoutItem_3_frame, text="Palabok Fiesta                             ₱160.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_3(*args):
    amountItem_3_val = 160 * int(quantityItem_3.get())
    amountItem_3.configure(text=amountItem_3_val)
    Total['TA_3'] = 160 * int(quantityItem_3.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")


quantityItem_3 = customtkinter.CTkOptionMenu(master=checkoutItem_3_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_3)
quantityItem_3.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_3_val = 160 * int(quantityItem_3.get())
amountItem_3 = CTkLabel(master=checkoutItem_3_frame, text=amountItem_3_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_3.pack(side='left', padx=(49, 0))

removeItem_3_button = CTkButton(master=checkoutItem_3_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_3)
removeItem_3_button.pack(side='left', padx=(57, 49))

#item 4

checkoutItem_4_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_4_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_4_frame.forget()

CTkLabel(master=checkoutItem_4_frame, text="Chicken Sandwich                      ₱ 65.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_4(*args):
    amountItem_4_val = 65 * int(quantityItem_4.get())
    amountItem_4.configure(text=amountItem_4_val)
    Total['TA_4'] = 165 * int(quantityItem_4.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_4 = customtkinter.CTkOptionMenu(master=checkoutItem_4_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_4)
quantityItem_4.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_4_val = 65 * int(quantityItem_4.get())
amountItem_4 = CTkLabel(master=checkoutItem_4_frame, text=amountItem_4_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_4.pack(side='left', padx=(49, 0))

removeItem_4_button = CTkButton(master=checkoutItem_4_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_4)
removeItem_4_button.pack(side='left', padx=(60, 49))

#item 5

checkoutItem_5_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_5_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_5_frame.forget()

CTkLabel(master=checkoutItem_5_frame, text="Burger                                                  ₱ 50.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_5(*args):
    amountItem_5_val = 50 * int(quantityItem_5.get())
    amountItem_5.configure(text=amountItem_5_val)
    Total['TA_5'] = 50 * int(quantityItem_5.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_5 = customtkinter.CTkOptionMenu(master=checkoutItem_5_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_5)
quantityItem_5.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_5_val = 50 * int(quantityItem_5.get())
amountItem_5 = CTkLabel(master=checkoutItem_5_frame, text=amountItem_5_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_5.pack(side='left', padx=(49, 0))

removeItem_5_button = CTkButton(master=checkoutItem_5_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right" , command=removeItem_5)
removeItem_5_button.pack(side='left', padx=(60, 49))

#item 6

checkoutItem_6_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_6_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_6_frame.forget()

CTkLabel(master=checkoutItem_6_frame, text="Burger Steak                                   ₱ 85.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_6(*args):
    amountItem_6_val = 85 * int(quantityItem_6.get())
    amountItem_6.configure(text=amountItem_6_val)
    Total['TA_6'] = 85 * int(quantityItem_6.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_6 = customtkinter.CTkOptionMenu(master=checkoutItem_6_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_6)
quantityItem_6.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_6_val = 85 * int(quantityItem_6.get())
amountItem_6 = CTkLabel(master=checkoutItem_6_frame, text=amountItem_6_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_6.pack(side='left', padx=(49, 0))

removeItem_6_button = CTkButton(master=checkoutItem_6_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_6)
removeItem_6_button.pack(side='left', padx=(60, 49))

#item 7

checkoutItem_7_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_7_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_7_frame.forget()

CTkLabel(master=checkoutItem_7_frame, text="Fries                                                       ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_7(*args):
    amountItem_7_val = 35 * int(quantityItem_7.get())
    amountItem_7.configure(text=amountItem_7_val)
    Total['TA_7'] = 35 * int(quantityItem_7.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_7 = customtkinter.CTkOptionMenu(master=checkoutItem_7_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_7)
quantityItem_7.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_7_val = 35 * int(quantityItem_7.get())
amountItem_7 = CTkLabel(master=checkoutItem_7_frame, text=amountItem_7_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_7.pack(side='left', padx=(49, 0))

removeItem_7_button = CTkButton(master=checkoutItem_7_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_7)
removeItem_7_button.pack(side='left', padx=(60, 49))

#item 8

checkoutItem_8_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_8_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_8_frame.forget()

CTkLabel(master=checkoutItem_8_frame, text="Creamy Macaroni Soup         ₱ 55.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_8(*args):
    amountItem_8_val = 55 * int(quantityItem_8.get())
    amountItem_8.configure(text=amountItem_8_val)
    Total['TA_8'] = 55 * int(quantityItem_8.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_8 = customtkinter.CTkOptionMenu(master=checkoutItem_8_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_8)
quantityItem_8.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_8_val = 55 * int(quantityItem_8.get())
amountItem_8 = CTkLabel(master=checkoutItem_8_frame, text=amountItem_8_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_8.pack(side='left', padx=(49, 0))

removeItem_8_button = CTkButton(master=checkoutItem_8_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_8)
removeItem_8_button.pack(side='left', padx=(60, 49))

#item 9

checkoutItem_9_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_9_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_9_frame.forget()

CTkLabel(master=checkoutItem_9_frame, text="Rice                                                         ₱ 20.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_9(*args):
    amountItem_9_val = 20 * int(quantityItem_9.get())
    amountItem_9.configure(text=amountItem_9_val)
    Total['TA_9'] = 20 * int(quantityItem_9.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_9 = customtkinter.CTkOptionMenu(master=checkoutItem_9_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_9)
quantityItem_9.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_9_val = 20 * int(quantityItem_9.get())
amountItem_9 = CTkLabel(master=checkoutItem_9_frame, text=amountItem_9_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_9.pack(side='left', padx=(49, 0))

removeItem_9_button = CTkButton(master=checkoutItem_9_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_9)
removeItem_9_button.pack(side='left', padx=(60, 49))

#item 10

checkoutItem_10_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_10_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_10_frame.forget()

CTkLabel(master=checkoutItem_10_frame, text="Gravy                                                     ₱ 15.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_10(*args):
    amountItem_10_val = 15 * int(quantityItem_10.get())
    amountItem_10.configure(text=amountItem_10_val)
    Total['TA_10'] = 15 * int(quantityItem_10.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_10 = customtkinter.CTkOptionMenu(master=checkoutItem_10_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_10)
quantityItem_10.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_10_val = 15 * int(quantityItem_10.get())
amountItem_10 = CTkLabel(master=checkoutItem_10_frame, text=amountItem_10_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_10.pack(side='left', padx=(49, 0))

removeItem_10_button = CTkButton(master=checkoutItem_10_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_10)
removeItem_10_button.pack(side='left', padx=(60, 49))

#item 11

checkoutItem_11_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_11_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_11_frame.forget()

CTkLabel(master=checkoutItem_11_frame, text="Peach Mango Pie                          ₱ 39.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_11(*args):
    amountItem_11_val = 39 * int(quantityItem_11.get())
    amountItem_11.configure(text=amountItem_11_val)
    Total['TA_11'] = 39 * int(quantityItem_11.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_11 = customtkinter.CTkOptionMenu(master=checkoutItem_11_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_11)
quantityItem_11.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_11_val = 39 * int(quantityItem_11.get())
amountItem_11 = CTkLabel(master=checkoutItem_11_frame, text=amountItem_11_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_11.pack(side='left', padx=(49, 0))

removeItem_11_button = CTkButton(master=checkoutItem_11_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_11)
removeItem_11_button.pack(side='left', padx=(60, 49))

#item 12

checkoutItem_12_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_12_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_12_frame.forget()

CTkLabel(master=checkoutItem_12_frame, text="Chocolate Sundae                      ₱ 39.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_12(*args):
    amountItem_12_val = 39 * int(quantityItem_12.get())
    amountItem_12.configure(text=amountItem_12_val)
    Total['TA_12'] = 39 * int(quantityItem_12.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_12 = customtkinter.CTkOptionMenu(master=checkoutItem_12_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_12)
quantityItem_12.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_12_val = 39 * int(quantityItem_12.get())
amountItem_12 = CTkLabel(master=checkoutItem_12_frame, text=amountItem_12_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_12.pack(side='left', padx=(49, 0))

removeItem_12_button = CTkButton(master=checkoutItem_12_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_12)
removeItem_12_button.pack(side='left', padx=(60, 49))

#item 13

checkoutItem_13_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_13_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_13_frame.forget()

CTkLabel(master=checkoutItem_13_frame, text="Coke                                                      ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_13(*args):
    amountItem_13_val = 35 * int(quantityItem_13.get())
    amountItem_13.configure(text=amountItem_13_val)
    Total['TA_13'] = 35 * int(quantityItem_13.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_13 = customtkinter.CTkOptionMenu(master=checkoutItem_13_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_13)
quantityItem_13.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_13_val = 35 * int(quantityItem_13.get())
amountItem_13 = CTkLabel(master=checkoutItem_13_frame, text=amountItem_13_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_13.pack(side='left', padx=(49, 0))

removeItem_13_button = CTkButton(master=checkoutItem_13_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_13)
removeItem_13_button.pack(side='left', padx=(60, 49))

#item 14

checkoutItem_14_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_14_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_14_frame.forget()

CTkLabel(master=checkoutItem_14_frame, text="Sprite                                                    ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_14(*args):
    amountItem_14_val = 35 * int(quantityItem_14.get())
    amountItem_14.configure(text=amountItem_14_val)
    Total['TA_14'] = 35 * int(quantityItem_14.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_14 = customtkinter.CTkOptionMenu(master=checkoutItem_14_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_14)
quantityItem_14.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_14_val = 35 * int(quantityItem_14.get())
amountItem_14 = CTkLabel(master=checkoutItem_14_frame, text=amountItem_14_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_14.pack(side='left', padx=(49, 0))

removeItem_14_button = CTkButton(master=checkoutItem_14_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_14)
removeItem_14_button.pack(side='left', padx=(60, 49))

#item 15

checkoutItem_15_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_15_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_15_frame.forget()

CTkLabel(master=checkoutItem_15_frame, text="Pineapple juice                             ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_15(*args):
    amountItem_15_val = 35 * int(quantityItem_15.get())
    amountItem_15.configure(text=amountItem_15_val)
    Total['TA_15'] = 35 * int(quantityItem_15.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_15 = customtkinter.CTkOptionMenu(master=checkoutItem_15_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_15)
quantityItem_15.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_15_val = 35 * int(quantityItem_15.get())
amountItem_15 = CTkLabel(master=checkoutItem_15_frame, text=amountItem_15_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_15.pack(side='left', padx=(49, 0))

removeItem_15_button = CTkButton(master=checkoutItem_15_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_15)
removeItem_15_button.pack(side='left', padx=(60, 49))

#item 16

checkoutItem_16_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_16_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_16_frame.forget()

CTkLabel(master=checkoutItem_16_frame, text="Hot Chocolate                                ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_16(*args):
    amountItem_16_val = 35 * int(quantityItem_16.get())
    amountItem_16.configure(text=amountItem_16_val)
    Total['TA_16'] = 35 * int(quantityItem_16.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")

quantityItem_16 = customtkinter.CTkOptionMenu(master=checkoutItem_16_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_16)
quantityItem_16.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_16_val = 35 * int(quantityItem_16.get())
amountItem_16 = CTkLabel(master=checkoutItem_16_frame, text=amountItem_16_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_16.pack(side='left', padx=(49, 0))

removeItem_16_button = CTkButton(master=checkoutItem_16_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_16)
removeItem_16_button.pack(side='left', padx=(60, 49))

#item 17

checkoutItem_17_frame = CTkFrame(master=checkoutScrollable_frame, fg_color="#191D32", width=621, height=42, corner_radius=4)
checkoutItem_17_frame.pack(anchor="nw", pady=(12, 0)) 
checkoutItem_17_frame.forget()

CTkLabel(master=checkoutItem_17_frame, text="Iced Tea                                              ₱ 35.00", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0))

def update_amountItem_17(*args):
    amountItem_17_val = 35 * int(quantityItem_17.get())
    amountItem_17.configure(text=amountItem_17_val)
    Total['TA_17'] = 35 * int(quantityItem_17.get())
    Total_Amount = sum(Total.values())
    totalAmount.configure(text="₱ " + str(Total_Amount) + ".00") 

quantityItem_17 = customtkinter.CTkOptionMenu(master=checkoutItem_17_frame, values=[str(i) for i in range(1, 101)], width=50, height=22, font=("Poppins Bold", 14), command=update_amountItem_17)
quantityItem_17.pack(side="left", padx=(68, 30), pady=(7, 7))

amountItem_17_val = 35 * int(quantityItem_17.get())
amountItem_17 = CTkLabel(master=checkoutItem_17_frame, text=amountItem_17_val, text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14))
amountItem_17.pack(side='left', padx=(49, 0))

removeItem_17_button = CTkButton(master=checkoutItem_17_frame, image=remove_img, text="", fg_color="#981616", font=("Poppins Bold", 12), hover_color="#480A0A", anchor="e", width=25, height=25, compound="right", command=removeItem_17)
removeItem_17_button.pack(side='left', padx=(60, 49))

#BOTTOM FRAME

checkoutBottom_frame = CTkFrame(master=checkout_frame, fg_color="#0C1F0E", width=700)
checkoutBottom_frame.pack(anchor="s", padx=(0, 0), pady=(25, 0))  

CTkLabel(master=checkoutBottom_frame, text="Total Amount: ", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 14),).pack(side='left', padx=(10, 0), pady=(10, 10))

def update_total_amount():  
    print(Total_Amount)
    
totalAmount = CTkLabel(master=checkoutBottom_frame, text="₱ " + str(Total_Amount) + ".00" , fg_color="#010311", text_color="#fff", anchor="w", justify="left", font=("Poppins Bold", 12), height=30, width=157, corner_radius=4)
totalAmount.pack(side='left', padx=(5, 0), pady=(10, 10))

#disable the addQueue_button until dineoption != "[Dine Type]" and payment != "[Payment]"
def update_addQueue_button_state(*args):
    if dineoption.get() != "[Dine Type]" and payment.get() != "[Payment]":
        addQueue_button.configure(state="normal")
    else:
        addQueue_button.configure(state="disabled")

dineoption = CTkOptionMenu(master=checkoutBottom_frame, values=["[Dine Type]", "Dine In", "Take Out", "Drive Thru"], width=98, height=22, font=("Poppins Bold", 10), command=update_addQueue_button_state)
dineoption.pack(side="left", padx=(10, 0), pady=(7, 7))

payment = CTkOptionMenu(master=checkoutBottom_frame, values=["[Payment]","Cash", "Card", "E-Money"], width=98, height=22, font=("Poppins Bold", 10), command=update_addQueue_button_state)
payment.pack(side="left", padx=(10 ,0), pady=(7, 7))

def generate_order_id():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    # Generate a new order_id
    mycursor.execute("SELECT MAX(order_id) FROM orders")
    result = mycursor.fetchone()
    if result[0] is not None:
        new_order_id = result[0] + 1
    else:
        new_order_id = 1001
    return new_order_id

def create_cart_entries(order_id, Total):
    # Connect to the MySQL database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    # Iterate through the 'Total' dictionary
    for key, value in Total.items():
        if value > 0:
            # Extract the item code (e.g., 'TA_3' to '3')
            item_code = int(key.split('_')[1])

            # Retrieve the price from the 'menu' table
            mycursor.execute("SELECT price FROM menu WHERE item_code = %s", (item_code,))
            price_result = mycursor.fetchone()
            if price_result is not None:
                price = price_result[0]
            else:
                price = 0  # Handle if item not found in the menu

            # Get the quantity 
            quantity = value // price   

            # Calculate the amount
            amount = price * quantity

            # Insert the data into the 'cart' table with the same new_order_id
            sql = "INSERT INTO cart (order_id, item_code, price, quantity, amount) VALUES (%s, %s, %s, %s, %s)"
            val = (order_id, item_code, price, quantity, amount)
            mycursor.execute(sql, val)
            mydb.commit()

    # Close the database connection
    mydb.close()


def addInQueue_OrdersTable():
    print("addInQueue Button Pressed")
    try:
        order_id = generate_order_id()

        # Get the current time
        current_time = datetime.now()

        # Calculate the Total_Amount
        Total_Amount = sum(Total.values())

        # Define the "Processing" status
        status = "Processing"

        # Initialize estimated_time and finished_time
        estimated_time = "0"
        finished_time = "0"
        highest_est_time = 0

        # Find the items in the Total dictionary with quantities greater than 0
        items_with_quantity = [item for item, quantity in Total.items() if quantity > 0]

        if items_with_quantity:
            # Extract item codes (e.g., 'TA_1' to 1) and convert them to integers
            item_codes = [int(item.split('_')[1]) for item in items_with_quantity]

            # Connect to the database and fetch the maximum est-time for selected items
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
            mycursor = mydb.cursor()

            placeholders = ', '.join(['%s'] * len(item_codes))
            sql = f"SELECT est_time FROM menu WHERE item_code IN ({placeholders})"
            mycursor.execute(sql, item_codes)
            est_time_results = mycursor.fetchall()

            max_est_time_result = max(result[0] for result in est_time_results)

            estimated_time = str(max_est_time_result) + " minutes"
            finished_time = current_time + timedelta(minutes=max_est_time_result)

        # Insert the new order into the "orders" table
        sql = "INSERT INTO orders (order_id, time_ordered, sales, status, time_est, time_finished) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (order_id, current_time, Total_Amount, status, estimated_time, finished_time)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.close()
        mydb.close()

        # Create a message box
        CTkMessagebox(title="Info", message="New order in queue \nOrder ID: " + str(order_id))
        create_cart_entries(order_id, Total)

        delays_popup()

        # Resets everything after an order
        for i in range(1, 18):
            exec(f"itemNumber_{i}.deselect()")
            exec(f"checkoutItem_{i}_frame.forget()")
            exec(f"Total['TA_{i}'] = 0")
            Total_Amount = sum(Total.values())
            totalAmount.configure(text="₱ " + str(Total_Amount) + ".00")
        addQueue_button.configure(state="disabled")
        dineoption.set("[Dine Type]")
        payment.set("[Payment]")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


addQueue_button = CTkButton(master=checkoutBottom_frame, text="Add to Queue", fg_color="#158921", font=("Poppins Bold", 10), hover_color="#0A3D0F", anchor="center", width=136, height=22, command=addInQueue_OrdersTable)
addQueue_button.pack(side='left', padx=(15, 15))
addQueue_button.configure(state="disabled")


#################################################################################
#Inventory Frame
#################################################################################

inventory_frame = CTkFrame(master=app, fg_color="#020410",  width=680, height=645, corner_radius=0)
inventory_frame.pack_forget()
inventory_frame.pack_propagate(0)
inventory_frame.pack(side="left")

CTkLabel(master=inventory_frame, text="Inventory", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="w", padx=(27, 0), pady=(29, 0))

# Rectangle Parent frame of Rectangles
inventoryRectangle_frame = CTkFrame(master=inventory_frame, fg_color="transparent", width=680, height=70, corner_radius=4)
inventoryRectangle_frame.pack(anchor="w", padx=(27, 0), pady=(15, 0))

def completedOrdersLabel_command():
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    #retrieve the orders table data which only gets the status that is "Completed" and "Delayed"
    sql = "SELECT order_id, time_ordered, sales, status FROM orders WHERE status = 'Completed' OR status = 'Delayed'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #count the number of completed orders and delayed orders and put it in the label
    numofcompletedorders_NUM.configure(text=str(len(myresult)))

def totalSalesLabel_command():
    #connect to database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    #retrieve the orders table data which only gets the sales except the status that is "Voided"
    sql = "SELECT sales FROM orders WHERE status != 'Voided'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #count the number of completed orders and delayed orders and put it in the label
    total_sales = 0
    for sales in myresult:
        total_sales += sales[0]
    numoftotalSales_NUM.configure(text="₱ " + str(total_sales))

# Completed Orders Rectangle
inventoryOrders_rectangle = CTkFrame(master=inventoryRectangle_frame, fg_color="#70179A", width=201, height=70, corner_radius=4)
inventoryOrders_rectangle.pack_propagate(False)
inventoryOrders_rectangle.pack(side='left')

numofcompletedorders_label = CTkLabel(master=inventoryOrders_rectangle, text="Completed Orders", fg_color="transparent", text_color="#fff", font=("Poppins Bold", 15), anchor="w", width=201)
numofcompletedorders_label.pack(anchor="w", padx=(10, 0), pady=(5, 0))

numofcompletedorders_NUM = CTkLabel(master=inventoryOrders_rectangle, text="₱ 0.00", text_color="#fff",fg_color="transparent", font=("Poppins Bold", 25), anchor="w", width=201)
numofcompletedorders_NUM.pack(anchor="w" , padx=(10, 0), pady=(0, 0))

# Total Sales Rectangle
totalSales_rectangle = CTkFrame(master=inventoryRectangle_frame, fg_color="#146C63", width=201, height=70, corner_radius=4)
totalSales_rectangle.pack_propagate(False)
totalSales_rectangle.pack(side='left', padx=(20, 0))

numoftotalSales_label = CTkLabel(master=totalSales_rectangle, text="Total Sales", fg_color="transparent", text_color="#fff", font=("Poppins Bold", 15), anchor="w", width=201)
numoftotalSales_label.pack(anchor="w", padx=(10, 0), pady=(5, 0))

numoftotalSales_NUM = CTkLabel(master=totalSales_rectangle, text="0", text_color="#fff",fg_color="transparent", font=("Poppins Bold", 25), anchor="w", width=201)
numoftotalSales_NUM.pack(anchor="w" , padx=(10, 0), pady=(0, 0))

completedOrdersLabel_command()
totalSalesLabel_command()

CTkLabel(master=inventory_frame, text="Order History", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="nw" , padx=(27, 0), pady=(20, 0))

InventTable_data = [["Order ID", "Time Ordered", "Sales", "Status"]]  # Initialize with headers

InventTable_frame = CTkScrollableFrame(master=inventory_frame, fg_color="transparent")
InventTable_frame.pack(expand=True, fill="both", padx=27, pady=21, side='bottom')


def show_InventTable():
    global InventTable
    global InventTable_data
    def retreive_data_for_database():
        #retrieve data from database and put it in the table
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        #retrieve the orders table data which only order_id, time_ordered, time_est
        sql = "SELECT order_id, time_ordered, sales, status FROM orders"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    def format_result_to_table_data(myresult, header=["Order ID", "Time Ordered", "Sales", "Status"]):
        InventTable_data = [header]
        for order_id, time_ordered, sales, status in myresult:
            formatted_time_ordered = time_ordered.strftime("%Y-%m-%d %H:%M:%S")
            InventTable_data.append([order_id, formatted_time_ordered, sales, status])

        return InventTable_data
    
    InventTable_data = format_result_to_table_data(retreive_data_for_database())

    InventTable.destroy()

    InventTable = CTkTable(master=InventTable_frame, values=InventTable_data, colors=["#010311", "#070b21"], header_color="#1f6aa5", hover_color="#181A27")
    InventTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    InventTable.pack(expand=True)

InventTable = CTkTable(master=InventTable_frame, values=InventTable_data, colors=["#010311", "#070b21"], header_color="#1f6aa5", hover_color="#181A27")
InventTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
InventTable.pack(expand=True)

show_InventTable()

#################################################################################
#Account Settings Frame
#################################################################################

accountsettings_frame = CTkFrame(master=app, fg_color="#020410",  width=680, height=645, corner_radius=0)
accountsettings_frame.pack_forget()
accountsettings_frame.pack_propagate(0)
accountsettings_frame.pack(side="left")

CTkLabel(master=accountsettings_frame, text="Account Settings", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="w", padx=(27, 0), pady=(29, 0))

#create scrollable frame
accountsettingsScrollable_frame = CTkScrollableFrame(master=accountsettings_frame, fg_color="transparent")
accountsettingsScrollable_frame.pack(expand=True, fill="both", side='bottom')

accountEdit_frame = CTkFrame(master=accountsettingsScrollable_frame, fg_color="#0E1121", width=630, height=100, corner_radius=4)
accountEdit_frame.pack(anchor="w", padx=(27, 0), pady=(15, 0))

CTkLabel(master=accountEdit_frame, text="Edit Account", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="nw" , padx=(27, 0), pady=(20, 0))

CTkLabel(master=accountEdit_frame, text="Employee ID:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0), pady=(5, 0))
employeeid_entry = customtkinter.CTkEntry(master=accountEdit_frame, width=350, height=25, placeholder_text=loggedin_employee_id)
employeeid_entry.pack(anchor="w", padx=(27, 227))

CTkLabel(master=accountEdit_frame, text="First Name:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0))
fname_entry = customtkinter.CTkEntry(master=accountEdit_frame, width=350, height=25, placeholder_text=loggedin_fname)
fname_entry.pack(anchor="w", padx=(27, 227))

CTkLabel(master=accountEdit_frame, text="Last Name:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0))
lname_entry = customtkinter.CTkEntry(master=accountEdit_frame, width=350, height=25, placeholder_text=loggedin_lname)
lname_entry.pack(anchor="w", padx=(27, 227))


CTkLabel(master=accountEdit_frame, text="Confirm Password:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0))
confirmpassword_entry = customtkinter.CTkEntry(master=accountEdit_frame, width=350, height=25, show="*")
confirmpassword_entry.pack(anchor="w", padx=(27, 227))

def update_account():
    # Get the values from the entries
    employee_id = employeeid_entry.get() if employeeid_entry.get() else loggedin_employee_id
    fname = fname_entry.get() if fname_entry.get() else loggedin_fname
    lname = lname_entry.get() if lname_entry.get() else loggedin_lname
    confirm_password = confirmpassword_entry.get()
    new_password = newpassword_entry.get()

    # Connect to the database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    # Verify the employee ID and password
    sql = "SELECT * FROM users WHERE employee_id = %s AND password = %s"
    val = (employee_id, confirm_password)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    # If the employee ID and password are correct, update the account
    if myresult:
        sql = "UPDATE users SET fname = %s, lname = %s WHERE employee_id = %s"
        val = (fname, lname, employee_id)
        print(mycursor.rowcount, "Account record(s) affected")
        msg = CTkMessagebox(message="Account Updated! \nPlease Log in again", icon="check", option_1="Thanks")
        if msg.get() == "Thanks":
            mycursor.execute(sql, val)
            mydb.commit()
            app.destroy()
            os.system("python startup.py")

    else:
        print("Incorrect employee ID or password")
        CTkMessagebox(title="Error", message="You entered incorrect \nEmployee ID or Password!\nPlease try again", icon="cancel")

updateAccount_button = CTkButton(master=accountEdit_frame, text="Update Account", font=("Poppins Bold", 10), hover_color="#08365A", anchor="center", width=118, height=20, command=update_account)
updateAccount_button.pack(anchor='center', padx=(10, 15), pady=(15, 10))

#Change password
changepassword_frame = CTkFrame(master=accountsettingsScrollable_frame, fg_color="#0E1121", width=604, height=100, corner_radius=4)
changepassword_frame.pack(anchor="w", padx=(27, 0), pady=(15, 0))

CTkLabel(master=changepassword_frame, text="Change Password", text_color="#E7F3F3", anchor="w", justify="left", font=("Poppins Bold", 27),).pack(anchor="nw" , padx=(27, 0), pady=(20, 0))

CTkLabel(master=changepassword_frame, text="Current Password:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0))
currentpassword_entry = customtkinter.CTkEntry(master=changepassword_frame, width=350, height=25, show="*")
currentpassword_entry.pack(anchor="w", padx=(27, 227))

CTkLabel(master=changepassword_frame, text="New Password:", text_color="#7E7E7E", anchor="w", justify="left", font=("Poppins Bold", 12),).pack(anchor="nw" , padx=(27, 0))
newpassword_entry = customtkinter.CTkEntry(master=changepassword_frame, width=350, height=25, show="*")
newpassword_entry.pack(anchor="w", padx=(27, 227))

def changepassword_command():
    employee_id = employeeid_entry.get() if employeeid_entry.get() else loggedin_employee_id
    current_password = currentpassword_entry.get()
    new_password = newpassword_entry.get()
    # Connect to the database
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
    mycursor = mydb.cursor()

    # Verify the employee ID and password
    sql = "SELECT * FROM users WHERE employee_id = %s AND password = %s"
    val = (employee_id, current_password)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    #f statement if the current password is not correct
    if not myresult:
        print("Incorrect employee ID or password")
        CTkMessagebox(title="Error", message="You entered incorrect \nEmployee ID or Password!\nPlease try again", icon="cancel")
        return

    #if statement if the new password is the same as blank
    if new_password == "":
        print("New password cannot be blank")
        CTkMessagebox(title="Error", message="New password cannot be blank!\nPlease try again", icon="cancel")
        return

    sql = "UPDATE users SET password = %s WHERE employee_id = %s"
    val = (new_password, employee_id)
    mycursor.execute(sql, val)
    mydb.commit()
    msg = CTkMessagebox(message="Account Password Updated! \nPlease Log in again", icon="check", option_1="Thanks")
    print(mycursor.rowcount, "Password record(s) affected")
    if msg.get() == "Thanks":
        mydb.commit()
        app.destroy()
        os.system("python startup.py")
    else:
        print("Incorrect Employee ID or Password")
        CTkMessagebox(title="Error", message="You entered incorrect \nEmployee ID or Password!\nPlease try again", icon="cancel")

changepassword_button = CTkButton(master=changepassword_frame, text="Change Password", font=("Poppins Bold", 10), hover_color="#08365A", anchor="center", width=118, height=20, command=changepassword_command)
changepassword_button.pack(anchor='center', padx=(10, 15), pady=(15, 10))

####

def deleteAccount_command():
    employee_id = employeeid_entry.get() if employeeid_entry.get() else loggedin_employee_id
   
    msg = CTkMessagebox(title="DELETING YOUR ACCOUNT?", message="Do you want to delete this account?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()

    if response=="Yes":
        #connect to a database and delete all the data in the orders table
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        sql = "DELETE FROM users WHERE employee_id = %s"
        val = (employee_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Account record(s) deleted")
        mycursor.close()
        mydb.close()
        #create a message box
        msg = CTkMessagebox(message="Account has been deleted!", icon="check", option_1="Thanks")
        print(mycursor.rowcount, "Password record(s) affected")
        if msg.get() == "Thanks":
            app.destroy()
    else:
        pass

deleteAccount_button = CTkButton(master=accountsettingsScrollable_frame, text="Delete Account", font=("Poppins Bold", 10), hover_color="#480A0A", anchor="center", width=118, height=20, fg_color="#981616", command=deleteAccount_command)
deleteAccount_button.pack(anchor='center', padx=(10, 15), pady=(15, 0))

def resetInventory_command():
    # get yes/no answers
    msg = CTkMessagebox(title="RESET INVENTORY?", message="Do you want to reset the \nENTIRE INVENTORY?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
        #connect to a database and delete all the data in the orders table
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
        mycursor = mydb.cursor()
        sql = "DELETE FROM cart"
        mycursor.execute(sql)
        sql = "DELETE FROM orders"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        #create a message box
        CTkMessagebox(title="Info", message="Inventory has been reset!")
    else:
        pass

resetInventory_button = CTkButton(master=accountsettingsScrollable_frame, text="Reset Inventory", font=("Poppins Bold", 10), hover_color="#480A0A", anchor="center", width=118, height=20, fg_color="#981616", command=resetInventory_command)
resetInventory_button.pack(anchor='center', padx=(10, 15), pady=(15, 10))


app.mainloop()