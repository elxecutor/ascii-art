
# DB32 Pixel Art Generator

Convert images to authentic pixel art using the DawnBringer 32 (DB32) color palette. This tool downscales images, quantizes them to the DB32 palette, and produces crisp, retro-style pixel art with optional decorative borders.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Downscale images to pixel art resolution (max 128px)
- Quantize colors to the exact DB32 palette (32 colors)
- Nearest-neighbor scaling (no anti-aliasing)
- Optional multi-layer decorative borders
- Configurable output scale factor
- Command-line interface and demo script

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/noiz-x/asciiart.git
cd asciiart
pip install -r requirements.txt
```

## Usage
1. Generate pixel art from an image:
	 ```bash
	 python3 ascii_art.py docs/samurai_champloo.jpg output.png
	 ```
2. Run the demo script to see various examples:
	 ```bash
	 python3 demo_pixel_art.py
	 ```

### Common Options
- Scale output:
	```bash
	python3 ascii_art.py input.jpg output.png -s 6
	```
- Change base resolution:
	```bash
	python3 ascii_art.py input.jpg output.png --max_size 64
	```
- Remove border:
	```bash
	python3 ascii_art.py input.jpg output.png --no-border
	```

## File Overview
- `ascii_art.py` — Main pixel art generator (DB32 palette, CLI)
- `demo_pixel_art.py` — Demo script with example outputs
- `requirements.txt` — Python dependencies (Pillow, numpy)
- `docs/` — Example images (e.g., `samurai_champloo.jpg`)
- `fonts/` — Font files for advanced use
- `CONTRIBUTING.md` — Contribution guidelines
- `CODE_OF_CONDUCT.md` — Code of conduct
- `LICENSE` — MIT License

## Contributing
We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for details.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or support, please open an issue or contact the maintainer via [X](https://x.com/elxecutor/).