from PIL import Image, ImageDraw, ImageFont
import datetime

# Load quotes
with open("quotes.daily", "r") as f:
    quotes = [line.strip() for line in f if line.strip()]

# Pick quote based on day of month
day = datetime.datetime.now().day
quote = quotes[day % len(quotes)]

# Create image
img = Image.new('RGB', (800, 200), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Load font
try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

# Draw text
draw.text((50, 80), quote, font=font, fill=(255, 255, 255))

# Save to docs folder
img.save("docs/dailyquote.png")
