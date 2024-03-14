from PIL import Image

# Load the pixel art image
image_path = "hello.png"
pixel_art_image = Image.open(image_path)

# Get the width and height of the image
width, height = pixel_art_image.size

# Ensure the image size is 32x32
if width != 64 or height != 64:
    raise ValueError("The image dimensions are not 32x32. Please resize the image first.")

# Create a list to store the formatted RGB values of each pixel (all 1024 values)
all_pixel_rgb_values = []

# Iterate over each pixel and get its RGB value
for y in range(height):
    for x in range(width):
        pixel_rgb = pixel_art_image.getpixel((x, y))
        formatted_rgb = f"0x{pixel_rgb[0]:02X}{pixel_rgb[1]:02X}{pixel_rgb[2]:02X}"
        all_pixel_rgb_values.append(formatted_rgb)

# Save all formatted RGB values into a text file
output_file = "all_pixel_rgb_values.txt"
with open(output_file, "w") as file:
    file.write(",".join(all_pixel_rgb_values))
