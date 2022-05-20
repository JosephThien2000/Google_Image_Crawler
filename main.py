# Import necessary modules
from tkinter import *
from time import sleep
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
from download_image import *
from google_crawler import *
from pathlib import *
from tkinter.scrolledtext import ScrolledText
from crawler import *
import re

print(os.getcwd())
parent_path = os.path.dirname(os.path.abspath(__file__))
download_folder = os.path.join(parent_path, "download/")
output_folder = os.path.join(parent_path, "output/")
img_list_confirm = []
condition = True

# Class Main
class Main(Frame):

    # Constructor
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initUI()

    # initialize UI
    def initUI(self):

        global path_img
            
        # main frame
        self.pack(fill=BOTH, expand=True)
        self.frm_main = ttk.Frame(self, borderwidth=1)
        self.frm_main.pack(fill=BOTH, expand=True)

        # Frame folder picker
        self.frm_folder_picker = ttk.Frame(self.frm_main, borderwidth=1)
        self.frm_folder_picker.columnconfigure([0,1,2], weight=1)
        self.frm_folder_picker.rowconfigure([0,1], weight=1)
        self.frm_folder_picker.grid(row=0, columnspan=3, rowspan=2, sticky="nsew")

        # Label and entry in frame folder picker
        self.lbl_folder_picker = ttk.Label(self.frm_folder_picker, text="Please choose the save-img folder")
        self.lbl_folder_picker.grid(row=0, columnspan=3, sticky="wnse")
        self.btn_folder_picker = ttk.Button(self.frm_folder_picker, text="Choose", command=self.folder_picker_button)
        self.btn_folder_picker.grid(row=1, column=0, sticky="wns", pady=10)

        # Frame save-img folder shower
        self.frm_folder_shower = ttk.Frame(self.frm_main, borderwidth=1)
        self.frm_folder_shower.columnconfigure([0,1,2], weight=1)
        self.frm_folder_shower.rowconfigure([0,1], weight=1)
        self.frm_folder_shower.grid(row=2, columnspan=3, rowspan=2, sticky="nsew")

        # Label and entry in frame save-img folder shower
        self.lbl_folder_shower = ttk.Label(self.frm_folder_shower, text="Your save-img folder is:", width=100)
        self.lbl_folder_shower.grid(row=0, columnspan=3, sticky="wnse")
        self.ent_folder_shower = ttk.Entry(self.frm_folder_shower)
        self.ent_folder_shower.grid(row=1, columnspan=3, sticky="wens", pady=10)

