import numpy as np
from PIL import Image

MAX_ITERATIONS = 1000

# TODO: Understand why threshold = 2 is sufficient
def mandelbrot(c, max_iterations=MAX_ITERATIONS, threshold=2):
    """
    Determine if the complex number c is in the Mandelbrot set.
    
    Args:
    - c: A complex number to check.
    - max_iterations: The maximum number of iterations (default MAX_ITERATIONS).
    - threshold: The value at which we consider the sequence to diverge (default 2).
    
    Returns:
    - True if the sequence does not diverge, False if it does.
    """
    z = 0
    for i in range(max_iterations):
        z = z * z + c
        if abs(z) > threshold:
            return False  # Diverges
    return True  # Stays bounded within threshold

def generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iterations=MAX_ITERATIONS):
    # Create a blank image (all white)
    image = np.zeros((height, width), dtype=np.uint8)
    
    # Map each pixel to a point in the complex plane
    for px in range(width):
        for py in range(height):
            # Map pixel position to a point in the complex plane
            real = x_min + (px / width) * (x_max - x_min)
            imag = y_max - (py / height) * (y_max - y_min)
            c = complex(real, imag)
            
            # Check if this point is in the Mandelbrot set
            if mandelbrot(c, max_iterations):
                image[py, px] = 0  # Black for points in the set
            else:
                image[py, px] = 255  # White for points outside the set

    # Convert the numpy array to an image
    img = Image.fromarray(image)
    return img

# Image dimensions
width = 1920
height = 1080

# Define the region of the complex plane to visualize
x_min = -2.2
x_max = 0.5
y_min = 0
y_max = 1.12

# Generate the image
mandelbrot_img = generate_mandelbrot_image(width, height, x_min, x_max, y_min, y_max)

# Save the image
mandelbrot_img.save("mandelbrot_1920x1080.png")
# mandelbrot_img.show()  # Show the image (optional)
