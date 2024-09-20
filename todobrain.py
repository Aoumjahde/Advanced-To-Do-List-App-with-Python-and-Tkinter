from tkinter import *
BRONZ = "#d0d7db"
GREEN= "#495e57"
YELLOW= "#f4ce14"
DARKBROWN = "#45474b"
BLACK ="#16161e"





class TododBrain:
    def __init__(self) -> None:
        self.task_list = []
        self.window = Tk()
        self.window.title("ToDo List App")
        self.window.config(width=400, height=450, bg=BLACK, padx=10, pady=10)

        self.WLC_lae = Label(text="WELCOME.", bg=BLACK, font=("Rowdies", 25, "bold"), fg=YELLOW)
        self.WLC_lae.grid(column=0, row=0, padx=10, pady=80)

        self.start_button = Button(text="START", width=10, bg=YELLOW,
                                   font=("Rowdies", 15, "bold"), fg=BLACK,
                                   border=0, highlightthickness=0,
                                   activebackground=YELLOW, command=self.choise_screen)
        self.start_button.grid(column=0, row=1, padx=10, pady=80)
        self.window.mainloop()

    def choise_screen(self):
        self.second_window = Toplevel(self.window)
        self.second_window.title("Chosing What you want!")
        self.second_window.config(width=400, height=450, bg=BLACK, padx=10, pady=10)

        self.add_button = Button(self.second_window, text="ADD TASK", width=15, bg=BRONZ,
                                 font=("Rowdies", 15, "bold"), fg=BLACK, border=0,
                                 highlightthickness=0, activebackground=BRONZ, command=self.add_task)
        self.add_button.grid(column=0, row=1, pady=13, padx=20)

        self.list_task = Button(self.second_window, text="TASK list", width=15, bg=BRONZ,
                                font=("Rowdies", 15, "bold"), fg=BLACK, border=0,
                                highlightthickness=0, activebackground=BRONZ,command=self.list_of_task)
        self.list_task.grid(column=0, row=2, pady=13, padx=20)

        self.remove_task = Button(self.second_window, text="REMOVE TASK", width=15, bg=BRONZ,
                                  font=("Rowdies", 15, "bold"), fg=BLACK, border=0,
                                  highlightthickness=0, activebackground=BRONZ,command=self.remov_task)
        self.remove_task.grid(column=0, row=3, pady=13, padx=20)

        self.exit_button = Button(self.second_window, text="EXIT", width=10, bg=YELLOW,
                                  font=("Rowdies", 15, "bold"), fg=BLACK, border=0,
                                  highlightthickness=0, activebackground=YELLOW)
        self.exit_button.grid(column=0, row=4, pady=13, padx=20)

    def add_task(self):
        self.add_task_windows = Toplevel(self.window)
        self.add_task_windows.title("Adding New Task!")
        self.add_task_windows.config(width=400, height=450, bg=BLACK, padx=20, pady=20)

        self.label_textbox = Label(self.add_task_windows, text="Add your task below!", font=("Rowdies", 15, "bold"))
        self.label_textbox.grid(column=0, row=0, columnspan=2, pady=1)
        self.label_textbox.focus()

        self.new_task = Text(self.add_task_windows, width=30, height=10)
        self.new_task.grid(column=0, row=1, pady=10)

        self.add_task_button = Button(self.add_task_windows, text="ADD MY TASK", width=15, bg=BRONZ,
                                      font=("Rowdies", 15, "bold"), fg=BLACK, border=0,
                                      highlightthickness=0, activebackground=BRONZ, command=self.task)
        self.add_task_button.grid(column=0, row=2, pady=13)

    def task(self):
        user_input = self.new_task.get("1.0", "end-1c").strip()  # Get text and remove trailing whitespace
        if user_input:  # Only add non-empty tasks
            self.task_list.append(user_input)
            self.new_task.delete("1.0", "end")  # Clear the input field
            print(f"Current List: {self.task_list}")

    def list_of_task(self):
        self.task_of_lis = Toplevel(self.window)
        self.task_of_lis.title("My Task List")
        self.task_of_lis.config(width=400, height=450, bg=BLACK, padx=20, pady=20)

        # Create a label to display the tasks
        tasks = "\n".join(self.task_list)  # Joining tasks with newline for a clean display
        self.label = Label(self.task_of_lis, text=f"Tasks:\n\n  {tasks}", bg=BLACK, fg=YELLOW, font=("Rowdies", 15))
        self.label.grid(column=0, row=0, padx=10, pady=10)

        # Add a close button
        self.close_button = Button(self.task_of_lis, text="CLOSE", command=self.task_of_lis.destroy, width=10, bg=YELLOW,
                                font=("Rowdies", 12), fg=BLACK, border=0, highlightthickness=0, activebackground=YELLOW)
        self.close_button.grid(column=0, row=1, pady=20)

    