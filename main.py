import customtkinter
import pyperclip
import requests
import base64

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Decode the auth variable
auth_base64 = 'Y3JlZGl0cyB0byBsdW5hcmluZ3Mgb24gZGlzY29yZA=='
auth = base64.b64decode(auth_base64).decode('utf-8')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        

        self.geometry("500x550")
        self.title("IP Information")
            #self.iconbitmap("favicon.ico") use your own favicon here

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, expand=True, fill="both")

        self.key = customtkinter.CTkLabel(self.frame, text="key", font=("TimesNewRoman", 20))
        self.key.pack(padx=10, pady=10, side="left")

        self.value = customtkinter.CTkLabel(self.frame, text="value", font=("TimesNewRoman", 20))
        self.value.pack(padx=10, pady=10, side="right")

            # important stuff

        self.button = customtkinter.CTkButton(self, text="Search Up", hover_color='#689E7B', fg_color="#8ABD91", command=self.get_info)
        self.button.pack(padx=10, pady=10, side="bottom", fill="both")

        self.input_box = customtkinter.CTkEntry(self)
        self.input_box.pack(padx=10, pady=10, side="bottom", fill="both")

        self.copy_button = customtkinter.CTkButton(self, text="Copy info", hover_color='#689E7B', fg_color="#8ABD91",  command=self.copy)
        self.copy_button.pack(padx=10, pady=10, side="bottom", fill="both")

            # Print the decoded auth variable
        print(f'Decoded auth: {auth}')


    def get_info(self):
        query = self.input_box.get()
        self.response = requests.get(f"http://ip-api.com/json/{query}").json()

        self.key.configure(text='\n'.join(self.response.keys()))
        self.value.configure(text='\n'.join(str(value) for value in self.response.values()))

    def copy(self):
        info_string = '\n'.join(f'{key}: {value}' for key, value in self.response.items())
        pyperclip.copy(info_string)

if __name__ == "__main__":
    App().mainloop()
