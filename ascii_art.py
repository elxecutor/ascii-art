# ascii_art.py

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import argparse
import os

# Japanese characters (dark to light)
JAPANESE_CHARS = "鬱霊愛夢福嵐龍鳥魚星空花雪日月木水火土川山口目耳手足心人入大中小上下左右一二三四五六七八九十あいえうおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"[::-1]

def map_pixel_to_ascii(brightness, gamma=0.8):
    adjusted = (brightness / 255)
    index = int(adjusted * (len(JAPANESE_CHARS) - 1))
    return JAPANESE_CHARS[index]

def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height), resample=Image.LANCZOS)

def image_to_ascii_color(image, width, signature=None):
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    image = resize_image(image, new_width=width)
    image = image.convert("RGB")
    pixels = np.array(image)

    ascii_pixels = []
    for row in pixels:
        ascii_row = []
        for r, g, b in row:
            brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
            char = map_pixel_to_ascii(brightness)
            ascii_row.append((char, (r, g, b)))
        ascii_pixels.append(ascii_row)

    if signature:
        last_row = ascii_pixels[-1]
        row_len = len(last_row)
        sig_len = min(len(signature), row_len)
        start = row_len - sig_len
        for i, c in enumerate(signature[-sig_len:]):
            last_row[start + i] = (c, (255, 255, 255))

    return ascii_pixels, image

def ascii_to_image(ascii_pixels, font_path, font_size, bg_color=(0, 0, 0)):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Use dummy draw to measure character size
    dummy_img = Image.new("RGB", (100, 100))
    dummy_draw = ImageDraw.Draw(dummy_img)

    test_char = "あ"
    bbox = dummy_draw.textbbox((0, 0), test_char, font=font)
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]

    img_width = int(len(ascii_pixels[0]) * char_width)
    img_height = int(len(ascii_pixels) * char_height)

    image = Image.new("RGB", (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(ascii_pixels):
        for x, (char, color) in enumerate(row):
            draw.text((x * char_width, y * char_height), char, fill=color, font=font)

    return image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="High-quality Japanese ASCII art generator.")
    parser.add_argument("input_path", help="Input image file path")
    parser.add_argument("output_path", help="Output image file path")
    parser.add_argument("-s", "--signature", default="＠レダクト", help="Signature text")
    parser.add_argument("-f", "--font_size", type=int, default=18, help="Font size (default: 18)")
    parser.add_argument("-p", "--font_path", default="fonts/NotoSansMonoCJKjp-Regular.otf", help="Font path")
    parser.add_argument("-w", "--width", type=int, default=200, help="ASCII width (default: 200)")

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        raise FileNotFoundError(f"Input file not found: {args.input_path}")

    img = Image.open(args.input_path)

    ascii_pixels, processed_img = image_to_ascii_color(img, width=args.width, signature=args.signature)

    final_img = ascii_to_image(ascii_pixels, font_path=args.font_path, font_size=args.font_size)
    final_img.save(args.output_path)

    print(f"✅ Saved high-quality Japanese ASCII art to: {args.output_path}")
