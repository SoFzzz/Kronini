from datetime import datetime
from clock_view import ClockView
from circular_list import CircularDoublyLinkedList
from stopwatch import Stopwatch, StopwatchView
import tkinter as tk

class AppController:
    def __init__(self, root, canvas, theme, widgets):
        self._root = root
        self._canvas = canvas
        self._theme = theme
        self._widgets = widgets
        
        self._modes = CircularDoublyLinkedList()
        self._modes.append("clock")
        self._modes.append("stopwatch")
        
        self._current_theme = "day"
        self._last_theme = None
        self._last_mode = None
        
        self._sw = Stopwatch()
        self._view_clock = ClockView(canvas, theme)
        self._view_sw = StopwatchView(canvas, theme, self._sw)
        
        self._widgets["btn_theme"].config(command=self.toggle_theme)
        self._widgets["btn_action"].config(command=self.action)
        self._widgets["btn_reset"].config(command=self.reset_chrono)
        self._canvas.bind("<Button-3>", self._secondary_action)
        
    def start(self):
        self._tick()
        
    def _tick(self):
        now = datetime.now()
        mode = self._modes.get_current()
        
        # Update colors only when theme changes
        if self._current_theme != self._last_theme:
            self._last_theme = self._current_theme
            self._theme.switch(self._current_theme)
            
            bg_color = self._theme.get("bg")
            fg_color = self._theme.get("label")
            
            self._root.configure(bg=bg_color)
            self._widgets["top_frame"].configure(bg=bg_color)
            self._widgets["bottom_frame"].configure(bg=bg_color)
            self._widgets["lbl"].configure(bg=bg_color, fg=fg_color)
            
            for btn_name in ["btn_prev", "btn_next", "btn_theme", "btn_action", "btn_reset"]:
                btn = self._widgets[btn_name]
                if btn_name in ("btn_theme", "btn_action", "btn_reset"):
                    btn.configure(bg=self._theme.get("button_fill"), fg=self._theme.get("button_text"), 
                                  activebackground=self._theme.get("button_fill"), activeforeground=self._theme.get("button_text"))
                else:
                    btn.configure(bg=bg_color, fg=self._theme.get("nav_icon"), 
                                  activebackground=self._theme.get("nav_border"), activeforeground=self._theme.get("nav_icon"))
        
        # Update layout only when mode changes
        if mode != self._last_mode:
            self._last_mode = mode
            btn_theme = self._widgets["btn_theme"]
            btn_action = self._widgets["btn_action"]
            btn_reset = self._widgets["btn_reset"]
            
            btn_theme.pack_forget()
            btn_action.pack_forget()
            btn_reset.pack_forget()
            
            if mode == "clock":
                btn_theme.pack(ipadx=8, ipady=2)
            elif mode == "stopwatch":
                btn_theme.pack(side=tk.LEFT, expand=True, padx=5, ipadx=8, ipady=2)
                btn_action.pack(side=tk.LEFT, expand=True, padx=5, ipadx=8, ipady=2)
                btn_reset.pack(side=tk.LEFT, expand=True, padx=5, ipadx=8, ipady=2)
        
        # Draw frame
        bg_color = self._theme.get("bg")
        self._canvas.delete("all")
        self._canvas.configure(bg=bg_color)
        
        if mode == "clock":
            self._view_clock.draw(now, self._current_theme)
            mode_text = f"K R O N I N I  -  {self._current_theme.upper()}"
        elif mode == "stopwatch":
            self._view_sw.draw(now, self._current_theme)
            status = "STOP" if self._sw._running else "START"
            self._widgets["btn_action"].config(text=status)
            mode_text = f"K R O N I N I  -  {mode.upper()}"
            
        self._widgets["lbl"].config(text=mode_text)
        
        self._root.after(50, self._tick)

    def toggle_theme(self):
        self._current_theme = "dark" if self._current_theme == "day" else "day"

    def action(self):
        mode = self._modes.get_current()
        if mode == "stopwatch":
            self._sw.toggle()

    def reset_chrono(self):
        mode = self._modes.get_current()
        if mode == "stopwatch":
            self._sw.reset()

    def _secondary_action(self, event):
        self.reset_chrono()

    def next_mode(self):
        self._modes.forward()

    def prev_mode(self):
        self._modes.backward()
