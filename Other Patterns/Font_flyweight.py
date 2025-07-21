from typing import Dict

# Flyweight Interface
class FontFlyweight:
    def render_text(self, text):
        pass

# Concrete Flyweight
class ConcreteFontFlyweight(FontFlyweight):
    def __init__(self, font_name, font_size):
        self.font_name = font_name
        self.font_size = font_size

    def render_text(self, text):
        print(f"Rendering '{text}' with {self.font_name}, size {self.font_size}")

# Flyweight Factory
class FontFlyweightFactory:
    def __init__(self):
        self.fonts: Dict[str, FontFlyweight] = {}

    def get_font(self, font_name, font_size):
        key = f"{font_name}_{font_size}"
        if key not in self.fonts:
            self.fonts[key] = ConcreteFontFlyweight(font_name, font_size)
        return self.fonts[key]

# Client Code (Text Editor)
class TextEditor:
    def __init__(self, font_factory):
        self.font_factory = font_factory

    def set_text(self, text, font_name, font_size):
        font = self.font_factory.get_font(font_name, font_size)
        font.render_text(text)

# Application
if __name__ == "__main__":
    font_factory = FontFlyweightFactory()

    editor = TextEditor(font_factory)
    editor.set_text("Hello, World!", "Arial", 12)

    another_editor = TextEditor(font_factory)
    another_editor.set_text("Flyweight Pattern", "Arial", 12)
