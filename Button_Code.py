from tkinter import *
from tkinter import messagebox
import os, math, shutil

root = Tk()
root.title("File system project")
root.geometry("495x310")

# ----------------------------------<dirctory>----------------------------------
dirctory = r'C:\Users\Family\Desktop\TEST'


# ----------------------------------<Define functions>----------------------------------
def create_folder():
    selected_item = listbox.curselection()[0]
    # print (dirpath,listbox.get(selected_item))
    # print (a, name_folder,listbox.get(selected_item))
    print(loction_file, listbox.get(selected_item))

    # listbox.get(selected_item)
    # os.makedirs(loction_file + "\\" +selected_item )


def delete_folder():
    selected_item = listbox.curselection()[0]
    listbox.delete(selected_item)


    items = system_dict.items()
    for c, v in items:
        print(c, v)
    # From_dirctory = shutil.rmtree(dirctory + "\\" + listbox.get(selected_item_index))


def search_file():
    selected_file = listbox.curselection()[0]
    # print(dirctory + "\\" + listbox.get(selected_item_index))


def run_file():
    selected_file = listbox.curselection()[0]


def filter_file():
    selected_item = listbox.curselection()[0]


# ----------------------------------<list of folder and file>----------------------------------
list_folder = []
list_files = []
size_files = []
list_loction_file = []

listbox = Listbox(root, width=20)
for name_folder in list_folder:
    # listbox.insert(0, name_folder)
    pass

listbox_1 = Listbox(root, width=37)
for file in list_files:
    # listbox_1.insert(0, file)
    pass

for dirpath, dirnames, filenames in os.walk(dirctory):
    for folder in dirnames:
        #list_folder.append(folder)

        listbox.insert(1, folder)
        listbox.pack()

    for file in filenames:
        loction_file = os.path.join(dirpath, file)
        list_loction_file.append(dirpath)

        Size_file = os.path.getsize(loction_file)
        list_files.append(file)
        list_loction_file.append(file)


        # system_dict = {folder: loction_file}

        listbox_1.insert(0, file)

        listbox.pack()


try:
    listbox.grid(row=0, column=1, padx=60, sticky=W, pady=20)

    listbox_1.grid(row=0, column=1, padx=210, sticky=W)

    listbox.grid(row=0, column=1, padx=60, sticky=W, pady=20)

    listbox_1.grid(row=0, column=1, padx=210, sticky=W)

    Button_create_folder = Button(root, text="+", command=create_folder, width=6).grid(padx=60, row=3, column=1, sticky=W,pady=20)

    Button_delete = Button(root, text="-", command=delete_folder, width=6).grid(padx=120, row=3, column=1,sticky=W, pady=20)

    Button_Go = Button(root, text="Go", width=6).grid(padx=180, row=3, column=1, sticky=W, pady=20)

    Button_Search = Button(root, text="Search", width=6).grid(padx=240, row=3, column=1, sticky=W, pady=20)

    Button_Filter = Button(root, text="Filter", width=6).grid(padx=380, row=3, column=1, sticky=W, pady=2)

    Button.pack()

except:

    pass





# ----------------------------------<Create button>----------------------------------

# ----------------------------------<Create button>----------------------------------


# ----------------------------------<Create Label>----------------------------------

Label(root, text='Total size: ').grid(row=1, column=1, padx=60, sticky=W, pady=2)
Label(root, text=dirctory).grid(row=1, column=1, padx=210, sticky=W, pady=2)

# ----------------------------------<Create Entry>----------------------------------
entry_filter = Entry(root, width=7).grid(padx=323, row=3, column=1, sticky=W, pady=2)

root.mainloop()


