import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

ws = Tk()
ws.title('Black and White Filter')
ws.geometry('700x500')
ws.config(bg='#4a7a8c')
frame = Frame(ws)
frame.pack()

file_label = Label(frame, text='Selected File')
file_label.pack(side=LEFT)
file_label.config(bg='#E9967A')
message_label = Label(frame, text='')
message_label.pack(side=BOTTOM)

image = ''

def select_file():
    global image
    
    filetypes = (('All files', '*.*'),
        ('text files', '*.txt'))

    filename = fd.askopenfilename(title='Select File', initialdir='/home', filetypes=filetypes)
    
    image = Image.open(filename)
    file_label.config(text= filename)
    file_label.config(bg='#8FBC8F')
    try:
        w = 400
        h = 400
        resize_img = image.resize((w, h))
        img = ImageTk.PhotoImage(resize_img)
        disp_img.config(image=img)
        disp_img.image = img
        img = ImageTk.PhotoImage(resize_img)
        disp_img.config(image=img)
        disp_img.image = img
        message_label.config(text= 'Ready to Filter')
        message_label.config(bg = '#FFFFFF')

    except:
        message_label.config(text= 'File Not Recognized')
        message_label.config(bg = '#E9967A')

def black_and_white(pixel):
    new_color = (pixel[0] + pixel[1] + pixel[2]) // 3
    return new_color
    
def filter_func():
    global image
    try:
        image = image.convert(mode="1", dither=Image.NONE)
        w = 400
        h = 400
        resize_img = image.resize((w, h))
        img = ImageTk.PhotoImage(resize_img)
        disp_img.config(image=img)
        disp_img.image = img
        img = ImageTk.PhotoImage(resize_img)
        disp_img.config(image=img)
        disp_img.image = img
        message_label.config(text= 'Filter Applied')
        message_label.config(bg = '#FFFFFF')

    except:
        message_label.config(text= 'File Not Recognized')
        message_label.config(bg = '#E9967A')
        
def save():
    global image
    #ext = image.split(".")[-1]
    file=asksaveasfilename(filetypes=[("PNG file","*.png"),("jpg file","*.jpg")])
    image.save(file)
            
open_btn = Button(
    frame,
    text='Select File',
    command=select_file
)
open_btn.pack(side=LEFT)

filter_btn = Button(
    frame,
    text='Filter',
    command=filter_func
)
filter_btn.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)

save_button = Button(frame, text="Save", width=8, bg='blue', fg='white', font=('ariel 9 bold'), relief=GROOVE, command=save)
save_button.pack(side=LEFT)
exit_button = Button(frame, text="Exit", width=8, bg='blue', fg='white', font=('ariel 9 bold'), relief=GROOVE, command=ws.destroy)
exit_button.pack(side=LEFT)
ws.mainloop()