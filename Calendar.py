import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

app = tk.Tk()
app.title("To Do List")

def add_task():
    try:
        task = task_entry.get()
        date = calendar.get_date()
        if not task:
            raise ValueError("Task cannot be empty")
        task_listbox.insert(tk.END, f"{date}: {task}")
        task_entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def update_task():
   try:
       task = task_entry.get()
       date = calendar.get_date()
       selected_task_index = task_listbox.curselection()[0]
       for selected_task_index in task_listbox:
           task_listbox.delete(selected_task_index)
           task_listbox.insert(tk.END, f"{date}: {task}")
   except IndexError:
       messagebox.showwarning("Warning", "You must select a task to update.")

calendar = Calendar(app, selectmode='day')
calendar.grid(column=1, row=0, padx=10, pady=10)

task_entry = tk.Entry(app, width=50)
task_entry.grid(column= 1, row=2, padx=10, pady=10)


task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.grid(column=1, row= 3, padx=10, pady=10)

add_task_button = tk.Button(app, text="Add Task", command=add_task)
add_task_button.grid(column=0, row=1, padx=5, pady=5)

remove_task_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_task_button.grid(column=1, row=1, pady=5)

update_task_button = tk.Button(app, text="Update Task", command=update_task)
update_task_button.grid(column=2, row=1, padx=5, pady=5)

app.mainloop()