# Frame inputs
        self.inputs = ttk.Frame(self.frm_main, borderwidth=1)
        self.inputs.columnconfigure([0,1,2], weight=1)
        self.inputs.rowconfigure([0,1,2], weight=1)
        self.inputs.grid(row=4, columnspan=5, rowspan=2, sticky="nsew")

        # Keyword
        self.lbl_keyword = ttk.Label(self.inputs, text="Keyword")
        self.lbl_keyword.grid(row=0, column=0, sticky="wnse")
        self.ent_keyword = ttk.Entry(self.inputs)
        self.ent_keyword.grid(row=1, column=0, sticky="wens", pady=10)

        # Url
        self.lbl_url = ttk.Label(self.inputs, text="Url")
        self.lbl_url.grid(row=0, column=1, columnspan=2, sticky="wnse")
        self.ent_url = ttk.Entry(self.inputs)
        self.ent_url.grid(row=1, column=1, columnspan=2, sticky="wens", pady=10)

        # Number of images
        self.lbl_num_page = ttk.Label(self.inputs, text="Number of images")
        self.lbl_num_page.grid(row=0, column=3, sticky="wnse")
        self.num_page = ttk.Spinbox(self.inputs, from_=1, to=100)
        self.num_page.grid(row=1, column=3, sticky="wens", pady=10)

        # Buttons
        self.btn_search = ttk.Button(self.inputs, text="Search", command=self.search_button)
        self.btn_search.grid(row=2, column=0, sticky="ns", pady=10)

        self.btn_save_resize = ttk.Button(self.inputs, text="Save and Resize", command=self.save_Resize_Button)
        self.btn_save_resize.grid(row=2, column=1, sticky="ns", pady=10)

        self.btn_save_origin = ttk.Button(self.inputs, text="Save originally", command=self.save_Original_Button)
        self.btn_save_origin.grid(row=2, column=2, sticky="ns", pady=10)

        self.btn_show_image = ttk.Button(self.inputs, text="Show Image", command=self.open_window)
        self.btn_show_image.grid(row=2, column=3, sticky="ns", pady=10)

    # Search button method
    def search_button(self):
        if self.ent_keyword.get() != "":
            # check if directory exists
            if os.path.exists(download_folder):
                print("Folder exists!") 
                for img in os.listdir(download_folder):
                    os.remove(download_folder + img)
                os.rmdir(download_folder)
                keyword = self.ent_keyword.get()
                google_crawler(keyword, self.num_page.get())
            else:
                keyword = self.ent_keyword.get()
                google_crawler(keyword, self.num_page.get())
        if self.ent_url.get() != "":
            # check if directory exists
            if os.path.exists(output_folder):
                print("Folder exists!") 
                for img in os.listdir(output_folder):
                    os.remove(output_folder + img)
                os.rmdir(output_folder)
                self.url = self.ent_url.get()
                crawl(self.url)
            else:
                self.url = self.ent_url.get()
                crawl(self.url)

    # Folder picker button method
    def folder_picker_button(self):
        save_dir = askdirectory(
            # initialdir=self.ent_folder_shower.get(),
            title="Please choose the save-img folder"
        )
        self.ent_folder_shower.delete(0, END)
        self.ent_folder_shower.insert(0, save_dir)
        
        with open(f"{parent_path}/save_dir.txt", "w") as f:
            f.write(save_dir)

    # Button click method
    def btn_click(self):
        print("Button clicked")
    
    # Show images method
    def show_image(self):
        global var_list, row
        row = column = 0
        self.photo_list = []
        self.cb_list = []
        self.name_image_list = []
        self.var_list = []
        self.window.update()
        
        if self.ent_keyword.get() != "":
            # Read images in download_folder
            for img in os.listdir(download_folder):
                self.path_img = os.path.join(download_folder, img)
                self.photo = Image.open(self.path_img)
                self.photo = self.photo.resize((224, 224))
                self.photo = ImageTk.PhotoImage(self.photo)
                self.photo_list.append(self.photo)
                self.name_image_list.append(img)

        if self.ent_url.get() != "":
            # Read images in output
            for img in os.listdir(output_folder):
                self.path_img = os.path.join(output_folder, img)
                self.photo = Image.open(self.path_img)
                self.photo = self.photo.resize((224, 224))
                self.photo = ImageTk.PhotoImage(self.photo)
                self.photo_list.append(self.photo)
                self.name_image_list.append(img)
        # Create scrollbar
        self.scrollbar = ScrolledText(self.window, borderwidth=5, wrap="none")
        self.scrollbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
        # Insert images into listbox
        for i, self.photo in enumerate(self.photo_list):
            self.var = IntVar()
            self.var_list.append(self.var)
            self.cb = Checkbutton(
                self.scrollbar
                , image=self.photo
                , text=f"{self.name_image_list[i]}"
                , compound='top'
                , onvalue=1
                , offvalue=0
                , highlightcolor="Blue"
                , activebackground="red"
                , variable=self.var_list[i])

            self.cb.grid(row=row, column=column)
            self.scrollbar.window_create(END, window=self.cb)
            self.scrollbar.insert("end", " ")
            self.cb_list.append(self.cb)
        
            # Check if row is full (3 images per row)
            column += 1
            if column == 3:
                self.scrollbar.insert("end", "\n")
                self.scrollbar['width'] = 100
                column = 0
                row += 1
    
    def selection_clear(self, **kw):
        return super().selection_clear(**kw)
    
    # Select and deselect button method
    def select_all_Button(self):
        for i, self.var in enumerate(self.var_list):
            self.var.set(1)
            self.cb_list[i].select()
            self.cb_list[i].config(bg="red")
            print("Select all!")

    def deselect_all_Button(self):
        for i, self.var in enumerate(self.var_list):
            self.var.set(0)
            self.cb_list[i].deselect() 
            self.cb_list[i].config(bg="white")
            print("Unselect all!")

    def select_deselect_button(self):
        if self.btn_select_all.config("text")[-1] == "Select":
            self.btn_select_all.config(text="Deselect")
            self.deselect_all_Button()
        else:
            self.btn_select_all.config(text="Select")
            self.select_all_Button()

    # Confirm Button method
    def confirm_Button(self):
        """
            Confirm the checked images
        """
        # global cb_list
        self.scrollbar.update()
        if self.ent_keyword .get() != "":
            self.label_name = self.lbl_entry.get()
        if self.ent_url .get() != "":
            self.label_name = self.lbl_entry.get()
        try:
            img_list_confirm.clear()
            for i, var in enumerate(self.var_list):
                if var.get() == 1:
                    img_confirm = self.cb_list[i]['text']
                    img_list_confirm.append(img_confirm)
                    print(img_confirm, end=" ")
                    self.cb_list[i].deselect()
            self.window.destroy()
            print("Successfully choose images!")
        except:
            pass
    
    # Save button method
    def save_Resize_Button(self):
        global download_folder, img_list_confirm, output_folder
        self.scrollbar.update()
        if self.ent_keyword .get() != "":
            with open(f"{parent_path}/save_dir.txt", "r") as f:
                path_dir = f.readline()
            
            subdir_name = self.ent_keyword.get()
            # creat a new directory, change, and save image
            change_dir_Resize(path_dir, subdir_name)
            image_dir = path_dir + "/images/" + subdir_name + "_resized"
            # Check in the confirmed images list and download it
            for img_confirm in img_list_confirm:
                path_download = download_folder +  img_confirm
                url_extension = img_confirm.split(".")[-1]
                name_image = self.label_name + "_" + str(len(os.listdir(image_dir))+1) +"." + url_extension
                download_image_resize(path_download, name_image)      
            # print("Downloaded: ", name_image)
        
        if self.ent_url .get() != "":
            with open(f"{parent_path}/save_dir.txt", "r") as f:
                path_dir = f.readline()
            
            pattern = re.sub("http.://", "", self.ent_url.get())
            subdir_name = pattern.strip('/r/n/t').replace("/", "_")
            # creat a new directory, change, and save image
            change_dir_Resize(path_dir, subdir_name)
            image_dir = path_dir + "/images/" + subdir_name + "_resized"
            # Check in the confirmed images list and download it
            for img_confirm in img_list_confirm:
                path_download = output_folder +  img_confirm
                url_extension = img_confirm.split(".")[-1]
                name_image = self.label_name + "_" + str(len(os.listdir(image_dir))+1) +"." + url_extension
                download_image_resize(path_download, name_image)
            # print("Downloaded: ", name_image)

        sleep(1)
        # Show up the folder you save currently
        os.startfile(image_dir)
        # Shift the path from path_download to parent path
        os.chdir(parent_path) # path
        print("Sucessfully save and resize images!")

         # Save button method
    def save_Original_Button(self):
        global download_folder, img_list_confirm
        self.scrollbar.update()
        if self.ent_keyword .get() != "":
            with open(f"{parent_path}/save_dir.txt", "r") as f:
                path_dir = f.read()
            
            subdir_name = self.ent_keyword.get()
            # creat a new directory, change, and save image
            change_dir_Original(path_dir, subdir_name)
            image_dir = path_dir + '/' + "images/" + subdir_name + "_original"
            # Check in the confirmed images list and download it
            for img_confirm in img_list_confirm:
                path_download = download_folder +  img_confirm
                url_extension = img_confirm.split(".")[-1]
                name_image = self.label_name + "_" + str(len(os.listdir(image_dir))+1) +"." + url_extension
                download_image_originally(path_download, name_image)      
            # print("Downloaded: ", name_image)
        if self.ent_url .get() != "":
            with open(f"{parent_path}/save_dir.txt", "r") as f:
                path_dir = f.read()

            pattern = re.sub("http.://", "", self.ent_url.get())
            subdir_name = pattern.strip('/r/n/t').replace('/', '_')
            # creat a new directory, change, and save image
            change_dir_Original(path_dir, subdir_name)
            image_dir = path_dir + '/' + "images/" + subdir_name + "_original"
            # Check in the confirmed images list and download it
            for img_confirm in img_list_confirm:
                path_download = output_folder +  img_confirm
                url_extension = img_confirm.split(".")[-1]
                name_image = self.label_name + "_" + str(len(os.listdir(image_dir))+1) +"." + url_extension
                download_image_originally(path_download, name_image)
            # print("Downloaded: ", name_image)

        sleep(1)
        # Show up the folder you save currently
        os.startfile(image_dir)
        # Shift the path from path_download to parent path
        os.chdir(parent_path) # path
        print("Sucessfully save Originally images!")

    # Create a new top level
    def open_window(self):
        global row

        # Design for top level layout
        self.window = Toplevel(self.frm_main)
        self.window.title("Show Data")
        # self.window.geometry("1000x600")
        self.window.resizable(False, False)

        # self.window.rowconfigure([0,1], weight=1)
        self.window.columnconfigure([0,1,2,3], weight=1)

        # Show images
        self.show_image()

        # Frame Buttons
        self.frm_buttons = ttk.Frame(self.window, borderwidth=1)
        self.frm_buttons.grid(row=0, column=3, sticky="nsew")

        # Buttons
        self.btn_select_all = ttk.Button(self.frm_buttons, text="Select all", command=self.select_deselect_button)
        self.btn_select_all.grid(row =0,  sticky="ew")
        self.btn_confirm = ttk.Button(self.frm_buttons, text="Confirm", command=self.confirm_Button)
        self.btn_confirm.grid(row = 1, sticky="ew")
        self.btn_cancel = ttk.Button(self.frm_buttons, text="Cancel", command=self.window.destroy)
        self.btn_cancel.grid(row=2, sticky="ew")

        # Name for Image Label
        self.lbl_name = ttk.Label(self.frm_buttons, text="Label of images:")
        self.lbl_name.grid(row = 3, sticky="ew")
        self.lbl_entry = ttk.Entry(self.frm_buttons)
        self.lbl_entry.grid(row = 4, sticky="ew")

# Root class
class Root(Tk):
    # Constructor
    def __init__(self):
        super().__init__()
        self.title('Crawl Image')
        self.resizable(False, False)
        self['background'] = 'white'

# Main function  
def main():
    root = Root()
    app = Main(root)
    root.mainloop()

# Run main
if __name__ == '__main__':
    main()
