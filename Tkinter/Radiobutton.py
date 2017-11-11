import tkinter as tk

window=tk.Tk()
window.title('test')
window.geometry()
var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()
def print_selection():
    l.config(text='you have selected:'+var.get())
r1=tk.Radiobutton(window,text='optina a',variable=var,value='a',command=print_selection)
r1.pack()
r2=tk.Radiobutton(window,text='optina b',variable=var,value='b',command=print_selection)
r2.pack()
r2=tk.Radiobutton(window,text='optina c',variable=var,value='c',command=print_selection)
r2.pack()

window.mainloop()
