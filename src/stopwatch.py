import time
import math
from clock_view import ClockView

class Stopwatch:
    def __init__(self):
        self._start = 0.0
        self._elapsed = 0.0
        self._running = False
        
    def toggle(self):
        if self._running:
            self._elapsed = time.time() - self._start
            self._running = False
        else:
            self._start = time.time() - self._elapsed
            self._running = True
            
    def reset(self):
        self._start = time.time()
        self._elapsed = 0.0
        if not self._running:
            self._start = 0.0
            
    def get_elapsed(self):
        if self._running:
            return time.time() - self._start
        return self._elapsed

class StopwatchView(ClockView):
    def __init__(self, canvas, theme, sw):
        super().__init__(canvas, theme)
        self._sw = sw
        
    def draw(self, now, mode):
        # We inherit face drawing logic from ClockView
        self._draw_shadows()
        self._draw_face()
        self._draw_texture()
        self._draw_markers()
        # No date in stopwatch
        self._draw_hands_sw()
        self._draw_center_jewel()
        self._draw_digital_display()

    def _draw_hands_sw(self):
        elapsed = self._sw.get_elapsed()
        sec = elapsed % 60
        min_ = (elapsed / 60) % 60
        hour = (elapsed / 3600) % 12

        shadow_color = self._theme.get("shadow")
        offset = 4

        # Hour Hand (Thick Geometric Triangle) mapped to stopwatch hours
        hour_angle = math.radians(hour * 30 - 90)
        h_len = self.r * 0.45
        h_base = 32
        
        hx = self.cx + h_len * math.cos(hour_angle)
        hy = self.cy + h_len * math.sin(hour_angle)
        base_x = self.cx - math.cos(hour_angle) * 12
        base_y = self.cy - math.sin(hour_angle) * 12
        perp_dx = -math.sin(hour_angle) * (h_base / 2)
        perp_dy = math.cos(hour_angle) * (h_base / 2)
        
        pts_hour = [hx, hy, base_x - perp_dx, base_y - perp_dy, base_x + perp_dx, base_y + perp_dy]
        pts_hour_shadow = [p + offset for p in pts_hour]
        
        self._canvas.create_polygon(pts_hour_shadow, fill=shadow_color, outline="")
        self._canvas.create_polygon(pts_hour, fill=self._theme.get("hand_hour"), outline=self._theme.get("pivot_out"), width=1)

        # Minute Hand
        min_angle = math.radians(min_ * 6 - 90)
        m_len = self.r * 0.8
        m_width = 12
        mx = self.cx + m_len * math.cos(min_angle)
        my = self.cy + m_len * math.sin(min_angle)
        m_base_x = self.cx - math.cos(min_angle) * 15
        m_base_y = self.cy - math.sin(min_angle) * 15
        perp_dx = -math.sin(min_angle) * (m_width / 2)
        perp_dy = math.cos(min_angle) * (m_width / 2)
        
        pts_min = [mx + perp_dx, my + perp_dy, mx - perp_dx, my - perp_dy, m_base_x - perp_dx, m_base_y - perp_dy, m_base_x + perp_dx, m_base_y + perp_dy]
        pts_min_shadow = [p + offset for p in pts_min]
        
        self._canvas.create_polygon(pts_min_shadow, fill=shadow_color, outline="")
        self._canvas.create_polygon(pts_min, fill=self._theme.get("hand_min"), outline=self._theme.get("pivot_out"), width=1)

        # Second Hand
        sec_angle = math.radians(sec * 6 - 90)
        s_len = self.r * 0.9
        tail_len = 40
        sx = self.cx + s_len * math.cos(sec_angle)
        sy = self.cy + s_len * math.sin(sec_angle)
        tx = self.cx - tail_len * math.cos(sec_angle)
        ty = self.cy - tail_len * math.sin(sec_angle)
        
        self._canvas.create_line(tx + offset, ty + offset, sx + offset, sy + offset, fill=shadow_color, width=2)
        self._canvas.create_oval(tx - 6 + offset, ty - 6 + offset, tx + 6 + offset, ty + 6 + offset, fill=shadow_color, outline="")
        self._canvas.create_line(tx, ty, sx, sy, fill=self._theme.get("hand_sec"), width=2)
        self._canvas.create_oval(tx - 6, ty - 6, tx + 6, ty + 6, fill=self._theme.get("hand_sec"), outline="")

    def _draw_digital_display(self):
        # Move it lower down
        box_y = self.cy + self.r + 55
        box_w = 110
        box_h = 28
        
        self._canvas.create_rectangle(self.cx - box_w + 2, box_y - box_h + 2, self.cx + box_w + 2, box_y + box_h + 2, fill=self._theme.get("shadow"), outline="")
        self._canvas.create_rectangle(self.cx - box_w, box_y - box_h, self.cx + box_w, box_y + box_h, fill=self._theme.get("date_bg"), outline=self._theme.get("date_border"), width=2)
        
        self._canvas.create_text(self.cx - 60, box_y - 18, text="CHR | 100", font=self._theme.get("font_chrono_label"), fill=self._theme.get("text_muted"))
        
        elapsed = self._sw.get_elapsed()
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        msecs = int((elapsed * 100) % 100)
        time_str = f"{mins:02d}:{secs:02d}.{msecs:02d}"
        
        color = self._theme.get("hand_hour") if self._sw._running else self._theme.get("text")
        self._canvas.create_text(self.cx + 10, box_y + 4, text=time_str, font=self._theme.get("font_chrono_time"), fill=color)
