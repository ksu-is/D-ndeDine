import customtkinter as ctk
from random import choice

class FoodDecider(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = 'Red')
        # Initializing window
        self.title("Donde Dine")
        self.resizable(width=False, height=False)
        self.geometry('600x400')

        # Variables for 2 users 
       self.user1_choices = []
        self.user2_choices = []
        self.user1_revoked = 0  # Incase Girlfriend "Does not care"
        self.user2_revoked = 0  # Incase Boyfriend "Does not Care"
        
        # StringVars for input/output (Strings for Widget text)
        self.entry_string_user1 = ctk.StringVar()
        self.entry_string_user2 = ctk.StringVar()
        self.output_string = ctk.StringVar()

        # Widgets
        self.create_widgets()

        # run the application
        self.mainloop()
    def create_widgets(self):
        EntrySide(self, self.entry_string_user1, self.entry_string_user2, self.output_string, self.submit_choices)
        OutputSide(self, self.output_string)
        
    def submit_choices(self, user, entry_string):
        choices = [choice.strip() for choice in entry_string.get().split(',')]
        if user == "User1":
            self.user1_choices = choices
            print("Girlfriend Choices:", self.user1_choices)
        elif user == "User2":
            self.user2_choices = choices
            print("Boyfriend Choices:", self.user2_choices)
        self.output_string.set("Choices submitted!")
        
    def find_matches(self):
        matches = list(set(self.user1_choices) & set(self.user2_choices))
        if matches:
            self.output_string.set(f"Matched options: {', '.join(matches)}")
        else:
            self.output_string.set("No matches found!")
        print("Matched options:", matches)
    def revoke_choice(self, user):
        if user == "User1" and self.user1_revoked < 1:
            self.user1_revoked += 1
            self.random_choice()  # Randomize again
            self.output_string.set(f"User 1 revoked! Remaining attempts: {1 - self.user1_revoked}")
        elif user == "User2" and self.user2_revoked < 1:
            self.user2_revoked += 1
            self.random_choice()  # Randomize again
            self.output_string.set(f"User 2 revoked! Remaining attempts: {1 - self.user2_revoked}")
        else:
            self.output_string.set("Revoke limit reached!")    

class EntrySide(ctk.CTkFrame):
    def __init__(self, parent, entry_string, output_string, save_func):
        super().__init__(parent, fg_color = '#b3f2dd', corner_radius = 0)
        # placing frame
        self.place(relx = 0.25, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = 'center')

        self.entry_string = entry_string
        self.output_string = output_string

        # layout
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # label
        label = ctk.CTkLabel(self, text = 'Enter Options Separated by Commas', text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 15, weight = 'bold'))
        label.grid(row = 0, column = 0, sticky = 'nsew')

        # entrybox
        entry_box = ctk.CTkEntry(self, textvariable = entry_string)
        entry_box.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)

        # button
        button = ctk.CTkButton(
            self,
            text = 'get random',
            command = save_func,
            fg_color = '#97f0d2',
            text_color = 'gray',
            font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'),
            hover_color = '#88dbc0')
        button.grid(row = 2, column = 0, sticky = 'nsew', padx = 15, pady = 40)
    
class OutputSide(ctk.CTkFrame):
    def __init__(self, parent, output_string):
        super().__init__(parent, fg_color = '#b3f2f1', corner_radius = 0)
        # placing frame
        self.place(relx = 0.75, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = 'center')
        self.output_string = output_string

        # layout
        self.rowconfigure((0,1), weight = 1, uniform = 'b')
        self.columnconfigure(0, weight = 1, uniform = 'b')

        # label
        label = ctk.CTkLabel(self, text = 'Random Choice is:', text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'))
        label.grid(row = 0, column = 0, sticky = 'nsew')

        # output label
        output_label = ctk.CTkLabel(self, textvariable = self.output_string, text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'))
        output_label.grid(row = 1, column = 0, sticky = 'new')

FoodDecider()
