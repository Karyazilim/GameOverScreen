"""
PixelBox component that replicates CSS pixel-box styling with inner shadows.
"""

import pygame
from .styles import RGB_COLORS, PIXEL_BORDER_WIDTH


class PixelBox:
    """
    A container that renders with pixel art styling including:
    - 4px black border
    - Inset shadows (dark top-left, light bottom-right)
    """
    
    def __init__(self, x, y, width, height, background_color='panel_bg'):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = RGB_COLORS[background_color]
        self.border_color = RGB_COLORS['border_black']
        self.shadow_dark = RGB_COLORS['shadow_dark']
        self.shadow_light = RGB_COLORS['shadow_light']
    
    def draw(self, surface):
        """Draw the pixel box with borders and inner shadows."""
        # Fill background
        pygame.draw.rect(surface, self.background_color, self.rect)
        
        # Draw 4px black border
        pygame.draw.rect(surface, self.border_color, self.rect, PIXEL_BORDER_WIDTH)
        
        # Draw inner shadows (inset effect)
        # Dark shadow on top and left (inset top-left)
        inner_rect = self.rect.inflate(-PIXEL_BORDER_WIDTH * 2, -PIXEL_BORDER_WIDTH * 2)
        
        # Top shadow (dark)
        top_shadow = pygame.Rect(
            inner_rect.left, 
            inner_rect.top, 
            inner_rect.width, 
            PIXEL_BORDER_WIDTH
        )
        pygame.draw.rect(surface, self.shadow_dark, top_shadow)
        
        # Left shadow (dark)
        left_shadow = pygame.Rect(
            inner_rect.left, 
            inner_rect.top, 
            PIXEL_BORDER_WIDTH, 
            inner_rect.height
        )
        pygame.draw.rect(surface, self.shadow_dark, left_shadow)
        
        # Bottom shadow (light)
        bottom_shadow = pygame.Rect(
            inner_rect.left, 
            inner_rect.bottom - PIXEL_BORDER_WIDTH, 
            inner_rect.width, 
            PIXEL_BORDER_WIDTH
        )
        pygame.draw.rect(surface, self.shadow_light, bottom_shadow)
        
        # Right shadow (light)
        right_shadow = pygame.Rect(
            inner_rect.right - PIXEL_BORDER_WIDTH, 
            inner_rect.top, 
            PIXEL_BORDER_WIDTH, 
            inner_rect.height
        )
        pygame.draw.rect(surface, self.shadow_light, right_shadow)
    
    def get_content_rect(self):
        """Get the inner rectangle for content placement."""
        return self.rect.inflate(-PIXEL_BORDER_WIDTH * 4, -PIXEL_BORDER_WIDTH * 4)