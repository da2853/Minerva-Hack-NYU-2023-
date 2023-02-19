import io
import os


# Import the Google Cloud Vision API client library
from google.cloud import vision
from google.cloud.vision_v1 import types

# Set the environment variable for Google Application Credentials to access the API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'google_api.json'

# Define the function to extract text from image
def detect_text(image_path):
    """Detects text in the image file using Google Vision API."""
    # Create a client object for the vision API
    client = vision.ImageAnnotatorClient()

    # Read the image file into memory
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an image object from the image data
    image = types.Image(content=content)

    # Perform text detection on the image
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Print the extracted text
    print('Extracted text:')
    return texts[0].description
    # for text in texts:
    #      print('\n"{}"'.format(text.description))

# Call the detect_text function with the path to the image file as an argument
# detect_text('test_image.jpg')