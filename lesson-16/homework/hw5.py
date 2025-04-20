import numpy as np
from PIL import Image

# --- Functions for Image Manipulation ---

def flip_image(image_array):
    """Flip image horizontally and vertically."""
    flipped = np.flipud(np.fliplr(image_array))
    return flipped

def add_noise(image_array, noise_level=30):
    """Add random noise to the image."""
    noise = np.random.randint(-noise_level, noise_level+1, image_array.shape, dtype=np.int16)
    noisy_image = image_array.astype(np.int16) + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def brighten_channels(image_array, increment=40):
    """Brighten all color channels by a fixed amount."""
    brightened = image_array.astype(np.int16) + increment
    return np.clip(brightened, 0, 255).astype(np.uint8)

def apply_mask(image_array, mask_size=(100, 100)):
    """Apply a black mask to the center of the image."""
    output = image_array.copy()
    h, w = output.shape[:2]
    mh, mw = mask_size
    start_y = h // 2 - mh // 2
    start_x = w // 2 - mw // 2
    output[start_y:start_y+mh, start_x:start_x+mw] = [0, 0, 0]
    return output

# --- Main Execution ---

# Load the image
input_path = '/Users/ibrokhimkamolov/Documents/Analytics_Studies/Python/Pythonhomework/lesson-16/images/birds.png'
output_path = '/Users/ibrokhimkamolov/Documents/Analytics_Studies/Python/Pythonhomework/lesson-16/images/birds_modified.png'

# Read using PIL
image = Image.open(input_path)
image_array = np.array(image)

# Apply manipulations
image_array = flip_image(image_array)
image_array = add_noise(image_array)
image_array = brighten_channels(image_array, increment=40)
image_array = apply_mask(image_array, mask_size=(100, 100))

# Convert back to PIL image and save
result_image = Image.fromarray(image_array)
result_image.save(output_path)

print(f"Image processing complete. Saved to {output_path}")
