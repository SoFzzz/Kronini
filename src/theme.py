class Theme:
    PALETTES = {
        "day": {
            "bg": "#F4F0E7",            # Warm gallery white
            "bg_top": "#FBF7EF",
            "bg_bottom": "#E6D8BE",
            "shadow": "#C9C1B3",        # Soft brass-tinted shadow
            "bezel": "#1A1A1A",         # backwards compat
            "bezel_outer": "#161616",   # Dark edge
            "bezel_inner": "#242424",   # Stepped bezel
            "bezel_text": "#F3EEE4",    # High contrast text on bezel
            "face": "#F7F2E8",          # Main face
            "face_inner": "#EFE8DA",    # Slight gradient effect
            "text": "#1E1D1A",
            "text_muted": "#726B61",
            "sub_dial": "#E6DDCC",      # Recessed sub-dial
            "sub_dial_border": "#D2C6B2",
            "hand_min": "#007BFF",      # Primary Blue
            "hand_sec": "#FFDD00",      # Primary Yellow
            "hand_hour": "#E63946",     # Primary Red
            "pivot_out": "#1A1A1A",
            "pivot_in": "#FFDD00",
            "marker_12": "#E63946",     # Red
            "marker_3": "#007BFF",      # Blue
            "marker_6": "#FFDD00",      # Yellow
            "marker_9": "#007BFF",      # Blue
            "marker": "#5C5A53",        # Standard indices
            "minute_dot": "#8E877B",
            "date_bg": "#FFFDF9",
            "date_fg": "#22211E",
            "date_border": "#B7A98F",
            "label": "#2D2922",
            "nav_border": "#D6CBBB",
            "nav_icon": "#2D2922",
            "panel": "#EFE7D8",
            "panel_border": "#CDBEA5",
            "button_fill": "#1E1D1A",
            "button_text": "#F7F2E8",
            "button_accent": "#E63946",
            "red_marker": "#E63946"
        },
        "dark": {
            "bg": "#121212",            
            "bg_top": "#202020",
            "bg_bottom": "#070707",
            "shadow": "#050505",        
            "bezel": "#0A0A0A",         # backwards compat
            "bezel_outer": "#0A0A0A",   
            "bezel_inner": "#1A1A1A",   
            "bezel_text": "#D8D8D8",
            "face": "#222222",          
            "face_inner": "#1E1E1E",    
            "text": "#E0E0E0",          
            "text_muted": "#9A9A9A",
            "sub_dial": "#1A1A1A",      
            "sub_dial_border": "#333333",
            "hand_min": "#4DB8FF",      
            "hand_sec": "#FFDD00",      
            "hand_hour": "#FF4D4D",     
            "pivot_out": "#E0E0E0",
            "pivot_in": "#FFDD00",
            "marker_12": "#FF4D4D",     
            "marker_3": "#4DB8FF",      
            "marker_6": "#FFDD00",      
            "marker_9": "#4DB8FF",      
            "marker": "#888888",
            "minute_dot": "#767676",
            "date_bg": "#1A1A1A",
            "date_fg": "#E0E0E0",
            "date_border": "#444444",
            "label": "#E0E0E0",
            "nav_border": "#333333",
            "nav_icon": "#E0E0E0",
            "panel": "#191919",
            "panel_border": "#2D2D2D",
            "button_fill": "#F0E4CC",
            "button_text": "#111111",
            "button_accent": "#4DB8FF",
            "red_marker": "#FF4D4D"
        }
    }

    FONTS = {
        "font_bezel": ("Bahnschrift SemiBold", 11),
        "font_label": ("Bahnschrift Light", 16),
        "font_title": ("Bahnschrift Light", 22),
        "font_date": ("Bahnschrift SemiBold", 11),
        "font_button": ("Bahnschrift SemiBold", 14),
        "font_mono": ("Consolas", 13, "bold"),
        "font_chrono_label": ("Bahnschrift", 12),
        "font_chrono_time": ("Bahnschrift SemiBold", 24)
    }

    def __init__(self):
        self._active = "day"

    def get(self, key):
        if key in self.PALETTES[self._active]:
            return self.PALETTES[self._active][key]
        return self.FONTS.get(key, None)

    def switch(self, name):
        if name in self.PALETTES:
            self._active = name
