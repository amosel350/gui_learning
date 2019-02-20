import tkinter
root = tkinter.Tk()

def hello():
    print("hey")

button1 = tkinter.Button(root)
button1.config(text="Say hello!", command=hello)
button1.grid()

label1 = tkinter.Label(root)
label1.config(text="HEY")
label1.grid()

root.mainloop()

