from tkinter import *
import smtplib
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog

root = Tk()
root.title('GmailSender')
root.resizable(False, False)
root.iconbitmap()
color = '#708090'
root.configure(bg=color)

obj = smtplib.SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()

def login():
    global emailinput
    global pwdinput
    emailin = emailinput.get()
    pwdin = pwdinput.get()

    try:
        if emailin.__contains__('@') and emailin.__contains__('.com'):
            obj.login(emailin, pwdin)
            messagebox.showinfo("Login","Login Successful!")
        else:
            messagebox.showerror("Login","Login Unsuccessful!\nCheck your Email")
    except smtplib.SMTPHeloError:
        messagebox.showerror("Error",'Login Unsuccessful!\nThe server didn’t reply properly to the HELO greeting')
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error",'Login Unsuccessful!\nUsername/Password is incorrect')
    except smtplib.SMTPNotSupportedError:
        messagebox.showerror("Error",'Login Unsuccessful!\nThe AUTH command is not supported by the server')
    except smtplib.SMTPException:
        messagebox.showerror("Error",'Login Unsuccessful!\nNo suitable authentication method was found')
    except smtplib.RuntimeError:
        messagebox.showerror("Error",'Login Unsuccessful!\nSSL/TLS support is not available to your Python interpreter.')
lframe = LabelFrame(root, text = 'Login',fg='white', font = ("Calibri", 12), padx=10, pady=10)
lframe.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
lframe.configure(bg=color)

Label(lframe, text='Email',bg=color,fg='white', font = ("Calibri", 12), padx=10, pady=10).grid(row=0, column=0, columnspan=1)
emailinput = Entry(lframe, font = ("Calibri", 12), width=40, borderwidth=2)
emailinput.grid(row=0, column=1, padx=30, columnspan=1)
Label(lframe, text='App Password',bg=color,fg='white', font = ("Calibri", 12), padx=10, pady=10).grid(row=1, column=0, columnspan=1)
pwdinput = Entry(lframe, show='*', font = ("Calibri", 12), width=40, borderwidth=2)
pwdinput.grid(row=1, column=1, padx=30, columnspan=1)
loginbtn = Button(lframe, text='Login', width=10, fg='white', bg='black', command=login).grid(row=2, column=0, columnspan=2)

bframe = LabelFrame(root, text = 'Body',fg='white', font = ("Calibri", 12), padx=10, pady=10)
bframe.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
bframe.configure(bg=color)

def send():
    global emailinput
    global toemailinput
    global en_message
    toemail = toemailinput.get()
    email = emailinput.get()
    message = en_message.get('1.0', END)
    subject = subjectinput.get()
    from_add = email
    to_add = toemail
    try:
        if len(str(to_add)) == 0 or len(str(subject)) == 0 or len(str(message))==0:
                messagebox.showinfo("Unsuccessful",'Provide valid details')
        else:
            msg= 'Subject: '+subject+'\n'+message
            obj.sendmail(from_add, to_add, msg)
            messagebox.showinfo("Email sent",'Email sent successfully!')
            subjectinput.delete(0, 'end')
            en_message.delete('1.0', 'end')
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror("Error",'Login Unsuccessful!\nRecipients refused')
    except smtplib.SMTPSenderRefused:
        messagebox.showerror("Error",'Login Unsuccessful!\nThe server didn’t accept the "From Address".')
    except smtplib.SMTPDataError:
        messagebox.showerror("Error",'Login Unsuccessful!\nThe server replied with an unexpected error code')
    except smtplib.SMTPHeloError:
        messagebox.showerror("Error",'Login Unsuccessful!\nThe server didn’t reply properly to the HELO greeting')

Label(bframe, text='To', font = ("Calibri", 12),fg='white', bg=color, padx=10, pady=10).grid(row=0, column=0, columnspan=1)
toemailinput = Entry(bframe, font = ("Calibri", 12), width=40, borderwidth=2)
toemailinput.grid(row=0, column=1, padx=30, columnspan=1)
Label(bframe, text='Subject',bg=color,fg='white', font = ("Calibri", 12), padx=10, pady=10).grid(row=1, column=0, columnspan=1)
subjectinput = Entry(bframe, font = ("Calibri", 12), width=40, borderwidth=2)
subjectinput.grid(row=1, column=1, padx=30, columnspan=1)
Label(bframe, text='Message',bg=color, fg='white', font = ("Calibri", 12)).grid(row=2, column=0, columnspan=2)
en_message = scrolledtext.ScrolledText(bframe, borderwidth=2, wrap=WORD, height=15, width=60, font = ("Calibri", 12))
en_message.grid(row=3, column=0, columnspan=2, pady=10)
def quit():
    obj.quit()
    root.quit()
attachbtn = Button(bframe, text='Exit', bg='black', fg='white', width = 10, command=quit)
attachbtn.grid(row=4, column=0, padx=10, sticky=E+W)
sendbtn = Button(bframe, text='Send', bg='black', fg='white', width = 10, command=send)
sendbtn.grid(row=4, column=1, padx=10, sticky=E+W)

Label(root, text= "Project by Subareesh", bg=color,fg='yellow').grid(row=5, column=0, columnspan=2)

root.mainloop()
