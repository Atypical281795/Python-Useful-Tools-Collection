import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3
from datetime import datetime

class AccountingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accounting App")

        self.create_widgets()

    def create_widgets(self):
        self.activities_frame = ttk.LabelFrame(self.root, text="Activities")
        self.activities_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.add_activity_label = ttk.Label(self.activities_frame, text="New Activity Name:")
        self.add_activity_label.grid(row=0, column=0, padx=5, pady=5)

        self.activity_name_entry = ttk.Entry(self.activities_frame)
        self.activity_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_activity_button = ttk.Button(self.activities_frame, text="Add Activity", command=self.add_activity)
        self.add_activity_button.grid(row=0, column=2, padx=5, pady=5)

        self.activities_listbox = tk.Listbox(self.activities_frame)
        self.activities_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.activities_listbox.bind('<<ListboxSelect>>', self.load_entries)

        self.entries_frame = ttk.LabelFrame(self.root, text="Entries")
        self.entries_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.item_label = ttk.Label(self.entries_frame, text="Item:")
        self.item_label.grid(row=0, column=0, padx=5, pady=5)

        self.item_entry = ttk.Entry(self.entries_frame)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.entries_frame, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = ttk.Entry(self.entries_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.claimant_label = ttk.Label(self.entries_frame, text="Claimant:")
        self.claimant_label.grid(row=2, column=0, padx=5, pady=5)

        self.claimant_entry = ttk.Entry(self.entries_frame)
        self.claimant_entry.grid(row=2, column=1, padx=5, pady=5)

        self.date_label = ttk.Label(self.entries_frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=3, column=0, padx=5, pady=5)

        self.date_entry = ttk.Entry(self.entries_frame)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        self.attachment_label = ttk.Label(self.entries_frame, text="Attachment:")
        self.attachment_label.grid(row=4, column=0, padx=5, pady=5)

        self.attachment_entry = ttk.Entry(self.entries_frame)
        self.attachment_entry.grid(row=4, column=1, padx=5, pady=5)

        self.attachment_button = ttk.Button(self.entries_frame, text="Browse", command=self.browse_file)
        self.attachment_button.grid(row=4, column=2, padx=5, pady=5)

        self.add_entry_button = ttk.Button(self.entries_frame, text="Add Entry", command=self.add_entry)
        self.add_entry_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        self.entries_treeview = ttk.Treeview(self.entries_frame, columns=("item", "amount", "claimant", "date", "attachment"), show='headings')
        self.entries_treeview.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
        self.entries_treeview.heading("item", text="Item")
        self.entries_treeview.heading("amount", text="Amount")
        self.entries_treeview.heading("claimant", text="Claimant")
        self.entries_treeview.heading("date", text="Date")
        self.entries_treeview.heading("attachment", text="Attachment")

        self.load_activities()

    def add_activity(self):
        name = self.activity_name_entry.get()
        if name:
            conn = sqlite3.connect('accounting.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO activities (name) VALUES (?)", (name,))
            conn.commit()
            conn.close()
            self.activity_name_entry.delete(0, tk.END)
            self.load_activities()

    def load_activities(self):
        self.activities_listbox.delete(0, tk.END)
        conn = sqlite3.connect('accounting.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM activities")
        activities = cursor.fetchall()
        conn.close()
        for activity in activities:
            self.activities_listbox.insert(tk.END, f"{activity[0]}: {activity[1]}")

    def load_entries(self, event):
        selected = self.activities_listbox.curselection()
        if selected:
            activity_id = int(self.activities_listbox.get(selected[0]).split(":")[0])
            self.entries_treeview.delete(*self.entries_treeview.get_children())
            conn = sqlite3.connect('accounting.db')
            cursor = conn.cursor()
            cursor.execute("SELECT item, amount, claimant, date, attachment FROM entries WHERE activity_id=?", (activity_id,))
            entries = cursor.fetchall()
            conn.close()
            for entry in entries:
                self.entries_treeview.insert("", tk.END, values=entry)

    def add_entry(self):
        selected = self.activities_listbox.curselection()
        if selected:
            activity_id = int(self.activities_listbox.get(selected[0]).split(":")[0])
            item = self.item_entry.get()
            amount = float(self.amount_entry.get())
            claimant = self.claimant_entry.get()
            date = self.date_entry.get()
            attachment = self.attachment_entry.get()

            conn = sqlite3.connect('accounting.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO entries (activity_id, item, amount, claimant, date, attachment) VALUES (?, ?, ?, ?, ?, ?)",
                           (activity_id, item, amount, claimant, date, attachment))
            conn.commit()
            conn.close()

            self.item_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.claimant_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.attachment_entry.delete(0, tk.END)

            self.load_entries(None)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.attachment_entry.delete(0, tk.END)
            self.attachment_entry.insert(0, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountingApp(root)
    root.mainloop()
