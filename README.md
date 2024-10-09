# Mandelbrot Set Image Generator

This script generates and saves an image of the Mandelbrot set using Python. The image size, region of the complex plane, and iteration limit are all customizable.

## Requirements

Make sure you have the following Python libraries installed:
- `numpy`
- `PIL` (Pillow)

You can install them with:
```bash
pip install -r requirments.txt
```

## Usage

1. **Adjust Parameters**: You can modify the following parameters in the script:
   - `width` and `height`: Dimensions of the output image (default: 1920x1080).
   - `x_min`, `x_max`, `y_min`, `y_max`: Define the region of the complex plane to visualize.
   - `MAX_ITERATIONS`: Controls the maximum number of iterations for determining membership in the Mandelbrot set.

2. **Run the Script**: Execute the script to generate and save the Mandelbrot set image:
```bash
python mandelbrot.py
```

   The image will be saved as `mandelbrot_1920x1080.png` in the current directory.

3. **Optional**: Uncomment `mandelbrot_img.show()` at the end of the script to display the image directly after generating it.

Feel free to adjust the parameters to explore different areas of the Mandelbrot set!
