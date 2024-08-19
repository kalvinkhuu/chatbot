from tkinter import *
from tkinter import filedialog
import os
import glob

def browseFolder():
    foldername = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    label_folder_explorer.configure(text="Folder Selected: " + foldername)
    entry_folder_path.delete(0, END)
    entry_folder_path.insert(0, foldername)

def merge_files(folder_path, output_file_name):
    # Get a list of all files in the folder
    files = glob.glob(os.path.join(folder_path, '*'))
    
    # Sort the files based on their creation time
    files.sort(key=os.path.getctime)
    
    # Open the output file in write mode
    with open(output_file_name, 'w') as outfile:
        # Loop over the sorted list of files
        for file in files:
            # Open each file in read mode
            with open(file, 'r') as infile:
                outfile.write('\n\n--- ' + file + ' ---\n\n')
                # Read the content of the file and write it to the output file
                outfile.write(infile.read())

def merge_files_gui():
    folder_path = entry_folder_path.get()
    output_file_name = entry_output_file_name.get()
    merge_files(folder_path, output_file_name)
    label_status.configure(text="Files merged successfully!")

if __name__ == '__main__':
    window = Tk()
    window.title("Merge Files")

    # Set window size
    window.geometry("500x300")
    
    # Set window background color
    window.config(background="white")

    # Configure grid to expand with window size
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.rowconfigure(4, weight=1)
    window.rowconfigure(5, weight=1)
    window.rowconfigure(6, weight=1)
    window.rowconfigure(7, weight=1)

    # Folder selection
    label_folder_explorer = Label(window, text="Select Folder", width=50, height=2, fg="blue")
    label_folder_explorer.grid(column=1, row=1, sticky="nsew")

    button_explore = Button(window, text="Browse Folder", command=browseFolder)
    button_explore.grid(column=1, row=2, sticky="nsew")

    entry_folder_path = Entry(window, width=50)
    entry_folder_path.grid(column=1, row=3, sticky="nsew")

    # Output file name
    label_output_file = Label(window, text="Output File Name", width=50, height=2, fg="blue")
    label_output_file.grid(column=1, row=4, sticky="nsew")

    entry_output_file_name = Entry(window, width=50)
    entry_output_file_name.grid(column=1, row=5, sticky="nsew")

    # Merge files button
    button_merge = Button(window, text="Merge Files", command=merge_files_gui)
    button_merge.grid(column=1, row=6, sticky="nsew")

    # Status label
    label_status = Label(window, text="", width=50, height=2, fg="green")
    label_status.grid(column=1, row=7, sticky="nsew")

    window.mainloop()