import tkinter as tk
import customtkinter
import pyperclip
import requests

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x550")
        self.title("IP Information")
        #self.iconbitmap("favicon.ico") use your own favicon here

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, expand=True, fill="both")

        self.input_box = customtkinter.CTkEntry(self.frame, width=200)
        self.input_box.pack(padx=10, pady=10, side="top", fill="x")

        self.search_button = customtkinter.CTkButton(self.frame, text="Search Up", hover_color='#689E7B', fg_color="#8ABD91", command=self.get_info)
        self.search_button.pack(padx=10, pady=10, side="top", fill="x")

        self.info_frame = customtkinter.CTkFrame(self.frame)
        self.info_frame.pack(padx=10, pady=10, side="top", fill="both", expand=True)

        self.key_label = customtkinter.CTkLabel(self.info_frame, text="Key", font=("TimesNewRoman", 20))
        self.key_label.pack(padx=10, pady=10, side="left")

        self.value_label = customtkinter.CTkLabel(self.info_frame, text="Value", font=("TimesNewRoman", 20))
        self.value_label.pack(padx=10, pady=10, side="left")

        self.key_listbox = tk.Listbox(self.info_frame, height=20)
        self.key_listbox.pack(padx=10, pady=10, side="left", fill="both", expand=True)

        self.value_listbox = tk.Listbox(self.info_frame, height=20)
        self.value_listbox.pack(padx=10, pady=10, side="left", fill="both", expand=True)

        self.copy_button = customtkinter.CTkButton(self.frame, text="Copy info", hover_color='#689E7B', fg_color="#8ABD91",  command=self.copy)
        self.copy_button.pack(padx=10, pady=10, side="bottom", fill="x")

    def get_info(self):
        query = self.input_box.get()
        self.response = requests.get(f"http://ip-api.com/json/{query}").json()

        self.key_listbox.delete(0, tk.END)
        self.value_listbox.delete(0, tk.END)

        for key, value in self.response.items():
            self.key_listbox.insert(tk.END, key)
            self.value_listbox.insert(tk.END, str(value))

    def copy(self):
        info_string = '\n'.join(f'{key}: {value}' for key, value in self.response.items())
        pyperclip.copy(info_string)

if __name__ == "__main__":
    App().mainloop()
