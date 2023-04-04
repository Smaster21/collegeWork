from tkinter import *

def write():
    
    data = entry.get()
    with open('C:/SAFU MASTER/College/sem4/py2.txt', 'w') as ls:
        ls.write(data)
        print(data)
        


root = Tk()
root.title("Practical9")
root.geometry("500x250")

label = Label(root, text="Enter Something:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Submit", command=write)
button.pack()

root.mainloop()
