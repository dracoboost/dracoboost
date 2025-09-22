#!/usr/bin/env python

import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def get_image(path_or_url):
    """Fetches an image from a URL or opens it from a local path."""
    if path_or_url.startswith("http"):
        try:
            response = requests.get(path_or_url)
            response.raise_for_status()
            return Image.open(BytesIO(response.content))
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image from {path_or_url}: {e}")
            return None
    else:
        try:
            return Image.open(path_or_url)
        except FileNotFoundError:
            print(f"Error: Image not found at {path_or_url}")
            return None


def create_hohatch_card(base_image_path, font_path, output_path):
    """
    Creates a card for HoHatch with a shadow and text overlay.
    """
    base_image = get_image(base_image_path)
    if not base_image:
        return

    base_image = base_image.convert("RGBA")
    base_image_width, base_image_height = base_image.size

    # Create a black shadow overlay
    shadow_height = int(base_image_height * 0.4)
    shadow = Image.new("RGBA", (base_image_width, shadow_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)

    for i in range(shadow_height):
        alpha = int(180 * (i / shadow_height))  # Gradient from 0 to 180
        draw.line([(0, i), (base_image_width, i)], fill=(0, 0, 0, alpha))

    base_image.paste(shadow, (0, base_image_height - shadow_height), shadow)

    # Add text
    draw = ImageDraw.Draw(base_image)
    try:
        title_font = ImageFont.truetype(font_path, size=72)
        subtitle_font = ImageFont.truetype(font_path, size=24)
    except IOError:
        print(f"Font not found at {font_path}. Using default font.")
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Title
    title_text = "HoHatch"
    title_width, title_height = draw.textbbox((0, 0), title_text, font=title_font)[2:4]
    title_x = (base_image_width - title_width) / 2
    title_y = base_image_height - shadow_height + 64
    draw.text((title_x, title_y), title_text, font=title_font, fill=(255, 255, 255, 255))

    # Subtitle
    subtitle_text = "Streamline Shadowverse: Worlds Beyond Modding"
    subtitle_width = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)[2]
    subtitle_x = (base_image_width - subtitle_width) / 2
    subtitle_y = title_y + title_height + 16
    draw.text((subtitle_x, subtitle_y), subtitle_text, font=subtitle_font, fill=(255, 255, 255, 220))

    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_image.convert("RGB").save(output_path, "jpeg")
    print(f"Successfully created card: {output_path}")


def download_font(font_url, font_path):
    """Downloads the font if it doesn't exist."""
    font_dir = os.path.dirname(font_path)
    if not os.path.exists(font_dir):
        os.makedirs(font_dir)

    if not os.path.exists(font_path):
        print(f"Downloading font from {font_url}...")
        try:
            response = requests.get(font_url)
            response.raise_for_status()
            with open(font_path, "wb") as f:
                f.write(response.content)
            print(f"Successfully downloaded font to {font_path}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading font: {e}")
            return False
    return True


def main():
    """Main function to generate the HoHatch card."""
    base_image = "images/hohatch/hohatch-application-screenshot.jpg"
    font_url = "https://github.com/EkType/Baloo2-Variable/raw/v2.000/fonts/ttf/BalooTamma2-Regular.ttf"
    font_path = "fonts/BalooTamma2-Regular.ttf"
    output_file = "images/cards/hohatch-application-screenshot.jpg"

    if not download_font(font_url, font_path):
        return

    print("Starting HoHatch card generation...")
    create_hohatch_card(base_image, font_path, output_file)
    print("HoHatch card generation finished.")


if __name__ == "__main__":
    main()
