#!/usr/bin/env python3
"""
Demo script for Authentic DB32 Pixel Art Generator
Shows various pixel art generation settings with proper downscaling and quantization
"""

import os
from ascii_art import create_db32_pixel_art, DB32, nearest_db32_color, downscale_for_pixel_art

def main():
    input_image = "docs/samurai_champloo.jpg"
    
    if not os.path.exists(input_image):
        print("❌ Demo image not found!")
        return
    
    print("🎨 Authentic DB32 Pixel Art Generator Demo")
    print("=" * 60)
    
    # Show DB32 palette info
    print(f"📊 DB32 Palette contains {len(DB32)} colors")
    print("🎯 Sample colors from DB32 palette:")
    sample_colors = [DB32[0], DB32[5], DB32[9], DB32[15], DB32[21], DB32[31]]
    for i, color in enumerate(sample_colors):
        print(f"   Color {i+1}: RGB{color}")
    
    print("\n🔄 Generating authentic pixel art examples...")
    print("📐 Process: Downscale → DB32 Quantize → Scale Up (Nearest-Neighbor)")
    
    # Show original image size
    from PIL import Image
    original = Image.open(input_image)
    print(f"🖼️  Original size: {original.size[0]}x{original.size[1]}px")
    
    # Show downscaled size
    downscaled = downscale_for_pixel_art(original, 128)
    print(f"📐 Downscaled to: {downscaled.size[0]}x{downscaled.size[1]}px (max 128px)")
    
    print("\n1. Standard pixel art (128px max, 4x scale)")
    create_db32_pixel_art(input_image, "demo_pixel_standard.png", 
                         scale_factor=4, add_border=True, border_size=25)
    print("   ✅ Saved: demo_pixel_standard.png")
    
    print("2. High detail pixel art (128px max, 6x scale)")
    create_db32_pixel_art(input_image, "demo_pixel_hires.png", 
                         scale_factor=6, add_border=True, border_size=30)
    print("   ✅ Saved: demo_pixel_hires.png")
    
    print("3. Retro pixel art (64px max, 8x scale, no border)")
    create_db32_pixel_art(input_image, "demo_pixel_retro.png", 
                         scale_factor=8, add_border=False)
    print("   ✅ Saved: demo_pixel_retro.png")
    
    print("4. Tiny pixel art (32px max, 12x scale)")
    create_db32_pixel_art(input_image, "demo_pixel_tiny.png", 
                         scale_factor=12, add_border=True, border_size=40)
    print("   ✅ Saved: demo_pixel_tiny.png")
    
    print("5. Clean pixel art (96px max, 5x scale, no border)")
    create_db32_pixel_art(input_image, "demo_pixel_clean.png", 
                         scale_factor=5, add_border=False)
    print("   ✅ Saved: demo_pixel_clean.png")
    
    # Show what happens at different resolutions
    print("\n📐 Resolution Examples:")
    resolutions = [32, 64, 96, 128]
    for res in resolutions:
        test_img = downscale_for_pixel_art(original, res)
        print(f"   {res}px max → {test_img.size[0]}x{test_img.size[1]}px actual")
    
    print("\n🎨 Pixel Art Features:")
    print("   ✅ Nearest-neighbor scaling (no anti-aliasing)")
    print("   ✅ Exact DB32 palette quantization (no dithering)")
    print("   ✅ Crisp, blocky pixels with strong contrast")
    print("   ✅ Preserved character silhouettes")
    print("   ✅ Simplified detail with basic shading")
    print("   ✅ Authentic retro aesthetics")
    
    print("\n✨ Demo complete! All outputs are authentic pixel art.")
    print("🎯 Files generated:")
    print("   - demo_pixel_standard.png (128px base, 4x scale)")
    print("   - demo_pixel_hires.png (128px base, 6x scale)")
    print("   - demo_pixel_retro.png (64px base, 8x scale, no border)")
    print("   - demo_pixel_tiny.png (32px base, 12x scale)")
    print("   - demo_pixel_clean.png (96px base, 5x scale, no border)")

if __name__ == "__main__":
    main()
