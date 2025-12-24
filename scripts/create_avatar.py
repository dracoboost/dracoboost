#!/usr/bin/env python

import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw

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

def apply_circular_mask(image):
    """Applies a circular mask to an image, making the outside transparent."""
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    output = image.copy()
    output.putalpha(mask)
    return output


def main():
    """
    Downloads an avatar, resizes it, makes it circular,
    and saves it as a PNG.
    """
    avatar_url = "https://avatars.githubusercontent.com/u/212660489?v=4"
    size = (480, 480)

    print(f"Downloading avatar from {avatar_url}...")
    avatar = get_image(avatar_url)

    if not avatar:
        return

    # Convert to RGBA for transparency
    avatar = avatar.convert("RGBA")

    print(f"Resizing avatar to {size[0]}x{size[1]}...")
    avatar = avatar.resize(size, Image.Resampling.LANCZOS)

    print("Applying circular crop...")
    circular_avatar = apply_circular_mask(avatar)

    output_dir = "github_profile/images/avatars"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = "dracoboost.png"
    output_path = os.path.join(output_dir, output_filename)
    print(f"Saving circular avatar to {output_path}...")
    circular_avatar.save(output_path, "png")
    print("Successfully created circular avatar.")


if __name__ == "__main__":
    main()
