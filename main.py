from tkinter import *                   # importing all the widgets and modules from tkinter  
from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
from tkinter import filedialog as fd    # importing the filedialog module from tkinter  
import os                               # importing the os module  
import shutil                           # importing the shutil module  



def Folder_delete():  

   to_be_deleted_folder = fd.askdirectory(title = 'Select a folder you want to delete')  
    
   shutil.rmtree(to_be_deleted_folder)
    
   mb.showinfo("Folder Deleted!", "The Folder you selected has been deleted!")  
  
def folder_move():  
   
   folderToMove = fd.askdirectory(title = 'Select the folder you want to move')  
    
   mb.showinfo(message = 'Folder selected. Where do you want to move it to?.')  
  
   des = fd.askdirectory(title = 'Destination')  
 
   try:  
   
      shutil.move(folderToMove, des)  
       
      mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')  
   except:  
     
      mb.showerror('Error!', 'The Folder selected can not be moved.Make sure the destination path does exist')  
  
def Files_in_folder():  
   i = 0  

   selected_folder = fd.askdirectory(title = "Select the Folder you want see files")  
  
   files_folder = os.listdir(os.path.abspath(selected_folder))  
  
   listFilesWindow = Toplevel(win_root)  
   # specifying the title of the pop-up window  
   listFilesWindow.title(f'List of Files in {selected_folder}')  
   # specifying the size and position of the window  
   listFilesWindow.geometry("500x500+300+200")  
   # disabling the resizable option  
   listFilesWindow.resizable(0, 0)  
   # setting the background color of the window to #EC2FB1  
   listFilesWindow.configure(bg = "#EC2FB1")  
   
   
 
   the_listbox = Listbox(  
      listFilesWindow,  
      selectbackground = "#F24FBF",  
      font = ("Verdana", "10"),  
      background = "#88AB8E"  
      )  
   # list box on the window  
   the_listbox.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)  
     
   #scrollbar
   the_scrollbar = Scrollbar(  
      the_listbox,  
      orient = VERTICAL,  
      command = the_listbox.yview  
      )  
   # scroll bar to the right side of the window  
   the_scrollbar.pack(side = RIGHT, fill = Y)  
  
   the_listbox.config(yscrollcommand = the_scrollbar.set)  
  
   # iterating through the files in the folder  
   while i < len(files_folder):  
        
      the_listbox.insert(END, "[" + str(i+1) + "] " + files_folder[i])  
      i += 1  
   the_listbox.insert(END, "")  
   the_listbox.insert(END, "Total Files: " + str(len(files_folder)))  
  

