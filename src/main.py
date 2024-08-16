import time
import threading
import queue
import csv
import requests
import getBooklist
import barcode_scanner as barcode
import os

from datetime import datetime, date, timedelta

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_adc as adc
from hal import hal_buzzer as buzzer
from hal import hal_keypad as keypad
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_input_switch as input_switch
from hal import hal_ir_sensor as ir_sensor
from hal import hal_rfid_reader as rfid_reader
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_usonic as usonic
from hal import hal_dc_motor as dc_motor
from hal import hal_accelerometer as accel

LCD = LCD.lcd()

# Pulling Dictionaries from Docker App
"""
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors
return response.text
reader = csv.DictReader(StringIO(csv_str))
return [row for row in reader]
url = 'http://<EXTERNAL-IP>/get_csv'  # Replace with URL from docker
AccountInfo_csv = fetch_csv_data(url)
AccountInfo = csv_to_dict(csv_data)
################################################################################
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors
return response.text
reader = csv.DictReader(StringIO(csv_str))
return [row for row in reader]
url = 'http://<EXTERNAL-IP>/get_csv'  # Replace with URL from docker
Loan_Info_csv = fetch_csv_data(url)
Loan_Info = csv_to_dict(csv_data)
"""
#########################################
# get dictionary for reserved and borrowed books
def getList():
    global reserveList
    global borrowList
    checkChangeReserve = {}
    checkChangeBorrow = {}
    
    while True:
        data = getBooklist.getReserve()
        reserveList_raw = data[0]
        borrowList_raw = data[1]

        reserveList = []
        for id, books in reserveList_raw.items():
            for book in books:
                book_info = {
                    "id": id,
                    "bookId": book[0],
                    "location": book[1], 
                    "date": book[2]
                }
                reserveList.append(book_info)

        borrowList = []
        for id, books in borrowList_raw.items():
            for book in books:
                book_info = {
                    "id": id,
                    "bookId": book[0],
                    "location": "borrowed", 
                    "date": book[1]
                }
                borrowList.append(book_info)

        if reserveList != checkChangeReserve:
            print('reserve: ', reserveList)
            checkChangeReserve = reserveList

        if borrowList != checkChangeBorrow:
            print('borrow: ', borrowList)
            checkChangeBorrow = borrowList
################################################################################
#  Function to Read RFID Tag
def read_rfid():
    reader = rfid_reader.init()
    RFID_Tag = reader.read_id_no_block()
    if RFID_Tag is None:
        return False
    else:
        return True  
#########################################
# servo motor turn
def book_dispensal():
    servo.init()
    servo.set_servo_position(0)   
    servo.sleep(1)                 
    servo.set_servo_position(180)  
    servo.sleep(1)                

# Keypad stuff
keypad_queue = queue.Queue()

def key_pressed(key):
    keypad_queue.put(key)

#####################################################################
# Managing Book Extensions
def extension_filter(due_date):
    extension_info = []
    today_date = datetime.now().date()
    print(f"today's date is {today_date}")
    
    for item in due_date:
        if isinstance(item, dict) and "borrow_date" in item and "due_date" in item:
            borrow_date = datetime.strptime(item["borrow_date"], "%Y-%m-%d %H:%M:%S").date()
            days_borrowed = (today_date - borrow_date).days 
            days_borrowed -= 22  # There is some bug here wher ethe days_borrowed is extended by 22 days
            print(f"Book ID {item['bookId']} borrowed for {days_borrowed} days.")
            if days_borrowed <= 18:   
                extension = { 
                    "bookId": item["bookId"],
                    "due_date": item["due_date"],
                    "borrow_date": item["borrow_date"]
                }
                extension_info.append(extension)

    number_of_extensions = len(extension_info)
    print("Extension_Info: ")
    print(str(extension_info))
    return extension_info,number_of_extensions

def update_extension(account_id, new_due_date_str):
    global location

    current_dir = os.getcwd()  # This will get the current working directory
    file_path = os.path.join(current_dir, 'src', 'website', 'reserveList.csv')

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        tempList = list(reader)

    for item in tempList:
        if item['id'] == account_id and item['location'] == 'borrowed':
            item['date'] = new_due_date_str
    print('==========================================\n')
    print(tempList)
    print('==========================================\n')
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['id', 'bookId', 'location', 'date']  
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tempList)

#########################################
# main function for extending the book due date
def book_extention(due_date):
    global account_id
    extension_info, number_of_extensions = extension_filter(due_date)
    LCD.lcd_display_string("Available",1)
    LCD.lcd_display_string(str(number_of_extensions),2)
    time.sleep(3)

    i = 0
    
    for i in range (number_of_extensions):
        LCD.lcd_clear()
        LCD.lcd_display_string("1. Extend",1)
        LCD.lcd_display_string("2. Next",2)
        time.sleep(2)
        LCD.lcd_clear()
        LCD.lcd_display_string("Book ID",1)
        LCD.lcd_display_string(str(extension_info[i]["bookId"]),2)
        time.sleep(2)
        keyvalue = None
        while keyvalue not in [1, 2]:
            keyvalue= keypad_queue.get()

        if keyvalue == 1:
            current_due_date = datetime.strptime(extension_info[i]["due_date"], "%Y-%m-%d %H:%M:%S")
            new_due_date = current_due_date + timedelta(days=7)
            new_due_date_str = new_due_date.strftime("%Y-%m-%d %H:%M:%S")
            extension_info[i]["due_date"] = new_due_date_str
            LCD.lcd_clear()
            LCD.lcd_display_string("New Due Date:", 1)
            LCD.lcd_display_string(str(new_due_date_str), 2)
            update_extension(account_id,new_due_date_str)
            time.sleep(1)

        elif keyvalue == 2:
            LCD.lcd_display_string("Next...",1)
            time.sleep(2)
            continue
        
    extension_cost = i * 1.05
    return extension_cost
