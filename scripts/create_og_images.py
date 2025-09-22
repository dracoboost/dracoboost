from PIL import Image, ImageDraw, ImageFont
import os

def generate_og_image(width, height, output_path):
    # --- Configuration ---
    BG_COLOR = "#0d1117"
    TITLE_COLOR = "#f0f6fc"

    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths are relative to the script's location
    FONT_PATH = os.path.join(script_dir, "..", "fonts", "BalooTamma2-Regular.ttf")
    AVATAR_PATH = os.path.join(script_dir, "..", "website", "public", "images", "avatars", "dracoboost.png")

    # Output path is relative to the project root, so we construct it differently
    project_root = os.path.join(script_dir, "..")
    absolute_output_path = os.path.join(project_root, output_path)
    OUTPUT_DIR = os.path.dirname(absolute_output_path)

    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- Create Base Image ---
    image = Image.new("RGB", (width, height), color=BG_COLOR)
    draw = ImageDraw.Draw(image)

    # --- Load Assets ---
    try:
        title_font = ImageFont.truetype(FONT_PATH, 80)
        subtitle_font = ImageFont.truetype(FONT_PATH, 40)
    except IOError:
        print(f"Font not found at {FONT_PATH}. Using default font.")
        title_font = ImageFont.load_default(size=80)
        subtitle_font = ImageFont.load_default(size=40)

    avatar_img = Image.open(AVATAR_PATH).convert("RGBA")

    # --- Draw Text ---
    title_text = "dracoboost's Blog"

    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]

    avatar_size = 256

    # Recalculate vertical positioning for centering
    content_height = avatar_size + 40 + title_height
    y_offset = (height - content_height) // 2

    avatar_y = y_offset
    image.paste(avatar_img, ((width - avatar_size) // 2, avatar_y), avatar_img)

    title_x = (width - title_width) // 2
    title_y = avatar_y + avatar_size + 40

    draw.text((title_x, title_y), title_text, font=title_font, fill=TITLE_COLOR)

    # --- Save Image ---
    image.save(absolute_output_path)
    print(f"Successfully generated {absolute_output_path}")

if __name__ == "__main__":
    # Define output paths relative to the project root
    output_path_600 = os.path.join("website", "public", "images", "og", "dracoboost-og-1200x600.png")
    output_path_630 = os.path.join("website", "public", "images", "og", "dracoboost-og-1200x630.png")

    generate_og_image(1200, 600, output_path_600)
    generate_og_image(1200, 630, output_path_630)
