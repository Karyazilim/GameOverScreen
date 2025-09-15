"""
Game Over Screen implementation with pixel art styling.
"""

import os
import sys
import pygame
import requests
from ui import PixelBox, Button, RGB_COLORS
from ui.styles import (
    TITLE_FONT_SIZE, SCORE_FONT_SIZE, BUTTON_FONT_SIZE, 
    CONTENT_MAX_WIDTH, CONTENT_PADDING, BUTTON_HEIGHT
)


class GameOverScreen:
    """Main Game Over screen with pixel art styling and interactions."""
    
    def __init__(self, score=1250):
        pygame.init()
        
        # Initialize display
        self.screen_width = 800
        self.screen_height = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Game Over")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = score
        
        # Load fonts
        self.load_fonts()
        
        # Load or download image
        self.load_image()
        
        # Initialize UI elements
        self.init_ui()
        
        # Keyboard navigation
        self.focused_button = 0
        self.buttons[self.focused_button].set_focus(True)
    
    def load_fonts(self):
        """Load VT323 font for UI text."""
        font_path = os.path.join('assets', 'fonts', 'VT323-Regular.ttf')
        
        try:
            self.title_font = pygame.font.Font(font_path, TITLE_FONT_SIZE)
            self.score_font = pygame.font.Font(font_path, SCORE_FONT_SIZE)
            self.button_font = pygame.font.Font(font_path, BUTTON_FONT_SIZE)
            self.nav_font = pygame.font.Font(font_path, 18)
        except FileNotFoundError:
            print(f"Font not found at {font_path}, using default font")
            self.title_font = pygame.font.Font(None, TITLE_FONT_SIZE)
            self.score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
            self.button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
            self.nav_font = pygame.font.Font(None, 18)
    
    def load_image(self):
        """Load or download the portrait image."""
        image_path = os.path.join('assets', 'images', 'portrait.png')
        
        if not os.path.exists(image_path):
            print("Downloading portrait image...")
            self.download_image(image_path)
        
        try:
            # Load image and scale with nearest neighbor for pixelated effect
            original_image = pygame.image.load(image_path)
            self.portrait_image = original_image
        except (pygame.error, FileNotFoundError):
            print("Failed to load image, creating placeholder")
            self.portrait_image = self.create_placeholder_image()
    
    def download_image(self, image_path):
        """Download the portrait image from the provided URL."""
        image_url = "https://lh3.googleusercontent.com/aida-public/AB6AXuC5qF_O2qZUkZr3_sbkWaBLXn6-FR-ZopNoj4w4VddgZzJ7JLfCuzMfxnpa7MmV0YHhWO64hRwU8CmYAjQTwGs3tlLRmOD4rb3e7alI3V_2deXkbOcevwGVocNRv0Mkh0IjAIbseiwQ5HUHq9EUbChXDWLTYRBiNi3Z4csnNSlkHWhOkMpnoFIjkv9L8oHim4J0uDu87CbZ1F10Y8pGaAWKIsrBgQV9lqqwb3JH3VFeBhrXDD8JnChpVAB34Y_HaOLrGIePREu0-xs"
        
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"Image downloaded to {image_path}")
        except Exception as e:
            print(f"Failed to download image: {e}")
    
    def create_placeholder_image(self):
        """Create a placeholder image if download fails."""
        placeholder = pygame.Surface((200, 200))
        placeholder.fill(RGB_COLORS['button_secondary'])
        
        # Add some simple pattern
        for i in range(0, 200, 20):
            pygame.draw.line(placeholder, RGB_COLORS['text_white'], (i, 0), (i, 200), 2)
            pygame.draw.line(placeholder, RGB_COLORS['text_white'], (0, i), (200, i), 2)
        
        return placeholder
    
    def init_ui(self):
        """Initialize UI elements with proper positioning."""
        self.update_layout()
    
    def update_layout(self):
        """Update layout based on current screen size."""
        # Calculate scale factor based on screen height, clamped to reasonable bounds
        scale_factor = max(0.8, min(2.0, self.screen_height / 900))
        
        # Content area
        content_width = min(CONTENT_MAX_WIDTH * scale_factor, self.screen_width - 40)
        content_x = (self.screen_width - content_width) // 2
        
        # Title position
        self.title_y = 60 * scale_factor
        
        # Image panel
        image_size = int(content_width - CONTENT_PADDING * 2)
        image_x = content_x
        image_y = int(self.title_y + 120 * scale_factor)
        
        self.image_panel = PixelBox(image_x, image_y, content_width, image_size + CONTENT_PADDING * 2)
        
        # Scale image to fit the panel with nearest neighbor
        image_content_rect = self.image_panel.get_content_rect()
        image_display_size = min(image_content_rect.width, image_content_rect.height)
        
        self.scaled_image = pygame.transform.scale(
            self.portrait_image, 
            (image_display_size, image_display_size)
        )
        # Apply nearest neighbor scaling for pixelated effect
        if hasattr(pygame.transform, 'scale_by'):
            # For newer pygame versions
            pass  # Use default scaling
        
        self.image_rect = pygame.Rect(
            image_content_rect.x + (image_content_rect.width - image_display_size) // 2,
            image_content_rect.y + (image_content_rect.height - image_display_size) // 2,
            image_display_size,
            image_display_size
        )
        
        # Score panel
        score_y = image_y + image_size + CONTENT_PADDING * 3
        score_height = int(80 * scale_factor)
        self.score_panel = PixelBox(content_x, score_y, content_width, score_height)
        
        # Buttons
        button_y = score_y + score_height + CONTENT_PADDING * 2
        button_height = int(BUTTON_HEIGHT * scale_factor)
        button_spacing = int(16 * scale_factor)
        
        self.restart_button = Button(
            content_x, button_y, content_width, "RESTART", 
            'primary', self.button_font
        )
        
        self.menu_button = Button(
            content_x, button_y + button_height + button_spacing, content_width, "MAIN MENU",
            'secondary', self.button_font
        )
        
        self.buttons = [self.restart_button, self.menu_button]
        
        # Navigation bar
        nav_height = int(80 * scale_factor)
        self.nav_panel = PixelBox(0, self.screen_height - nav_height, self.screen_width, nav_height)
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.VIDEORESIZE:
                self.screen_width = event.w
                self.screen_height = event.h
                self.update_layout()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("main-menu")
                    self.running = False
                
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    # Navigate between buttons
                    self.buttons[self.focused_button].set_focus(False)
                    if event.key == pygame.K_UP:
                        self.focused_button = (self.focused_button - 1) % len(self.buttons)
                    else:
                        self.focused_button = (self.focused_button + 1) % len(self.buttons)
                    self.buttons[self.focused_button].set_focus(True)
                
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    # Activate focused button
                    result = self.buttons[self.focused_button].activate()
                    if result == 'clicked':
                        self.handle_button_click(self.focused_button)
            
            # Handle mouse events for buttons
            for i, button in enumerate(self.buttons):
                result = button.handle_event(event)
                if result == 'clicked':
                    self.handle_button_click(i)
    
    def handle_button_click(self, button_index):
        """Handle button click actions."""
        if button_index == 0:  # Restart button
            print("restart")
        elif button_index == 1:  # Main Menu button
            print("main-menu")
            self.running = False
    
    def draw(self):
        """Draw the entire screen."""
        # Clear screen with background color
        self.screen.fill(RGB_COLORS['background'])
        
        # Draw title
        title_surface = self.title_font.render("GAME OVER", True, RGB_COLORS['text_white'])
        title_rect = title_surface.get_rect(centerx=self.screen_width // 2, y=self.title_y)
        self.screen.blit(title_surface, title_rect)
        
        # Draw image panel
        self.image_panel.draw(self.screen)
        self.screen.blit(self.scaled_image, self.image_rect)
        
        # Draw score panel
        self.score_panel.draw(self.screen)
        score_text = f"SCORE: {self.score}"
        score_surface = self.score_font.render(score_text, True, RGB_COLORS['text_white'])
        score_rect = score_surface.get_rect(center=self.score_panel.get_content_rect().center)
        self.screen.blit(score_surface, score_rect)
        
        # Draw buttons
        for button in self.buttons:
            button.draw(self.screen)
        
        # Draw navigation bar
        self.nav_panel.draw(self.screen)
        nav_content = self.nav_panel.get_content_rect()
        
        # Navigation items
        nav_items = [
            ("Home", RGB_COLORS['text_inactive']),
            ("Play", RGB_COLORS['text_white']),  # Active
            ("Settings", RGB_COLORS['text_inactive'])
        ]
        
        item_width = nav_content.width // len(nav_items)
        for i, (text, color) in enumerate(nav_items):
            text_surface = self.nav_font.render(text, True, color)
            text_rect = text_surface.get_rect(
                centerx=nav_content.x + item_width * i + item_width // 2,
                centery=nav_content.centery
            )
            self.screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == "__main__":
    screen = GameOverScreen()
    screen.run()