#####################################################################
# Fine System and its functions
#########################################
# Filter information from borrowList
def filter_info(account_id):
    global location
    global borrowList
    print(str(location))
    filtered_info = []
    for item in borrowList:
        if isinstance(item, dict) and "id" in item:
            if str(item["id"]) == str(account_id):
                account_info = {
                    "id": item["id"],
                    "bookId": item["bookId"],  
                    "location": item["location"],
                    "date": item["date"],
                }     
                filtered_info.append(account_info)
    print("Filtered_Info: ")
    print(str(filtered_info))
    return filtered_info
#########################################
# Calculates the due date into a new dictionary            
def calculate_due_date(filtered_info):
    today_date = datetime.now().date()
    due_dates = []
    fine_status = 0
    
    for item in filtered_info:
        if isinstance(item, dict) and "date" in item and "bookId" in item:
            borrow_date_str = item["date"]
            borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d %H:%M:%S").date()
            due_date_value = borrow_date + timedelta(days=10)
            due_date_str = due_date_value.strftime("%Y-%m-%d %H:%M:%S")
            due_date = {
                "bookId": item["bookId"],
                "due_date": due_date_str,
                "borrow_date": item["date"]
            }
            due_dates.append(due_date)
        for item in due_dates:
            if isinstance(item, dict):
                if today_date > due_date_value:
                    fine_status = 1 
    print("Due_Dates: ")
    print(str(due_dates))
    print(str(fine_status))
    return due_dates, fine_status
#########################################
# Calculates the fines
def calculate_fines(due_date):
    days_overdue = 0
    today_date = datetime.now().date()
    for item in due_date:
        if isinstance(item, dict):
            due_date_str = item["due_date"]
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S").date()
            days_overdue = (today_date - due_date).days
        if days_overdue < 1:
            return 0
        else:
            fines_due = days_overdue *0.15
            return fines_due
#########################################
# Checks if the books in the dictionary can be extended
def book_extend_viability(due_date):   
    for item in due_date:
        if isinstance(item, dict) and "borrow_date" in item and "due_date" in item:
            borrow_date_str = item["borrow_date"]
            due_date_str = item["due_date"]
            borrow_date_value = datetime.strptime(borrow_date_str, "%Y-%m-%d %H:%M:%S").date()
            due_date_value = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S").date()
            if (due_date_value - borrow_date_value).days < 18 or (due_date_value - borrow_date_value).days < 0:
                return True
            else:
                return False
#########################################
# Makes buzzer beep
def buzzer_beep():
    buzzer.init()
    buzzer.turn_on()
    time.sleep(0.5)
    buzzer.turn_off()
#########################################
# Deducts the fines from the account's balance
def deduct_fines(fines_due, extension_cost):
    fines_deducted = fines_due + extension_cost
    message = "${:.2f}".format(fines_deducted)
    LCD.lcd_display_string("Fine Deduction:",1)
    LCD.lcd_display_string(str(message),2)
    return fines_deducted
