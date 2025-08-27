import tkinter as tk

def clear():
    entry.delete(0,tk.END)
    entry.insert(0,"0")

def click(value):
    current = entry.get()
    if current =='0':
        current = ""
    entry.delete(0,tk.END)
    entry.insert(0,current+str(value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))

    except:

        entry.delete(0,tk.END)
        entry.insert(0,"Error")

#====================Main Code=========================#
root=tk.Tk()
root.title("Simple Calculator")
root.geometry("370x400")
root.resizable(False,False)


entry=tk.Entry(root,font=("Arial",20),bd=8,relief='ridge',justify='right')
entry.place(x=10,y=0,width=350,height=60)
entry.insert(0,"0")

b1=tk.Button(root,text='C',command = clear,width=4,height=1,font=("Arial",20,"bold"),bg="royalblue",fg="white")
b1.place(x=10,y=70)
b2=tk.Button(root,text="/",command = lambda:click('/'),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b2.place(x=100,y=70)
b3=tk.Button(root,text="%",command = lambda:click('%'),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b3.place(x=190,y=70)
b4=tk.Button(root,text="*",command = lambda:click('*'),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b4.place(x=280,y=70)


b5=tk.Button(root,text=7,command = lambda:click(7),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b5.place(x=10,y=135)
b6=tk.Button(root,text=8,command =lambda:click(8),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b6.place(x=100,y=135)
b7=tk.Button(root,text=9,command = lambda:click(9),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b7.place(x=190,y=135)
b8=tk.Button(root,text='-',command = lambda:click('-'),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b8.place(x=280,y=135)


b9=tk.Button(root,text=4,command = lambda:click(4),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b9.place(x=10,y=200)
b10=tk.Button(root,text=5,command = lambda:click(5),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b10.place(x=100,y=200)
b11=tk.Button(root,text=6,command = lambda:click(6),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b11.place(x=190,y=200)
b12=tk.Button(root,text='+',command = lambda:click("+"),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b12.place(x=280,y=200)


b13=tk.Button(root,text=1,command = lambda:click(1),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b13.place(x=10,y=265)
b14=tk.Button(root,text=2,command = lambda:click(2),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b14.place(x=100,y=265)
b15=tk.Button(root,text=3,command = lambda:click(3),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b15.place(x=190,y=265)
b16=tk.Button(root,text='=',command = calculate,width=4,height=3,font=("Arial",20,"bold"),bg="orange",fg="white")
b16.place(x=280,y=265)

b17=tk.Button(root,text=0,command = lambda:click('0'),width=9,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b17.place(x=10,y=330)
b18=tk.Button(root,text='.',command = lambda:click('.'),width=4,height=1,font=("Arial",20,"bold"),bg="black",fg="white")
b18.place(x=190,y=330)

root.mainloop()
