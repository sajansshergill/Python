'''
Create a Python script that generates an image with a random programming joke (from pyjokes) 
overlaid on a visually appealing background using Pillow. The generated image can be shared on social media, 
set as a wallpaper, or emailed as a daily fun reminder. Use pyttsx to read the joke.

'''
import pyjokes
import pyttsx3
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from datetime import datetime

# ==== CONFIGURATION ====
WIDTH, HEIGHT = 1080, 1080
FONT_SIZE = 36
TEXT_COLOR = (255, 255, 255)
OUTPUT_DIR = "daily_jokes"
BG_GRADIENT_START = (58, 123, 213)  # Deep blue
BG_GRADIENT_END = (58, 213, 164)    # Light green

# ==== GET RANDOM JOKE ====
try:
    joke = pyjokes.get_joke(category="programming")
except Exception:
    joke = pyjokes.get_joke(category="neutral")

wrapped_joke = textwrap.fill(joke, width=40)

# ==== SPEAK JOKE ALOUD ====
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("Here's your joke of the day!")
engine.say(joke)
engine.runAndWait()

# ==== FUNCTION: CREATE GRADIENT BACKGROUND ====
def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    for y in range(height):
        gradient = int(255 * (y / height))
        for x in range(width):
            mask.putpixel((x, y), gradient)
    return Image.composite(top, base, mask)

# ==== CREATE IMAGE ====
bg_image = create_gradient(WIDTH, HEIGHT, BG_GRADIENT_START, BG_GRADIENT_END)
draw = ImageDraw.Draw(bg_image)

# ==== LOAD FONT ====
try:
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
except IOError:
    font = ImageFont.load_default()

# ==== CENTER TEXT ====
bbox = draw.multiline_textbbox((0, 0), wrapped_joke, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (WIDTH - text_width) / 2
y = (HEIGHT - text_height) / 2

# ==== DRAW TEXT ====
draw.multiline_text((x, y), wrapped_joke, fill=TEXT_COLOR, font=font, align="center")

# ==== SAVE IMAGE ====
os.makedirs(OUTPUT_DIR, exist_ok=True)
filename = f"joke_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
file_path = os.path.join(OUTPUT_DIR, filename)
bg_image.save(file_path)

# ==== DONE ====
print(f"✅ Joke image saved to: {file_path}")
print("🗣️ Joke was spoken aloud successfully.")
