from PIL import Image

def get_image_dpi(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Get DPI information
            dpi = img.info.get('dpi')

            if dpi:
                print(f"DPI of the image '(image_path)': (dpi[0]) x  ")
            else:
                print(f"No DPI information found for the image '(image_path)'")
    except Exception as e:
        print(f"Error: (e)")

# Example usage
image_path = 'path/to/your/image.jpg'
get_image_dpi(image_path)
