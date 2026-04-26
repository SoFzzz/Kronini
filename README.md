# Kronini - Alain Silberstein Inspired Analog Clock

Kronini is a premium analog clock application built entirely in Python using the `tkinter` library. It features a modern, artistic design inspired by the works of Alain Silberstein, with multiple modes including a functional chronograph (stopwatch).

## Features

- **Artistic Design**: Multi-layered dial with geometric hands (Triangle hour hand, Baton minute hand, Needle second hand).
- **Dual Themes**: Switch between **Day** (Gallery White) and **Dark** (Deep Gray) modes seamlessly.
- **Chronograph (Stopwatch)**: A functional stopwatch mode with its own digital display and dedicated controls.
- **Dynamic Date**: Real-time date display in Spanish (e.g., LUN 27).
- **Navigation**: Use the arrows to switch between the main Clock and the Chronograph.
- **Custom UI**: Built using a Circular Doubly-Linked List for efficient mode switching.

## Project Structure

- `main.py`: Entry point of the application.
- `app_controller.py`: Main logic coordinator and UI state manager.
- `clock_view.py`: Rendering logic for the analog clock face and hands.
- `stopwatch.py`: Stopwatch model and view logic.
- `circular_list.py`: Data structure for circular navigation between modes.
- `theme.py`: Design tokens and color palettes for Day/Dark themes.
- `alarm.py`: (Optional) Alarm model and settings view.

## Requirements

- Python 3.x
- Tkinter (included in standard Python installations)

## How to Run

Simply execute the main script:

```bash
python main.py
```

## Controls

- **Arrows (< >)**: Switch between Clock and Stopwatch views.
- **THEME Button**: Toggle between light and dark themes.
- **START/STOP Button**: (Stopwatch mode) Start or pause the timer.
- **RESET Button**: (Stopwatch mode) Reset the timer to zero.
- **Right Click**: Reset the stopwatch from the canvas.

---
Developed as a project for Data Structures class.
