import tkinter
from tkinter import filedialog, messagebox
window = tkinter.Tk()
# creat main window size and name of app 
window.geometry("800x500")
window.title("NotPade")

current_file = None


# function
def new_file():
    global current_file
    text_area.delete(1.0,tkinter.END)
    window.title("NotePade")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )    
    if not file_path:
        return 
    try:
        with open (file_path, 'r', encoding="utf-8") as f:
            text_area.delete(1.0,tkinter.END)
            text_area.insert(tkinter.END,f.read())
        current_file= file_path
        window.title(f"NotePade - {file_path}")
    except Exception as e:
        messagebox.showerror("Error",str(e))

def save_file():
    global current_file
    if current_file is None :
        save_as_file()
    else :
        try:
            with open(current_file, "w",encoding="utf-8") as f:
                f.write(text_area.get(1.0,tkinter.END))
        except Exception as e:
            messagebox.showerror("Error",str(e))

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return 
    try:
        with open (file_path,"w", encoding="utf-8") as f:
            f.write(text_area.get(1.0,tkinter.END))
        current_file = file_path ;
        window.title(f"NotePade - {file_path}")
    except Exception as e:
        messagebox.showerror("Error",str(e))

def exit_app():
    window.quit()

# text area + scrollbar
text_frame = tkinter.Frame(window)
text_frame.pack(fill=tkinter.BOTH,expand= True)

scrollbar = tkinter.Scrollbar(text_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text_area = tkinter.Text(
    text_frame,
    wrap="word",
    yscrollcommand=scrollbar.set,
    font=("Consolas",12)
)
text_area.pack(fill=tkinter.BOTH, expand=True)
scrollbar.config(command=text_area.yview)


# Menu Bar
menu_bar = tkinter.Menu(window)
file_menu = tkinter.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command= save_as_file)
file_menu.add_separator()
file_menu.add_command(label= "Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = tkinter.Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))

menu_bar.add_cascade(label="Edit",menu=edit_menu)

help_menu = tkinter.Menu(menu_bar,tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
    "About","Simple NotPad by ibra4im with Tkinter"
))
menu_bar.add_cascade(label="help",menu=help_menu)
window.config(menu=menu_bar)

# keybord shortcuts
window.bind("<Control-n>", lambda event: new_file())
window.bind("<Control-o>", lambda event: open_file())
window.bind("<Control-s>", lambda event: save_file())
# run app
window.mainloop()