"""
dp is not "dimmensional pixels". it's "(density) independent pixels".
They are based on the density of the device, not the resolution .

For example , for application icons , it's always 48 dp , since on mdpi(160 dpi) , 
48 dp== 48 pixels . therefore , on hdpi (240 dpi) , it's 48*1.5=72 pixels , on ldpi(120 dpi) 
it's 48*0.75=36 , and on xhdpi (320 dpi) it's 48*2=96 pixels.

Density independence
Your app achieves "density independence" when it preserves the physical size—from the user's point 
of view—of your UI design when displayed on screens with different pixel densities. Maintaining 
density independence is important, because without it, a UI element like a button might appear larger 
on a low-density screen and smaller on a high-density screen.

Android helps you achieve density independence by providing the density-independent pixel (dp or dip) 
as a unit of measurement that you use instead of pixels (px).

The conversion of dp units to screen pixels is as follows:

px = dp * (dpi / 160)

Print resolution is measured in dots per inch (or “DPI”) which means the number of dots of ink per inch 
that a printer deposits on a piece of paper.

A 600 dpi printer squeezes 600 dots horizontally and 600 dots vertically in every square inch of the sheet.

Images should be at least 300 DPI (dots per inch) at the final size in the layout. Images which include text 
should be 400 DPI at the final size in the layout. Resolution and image size are inversely proportional to 
each other. Enlarge an image, the resolution decreases; reduce an image, the resolution increases.

"""

# When pixels(px) are equal to PPI, then 1 PPI = 1 inch or 2.54cm.
# 1cm = 96pixels/2.54, or 1cm = 37.7952756 pixels at 96ppi
# As PPI increases, and number of pixels stay the same, cm decreases.
# As number of pixels increases, and PPI stays the same, cm increases.
# PPI * x = 96 and pixel height * y = 37.7952756

# Formulas
# 1cm = 96px / 2.54
# 1px = 2.54 cm / 96
# 1px = 2.54 cm / PPI
# cm = pixels * ( 2.54 / PPI )

import os, sys
from PIL import Image

# scale_size = int(input("Enter scale size in cm: "))
# scale_res = int(input("Enter scale resolution in PPI: "))
scale_size = 2
scale_res = 48
scale_px = scale_size/(2.54/scale_res)  # pixels number based on the equation: cm = pixels * ( 2.54 / PPI )
scale_unit = scale_px/scale_size  # what 1 cm of the scale will be in pixels
# print(scale_px)
# print(scale_unit)
# Import the image
#img = Image.open("scale_real.png")

def imageSize(imagefile):

    # dimension information in pixels
    px_width = imagefile.size[0]
    px_height = imagefile.size[1]
    dpi = imagefile.info['dpi']
    #outfile = f + ".gif"

    # Return information about the scanned image
    print('Pixel width of the image is:', px_width)
    print('Pixel height of the image is:', px_height)
    print('DPI of the image is:', dpi)
    print('PPI of the image is:', dpi[1])
    
    px_cm = 1/(2.54/dpi[1])  # how many pixels of the scanned image equal 1 cm
    scanned_cm = px_height*(2.54/dpi[1])  # cm of scanned image based on image resolution an pixel count
    multiplier = scale_unit/px_cm  # to equalize the pixels in 1cm of the scale and 1cm of the scanned image
    new_cm = multiplier*px_height

    print(f"For the scanned image, {px_cm} pixels at {dpi[1]} PPI is equal to 1 cm.")
    print(f"Based on scanning resolution, the imported image appears as {scanned_cm} centimeters in height on the screen.")
    print(f"Based on the provided scale of {scale_size} cm, at a DPI of {scale_res}, 1 cm will equate to {scale_unit} pixels.")

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".gif"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # dimension information in pixels
                px_width = im.size[0]
                px_height = im.size[1]
                dpi = im.info.get('dpi')
                #outfile = f + ".gif"

                # Return information about the scanned image
                print('Filename:', str(infile))
                print('Pixel width of the image is:', px_width)
                print('Pixel height of the image is:', px_height)
                print('DPI of the image is:', dpi)
                print('PPI of the image is:', dpi[1])
    
        except OSError:
            print("cannot convert", infile)





