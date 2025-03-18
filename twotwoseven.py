# p227_starter_one_button_shell.py

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import platform

def do_command(command):
    global command_textbox, url_entry

    url_val = url_entry.get()
    if (len(url_val) == 0):
        url_val = "::1"
      
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    if command == "nslookup":
        curl_command = ["curl", "-H", "Content-Type: application/dns-json", url_val]
        p = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "ipconfig":
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "tracert":
        tracert_command = [command , ' ' , url_val]
        p = subprocess.Popen(tracert_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "ping":
        ping_command = ["ping", url_val]
        p = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # p.wait()

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def mSave():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open (filename, mode = 'w')
    text_to_save = command_textbox.get("1.0", tk.END)
    
    file.write(text_to_save)
    file.close()

def get_ip_config_command():
    if platform.system().lower() == "windows":
        return "ipconfig"
    else:
        return "ifconfig"

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

frame_URL = tk.Frame(root, pady=10,  bg="purple") 
frame_URL.pack()

url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) 
url_entry.pack(side=tk.LEFT)

ping_btn = tk.Button(frame, text="Ping", command=lambda:do_command("ping"))
ping_btn.pack()

tracert_btn = tk.Button(frame, text="Tracert", command=lambda:do_command("tracert"))
tracert_btn.pack()

nsLookup_btn = tk.Button(frame, text="NS Lookup", command=lambda:do_command("nslookup"), bg = "purple")
nsLookup_btn.pack()

ip_config_cmd = get_ip_config_command()
ip_config_btn = tk.Button(frame, text="IP Config", command=lambda:do_command(ip_config_cmd))
ip_config_btn.pack()

save_btn = tk.Button(frame, text="Save", command=mSave)
save_btn.pack()

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

frame = tk.Frame(root,  bg="black")
frame.pack()

root.mainloop()
