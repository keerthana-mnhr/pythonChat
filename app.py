import tkinter as tk
import pymongo
import pymongo.mongo_client

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Pychat"]
messages_col = db["messages"]


#GUI

root =tk.Tk()
root.title("PythonChat")
root.geometry("300x300")

entry  = tk.Entry(root, width=40)
entry.pack(pady=5)

send_button = tk.Button(root, text ="send")
send_button.pack(pady=5)

root.mainloop()