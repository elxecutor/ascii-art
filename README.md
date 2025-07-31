# PixelArt - Authentic DB32 Pixel Art Generator

PixelArt is a specialized tool that converts images to authentic pixel art using the renowned **DB32 (DawnBringer 32) color palette**. This generator creates true pixel art by properly downscaling images and quantizing them to the exact 32-color DB32 palette without dithering or anti-aliasing.

## ✨ Features

### 🎨 **Authentic Pixel Art Process**
- **Proper Downscaling:** Reduces images to pixel art resolution (max 128px on longer edge)
- **Nearest-Neighbor Scaling:** No anti-aliasing for crisp, blocky pixels
- **Exact DB32 Quantization:** Maps all colors to the exact 32-color palette without dithering
- **Character Preservation:** Maintains silhouettes and basic shading while simplifying detail
- **Strong Contrast:** Creates bold, retro-style visuals with authentic pixel art aesthetics

### 🖼️ **Professional Output**
- **Crisp Pixels:** Clean, blocky pixels with no smoothing or blending
- **Scalable Results:** Configurable scale factors for final output size
- **Decorative Borders:** Optional multi-layer borders using DB32 palette colors
- **Multiple Resolutions:** Support for different pixel art scales (32px to 128px base)

### ⚙️ **Customizable Options**
- **Resolution Control:** Set maximum size for pixel art base (default: 128px)
- **Scale Factors:** Choose output scaling (1x to 12x+ for visibility)
- **Border Control:** Enable/disable decorative borders with custom thickness
- **Clean Output:** Option for borderless pixel art

## 🚀 Quick Start

### Basic Pixel Art Generation
```bash
python3 ascii_art.py input_image.jpg output.png
```

### High-Detail Pixel Art (6x scaling)
```bash
python3 ascii_art.py input_image.jpg output.png -s 6
```

### Retro Pixel Art (smaller resolution, larger pixels)
```bash
python3 ascii_art.py input_image.jpg output.png --max_size 64 -s 8
```

### Clean Pixel Art (no border)
```bash
python3 ascii_art.py input_image.jpg output.png --no-border
```

### Run Demo
```bash
python3 demo_pixel_art.py
```

## 📋 Command Line Options

### Basic Usage
```
python3 ascii_art.py INPUT_PATH OUTPUT_PATH [OPTIONS]
```

### Pixel Art Options
- `-s, --scale_factor SCALE_FACTOR` - Scale factor for final output (default: 4x)
- `--max_size MAX_SIZE` - Maximum size for longer edge before scaling (default: 128px)
- `--border_size BORDER_SIZE` - Border thickness in pixels (default: 20)
- `--no-border` - Disable decorative border

### Resolution Examples
- `--max_size 32` - Tiny pixel art (32px max → very chunky pixels)
- `--max_size 64` - Retro pixel art (64px max → classic game style)
- `--max_size 96` - Detailed pixel art (96px max → more detail retained)
- `--max_size 128` - High-detail pixel art (128px max → maximum detail)

## 🎨 Pixel Art Process

The generator follows an authentic pixel art creation process:

### Step 1: Intelligent Downscaling
- **Resolution Targeting:** Reduces to pixel art resolution (32px-128px on longer edge)
- **Aspect Ratio Preservation:** Maintains original proportions
- **Nearest-Neighbor Scaling:** No anti-aliasing for crisp edges

### Step 2: DB32 Palette Quantization  
- **Exact Color Matching:** Each pixel mapped to nearest DB32 color
- **No Dithering:** Pure color blocks for authentic pixel art look
- **Color Preservation:** Character silhouettes and basic shading maintained

### Step 3: Intelligent Upscaling
- **Configurable Scaling:** 1x to 12x+ scale factors
- **Pixel Preservation:** Nearest-neighbor keeps blocky pixel appearance
- **Sharp Output:** No smoothing or blending artifacts

## 🌈 DB32 Color Palette

The tool uses the official **DawnBringer 32** palette - a carefully curated 32-color palette designed for pixel art and retro aesthetics:

- **32 Total Colors:** Black, whites, grays, and vibrant colors
- **Optimized Selection:** Each color chosen for maximum versatility
- **Retro Aesthetic:** Perfect for pixel art, game graphics, and vintage looks
- **Color Harmony:** Colors work well together for cohesive artwork

### Sample DB32 Colors:
- `(0, 0, 0)` - Pure Black
- `(223, 113, 38)` - Vibrant Orange  
- `(153, 229, 80)` - Bright Green
- `(91, 110, 225)` - Electric Blue
- `(255, 255, 255)` - Pure White
- `(172, 50, 50)` - Deep Red

## 📁 Examples

The `docs/` folder contains sample images you can use for testing:

```bash
# Standard pixel art (128px base, 4x scale, with border)
python3 ascii_art.py docs/samurai_champloo.jpg samurai_standard.png

# High-detail pixel art (128px base, 6x scale)
python3 ascii_art.py docs/samurai_champloo.jpg samurai_hires.png -s 6

# Retro pixel art (64px base, 8x scale, no border)
python3 ascii_art.py docs/samurai_champloo.jpg samurai_retro.png --max_size 64 -s 8 --no-border

# Tiny pixel art (32px base, 12x scale)
python3 ascii_art.py docs/samurai_champloo.jpg samurai_tiny.png --max_size 32 -s 12

# Run comprehensive demo
python3 demo_pixel_art.py
```

## 🛠️ Requirements

- Python 3.6+
- PIL (Pillow)

Install dependencies:
```bash
pip install Pillow
```

## 🎯 Authentic Pixel Art Focus

This implementation creates **true pixel art** with authentic characteristics:

- **Proper Resolution:** Downscales to pixel art resolutions (32-128px base)
- **No Anti-Aliasing:** Uses nearest-neighbor scaling exclusively
- **No Dithering:** Pure DB32 color blocks without blending
- **Crisp Pixels:** Blocky, sharp pixels with strong contrast
- **Character Preservation:** Maintains silhouettes while simplifying detail
- **Retro Aesthetics:** Authentic 8-bit/16-bit game graphics style
- **Fast Processing:** Optimized for quick pixel art conversion

## 📝 License

This project is licensed under the [MIT License](LICENSE)