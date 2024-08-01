import time
from picamera import PiCamera
from pyzbar.pyzbar import decode
from PIL import Image

def capture_image(camera, file_path):
    camera.start_preview()
    # Allow the camera to warm up
    time.sleep(2)
    camera.capture(file_path)
    camera.stop_preview()

def scan_barcode(image_path):
    image = Image.open(image_path)
    barcodes = decode(image)
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"Found {barcode_type} barcode: {barcode_data}")
        return barcode_data
    return None

def main():
    camera = PiCamera()
    image_path = '/home/pi/barcode.jpg'
    
    print("Preparing to capture image...")
    capture_image(camera, image_path)
    
    print("Scanning for barcodes...")
    barcode_data = scan_barcode(image_path)
    
    if barcode_data:
        print(f"Barcode data: {barcode_data}")
        # Here, you can add code to check the barcode data against a database
        # For demonstration, we'll just print it
    else:
        print("No barcode found.")
    
    camera.close()

if __name__ == "__main__":
    main()
