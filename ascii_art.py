# ascii_art.py

from PIL import Image
import argparse
import os

# Official DB32 palette (32 colors)
DB32 = [
    (0, 0, 0), (34, 32, 52), (69, 40, 60), (102, 57, 49),
    (143, 86, 59), (223, 113, 38), (217, 160, 102), (238, 195, 154),
    (251, 242, 54), (153, 229, 80), (106, 190, 48), (55, 148, 110),
    (75, 105, 47), (82, 75, 36), (50, 60, 57), (63, 63, 116),
    (48, 96, 130), (91, 110, 225), (99, 155, 255), (95, 205, 228),
    (203, 219, 252), (255, 255, 255), (155, 173, 183), (132, 126, 135),
    (105, 106, 106), (89, 86, 82), (118, 66, 138), (172, 50, 50),
    (217, 87, 99), (215, 123, 186), (143, 151, 74), (138, 111, 48)
]

def nearest_palette_color(rgb):
    """Find the closest color in the restricted palette using Euclidean distance."""
    r, g, b = rgb
    return min(DB32, key=lambda c: (r - c[0])**2 + (g - c[1])**2 + (b - c[2])**2)

def apply_palette_block_style(image, block_size):
    """Apply solid color blocks over an image using the restricted palette."""
    width, height = image.size
    new_width = width // block_size
    new_height = height // block_size

    # Resize for color sampling, then apply palette mapping
    small_img = image.resize((new_width, new_height), Image.BILINEAR).convert("RGB")
    output_img = Image.new("RGB", (width, height))
    draw = output_img.load()

    for y in range(new_height):
        for x in range(new_width):
            original_color = small_img.getpixel((x, y))
            palette_color = nearest_palette_color(original_color)

            for dy in range(block_size):
                for dx in range(block_size):
                    px = x * block_size + dx
                    py = y * block_size + dy
                    if px < width and py < height:
                        draw[px, py] = palette_color

    return output_img

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render image using a restricted 5-color palette with solid color blocks.")
    parser.add_argument("input_path", help="Input image path")
    parser.add_argument("output_path", help="Output image path (PNG recommended)")
    parser.add_argument("-b", "--block_size", type=int, default=4, help="Block size (default: 4 pixels)")

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        raise FileNotFoundError(f"❌ File not found: {args.input_path}")

    original = Image.open(args.input_path).convert("RGB")
    output = apply_palette_block_style(original, block_size=args.block_size)
    output.save(args.output_path)

    print(f"✅ Image saved with restricted palette to: {args.output_path}")