#########################################
# Updates the information of the borrowed books inside of reserveList.csv
def update_status(account_id):
    global location
    global reserveList

    current_dir = os.getcwd()  # This will get the current working directory
    file_path = os.path.join(current_dir, 'src', 'website', 'reserveList.csv')

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        reserveList = list(reader)

    for item in reserveList:
        if item['id'] == account_id and item['location'] == location:
            item['location'] = 'borrowed'

    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['id', 'bookId', 'location', 'date']  
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reserveList)
#############################################
# The main fine system
def fine_system(): 
    global keyvalue
    global borrowList
    global account_id
    account_id = 0
    # getList()
    LCD.lcd_clear()
    LCD.lcd_display_string("Scan your Barcode", 1)
    time.sleep(5)
    extension_viability = False
    account_id = barcode.read_barcode(os.path.join(os.getcwd(), 'src/barcode.jpg'))
    if account_id == None:
        LCD.lcd_clear()
        LCD.lcd_display_string("Scan again", 1)
        
    print(account_id)
    

    # For Testing Purposes
    # account_id = '2302931'
    """borrowList = [
    {"id": 456, "bookId": 2, "location": "borrowed", "date": "2024-07-15 00:58:08"},  # 4 days borrowed (eligible)
    {"id": 456, "bookId": 13, "location": "borrowed", "date": "2024-07-10 00:58:18"}, # 9 days borrowed (eligible)
    {"id": 123, "bookId": 666, "location": "borrowed", "date": "2024-07-01 00:58:18"}, # 18 days borrowed (eligible)
    {"id": 123, "bookId": 13, "location": "borrowed", "date": "2024-06-25 00:58:08"},  # 24 days borrowed (not eligible)
    {"id": 123, "bookId": 14, "location": "borrowed", "date": "2024-06-20 00:58:08"},  # 29 days borrowed (not eligible)
    {"id": 123, "bookId": 12, "location": "borrowed", "date": "2024-07-05 00:58:08"}   # 14 days borrowed (eligible)
]"""
    filtered_info = filter_info(account_id)
    due_date, fine_status = calculate_due_date(filtered_info)
    overdue_fines_due = calculate_fines(due_date)
    extension_viability = book_extend_viability(due_date)

    if fine_status == 1 or extension_viability == True:
        while True:
            LCD.lcd_clear()
            LCD.lcd_display_string("You have Fines ",1)
            LCD.lcd_display_string("Extension Available",2)
            time.sleep(5)
            LCD.lcd_clear()
            LCD.lcd_display_string("1.Pay Fines",1)
            LCD.lcd_display_string("2.Exit",2)
            time.sleep(2)
            LCD.lcd_clear()
            LCD.lcd_display_string("3.Extend Loan",1)

            keyvalue = None
            while keyvalue not in [1, 2, 3]:
                keyvalue= keypad_queue.get()

            if keyvalue == 1:                             # Pay Fines
                LCD.lcd_clear()
                LCD.lcd_display_string("Scan RFID",1)
                RFID = read_rfid()
                print(str(RFID))

                if RFID == True:
                    buzzer_beep()
                    deduct_fines(overdue_fines_due, extension_cost=0)
                    break
            if keyvalue == 2:                              # Exit
                update_status(account_id)
                main_system()

            if keyvalue == 3:                              # Extension
                LCD.lcd_clear()
                LCD.lcd_display_string("Scan RFID",1)
                RFID = read_rfid()
               
                if RFID == True:
                    buzzer_beep()
                    extension_cost = book_extention(due_date)
                    deduct_fines(overdue_fines_due,extension_cost)
                    break
    elif fine_status == 1 and book_extend_viability(filtered_info,due_date) == False:
        while True:
                LCD.lcd_clear()
                LCD.lcd_display_string("You have Fines",1)
                LCD.lcd_display_string("Extension Available",2)
                time.sleep(5)
                LCD.lcd_display_string("1.Pay Fines",1)
                LCD.lcd_display_string("2.Exit",2)
                time.sleep(2)
                
                keyvalue = None
                while keyvalue not in [1, 2]:
                    keyvalue= keypad_queue.get()

                if keyvalue == 1:
                    LCD.lcd_clear()
                    LCD.lcd_display_string("Scan RFID",1)
                    RFID = read_rfid()
                    if RFID == True:
                        buzzer_beep()
                        deduct_fines(filtered_info, overdue_fines_due, extension_cost=0)
                        break
                if keyvalue == 2:
                    LCD.lcd_clear()
                    LCD.lcd_display_string("Exiting...",1)
                    time.sleep(1)
                    update_status(account_id)
                    main_system()       
    
    LCD.lcd_clear()
    LCD.lcd_display_string("1.Borrow",1)
    LCD.lcd_display_string("2.Exit",2)

    keyvalue = None
    while keyvalue not in [1, 2]:
        keyvalue= keypad_queue.get()

    if keyvalue == 1:
        book_dispensal()
        update_status(account_id)
        main_system()

    elif keyvalue == 2:
        LCD.lcd_clear()
        LCD.lcd_display_string("Exiting...",1)
        time.sleep(1)
        update_status(account_id)
        main_system() 
   
"""
def keypad_interrupt():
    global keyvalue
    keyvalue = keypad.get_key()
    return keyvalue"""
#######################################################################################
# Main system 
def main_system():
    global location
    LCD.lcd_display_string("Select your ", 1)
    LCD.lcd_display_string("Location",2)
    time.sleep(2)

    keyvalue = None
    while keyvalue not in [1, 2]:
        LCD.lcd_display_string("1.Location 1", 1)
        LCD.lcd_display_string("2.Location 2", 2)
        keyvalue= keypad_queue.get()

    LCD.lcd_clear()
    if keyvalue == 1:
        LCD.lcd_display_string("Location 1", 1)
        LCD.lcd_display_string("Selected", 2)
        location = "location1"
    elif keyvalue == 2:
        LCD.lcd_display_string("Location 2", 1)
        LCD.lcd_display_string("Selected", 2)
        location = "location2"

    fine_system()

def website():
    os.system('python src/website/website.py')


############################################################################################
# Main Function
def main():
    website_thread = threading.Thread(target=website)
    keypad.init(key_pressed)
    keypad_thread = threading.Thread(target=keypad.get_key)
    getList_thread = threading.Thread(target=getList)
    main_system_thread = threading.Thread(target=main_system)

    website_thread.start()
    getList_thread.start()
    main_system_thread.start()
    keypad_thread.start()

if __name__ == '__main__':
    main()
