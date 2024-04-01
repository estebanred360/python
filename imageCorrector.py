import os, sys
from PIL import Image


def convert_image(from_file: str, to_file: str) -> None:
    """
    Convert an image using PIL applying the following:

    The images received are in the wrong format:
        .tiff format
        Image resolution 192x192 pixel (too large)
        Rotated 90° anti-clockwise

    The images required for the launch should be in this format:
        .jpeg format
        Image resolution 128x128 pixel
        Should be straight

    from_file: The image file that should be converted
    to_file: The file to save the image to
    """
    deltaRotation = 270 # degrees counter-clockwise
    newSize = (128, 128)
    to_file = outfile + "150dp"

    if from_file != to_file:
        try:
            with Image.open(from_file) as im:
                print("Rotation: " + str(deltaRotation))
                print("New size: " + str(newSize))
                print("file name income: " + str(from_file))
                print("file name outcome: " + str(to_file))
                # im.rotate(deltaRotation).resize(newSize).save(to_file)
                im.save(to_file, "JPEG")
        except OSError:
            print("cannot convert", from_file)


def bulk_treatment(event: dict[str, Any], *_) -> None:
  """
  Cloud function entrypoint
  """
  # TODO: Extract the bucket name and the filename from the event
  bucket = #<YOUR-CODE-HERE>
  filename = #<YOUR-CODE-HERE>

  components = filename.split("/")
  # TODO: If the image is not in the raw folder, don't process it

  extension = '.' + components[-1].split('.')[-1]
  _, download_file = tempfile.mkstemp(suffix=extension)
  _, blurred_file = tempfile.mkstemp(suffix=extension)

  # TODO: Download the image to download_file

  # Process the Image
  convert_image(download_file, blurred_file)

  # TODO: Upload the image to the processed folder

  # Clean-Up
  os.remove(download_file)
  os.remove(blurred_file)




for infile in sys.argv[1:]:
    outfile, oldExtension = os.path.splitext(infile)
    print("file name: " + str(outfile) + " extension: " + str(outfile) )
    convert_image(infile, outfile)
