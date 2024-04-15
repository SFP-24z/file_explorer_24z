from tkinter import *                    
from tkinter import messagebox as mb     
from tkinter import filedialog as fd      
import os                                
import shutil                            



def copyFile():  
     
   fileToCopy = fd.askopenfilename(  
      title = "Which file do you want to copy?",  
      filetypes=[("All files", "*.*")]  
      )  
    
   directoryToPaste = fd.askdirectory(title = "Select the folder to paste the file")  
  
     
   try:  
        
      shutil.copy(fileToCopy, directoryToPaste)  
        
      mb.showinfo(  
         title = "File copied!",  
         message = "The selected file has been copied to the selected location."  
         )  
   except:  
       
      mb.showerror(  
         title = "Error!",  
         message = "Selected file is unable to copy to the selected location. Please try again!"  
         )  
  
  
def deleteFile():  
    
   the_file = fd.askopenfilename(  
      title = "Which file do you want to delete?",  
      filetypes = [("All files", "*.*")]  
      )  
    
   os.remove(os.path.abspath(the_file))  
    
   mb.showinfo(title = "File deleted!", message = "The selected file has been deleted.")  
  
 
def renameFile():  
     
   rename_window = Toplevel(win_root)  
    
   rename_window.title("Rename File")  
    
   rename_window.geometry("300x100+300+250")  
    
   rename_window.resizable(0, 0)
     
   rename_window.configure(bg = "#88AB8E")  
     
     
   rename_label = Label(  
      rename_window,  
      text = "Rename your new file:",  
      font = ("Arial", "10"),  
      bg = "#88AB8E",  
      fg = "#000000"  
      )  
     
   rename_label.pack(pady = 4)  
     
    
   rename_field = Entry(  
      rename_window,  
      width = 26,  
      textvariable = enteredFileName,  
      relief = GROOVE,  
      font = ("verdana", "10"),  
      bg = "#FFFFFF",  
      fg = "#000000"  
      
      )  
    
   
   rename_field.pack(pady = 4, padx = 4)  

  
  
   submitButton = Button(
    rename_window,
    text = 'submit',
    command=submitName,
    width = 12,
    relief=GROOVE,
    font= ("verdana," "8"),
    bg= '#F2F1EB',
    fg = '#000000',
    activebackground='#709218'
)

   submitButton.pack(pady = 2)

   
  
 
def getFilePath():  
   
   the_file = fd.askopenfilename(title = "Select the file to rename", filetypes = [("All files", "*.*")])  
   
   return the_file  
  

def submitName():  
     
   renameName = enteredFileName.get()  
   
   enteredFileName.set("")  
     
   fileName = getFilePath()  
    
   newFileName = os.path.join(os.path.dirname(fileName), renameName + os.path.splitext(fileName)[1])  
    
   os.rename(fileName, newFileName)  
     
   mb.showinfo(title = "File Renamed!", message = "The selected file has been renamed.")  

