import mysql.connector
import sched
import time
from datetime import datetime, timedelta

# Create a scheduler
scheduler = sched.scheduler(time.time, time.sleep)

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="queue_system")
mycursor = mydb.cursor()

# Define a function to show the notification
def show_notification(message):
    print(f"Notification: {message}")

# Define a function to fetch and schedule notifications
def schedule_notifications():
    #get the time_finished and order_id from the database table named orders that has a status of processing
    query = "SELECT time_finished, order_id FROM orders WHERE status = 'processing'"
    mycursor.execute(query)
    notifications = mycursor.fetchall()

# Fetch and schedule notifications
schedule_notifications()

# Fetch and schedule notifications
notifications = mycursor.fetchall()

# Loop through the notifications and schedule them
for scheduled_time, notification_message in notifications:
    # Calculate the delay until the scheduled time
    current_time = datetime.now()
    delay = (scheduled_time - current_time).total_seconds()

    if delay > 0:
        scheduler.enter(delay, 1, show_notification, (notification_message,))

# Start the scheduler
scheduler.run()

# Close the cursor and connection
mycursor.close()
mydb.close()