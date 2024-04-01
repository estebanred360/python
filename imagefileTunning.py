import os, sys
from PIL import Image

deltaRotation = 270 # degrees counter-clockwise
newSize = (128, 128)
#to_file = outfile + ".jpg"

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"

    """
    CONVERTER
    """
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                print(str(outfile))
                im.save(outfile)
                #im.rotate(deltaRotation).resize(newSize).save(outfile)
                #im.resize(newSize).save(outfile)
        except OSError:
            print("cannot convert", infile)

            