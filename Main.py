import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
import speech_recognition as sr
import subprocess
import os

def process_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        # Recognize the audio and convert it to text
        command = recognizer.recognize_google(audio, language="tr-TR").lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue connecting to the service.")
        return ""

def on_key_press1():
    command = process_voice_command()

    if "aç" in command or "çalıştır" in command or "run" in command or "open" in command or "start" in command:
        if "klasör" in command and ("don't" or "not") not in command:
            subprocess.run(["open", "."])  # Finder'i aç
        elif "notepad" in command and ("don't" or "not") not in command:
            subprocess.run(["open", "-e"])  # TextEdit'i aç
        elif "chrome" in command and ("don't" or "not") not in command:
            subprocess.run(["open", "-a", "Google Chrome"])  # Chrome'u aç
        elif "spotify" in command and ("don't" or "not") not in command:
            subprocess.run(["open", "-a", "Spotify"])  # Edge'i aç
        elif "hesap makinesi" in command and ("don't" or "not") not in command:
            subprocess.run(["open", "-a", "Calculator"])  # Hesap Makinesini aç
        else:
            print("Command not supported.")
    elif "goodbye" in command:
        print("Goodbye! Have a great day!")
        quit()  # Exit the program
    elif "stop" in command:
        print("Stopping the voice recognition system.")
        quit()  # Exit the program
    else:
        print("Command not supported.")

def start_listening():
    command = process_voice_command()

    if "proje oluştur" in command:
        create_project()
    elif "dosya oluştur" in command:
        create_file()
    elif "klasör aç" in command:
        open_folder()

def google_search():
    command = process_voice_command()
    google_search_entry.insert(0, command)
    search_google()

def search_google():
    query = google_search_entry.get()
    if query:
        url = "https://www.google.com/search?q=" + "+".join(query.split())
        webbrowser.open_new(url)

def clear_entry():
    google_search_entry.delete(0, tk.END)

def start_recording_thread():
    thread = threading.Thread(target=start_recording)
    thread.start()
    
def start_recording():
    global recording
    recording = True
    status_label1.config(text="Not Dinleniyor", foreground="green")
    update_label_animation(3)
    note_text = ""
    while recording:
        command = process_voice_command()
        if "not bitti" in command:
            recording = False
            status_label1.config(text="Not Alanı:", foreground="orangered")
            break
        note_text += command + " "
    text_area.insert(tk.END, note_text)

def update_label_animation(step):
    if recording:
        dots = "." * (step % 4)
        status_label1.config(text=f"Not Dinleniyor{dots}")
        status_label1.after(500, update_label_animation, step + 1)

def save_note():
    note_text = text_area.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(note_text)
        messagebox.showinfo("Success", "Note saved successfully!")

def clear_note():
    text_area.delete("1.0", tk.END)

def open_vscode():
    command = process_voice_command()
    if 'open code' in command:
        subprocess.run(["open", "-a", "Visual Studio Code"])   # Open Visual Studio Code

def create_project():
    os.mkdir("New Project")
    messagebox.showinfo("Success", "New project created successfully!")

def create_file():
    with open("New Project/index.py", "w") as file:
        file.write("# Your Python code here")
    messagebox.showinfo("Success", "New file created successfully!")

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        webbrowser.open(folder_path)

def search_stackoverflow():
    query = stack_search_entry.get()
    if query:
        url = "https://stackoverflow.com/search?q=" + "+".join(query.split())
        webbrowser.open_new(url)

def run_script(script_path):
    try:
        result = subprocess.run(
            ["python3", script_path], capture_output=True, text=True, check=True
        )
        print("Script Output:\n", result.stdout)
        return ""
    except subprocess.CalledProcessError as e:
        print("Error Occurred:\n", e.stderr)
        error_message = e.stderr.splitlines()[-1]  # Son satırı al
        return error_message

def search_error_on_stackoverflow():
    script_path = script_path_entry.get()
    if script_path:
        error_message = run_script(script_path)
        if error_message:
            query = error_message.replace("\n", " ")
            url = "https://stackoverflow.com/search?q=" + "+".join(query.split())
            webbrowser.open_new(url)

def stack_voice_search():
    command = process_voice_command()
    stack_search_entry.insert(0, command)
    search_stackoverflow()

root = tk.Tk()
root.title("Voice Command Interface")

# Ekranın tam ortasında açılması için ekran boyutunu al
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Pencere boyutunu belirle
window_width = 1000
window_height = 600

