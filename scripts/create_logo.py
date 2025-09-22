from PIL import Image, ImageDraw, ImageFont
import os

def generate_logo():
    # --- Configuration ---
    TEXT = "dracoboost's Blog"
    TEXT_COLOR = "#f0f6fc"
    FONT_SIZE = 60
    PADDING = 20

    # --- Paths ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    FONT_PATH = os.path.join(script_dir, "..", "fonts", "BalooTamma2-Regular.ttf")
    output_dir = os.path.join(script_dir, "..", "website", "public", "images", "logos")
    OUTPUT_PATH = os.path.join(output_dir, "dracoboost-blog-logo.png")

    os.makedirs(output_dir, exist_ok=True)

    # --- Font & Text Size ---
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        print(f"Font not found at {FONT_PATH}. Using default font.")
        font = ImageFont.load_default(size=FONT_SIZE)

    # Use a temporary draw object to measure text size
    temp_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    text_bbox = temp_draw.textbbox((0, 0), TEXT, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # --- Create Image ---
    image_width = text_width + PADDING * 2
    image_height = text_height + PADDING * 2
    image = Image.new("RGBA", (image_width, image_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # --- Draw Text ---
    # Adjust drawing position to account for the font's bounding box top value
    draw_y = PADDING - text_bbox[1]
    draw.text((PADDING, draw_y), TEXT, font=font, fill=TEXT_COLOR)

    # --- Save Image ---
    image.save(OUTPUT_PATH)
    print(f"Successfully generated logo at {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_logo()
