# Game Over Screen

A pixel art styled Game Over screen implementation in Python using Pygame, replicating the provided HTML/Tailwind CSS mockup.

## Features

- **Pixel Art Aesthetic**: Faithful recreation of CSS pixel box styling with inner shadows and borders
- **Interactive UI**: Mouse and keyboard navigation with visual feedback
- **Responsive Layout**: Scales appropriately with window resizing while maintaining aspect ratios
- **Font Integration**: Uses VT323 font from Google Fonts for authentic retro styling
- **Image Handling**: Pixelated image display with nearest-neighbor scaling and automatic download/caching

## Requirements

- Python 3.7+
- Pygame 2.5+
- Requests (for image downloading)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Karyazilim/GameOverScreen.git
cd GameOverScreen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Game Over screen:
```bash
python main.py
```

### Controls

**Mouse:**
- Click on "RESTART" or "MAIN MENU" buttons to trigger respective actions

**Keyboard:**
- **Up/Down arrows**: Navigate between buttons
- **Enter/Space**: Activate focused button
- **Escape**: Trigger Main Menu action and exit

## Project Structure

```
GameOverScreen/
├── main.py                 # Entry point
├── game_over_screen.py     # Main screen implementation
├── ui/                     # UI components
│   ├── __init__.py
│   ├── styles.py          # Color constants and styling
│   ├── pixel_box.py       # PixelBox component
│   └── button.py          # Button component with pixel styling
├── assets/
│   ├── fonts/
│   │   └── VT323-Regular.ttf  # VT323 font from Google Fonts
│   ├── images/
│   │   └── portrait.png       # Cached portrait image (auto-downloaded)
│   └── licenses/
│       └── OFL.txt           # Open Font License for VT323
├── requirements.txt
└── README.md
```

## Assets and Licensing

### Fonts
- **VT323**: Licensed under the SIL Open Font License (OFL)
- License file: `assets/licenses/OFL.txt`
- Font source: [Google Fonts](https://fonts.google.com/specimen/VT323)

### Images
- Portrait image is automatically downloaded from the provided URL on first run
- Cached locally in `assets/images/portrait.png`
- Fallback placeholder created if download fails

## Implementation Details

### CSS to Pygame Translation

The implementation carefully replicates the CSS pixel art effects:

- **Pixel Boxes**: Black borders with inset shadows (dark top-left, light bottom-right)
- **Button Styling**: Primary (#8013ec) and secondary (#302839) themes with custom shadow colors
- **Press Effects**: Visual feedback with 2px content offset on button press
- **Color Accuracy**: Exact hex color matching from the HTML mockup

### Performance

- Maintains 60 FPS rendering
- Efficient event handling and drawing
- Responsive window resizing with proper scaling

## Customization

The score can be customized by modifying the `GameOverScreen` constructor:

```python
screen = GameOverScreen(score=5000)  # Custom score
```

Colors and layout constants can be adjusted in `ui/styles.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Note: The VT323 font is licensed separately under the SIL Open Font License.