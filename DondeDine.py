import customtkinter as ctk
from random import choice

class FoodDecider(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#d0cec5')  # Background color updated
        # Initializing window
        self.title("Donde Dine")
        self.resizable(width=False, height=False)
        self.geometry('600x400')

        # Variables for 2 users 
        self.user1_choices = []
        self.user2_choices = []
        self.user1_revoked = 0 
        self.user2_revoked = 0  
        
        # StringVars for input/output (Strings for Widget text)
        self.entry_string_user1 = ctk.StringVar()
        self.entry_string_user2 = ctk.StringVar()
        self.output_string = ctk.StringVar()
        self.user1_name = ctk.StringVar(value="User 1") #Updates the name when user inputs
        self.user2_name = ctk.StringVar(value="User 2")

        # Widgets
        self.create_widgets()

        # run the application
        self.mainloop()
        
    def create_widgets(self):
        EntrySide(
            self,
            self.entry_string_user1,
            self.entry_string_user2,
            self.output_string,
            self.submit_choices,
            self.user1_name,
            self.user2_name,
        )
        OutputSide(self, self.output_string, self.random_choice)
        
    def submit_choices(self, user, entry_string):
        choices = [choice.strip() for choice in entry_string.get().split(',')]
        if user == "User1":
            self.user1_choices = choices
           print(f"{self.user1_name.get()} Choices:", self.user1_choices)
        elif user == "User2":
            self.user2_choices = choices
            print(f"{self.user2_name.get()} Choices:", self.user2_choices)
        self.output_string.set("Choices submitted!")

    # Command for matching the output responses
    def find_matches(self):
        matches = list(set(self.user1_choices) & set(self.user2_choices))
        if matches:
            self.output_string.set(f"Matched options: {', '.join(matches)}")
        else:
            self.output_string.set("No matches found!")
        print("Matched options:", matches)

    #Taking out the revoke choice as it was buggy and after talking to a few people didnt deem it useful
    def random_choice(self):
        combined_choices = self.user1_choices + self.user2_choices
        if combined_choices:
            random_choice = choice(combined_choices)
            self.output_string.set(f"Random choice: {random_choice}")
            print(f"Random choice: {random_choice}")
        else:
            self.output_string.set("No choices available to randomize!")
            print("No choices available to randomize!")   

class EntrySide(ctk.CTkFrame):
    def __init__(self, parent, entry_string_user1, entry_string_user2, output_string, save_func, user1_name, user2_name): #New Button for Users 
        super().__init__(parent, fg_color='#d0cec5', corner_radius=0)  # Background color updated
        # placing frame Update
        self.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=1, anchor='center')

         # Layout
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        # Label for Name Input
        label1 = ctk.CTkLabel(self, text="Enter User 1 Name:", font=("Calibri", 12, "bold"))
        label1.grid(row=0, column=0, sticky='nsew')
        name_entry1 = ctk.CTkEntry(self, textvariable=user1_name)
        name_entry1.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)

        label2 = ctk.CTkLabel(self, text="Enter User 2 Name:", font=("Calibri", 12, "bold"))
        label2.grid(row=2, column=0, sticky='nsew')
        name_entry2 = ctk.CTkEntry(self, textvariable=user2_name)
        name_entry2.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)

       # User 1 Entry
        label3 = ctk.CTkLabel(self, textvariable=user1_name, font=("Calibri", 15, "bold"))
        label3.grid(row=4, column=0, sticky='nsew')
        entry1 = ctk.CTkEntry(self, textvariable=entry_string_user1)
        entry1.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
        button1 = ctk.CTkButton(
            self,
            text="Submit User 1",
            command=lambda: save_func("User1", entry_string_user1),
            fg_color='#181917',  # Button color updated
            hover_color='#fb432f',  # Hover color updated
        )
        button1.grid(row=6, column=0, sticky='nsew', padx=10, pady=10)
       
        # User 2 Entry
        label4 = ctk.CTkLabel(self, textvariable=user2_name, font=("Calibri", 15, "bold"))
        label4.grid(row=7, column=0, sticky='nsew')
        entry2 = ctk.CTkEntry(self, textvariable=entry_string_user2)
        entry2.grid(row=8, column=0, sticky='nsew', padx=10, pady=10)
        button2 = ctk.CTkButton(
            self,
            text="Submit User 2",
            command=lambda: save_func("User2", entry_string_user2),
            fg_color='#181917',  # Button color updated
            hover_color='#fb432f',  # Hover color updated
        )
        button2.grid(row=9, column=0, sticky='nsew', padx=10, pady=10)
        
class OutputSide(ctk.CTkFrame): #Update to adjust for added buttons
    def __init__(self, parent, output_string, random_choice_func):
        super().__init__(parent, fg_color='#d0cec5', corner_radius=0)  # Background color updated
        # Placing frame
        self.place(relx=0.75, rely=0.5, relwidth=0.5, relheight=1, anchor='center')


       # Layout
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='b')
        self.columnconfigure(0, weight=1, uniform='b')

        # Label
        label = ctk.CTkLabel(
            self,
            text='Your going to:',
            text_color='#fb432f',  # Text color updated
            font=ctk.CTkFont(family='Calibri', size=20, weight='bold'),
        )
        label.grid(row=0, column=0, sticky='nsew')
        
        # Output Label
        output_label = ctk.CTkLabel(self, textvariable=output_string, font=("Calibri", 20, "bold"))
        output_label.grid(row=1, column=0, sticky='new')

         # Match Button Added that has the color updated to match the branding 
        match_button = ctk.CTkButton(
            self,
            text="Find Matches",
            command=parent.find_matches,
            fg_color='#181917',  # Button color updated
            hover_color='#fb432f',  # Hover color updated
        )
        match_button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

   # Randomize Button
        random_button = ctk.CTkButton(
            self,
            text="Randomize Choice",
            command=random_choice_func,
            fg_color='#181917',  # Button color updated
            hover_color='#fb432f',  # Hover color updated
        )
        random_button.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

#To run the application :)
FoodDecider()
