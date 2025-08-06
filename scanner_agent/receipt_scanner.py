import os
import time
import threading
from PIL import Image
import pytesseract
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
SCAN_FOLDER = "./assets/sample_receipts/"
OUTPUT_CSV = "./assets/price_database/scanned_data.csv"
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update for your system

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

class ScanHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"New receipt detected: {event.src_path}")
            process_receipt(event.src_path)

def process_receipt(image_path):
    """Extract text from scanned receipt and save to CSV"""
    try:
        # OCR Processing
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        
        # Parse receipt data (simplified)
        lines = text.split('\n')
        items = []
        for line in lines:
            if any(char.isdigit() for char in line) and not line.startswith(('TAX', 'TOTAL', 'SUB')):
                # Basic item parsing - customize for actual receipts
                parts = line.rsplit(' ', 1)
                if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                    items.append({
                        'product': parts[0].strip(),
                        'price': float(parts[1])
                    })
        
        # Append to CSV database
        with open(OUTPUT_CSV, 'a') as f:
            for item in items:
                f.write(f"{item['product']},{item['price']}\n")
                
        print(f"Processed {len(items)} items from {os.path.basename(image_path)}")
        
        # Trigger price comparison
        from price_comparator import compare_prices
        compare_prices(item['product'])
        
    except Exception as e:
        print(f"Error processing receipt: {str(e)}")

def start_scanner_monitor():
    """Monitor folder for new scanned receipts"""
    event_handler = ScanHandler()
    observer = Observer()
    observer.schedule(event_handler, SCAN_FOLDER, recursive=False)
    observer.start()
    print(f"Monitoring scanner folder: {SCAN_FOLDER}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_scanner_monitor()
