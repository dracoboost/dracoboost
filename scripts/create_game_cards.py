#!/usr/bin/env python
import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw


def create_circular_mask(size):
    """Create a circular mask of a given size."""
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    return mask


def apply_circular_mask(image):
    """Apply a circular mask to an image."""
    size = min(image.size)
    mask = create_circular_mask((size, size))
    # Resize mask to image size if image is not a square
    if image.size != (size, size):
        mask = mask.resize(image.size, Image.Resampling.LANCZOS)

    output = image.copy()
    output.putalpha(mask)
    return output


def get_image(path_or_url):
    """Fetches an image from a URL or opens it from a local path."""
    if path_or_url.startswith("http"):
        try:
            response = requests.get(path_or_url)
            response.raise_for_status()
            # Use BytesIO to handle the image data in memory
            return Image.open(BytesIO(response.content))
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image from {path_or_url}: {e}")
            return None
    else:
        try:
            return Image.open(path_or_url)
        except FileNotFoundError:
            print(f"Error: Base image not found at {path_or_url}")
            return None


def create_card(card_name, base_image_path, platforms, output_dir):
    """
    Creates a card by overlaying a platform icon in a colored triangle
    on a base image.
    """
    base_image = get_image(base_image_path)
    if not base_image:
        return

    base_image = base_image.convert("RGBA")

    if platforms:
        platform = platforms[0]  # Use the first platform

        color = None
        if platform == "nintendo-switch":
            # ff0a17
            color = (255, 10, 23, 255)  # Nintendo Red
        elif platform == "steam":
            # 1b4c7a
            color = (27, 76, 122, 255)  # Steam Blue

        icon_path = os.path.join("images/games/platforms", f"{platform}.png")

        if color and os.path.exists(icon_path):
            draw = ImageDraw.Draw(base_image)

            # Define triangle geometry in the bottom-right corner
            triangle_size = int(base_image.height * 0.27)
            triangle_vertices = [
                (base_image.width, base_image.height),
                (base_image.width - triangle_size, base_image.height),
                (base_image.width, base_image.height - triangle_size),
            ]
            draw.polygon(triangle_vertices, fill=color)

            # Load icon
            icon = Image.open(icon_path).convert("RGBA")

            # Apply circular mask for Steam icon
            if platform == "steam":
                icon = apply_circular_mask(icon)

            # Resize icon to fit inside the triangle
            icon_size = int(triangle_size * 0.42)
            icon = icon.resize((icon_size, icon_size), Image.Resampling.LANCZOS)

            # Position icon with padding from the corner
            padding = int(triangle_size * 0.08)
            position = (
                base_image.width - icon_size - padding,
                base_image.height - icon_size - padding,
            )

            base_image.paste(icon, position, icon)
        else:
            if not color:
                print(f"Warning: Unknown platform '{platform}'. No icon will be added.")
            else:  # icon file not found
                print(f"Warning: Platform icon not found for {platform} at {icon_path}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{card_name}.jpg")
    base_image.convert("RGB").save(output_path, "jpeg")
    print(f"Successfully created card: {output_path}")


GAMES_TO_GENERATE = [
    {
        "card_name": "metaphor-refantazio",
        "base_image_path": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2679460/header.jpg",
        "platforms": ["steam"],
    },
    {
        "card_name": "yugioh-master-duel",
        "base_image_path": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1449850/header.jpg",
        "platforms": ["steam"],
    },
    {
        "card_name": "shadowverse-worlds-beyond",
        "base_image_path": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2584990/header_japanese.jpg",
        "platforms": ["steam"],
    },
    {
        "card_name": "tales-of-arise",
        "base_image_path": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/740130/header.jpg",
        "platforms": ["steam"],
    },
    {
        "card_name": "undertale",
        "base_image_path": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/391540/header.jpg",
        "platforms": ["steam"],
    },
    {
        "card_name": "zelda-botw",
        "base_image_path": "images/games/nintendo_switch/the-legend-of-zelda_breath-of-the-wild.webp",
        "platforms": ["nintendo-switch"],
    },
    {
        "card_name": "romancing-saga-2-revenge-of-the-seven",
        "base_image_path": "images/games/nintendo_switch/romancing-saga-2_revenge-of-the-seven.jpg",
        "platforms": ["nintendo-switch"],
    },
    {
        "card_name": "octopath-traveler-2",
        "base_image_path": "images/games/nintendo_switch/octopath-traveler-ii.jpg",
        "platforms": ["nintendo-switch"],
    },
]


if __name__ == "__main__":
    output_dir = "images/games/cards"
    print("Starting card generation...")
    for game in GAMES_TO_GENERATE:
        print(f"Generating card for {game['card_name']}...")
        create_card(
            game["card_name"],
            game["base_image_path"],
            game["platforms"],
            output_dir
        )
    print("Card generation finished.")
