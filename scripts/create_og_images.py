from PIL import Image, ImageDraw, ImageFont
import os

def generate_og_image(width, height, output_path):
    # --- Configuration ---
    TITLE_COLOR = "#f0f6fc"

    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths are relative to the script's location
    FONT_PATH = os.path.join(script_dir, "..", "fonts", "BalooTamma2-Regular.ttf")
    AVATAR_PATH = os.path.join(script_dir, "..", "images", "avatars", "dracoboost.png")
    HEADER_PATH = os.path.join(script_dir, "..", "website", "public", "images", "headers", "maliss.png")

    # Output path is relative to the project root, so we construct it differently
    project_root = os.path.join(script_dir, "..")
    absolute_output_path = os.path.join(project_root, output_path)
    OUTPUT_DIR = os.path.dirname(absolute_output_path)

    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- Create Base Image (Background) ---
    header_img = Image.open(HEADER_PATH).convert("RGBA")

    # Aspect-ratio-preserving resize (cover)
    src_width, src_height = header_img.size
    dst_width, dst_height = width, height
    src_ratio = src_width / src_height
    dst_ratio = dst_width / dst_height

    if src_ratio > dst_ratio:
        # Fit to height, crop width
        new_height = dst_height
        new_width = int(new_height * src_ratio)
        resized_img = header_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        left = (new_width - dst_width) // 2 + new_width * 0.08  # Shift left by 8% of new width
        image = resized_img.crop((left, 0, left + dst_width, dst_height))
    else:
        # Fit to width, crop height
        new_width = dst_width
        new_height = int(new_width / src_ratio)
        resized_img = header_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        top = (new_height - dst_height) // 2
        image = resized_img.crop((0, top, dst_width, top + dst_height))

    # --- Load Assets ---
    avatar_img = Image.open(AVATAR_PATH).convert("RGBA")
    try:
        title_font = ImageFont.truetype(FONT_PATH, 80)
    except IOError:
        print(f"Font not found at {FONT_PATH}. Using default font.")
        title_font = ImageFont.load_default(size=80)

    # --- Add Shadow Overlay ---
    shadow_height = int(height * 0.5)  # Cover bottom 50%
    shadow = Image.new("RGBA", (width, shadow_height), (0, 0, 0, 0))
    draw_shadow = ImageDraw.Draw(shadow)

    for i in range(shadow_height):
        alpha = int(180 * (i / shadow_height))  # Gradient from 0 to 180
        draw_shadow.line([(0, i), (width, i)], fill=(0, 0, 0, alpha))

    # Paste the shadow on the bottom half of the image
    image.paste(shadow, (0, height - shadow_height), shadow)

    # --- Paste Avatar (Center Middle) ---
    avatar_size = 256
    avatar_img = avatar_img.resize((avatar_size, avatar_size), Image.Resampling.LANCZOS)
    avatar_x = (width - avatar_size) // 2
    avatar_y = (height - avatar_size) // 2
    image.paste(avatar_img, (avatar_x, avatar_y), avatar_img)

    # --- Draw Text ---
    draw = ImageDraw.Draw(image)
    title_text = "dracoboost's Blog"

    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]

    title_x = (width - title_width) // 2
    title_y = avatar_y + avatar_size + 20

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
