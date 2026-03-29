import tkinter as tk
import subprocess
import os
import time
from datetime import datetime

# --- Configuration ---
CONFIG = {
    "temp": os.path.expanduser("~/Pictures/Screenshots"),
    "docs": os.path.expanduser("~/Pictures/Hadasa")
}

def cap(mode):
    """
    Minimizes the window and handles folder logic based on the mode.
    'temp' -> Saves directly to Temp folder.
    'docs' -> Saves to a YYYY-MM-DD subfolder inside Documentation.
    """
    # Hide the window
    root.withdraw()
    root.update()
    
    # Wait for the window to disappear to avoid capturing it
    time.sleep(0.5)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    if mode == "docs":
        # Create subfolder for documentation per day
        date_folder = now.strftime("%Y-%m-%d")
        target_dir = os.path.join(CONFIG["docs"], date_folder)
    else:
        # Use base temp folder directly
        target_dir = CONFIG["temp"]

    # Ensure the directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Full path for the screenshot
    filepath = os.path.join(target_dir, f"{timestamp}.png")

    # Run the system command
    try:
        subprocess.run(["gnome-screenshot", "-f", filepath], check=True)
        print(f"Captured: {filepath}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Bring the UI back
        root.deiconify()

# --- UI Setup ---
root = tk.Tk()
root.title("Quick Cap")
root.geometry("250x120")
root.attributes("-topmost", True) # Keeps it accessible

# Button 1: Temp
btn_temp = tk.Button(
    root, 
    text="Temp", 
    command=lambda: cap("temp"),
    height=2
)
btn_temp.pack(expand=True, fill='x', padx=20, pady=5)

# Button 2: Documentation
btn_docs = tk.Button(
    root, 
    text="Documentation", 
    command=lambda: cap("docs"),
    height=2
)
btn_docs.pack(expand=True, fill='x', padx=20, pady=5)

if __name__ == "__main__":
    root.mainloop()
