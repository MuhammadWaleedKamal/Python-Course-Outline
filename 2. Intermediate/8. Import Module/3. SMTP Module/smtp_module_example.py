"""
SMTP module example.
Builds a simple email message without sending it.
"""

from email.message import EmailMessage

message = EmailMessage()
message['Subject'] = "Welcome to the course"
message['From'] = "instructor@example.com"
message['To'] = "student@example.com"
message.set_content("Hello! This is a sample email created in Python.")

print(message)

# Exercises:
# 1. Add a second recipient to the email.
# 2. Change the subject and body text.
# 3. Comment how smtplib.SMTP would be used to send this message.
