from tkinter import *

root = Tk()
root.title("Notepad")
root.geometry("500x200")

member = Menu(root)

fileMenu = Menu(member,tearoff=0)
fileMenu.add_command(label="New",command="Donothing")
fileMenu.add_command(label="Open",command="Donothing")
fileMenu.add_command(label="Save",command="Donothing")
fileMenu.add_command(label="Save As",command="Donothing")
fileMenu.add_command(label="close",command="Donothing")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command="root.quit")
member.add_cascade(label="File",menu=fileMenu)
root.config(menu=member)

# def test(event):
#     Label.config(text="You Enter: " + event.keysym)
#     Label.pack()
#     #print("Safu Master")
# #root.bind('<Return>',test)
# #root.unbind('<Return>',test)
# #root.bind_all('<Return>',test)

# root.bind("<Key>",test)
# label=Label(root)
# label.pack()

def testMouse(event):
    label.config(test="Mouse" + str(event.x) + "" + str(event.y))
    label.pack()
    
root.bind("<Button>", testMouse)
label=Label(root)
label.pack()

Show = Button(root, text="Close", command=root.quit)
Show.pack()




root.mainloop()

