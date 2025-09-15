"""
Button component with pixel art styling and interaction handling.
"""

import pygame
from .styles import RGB_COLORS, PIXEL_BORDER_WIDTH, BUTTON_HEIGHT


class Button:
    """
    A button with pixel art styling that supports:
    - Primary and secondary themes with custom shadows
    - Press effects (visual feedback)
    - Mouse and keyboard interaction
    """
    
    def __init__(self, x, y, width, text, button_type='primary', font=None):
        self.rect = pygame.Rect(x, y, width, BUTTON_HEIGHT)
        self.original_rect = self.rect.copy()
        self.text = text
        self.button_type = button_type
        self.font = font
        self.pressed = False
        self.focused = False
        
        # Set colors based on button type
        if button_type == 'primary':
            self.bg_color = RGB_COLORS['button_primary']
            self.shadow_dark = RGB_COLORS['button_primary_shadow_dark']
            self.shadow_light = RGB_COLORS['button_primary_shadow_light']
        else:  # secondary
            self.bg_color = RGB_COLORS['button_secondary']
            self.shadow_dark = RGB_COLORS['button_secondary_shadow_dark']
            self.shadow_light = RGB_COLORS['button_secondary_shadow_light']
        
        self.border_color = RGB_COLORS['border_black']
        self.text_color = RGB_COLORS['text_white']
    
    def handle_event(self, event):
        """Handle mouse events for button interaction."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.pressed = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.pressed:
                self.pressed = False
                if self.rect.collidepoint(event.pos):
                    return 'clicked'
        return False
    
    def set_focus(self, focused):
        """Set keyboard focus state."""
        self.focused = focused
    
    def activate(self):
        """Activate button (for keyboard interaction)."""
        return 'clicked'
    
    def draw(self, surface):
        """Draw the button with pixel art styling."""
        # Apply press effect (slight offset)
        draw_rect = self.rect.copy()
        if self.pressed:
            draw_rect.y += 2
        
        # Fill background
        pygame.draw.rect(surface, self.bg_color, draw_rect)
        
        # Draw 4px black border
        pygame.draw.rect(surface, self.border_color, draw_rect, PIXEL_BORDER_WIDTH)
        
        # Draw inner shadows (inset effect)
        inner_rect = draw_rect.inflate(-PIXEL_BORDER_WIDTH * 2, -PIXEL_BORDER_WIDTH * 2)
        
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
        
        # Draw focus indicator if focused
        if self.focused:
            focus_rect = draw_rect.inflate(4, 4)
            pygame.draw.rect(surface, RGB_COLORS['text_white'], focus_rect, 2)
        
        # Draw text
        if self.font and self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=draw_rect.center)
            if self.pressed:
                text_rect.y += 2
            surface.blit(text_surface, text_rect)