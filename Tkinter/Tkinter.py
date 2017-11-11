import tkinter as tk

window =tk.Tk()

window.title('test')
window.geometry()
var =tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()

on_hit=False

def click_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('haha')
    else:
        on_hit=False
        var.set('')
b =tk.Button(window,text='click me',width=12,height=2,command=click_me)
b.pack()
window.mainloop()