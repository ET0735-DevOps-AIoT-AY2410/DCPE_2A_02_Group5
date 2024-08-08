import time
from picamera2 import Picamera2
from pyzbar.pyzbar import decode
from PIL import Image

def capture_image(file_path):
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(2)  # Give the camera some time to adjust to lighting
    picam2.capture_file(file_path)
    picam2.stop()

def scan_barcode(image_path):
    image = Image.open(image_path)
    barcodes = decode(image)
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"Found {barcode_type} barcode: {barcode_data}")

if __name__ == "__main__":
    image_path = 'barcode.jpg'
    capture_image(image_path)
    scan_barcode(image_path)
