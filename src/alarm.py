class Alarm:
    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._enabled = False

    def toggle(self):
        self._enabled = not self._enabled

    def add_minute(self, mins=1):
        self._minute += mins
        if self._minute >= 60:
            self._minute %= 60
            self._hour = (self._hour + 1) % 24

    def is_triggered(self, now):
        return self._enabled and now.hour == self._hour and now.minute == self._minute and now.second == 0

    def get_time_str(self):
        return f"{self._hour:02d}:{self._minute:02d}"

class AlarmView:
    def __init__(self, canvas, theme, alarm):
        self._canvas = canvas
        self._theme = theme
        self._alarm = alarm
        self.cx = 250
        self.cy = 250
        self.r = 200

    def draw(self, _, __):
        self._theme.switch("dark")
        
        # Bezel and face
        self._canvas.create_oval(self.cx - self.r - 35, self.cy - self.r - 35, 
                                 self.cx + self.r + 35, self.cy + self.r + 35, 
                                 fill=self._theme.get("bezel"), outline="", tags="alarm")
        self._canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                                 self.cx + self.r, self.cy + self.r, 
                                 fill=self._theme.get("face"), outline="", tags="alarm")
                                 
        self._canvas.create_text(self.cx, self.cy - 60, text="ALARM SETTINGS", font=self._theme.get("font_label"), fill=self._theme.get("text"), tags="alarm")
        
        color = self._theme.get("hand_min") if self._alarm._enabled else self._theme.get("marker")
        self._canvas.create_text(self.cx, self.cy, text=self._alarm.get_time_str(), font=("Courier New", 48, "bold"), fill=color, tags="alarm")
        
        status = "ON" if self._alarm._enabled else "OFF"
        self._canvas.create_text(self.cx, self.cy + 60, text=f"STATUS: {status}", font=self._theme.get("font_label"), fill=color, tags="alarm")
