import tkinter as tk

root = tk.Tk()
root.title("Form UI with Tkinter")
root.geometry('600x700')

#setting up the grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

head_label = tk.Label(root,text="Form",background='black', foreground="white")
head_label.grid(column=1, row=0, columnspan=2, sticky= "N",pady=2 )
fname_label = tk.Label(root,text="First Name",background='black', foreground="white")
fname_label.grid(column=1, row=2)
sname_label = tk.Label(root,text="Last Name",background='black', foreground="white")
sname_label.grid(column=2 ,row=2)
bday_label = tk.Label(root,text="Date of Birth",background='black', foreground="white")
bday_label.grid(column=1, row=3)
age_label = tk.Label(root,text="Age",background='black', foreground="white")
age_label.grid(column=2, row=3)
fathername_label = tk.Label(root,text="Father's Name",background='black', foreground="white")
fathername_label.grid(column=1, row=4)
mobile_label = tk.Label(root,text="Mobile No.",background='black', foreground="white")
mobile_label.grid(column=1, row=5)
email_label = tk.Label(root,text="Email",background='black', foreground="white")
email_label.grid(column=2, row=5)

root.mainloop()
