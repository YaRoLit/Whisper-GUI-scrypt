from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import subprocess


def about():
    '''
    about me)
    '''
    mb.showinfo("About scrypt", "Made by Yaro Litavrin")

def clear():
    '''
    The function of clearing the file entry forms and the result record path.
    '''
    global files
    global out_path
    files = ''
    out_path = ''
    filename.delete(0, END)
    pathname.delete(0, END)

def insert_files():
    '''
    Function for selecting files to decrypt.
    '''
    global files
    global out_path
    clear()
    files = fd.askopenfilenames()
    path, file = os.path.split(files[0])
    out_path = path + '/results'
    filename.insert(0, files)
    pathname.insert(0, out_path)

def insert_path():
    '''
    Function for selecting the path for recording results.
    '''
    global out_path
    pathname.delete(0, END)
    out_path = fd.askdirectory()
    pathname.insert(0, out_path)

def start():
    '''
    Launch the Whisper audio transcription module with the selected parameters.
    '''
    if not files:
        mb.showerror("Error", "Select files to decrypt")
        return
    
    if not out_path:
        mb.showerror("Error", "Select the path for recording results")
        return
    
    for file in files:
        subprocess.call(['whisper', '--language=en', 
                         f'--output_format={out_type.get()}', 
                         f'--model={model_size.get()}', 
                         f'--output_dir={out_path}',
                         f'--verbose={verbose.get()}',
                         file])
    clear()


files = ''
out_path = ''

# Initialization of the main dialog window and its main parameters
root = Tk()
root.geometry('500x350')
root.title("Audiotranscriber")

# Изображение в левом верхнем углу
img_file = PhotoImage(file = 'image.png') 
Button(root, image=img_file, command=about).grid(row=0, column=0, columnspan=2, rowspan=8)

# Селектор выбора используемой модели
Label(text="Model size:").grid(row=0, column=2, 
                                sticky=N, padx=10)
model_size = StringVar()
model_size.set('small')
base = Radiobutton(text="Base",
                        variable=model_size, value='base')
small = Radiobutton(text="Small",
                        variable=model_size, value='small')
medium = Radiobutton(text="Medium",
                        variable=model_size, value='medium')
large = Radiobutton(text="Large",
                        variable=model_size, value='large')
base.grid(row=1, column=2,
                sticky=W, padx=10)
small.grid(row=2, column=2,
                sticky=W, padx=10)
medium.grid(row=3, column=2,
                sticky=W, padx=10)
large.grid(row=4, column=2,
                sticky=W,padx=10)

# Селектор выбора типа вывода
Label(text="Output format:").grid(row=0, column=3,
                            sticky=N, padx=10)
out_type = StringVar()
out_type.set('all')
txt = Radiobutton(text="Just phrases",
                  variable=out_type, value='txt')
time = Radiobutton(text="Time stamps",
                  variable=out_type, value='vtt')
table = Radiobutton(text="Table",
                  variable=out_type, value='tsv')
all = Radiobutton(text="All formats",
                  variable=out_type, value='all')
txt.grid(row=1, column=3,
                sticky=W, padx=10)
time.grid(row=2, column=3,
                sticky=W, padx=10)
table.grid(row=3, column=3,
                sticky=W, padx=10)
all.grid(row=4, column=3,
                sticky=W, padx=10)

# Selecting files to decrypt (label and button)
Label(text="").grid(row=8, column=0,
                sticky=W, padx=10, columnspan=4)
Label(text="Select files to decrypt:").grid(row=9, column=0,
                        sticky=W, padx=10, columnspan=4)
filename = Entry(width=35)
filename.grid(row=10, column=0,
            sticky=W, padx=10, columnspan=4)
Button(text="Select files", width=15, command=insert_files)\
        .grid(row=10, column=3, sticky=S, padx=10)

# Selecting the output path
Label(text="Select the output path:").grid(row=12, column=0,
                        sticky=W, padx=10, columnspan=4)
pathname = Entry(width=35)
pathname.grid(row=13, column=0,
            sticky=W, padx=10, columnspan=4)
Button(text="Choose a path", width=15, command=insert_path)\
        .grid(row=13, column=3, sticky=S, padx=10)

# Checkbox for decryption process display type
Label(text="").grid(row=14, column=0,
                sticky=W, padx=10, columnspan=4)
verbose = StringVar()
verbose.set('False')
verbose_check = Checkbutton(root, text="Displaying text in the terminal",
                 variable=verbose,
                 onvalue='True', offvalue='False')
verbose_check.grid(row=15, column=0,
                sticky=W, padx=10, columnspan=4)

# Main red button
start_button = Button(text="Start", width=15, command=start)
start_button['bg'] = '#fa4400'
start_button.grid(row=15, column=3, sticky=S, padx=10)

root.mainloop()
