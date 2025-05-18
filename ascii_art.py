# ascii_art.py

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import argparse

# Extended ASCII character set based on brightness
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

def map_pixel_to_ascii(brightness):
    scale = len(ASCII_CHARS)
    return ASCII_CHARS[int((brightness / 255) * (scale - 1))]

def resize_image(image, new_width=200):  # Increased width for better detail
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def image_to_ascii_color(image, signature=None):
    image = resize_image(image, new_width=args.width)
    image = image.convert("RGB")
    pixels = np.array(image)

    ascii_pixels = []
    for row in pixels:
        ascii_row = []
        for pixel in row:
            r, g, b = pixel
            brightness = int(0.299*r + 0.587*g + 0.114*b)
            char = map_pixel_to_ascii(brightness)
            ascii_row.append((char, (r, g, b)))
        ascii_pixels.append(ascii_row)

    # Insert signature on bottom-right of last row
    if signature:
        last_row = ascii_pixels[-1]
        row_len = len(last_row)
        sig_len = min(len(signature), row_len)
        start = row_len - sig_len
        for i, c in enumerate(signature[-sig_len:]):
            last_row[start + i] = (c, (255, 255, 255))  # white signature

    return ascii_pixels

def ascii_to_image(ascii_pixels, font_path="DejaVuSansMono.ttf", font_size=12, bg_color=(0, 0, 0)):
    char_width = font_size * 0.6
    char_height = font_size

    img_width = int(len(ascii_pixels[0]) * char_width)
    img_height = int(len(ascii_pixels) * char_height)

    image = Image.new("RGB", (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    for y, row in enumerate(ascii_pixels):
        for x, (char, color) in enumerate(row):
            draw.text((x * char_width, y * char_height), char, fill=color, font=font)

    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to colored ASCII art.")
    parser.add_argument("input_path", help="Input image file path")
    parser.add_argument("output_path", help="Output image file path")
    parser.add_argument("-s", "--signature", default="@Retr0", help="Signature text to embed (default: @Retr0)")
    parser.add_argument("-f", "--font_size", type=int, default=12, help="Font size for output image (default: 12)")
    parser.add_argument("-p", "--font_path", default="font/DejaVuSansMono.ttf", help="Path to TTF font file (default: DejaVuSansMono.ttf)")
    parser.add_argument("-w", "--width", type=int, default=200, help="Width to resize image for ASCII (default: 200)")

    args = parser.parse_args()

    img = Image.open(args.input_path)
    ascii_pixels = image_to_ascii_color(img, signature=args.signature)
    ascii_img = ascii_to_image(ascii_pixels, font_path=args.font_path, font_size=args.font_size)
    ascii_img.save(args.output_path)
    print(f"✅ Saved ASCII art with embedded bottom-right signature: {args.output_path}")
