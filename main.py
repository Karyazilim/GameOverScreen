"""
Main entry point for the Game Over screen demo.
"""

from game_over_screen import GameOverScreen


def main():
    """Launch the Game Over screen with a sample score."""
    try:
        screen = GameOverScreen(score=1250)
        screen.run()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())