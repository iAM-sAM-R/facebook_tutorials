from cryptography.fernet import Fernet
import smtplib



def email_key(receiver_email, master_key):
    try:
        smtp = smtplib.smptp('smtp.gmail.com', 587)
        #gmail uses port 587 for it's smtp services
        print("Generating SMTP session.")
        smtp.starttls()
        smtp.sendmail("testparkd4@gmail.com", receiver_email, master_key)
        smtp.quit()
    
    except:
        print(Exception)
        print("Above is the exception that may have caused the email to be not to delivered.")

def file_finder():
    choice_var = input("Please enter a file directory to find the file to encrypt:")
    file_name = input("Please enter the filename (With extension. E.g. .pdf, .docx):")
    filepath = choice_var + file_name
    return filepath, choice_var
    

filepath, choice_var = file_finder()


master_key = Fernet.generate_key()
email_key("emailaddress", master_key)


def enc_file(filepath):
    fernet = Fernet(master_key)
    unENC = open(filepath, 'rb').read()
    cypher = fernet.encrypt(unENC)
    
    open(filepath, 'wb').write(cypher)
    
    
def dcp_file():
    key = input("Please enter the master key here ::")
    fernet = Fernet(key)
    unDCP = open(filepath, 'rb').read()
    reverse_cypher = fernet.decrypt(unDCP)
    
    open(filepath, 'wb').write(reverse_cypher)
    
enc_file(filepath)
#dcp_file(filepath)


