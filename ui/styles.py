"""
UI styles and constants for the Game Over screen.
Contains color definitions and rendering utilities that replicate the CSS pixel art aesthetic.
"""

# Color constants matching the HTML/CSS mockup
COLORS = {
    'background': '#141118',
    'panel_bg': '#211c27',
    'text_white': '#ffffff',
    'text_inactive': '#ab9db9',
    
    # Button colors
    'button_primary': '#8013ec',
    'button_primary_shadow_dark': '#5a0e9d',
    'button_primary_shadow_light': '#a657ff',
    
    'button_secondary': '#302839',
    'button_secondary_shadow_dark': '#1c1721',
    'button_secondary_shadow_light': '#443951',
    
    # Pixel box shadow colors
    'shadow_dark': '#5a5a5a',
    'shadow_light': '#ffffff',
    'border_black': '#000000',
}

# Convert hex colors to RGB tuples for pygame
def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Convert all colors to RGB
RGB_COLORS = {key: hex_to_rgb(value) for key, value in COLORS.items()}

# Layout constants
PIXEL_BORDER_WIDTH = 4
BUTTON_HEIGHT = 64
TITLE_FONT_SIZE = 72
SCORE_FONT_SIZE = 48
BUTTON_FONT_SIZE = 24
CONTENT_MAX_WIDTH = 400
CONTENT_PADDING = 16