import smtplib
import random as r
import time

def send_email(receiver_email, message):
    
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        #587 is the default SMTP port for gmail.
        #It may be different for:
            #outlook/On-prem or Hybrid exchange server/Office 365
            #protonmail etc.
        
        print("Generating session. Please wait.")
        smtp.starttls()
        #gmail uses TLS certificate for encryption of all mail traffics
        
        
        ##########
        smtp.login("testing.suraim@gmail.com", "letstest2codes")
        ##########
        
        smtp.sendmail("testing.suraim@gmail.com", receiver_email, message)
        smtp.quit()
    
    except Exception:
        print(Exception)
        print("Above is the error message.")
        
        
        
#def verification functions will be added here on the next video
#This code will be extended to replicate the verification process, done by many major website.
#E.g. Facebook SignUp.
#We will send a verification code to a user email to verify the email address.

receiver_email = input("Please enter receiver email:")
message = input("PLease type a message:")
send_email(receiver_email, message)
