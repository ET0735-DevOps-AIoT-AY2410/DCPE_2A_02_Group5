import cv2
import sqlite3
from pyzbar.pyzbar import decode

def get_user_by_barcode(barcode):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT name FROM users WHERE barcode=?", (barcode,))
    user = c.fetchone()
    conn.close()
    return user

def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        
        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            user = get_user_by_barcode(barcode_data)
            
            if user:
                user_name = user[0]
                cv2.putText(frame, f"User: {user_name}", (barcode.rect.left, barcode.rect.top - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            else:
                cv2.putText(frame, "User not found", (barcode.rect.left, barcode.rect.top - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        cv2.imshow('Barcode Scanner', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()