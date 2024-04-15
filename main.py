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
   
   # main function  

if __name__ == "__main__":  
   # creating an object of the Tk() class  
   win_root = Tk()  
   # setting the title of the main window  
   win_root.title("SFP-File Explorer")  
   # set the size and position of the window  
   win_root.geometry("800x500+650+250")  
   # disabling the resizable option  
   win_root.resizable(0, 0)  
   # setting the background color to #D8E9E6  
   win_root.configure(bg = "#D8E9E6")  
  
   # creating the frames using the Frame() widget  
   header_frame = Frame(win_root, bg = "#88AB8E")  
   buttons_frame = Frame(win_root, bg = "#88AB8E")  
  
   # using the pack() method to place the frames in the window  
   header_frame.pack(fill = "both")  
   buttons_frame.pack(expand = TRUE, fill = "both")  
  
   # creating a label using the Label() widget  
   header_label = Label(  
      header_frame,  
      text = "File Explorer",  
      font = ("Arial", "20"),  
      bg = "#AFC8AD",  
      fg = "#1A3C37"  
      )  
  
   # using the pack() method to place the label in the window  
   header_label.pack(expand = TRUE, fill = "both", pady = 12)  


  
   # delete folder button  
   delete_folder_button = Button(  
      buttons_frame,  
      text = "Delete a Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = Folder_delete  
      )  
  
   # move folder button  
   move_folder_button = Button(  
      buttons_frame,  
      text = "Move Folder ",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = folder_move  
      )  
  
   # list all files button  
   list_button = Button(  
      buttons_frame,  
      text = "File Folder",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = Files_in_folder  
      )  


   # copy button  
   copy_button = Button(  
      buttons_frame,  
      text = "Copy File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = copyFile  
      )  
  
   # delete button  
   delete_button = Button(  
      buttons_frame,  
      text = "Delete File",  
      font = ("verdana", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = deleteFile  
      )  
  
   # rename button  
   rename_button = Button(  
      buttons_frame,  
      text = "RenameFile",  
      font = ("Arial", "10"),  
      width = 18,  
      bg = "#EEE7DA",  
      fg = "#000000",  
      relief = GROOVE,  
      activebackground = "#286F63",  
      activeforeground = "#D0FEF7",  
      command = renameFile  
      )  
  

   # using the pack() method to place the buttons in the window  
   
   
 
   copy_button.pack(pady = 8)  
   delete_button.pack(pady = 8)  
   rename_button.pack(pady = 8)  
   move_folder_button.pack(pady = 8)  
   delete_folder_button.pack(pady = 8)  
   list_button.pack(pady = 8)  
    
  
   # creating an object of the StringVar() class  
   enteredFileName = StringVar()  
   
win_root.mainloop() 

  

