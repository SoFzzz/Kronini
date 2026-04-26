import tkinter as tk
import sys
import os

# Add src to path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from theme import Theme
from app_controller import AppController

def main():
    root = tk.Tk()
    root.title("Kronini")
    root.geometry("640x760")
    root.resizable(False, False)
    
    theme = Theme()
    bg_color = theme.get("bg")
    root.configure(bg=bg_color)
    
    top_frame = tk.Frame(root, bg=bg_color)
    top_frame.pack(fill=tk.X, padx=24, pady=(16, 6))
    
    lbl = tk.Label(top_frame, text="K R O N I N I", font=theme.get("font_label"), bg=bg_color, fg=theme.get("label"))
    lbl.pack(side=tk.TOP)
    
    btn_prev = tk.Button(top_frame, text="<", font=theme.get("font_button"),
                         bg=bg_color, fg=theme.get("nav_icon"), 
                         activebackground=theme.get("nav_border"),
                         activeforeground=theme.get("nav_icon"),
                         relief=tk.FLAT, borderwidth=0, highlightthickness=1)
    btn_prev.place(x=18, y=0, width=38, height=30)
    
    btn_next = tk.Button(top_frame, text=">", font=theme.get("font_button"),
                         bg=bg_color, fg=theme.get("nav_icon"), 
                         activebackground=theme.get("nav_border"),
                         activeforeground=theme.get("nav_icon"),
                         relief=tk.FLAT, borderwidth=0, highlightthickness=1)
    btn_next.place(x=560, y=0, width=38, height=30)

    canvas = tk.Canvas(root, width=500, height=600, bg=bg_color, highlightthickness=0)
    canvas.pack(pady=(12, 8))
    
    bottom_frame = tk.Frame(root, bg=bg_color)
    bottom_frame.pack(fill=tk.X, padx=24, pady=(0, 20))
    
    btn_theme = tk.Button(bottom_frame, text="THEME", font=("Bahnschrift SemiBold", 13),
                           bg=theme.get("button_fill"), fg=theme.get("button_text"),
                           activebackground=theme.get("button_fill"),
                           activeforeground=theme.get("button_text"),
                           relief=tk.FLAT, borderwidth=0, highlightthickness=2,
                           padx=15, pady=12, cursor="hand2")
                           
    btn_action = tk.Button(bottom_frame, text="START", font=("Bahnschrift SemiBold", 13),
                           bg=theme.get("button_fill"), fg=theme.get("button_text"),
                           activebackground=theme.get("button_fill"),
                           activeforeground=theme.get("button_text"),
                           relief=tk.FLAT, borderwidth=0, highlightthickness=2,
                           padx=15, pady=12, cursor="hand2")

    btn_reset = tk.Button(bottom_frame, text="RESET", font=("Bahnschrift SemiBold", 13),
                           bg=theme.get("button_fill"), fg=theme.get("button_text"),
                           activebackground=theme.get("button_fill"),
                           activeforeground=theme.get("button_text"),
                           relief=tk.FLAT, borderwidth=0, highlightthickness=2,
                           padx=15, pady=12, cursor="hand2")
    
    widgets = {
        "top_frame": top_frame,
        "bottom_frame": bottom_frame,
        "lbl": lbl,
        "btn_prev": btn_prev,
        "btn_next": btn_next,
        "btn_theme": btn_theme,
        "btn_action": btn_action,
        "btn_reset": btn_reset
    }
    
    app = AppController(root, canvas, theme, widgets)
    
    btn_prev.config(command=app.prev_mode)
    btn_next.config(command=app.next_mode)
    
    app.start()
    root.mainloop()

if __name__ == "__main__":
    main()
