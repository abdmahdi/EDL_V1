import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




username='abderahmanemahdigharzouli19@gmail.com'
password='gvsfgvjvemrtvrxe'

def send_mail(text='Email_body',specialite='',matricule='',passw='',subject='Hello ',from_email='abdoumahdi19@icloud.com',to_emails=[]):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=", ".join(to_emails)
    msg['Subject']=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part = MIMEText(f"<p>Vous etes Accepter a specialite {specialite} annee 2022 votre matricule est {matricule},email est {to_emails[0]} , password is ''{passw}''  </p>", 'html')
    msg.attach(html_part)
    msg_str=msg.as_string()


    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()        
        