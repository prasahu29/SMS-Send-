import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def send_sms (num,msg):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization':'uqZKg0PcJmvn42pRhko37wt9QVHeTbjyIXfD8EYsLrNzOiSBdMlL65Yu0dW3vez798FkGgwnHT2UjOI1',
        'sender_id':'TXTIND',
        'message':msg,
        'language':'english',
        'route':'v3',
        'numbers':num
    }
    response = requests.get(url,params=params)
    dic = response.json()
    #print(dic)
    return dic.get('return')

# send_sms('9926415203','Hello BOT')   


# message send functin

def btnClik():
    num = textNumber.get()
    msg = textMessage.get('1.0',END)


    r = send_sms(num,msg)

    if(r):
        showinfo('send success','successfully sent')
    else:
        showerror('error','Something went wrong')
# Creating GUI 


root = Tk()
root.title("Message Sender")
root.geometry('400x500')
font = ("Helvetica", 22, "bold")
textNumber= Entry(root,font=font)
textNumber.pack(fill=X,pady=10)
textMessage = Text(root)
textMessage.pack(fill=X)
sendBtn = Button(root,text='send Message',command=btnClik)
sendBtn.pack(pady=10)


root.mainloop()
