# ascii_art.py - Authentic DB32 Pixel Art Generator
# Converts images to authentic pixel art using DB32 palette with proper downscaling

from PIL import Image, ImageDraw
import argparse
import os

# Official DB32 palette (32 colors) - DawnBringer's 32 color palette
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

def nearest_db32_color(rgb):
    """Find the closest color in the DB32 palette using Euclidean distance."""
    r, g, b = rgb
    return min(DB32, key=lambda c: (r - c[0])**2 + (g - c[1])**2 + (b - c[2])**2)

def downscale_for_pixel_art(image, max_size=128):
    """Downscale image to pixel art resolution with nearest-neighbor (no anti-aliasing)."""
    width, height = image.size
    
    # Calculate new size keeping aspect ratio, max 128px on longer edge
    if width > height:
        if width > max_size:
            new_width = max_size
            new_height = int((height * max_size) / width)
        else:
            new_width, new_height = width, height
    else:
        if height > max_size:
            new_height = max_size
            new_width = int((width * max_size) / height)
        else:
            new_width, new_height = width, height
    
    # Use NEAREST filter for crisp, blocky pixels (no anti-aliasing)
    return image.resize((new_width, new_height), Image.NEAREST)

def quantize_to_db32(image):
    """Quantize image to exact DB32 palette without dithering."""
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Create a new image with exact DB32 colors
    width, height = image.size
    quantized = Image.new('RGB', (width, height))
    pixels = quantized.load()
    
    # Map each pixel to nearest DB32 color
    for y in range(height):
        for x in range(width):
            original_color = image.getpixel((x, y))
            db32_color = nearest_db32_color(original_color)
            pixels[x, y] = db32_color
    
    return quantized

def create_authentic_pixel_art(image, scale_factor=1, add_border=True, border_size=20):
    """Create authentic pixel art with DB32 palette, proper downscaling and optional border."""
    
    # Step 1: Downscale to pixel art resolution using nearest-neighbor
    pixel_art = downscale_for_pixel_art(image, max_size=128)
    
    # Step 2: Quantize to exact DB32 palette (no dithering)
    pixel_art = quantize_to_db32(pixel_art)
    
    # Step 3: Scale up by scale_factor to make pixels visible (nearest-neighbor to keep crisp edges)
    if scale_factor > 1:
        width, height = pixel_art.size
        pixel_art = pixel_art.resize((width * scale_factor, height * scale_factor), Image.NEAREST)

    
    # Step 4: Add border if requested
    if add_border:
        width, height = pixel_art.size
        # Create new image with border
        bordered_width = width + (border_size * 2)
        bordered_height = height + (border_size * 2)
        bordered_img = Image.new('RGB', (bordered_width, bordered_height), nearest_db32_color((0, 0, 0)))
        
        # Paste the pixel art in center
        bordered_img.paste(pixel_art, (border_size, border_size))
        
        # Draw decorative border using DB32 colors
        border_draw = ImageDraw.Draw(bordered_img)
        
        # Outer border - Dark gray from DB32
        outer_color = nearest_db32_color((89, 86, 82))
        border_draw.rectangle([0, 0, bordered_width-1, bordered_height-1], outline=outer_color, width=4)
        
        # Middle border - Medium gray
        middle_color = nearest_db32_color((132, 126, 135))
        border_draw.rectangle([4, 4, bordered_width-5, bordered_height-5], outline=middle_color, width=3)
        
        # Inner border - DB32 accent color (orange)
        accent_color = nearest_db32_color((223, 113, 38))
        border_draw.rectangle([8, 8, bordered_width-9, bordered_height-9], outline=accent_color, width=2)
        
        # Innermost border - Light color
        inner_color = nearest_db32_color((155, 173, 183))
        border_draw.rectangle([12, 12, bordered_width-13, bordered_height-13], outline=inner_color, width=1)
        
        return bordered_img
    
    return pixel_art

def create_db32_pixel_art(input_path, output_path, **kwargs):
    """Create authentic pixel art using DB32 palette with proper downscaling."""
    
    # Load original image
    original = Image.open(input_path).convert("RGB")
    
    # Create authentic pixel art
    result = create_authentic_pixel_art(
        original, 
        scale_factor=kwargs.get('scale_factor', 4),
        add_border=kwargs.get('add_border', True),
        border_size=kwargs.get('border_size', 20)
    )
    
    result.save(output_path)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authentic DB32 Pixel Art Generator - Creates pixel art using DawnBringer's 32 color palette")
    parser.add_argument("input_path", help="Input image path")
    parser.add_argument("output_path", help="Output image path (PNG recommended)")
    
    # Pixel art options
    parser.add_argument("-s", "--scale_factor", type=int, default=4, 
                       help="Scale factor for final output (default: 4x)")
    parser.add_argument("--max_size", type=int, default=128,
                       help="Maximum size for longer edge before scaling (default: 128px)")
    parser.add_argument("--border_size", type=int, default=20,
                       help="Border thickness in pixels (default: 20)")
    parser.add_argument("--no-border", action="store_true",
                       help="Disable decorative border")

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        raise FileNotFoundError(f"❌ File not found: {args.input_path}")

    # Prepare options
    options = {
        'scale_factor': args.scale_factor,
        'border_size': args.border_size,
        'add_border': not args.no_border
    }

    # Generate the pixel art
    print(f"🎨 Creating authentic pixel art with DB32 palette...")
    print(f"📐 Downscaling to max {args.max_size}px, then scaling by {args.scale_factor}x")
    result = create_db32_pixel_art(args.input_path, args.output_path, **options)
    
    print(f"✅ DB32 pixel art saved to: {args.output_path}")
    print(f"🎯 Using DawnBringer's 32 color palette with {len(DB32)} colors")
    print(f"🖼️  Scaling: {args.scale_factor}x, Border: {'Yes' if options['add_border'] else 'No'}")
    if options['add_border']:
        print(f"🎨 Border size: {args.border_size}px with multi-layer DB32 colored borders")
    print("✨ Features: Nearest-neighbor scaling, No anti-aliasing, No dithering, Crisp pixels")