# Pencereyi ekranın ortasına yerleştir
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Bilgi Menüsü
def show_info():
    info_text = "Uygulama Aç ile:\n"
    info_text += "- Finder, TextEdit, Google Chrome, Microsoft Edge ve Calculator'u açabilirsiniz."
    messagebox.showinfo("Bilgi", info_text)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
bilgi_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Bilgi", menu=bilgi_menu)
bilgi_menu.add_command(label="Uygulama Aç Komutları", command=show_info)

# Sesli not alma bölümü
start_button = ttk.Button(main_frame, text="Not Al", command=start_recording_thread)
start_button.grid(row=0, column=0, padx=3, pady=3)

save_button = ttk.Button(main_frame, text="Notu Kaydet", command=save_note)
save_button.grid(row=0, column=1, padx=(0,100), pady=3)

clear_button = ttk.Button(main_frame, text="Notu Sil", command=clear_note)
clear_button.grid(row=0, column=2, padx=(0,100), pady=3)
# Not Alanı
status_label1 = ttk.Label(main_frame, foreground="orangered", text="Not Alanı:")
status_label1.grid(row=1, column=0, columnspan=3, padx=(0,500), pady=5)

text_area = tk.Text(main_frame, width=100, height=10, background="white", foreground="black")
text_area.grid(row=2, column=0, columnspan=3, padx=(115,100), pady=5)

# Sesli komutlarla uygulama açma ve Google'da arama yapma bölümü
start_button = ttk.Button(main_frame, text="Uygulama Aç", command=on_key_press1)
start_button.grid(row=4, column=0, padx=(150,0), pady=3)

google_button = ttk.Button(main_frame, text="Google'la", command=google_search)
google_button.grid(row=4, column=1, padx=3, pady=3)

status_label = ttk.Label(main_frame, text="Operasyonel İşlemler", foreground="dodgerblue")
status_label.grid(row=3, column=0, columnspan=2, padx=(150,0), pady=5)

# Google Arama Frame
google_frame = ttk.Frame(main_frame)
google_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

google_label = ttk.Label(google_frame, text="Google Search:", foreground="chartreuse")
google_label.grid(row=0, column=0, padx=(150,0), pady=3)

google_search_entry = ttk.Entry(google_frame, width=40)
google_search_entry.grid(row=0, column=1, padx=3, pady=3)

google_search_button = ttk.Button(google_frame, text="Search", command=search_google)
google_search_button.grid(row=0, column=2, padx=3, pady=3)

clear_button = ttk.Button(google_frame, text="Clear", command=clear_entry)
clear_button.grid(row=0, column=3, padx=3, pady=3)

# Visual Studio Code Frame
vscode_frame = ttk.Frame(root, padding="20")
vscode_frame.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label1 = ttk.Label(vscode_frame, text="1.")
label1.grid(row=0, column=0, padx=(350, 0))

vscode_button = ttk.Button(vscode_frame, text="VSCode", command=open_vscode)
vscode_button.grid(row=0, column=1, padx=5, pady=5)

label2 = ttk.Label(vscode_frame, text="2.")
label2.grid(row=1, column=0, padx=(350, 0))
start_button = ttk.Button(vscode_frame, text="Start Listening", command=start_listening)
start_button.grid(row=1, column=1, padx=5, pady=5)

# Stack Overflow Arama Frame
stack_frame = ttk.Frame(root, padding="20")
stack_frame.grid(row=7, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

stack_label = ttk.Label(stack_frame, text="Stack Overflow Search:", foreground="darkorange")
stack_label.grid(row=0, column=0, padx=(150, 0), pady=3)

stack_search_entry = ttk.Entry(stack_frame, width=40)
stack_search_entry.grid(row=0, column=1, padx=3, pady=3)

stack_search_button = ttk.Button(stack_frame, text="Search on Stack", command=search_stackoverflow)
stack_search_button.grid(row=0, column=2, padx=3, pady=3)

stack_voice_button = ttk.Button(stack_frame, text="Stack Voice", command=stack_voice_search)
stack_voice_button.grid(row=0, column=3, padx=3, pady=3)

# Python script hata arama frame
script_frame = ttk.Frame(root, padding="20")
script_frame.grid(row=8, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

script_label = ttk.Label(script_frame, text="Python Script Path:", foreground="red")
script_label.grid(row=0, column=0, padx=(150, 0), pady=3)

script_path_entry = ttk.Entry(script_frame, width=40)
script_path_entry.grid(row=0, column=1, padx=3, pady=3)

script_search_button = ttk.Button(script_frame, text="Run and Search Error", command=search_error_on_stackoverflow)
script_search_button.grid(row=0, column=2, padx=3, pady=3)

root.mainloop()
