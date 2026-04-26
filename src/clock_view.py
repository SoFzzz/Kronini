import math
from datetime import datetime

class ClockView:
    def __init__(self, canvas, theme):
        self._canvas = canvas
        self._theme = theme
        self.cx = 250
        self.cy = 250
        self.r = 210

    def draw(self, now, mode):
        self._draw_shadows()
        self._draw_face()
        self._draw_texture()
        self._draw_markers()
        self._draw_date(now)
        self._draw_hands(now)
        self._draw_center_jewel()

    def _draw_shadows(self):
        shadow_offset = 4
        shadow_color = self._theme.get("shadow")
        self._canvas.create_oval(self.cx - self.r - 20 + shadow_offset, self.cy - self.r - 20 + shadow_offset, 
                                 self.cx + self.r + 20 + shadow_offset, self.cy + self.r + 20 + shadow_offset, 
                                 fill=shadow_color, outline="")

    def _draw_face(self):
        self._canvas.create_oval(self.cx - self.r - 20, self.cy - self.r - 20, 
                                 self.cx + self.r + 20, self.cy + self.r + 20, 
                                 fill=self._theme.get("bezel_outer"), outline="")
        self._canvas.create_oval(self.cx - self.r - 5, self.cy - self.r - 5, 
                                 self.cx + self.r + 5, self.cy + self.r + 5, 
                                 fill=self._theme.get("bezel_inner"), outline="")
        self._canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                                 self.cx + self.r, self.cy + self.r, 
                                 fill=self._theme.get("face"), outline="")
                                 
        inner_r = self.r * 0.65
        self._canvas.create_oval(self.cx - inner_r, self.cy - inner_r, 
                                 self.cx + inner_r, self.cy + inner_r, 
                                 fill=self._theme.get("face_inner"), outline=self._theme.get("sub_dial_border"), width=1)
        
        self._draw_subdials()
        self._canvas.create_text(self.cx, self.cy - 18, text="CHRONOGRAPH", font=self._theme.get("font_chrono_label"), fill=self._theme.get("text_muted"))

    def _draw_subdials(self):
        sub_r = 45
        sub_12_y = self.cy - 90
        sub_6_y = self.cy + 90
        
        # Sub-dial 12
        self._canvas.create_oval(self.cx - sub_r, sub_12_y - sub_r, 
                                 self.cx + sub_r, sub_12_y + sub_r, 
                                 fill=self._theme.get("sub_dial"), outline=self._theme.get("sub_dial_border"), width=2)
        # Sub-dial 6
        self._canvas.create_oval(self.cx - sub_r, sub_6_y - sub_r, 
                                 self.cx + sub_r, sub_6_y + sub_r, 
                                 fill=self._theme.get("sub_dial"), outline=self._theme.get("sub_dial_border"), width=2)
                                 
        # Subdial 12 markings
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            length = 5 if i % 3 != 0 else 8
            x1 = self.cx + (sub_r - length) * math.cos(angle)
            y1 = sub_12_y + (sub_r - length) * math.sin(angle)
            x2 = self.cx + sub_r * math.cos(angle)
            y2 = sub_12_y + sub_r * math.sin(angle)
            self._canvas.create_line(x1, y1, x2, y2, fill=self._theme.get("text_muted"), width=1)
        self._canvas.create_text(self.cx - 20, sub_12_y + 10, text="20", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))
        self._canvas.create_text(self.cx + 20, sub_12_y + 10, text="10", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))
        self._canvas.create_text(self.cx, sub_12_y - 25, text="0", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))

        # Subdial 6 markings
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            length = 5 if i % 3 != 0 else 8
            x1 = self.cx + (sub_r - length) * math.cos(angle)
            y1 = sub_6_y + (sub_r - length) * math.sin(angle)
            x2 = self.cx + sub_r * math.cos(angle)
            y2 = sub_6_y + sub_r * math.sin(angle)
            self._canvas.create_line(x1, y1, x2, y2, fill=self._theme.get("text_muted"), width=1)
        self._canvas.create_text(self.cx, sub_6_y - 25, text="0", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))
        self._canvas.create_text(self.cx - 25, sub_6_y, text="9", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))
        self._canvas.create_text(self.cx + 25, sub_6_y, text="3", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))
        self._canvas.create_text(self.cx, sub_6_y + 25, text="6", font=("Bahnschrift", 9), fill=self._theme.get("text_muted"))

        # Static subdials hands for aesthetic
        self._canvas.create_line(self.cx, sub_12_y, self.cx, sub_12_y - 30, fill=self._theme.get("hand_hour"), width=2)
        self._canvas.create_oval(self.cx - 3, sub_12_y - 3, self.cx + 3, sub_12_y + 3, fill=self._theme.get("hand_min"), outline="")
        self._canvas.create_line(self.cx, sub_6_y, self.cx + 20, sub_6_y - 20, fill=self._theme.get("hand_sec"), width=2)
        self._canvas.create_oval(self.cx - 3, sub_6_y - 3, self.cx + 3, sub_6_y + 3, fill=self._theme.get("hand_min"), outline="")

    def _draw_texture(self):
        track_r = self.r - 20
        self._canvas.create_oval(self.cx - track_r, self.cy - track_r,
                                 self.cx + track_r, self.cy + track_r,
                                 outline=self._theme.get("sub_dial_border"), width=1)

    def _draw_date(self, now):
        dias = ["DOM", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]
        dia_str = dias[int(now.strftime("%w"))]
        num_str = now.strftime("%d")
        
        x = self.cx + self.r * 0.55
        y = self.cy
        w = 38
        h = 14
        
        self._canvas.create_rectangle(x - w + 2, y - h + 2, x + w + 2, y + h + 2, 
                                      fill=self._theme.get("shadow"), outline="")
        self._canvas.create_rectangle(x - w, y - h, x + w, y + h, 
                                      fill=self._theme.get("date_bg"), outline=self._theme.get("date_border"), width=1)
        self._canvas.create_line(x, y - h, x, y + h, fill=self._theme.get("date_border"), width=1)
        
        self._canvas.create_text(x - 18, y, text=dia_str, font=self._theme.get("font_date"), fill=self._theme.get("date_fg"))
        self._canvas.create_text(x + 18, y, text=num_str, font=self._theme.get("font_date"), fill=self._theme.get("date_fg"))

    def _draw_markers(self):
        bezel_r = self.r + 10
        min_track_r = self.r - 20
        
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            
            if i % 5 == 0:
                num = 60 if i == 0 else i
                color = self._theme.get("bezel_text")
                if num == 60:
                    color = self._theme.get("marker_12")
                x = self.cx + bezel_r * cos_a
                y = self.cy + bezel_r * sin_a
                self._canvas.create_text(x, y, text=str(num), font=self._theme.get("font_bezel"), fill=color)
            else:
                x = self.cx + bezel_r * cos_a
                y = self.cy + bezel_r * sin_a
                self._canvas.create_oval(x-1.5, y-1.5, x+1.5, y+1.5, fill=self._theme.get("minute_dot"), outline="")

            if i % 5 == 0:
                hour = i // 5
                if hour in (0, 3, 6, 9):
                    colors = {0: "marker_12", 3: "marker_3", 6: "marker_6", 9: "marker_9"}
                    c_color = self._theme.get(colors[hour])
                    mr = 8
                    x = self.cx + min_track_r * cos_a
                    y = self.cy + min_track_r * sin_a
                    self._canvas.create_oval(x - mr, y - mr, x + mr, y + mr, fill=c_color, outline="")
                else:
                    inner_r = min_track_r - 6
                    outer_r = min_track_r + 6
                    x1 = self.cx + inner_r * cos_a
                    y1 = self.cy + inner_r * sin_a
                    x2 = self.cx + outer_r * cos_a
                    y2 = self.cy + outer_r * sin_a
                    self._canvas.create_line(x1, y1, x2, y2, fill=self._theme.get("marker"), width=4)
            else:
                x = self.cx + min_track_r * cos_a
                y = self.cy + min_track_r * sin_a
                self._canvas.create_oval(x-1, y-1, x+1, y+1, fill=self._theme.get("marker"), outline="")

    def _draw_hands(self, now):
        sec = now.second + now.microsecond / 1000000.0
        min_ = now.minute + sec / 60.0
        hour = (now.hour % 12) + min_ / 60.0

        shadow_color = self._theme.get("shadow")
        offset = 4

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

    def _draw_center_jewel(self):
        shadow_color = self._theme.get("shadow")
        offset = 4
        self._canvas.create_oval(self.cx - 12 + offset, self.cy - 12 + offset, self.cx + 12 + offset, self.cy + 12 + offset, fill=shadow_color, outline="")
        self._canvas.create_oval(self.cx - 12, self.cy - 12, self.cx + 12, self.cy + 12, fill=self._theme.get("pivot_out"), outline="")
        self._canvas.create_oval(self.cx - 5, self.cy - 5, self.cx + 5, self.cy + 5, fill=self._theme.get("pivot_in"), outline="")
