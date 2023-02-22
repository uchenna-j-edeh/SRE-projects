"""
To write a script that monitors system resources and alerts when they exceed a certain threshold, you can use Python's psutil module to collect system resource metrics and a Python module such as smtplib to send email alerts. Here is an example script:
"""
import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time
import sys

# Set the threshold for CPU and memory usage (in percent)
cpu_threshold = 80
mem_threshold = 80

# Set the email sender and recipient
sender = "write2uche@gmail.com"
recipient = "write2uche@gmail.com"

# Set up the email server
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "username"
smtp_password = "password"

while True:
    # Get the current CPU and memory usage
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent

    # Check if the usage is above the threshold
    if cpu_percent > cpu_threshold or mem_percent > mem_threshold:
        # Send an email alert
        subject = "System Resource Alert"
        body = f"CPU usage: {cpu_percent}%\nMemory usage: {mem_percent}%"
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, message.as_string())
    else:
        sys.stdout.write("nothing to report, sleeping for the next 60 seconds...")
    # Wait for some time before checking again
    time.sleep(60)

