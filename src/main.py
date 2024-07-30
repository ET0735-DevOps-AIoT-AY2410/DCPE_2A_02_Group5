import time
import threading
import queue
import csv
import requests
import getBooklist
import barcode_scanner as barcode

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

def getList():
    global reserveList
    global borrowList
    checkChangeReserve = {}
    checkChangeBorrow = {}
    while(True):
        data = getBooklist.getReserve()
        reserveList = data[0]
        borrowList = data[1]

        if reserveList != checkChangeReserve:
            print('reserve: ', reserveList)
            checkChangeReserve = reserveList
        if borrowList != checkChangeBorrow:
            print('borrow: ',borrowList)
            checkChangeBorrow = borrowList


"""
# Converting CSVs to dictionaries we can use
Account_Info = 'passwords.csv'
# Convert CSV dictionary from website into dictionary

with open(Account_Info, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    Account_Info = [row for row in csv_reader]

Loan_Info = 'Loaninfo.csv'
# Convert CSV dictionary for book borrowing information into dictionary

with open(Loan_Info, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    Loan_Info = [row for row in csv_reader]
"""
################################################################################
#  Function to Read RFID Tag
def read_rfid():
    RFID_Tag = rfid_reader.SimpleMFRC522()
    if RFID_Tag is None:
        return False
    else:
        return True  

def filter_info(account_id):
    global location
    print(str(location))
    filtered_reserveList = []

    for item in reserveList:
        if str(item["id"]) == str(account_id):
            account_info = {
                "id": item["id"],
                "bookId": item["bookId"],  
                "location": item["location"],
                "date": item["date"],
            }
            filtered_reserveList.append(account_info)


    location_filtered_list = []
    for item in filtered_reserveList:
        if item["location"] == location:
            location_filtered_list.append(item) 
            
    print ("Information Successfully Filtered")
    return location_filtered_list

# I'm not super sure if the use of datetime is correct
# In progress but meant to check if the current date is past the due date
"""
def check_fines(account_info):
    fines = account_info.get("fines")
    return fines >= 1"""
            
# Calculates the fines             
def calculate_due_date(filtered_info):
    today_date = datetime.now().date()
    results = []
    
    for item in filtered_info:
        borrow_date_str = item["date"]
        borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d %H:%M:%S").date()
        due_date = borrow_date + timedelta(days=10)
        
        if due_date < today_date:
            fine_status = 1
        else:
            fine_status = 0
        """
        results.append({
            "id": item["id"],
            "bookId": item["bookId"],
            "due_date": due_date,
            "fine_status": fine_status
        })"""
        
    return due_date, fine_status

def calculate_fines(due_date):
    today_date = datetime.now().date()
    days_overdue = (today_date - due_date).days
    fines_due = days_overdue *0.15
    return fines_due
    

# Deducts the fines from the account's balance
def deduct_fines(account_info, fines_due, extension_cost):
    """account_balance = account_info.get("Account_Balance")
    new_balance = account_balance - fines_due
    LCD.lcd_display_string("New Balance",1)
    LCD.lcd_display_string(str(new_balance),2)"""
    fines_deducted = fines_due + extension_cost
    message = "$" + str(fines_deducted)
    LCD.lcd_display_string("Fine Deduction:",1)
    LCD.lcd_display_string(str(message),2)
    # return new_balance

# Checks if the account is available to extend the books for 7 more days. Also ensures that the book hasn't been borrowed for more than 18 days
def book_extend_viability(filtered_info,due_date):   
    """
    borrow_date_str = loan_info.get("date")
    borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
    due_date_str = loan_info.get("return_date")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")"""
    for item in filtered_info:
        borrow_date_str = item["date"]
        borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d %H:%M:%S").date()
        if due_date > borrow_date:
            if (due_date - borrow_date).days < 18:
                return True
        elif borrow_date > due_date:
            if (borrow_date - due_date).days < 18:
                return True
        else:
            return False

# Extends the due date and also calcualtes the new balance after extending the book's due date
def book_extend(account_info, due_date):
    """account_balance = account_info.get("Account_Balance")
    new_balance = account_balance - 1.05 # 0.15 * 7 = 1.05
    LCD.lcd_display_string("New Balance",1)
    LCD.lcd_display_string(str(new_balance),2)"""
    new_due_date = due_date + timedelta(days=7)
    # sleep(2)
    LCD.lcd_display_string("New Due Date:",1)
    LCD.lcd_display_string(str(new_due_date),2)
    return new_due_date.strftime("%Y-%m-%d")#, new_balance
"""
# Updates the new account balance after fine or extension (to main dictionary Loan_Info)
def update_balance(filtered_info,new_balance):
    account_info_id = filtered_info.get("account_id")
    for item in borrowList:
        if str(item["account_id"]) == account_info_id:
            borrowList["balance"] == new_balance
    #return Account_Info"""

# Updates the new due date after extending the due date (to main dicitonary Loan_Info)
def update_due_date(filtered_reserveList,new_due_date):
    account_info_id = filtered_reserveList.get("account_id")
    for item in borrowList:
        if str(item["account_id"]) == account_info_id:
            borrowList["due_date"] == new_due_date
    #return Account_Info

def book_dispensal():
    servo.init()
    servo.set_servo_position(0)   
    servo.sleep(1)                 
    servo.set_servo_position(180)  
    servo.sleep(1)                

def update_status(filtered_reserveList, account_id):
    account_id = filtered_reserveList["id"]
    for item in reserveList:
        if str(item["id"]) == account_id:
            reserveList["location"] == "borrowed"

# Keypad stuff
keypad_queue = queue.Queue()


def key_pressed(key):
    keypad_queue.put(key)

# Main function for the fine system + RFID
def fine_system(): 
    global keyvalue
    global reserveList
    # getList()
    LCD.lcd_clear()
    LCD.lcd_display_string("Scan your Barcode", 1)
    filtered_info = []
    account_id = barcode.scan_barcode()

    """
    # For Testing Purposes
    account_id = 123
    reserveList = [
    {"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:37:58"},
    {"id": 123, "bookId": 9, "location": "location2", "date": "2024-07-19 00:57:42"},
    {"id": 123, "bookId": 3, "location": "location2", "date": "2024-07-19 00:57:47"},
    {"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:57:52"},
    {"id": 123, "bookId": 12, "location": "location1", "date": "2024-07-19 00:57:55"},
    {"id": 456, "bookId": 2, "location": "borrowed", "date": "2024-07-19 00:58:08"},
    {"id": 456, "bookId": 666, "location": "location1", "date": "2024-07-19 00:58:14"},
    {"id": 456, "bookId": 13, "location": "borrowed", "date": "2024-07-19 00:58:18"}
    ]"""

    filtered_info = filter_info(account_id)
    due_date, fine_status = calculate_due_date(filtered_info)
    overdue_fines_due = calculate_fines(due_date)
    extension_viability = book_extend_viability(filtered_info,due_date)

    """
    # For Testing Purposes
    time.sleep(5)
    extension_viability = True
    fine_status = 1
    """
    
    if fine_status == 1 and extension_viability == True:
        while True:
            LCD.lcd_display_string("You have Fines due",1)
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

            if keyvalue == 1:
                LCD.lcd_clear()
                LCD.lcd_display_string("Scan RFID",1)
                RFID = read_rfid()
                
                if RFID == True:
                    # buzzer.turn_on_with_timer(0.5)
                    deduct_fines(filtered_info, overdue_fines_due, extension_cost=0)
                    break
            if keyvalue == 2:
               
                break
            if keyvalue == 3:
                LCD.lcd_clear()
                LCD.lcd_display_string("Scan RFID",1)
                RFID = read_rfid()
               
                if RFID == True:
                    # buzzer.turn_on_with_timer(0.5)
                    new_due_date = book_extend(filtered_info,due_date) 
                    update_due_date(filtered_info,new_due_date)
                    deduct_fines(filtered_info, overdue_fines_due,extension_cost=1.05)
    elif fine_status == 1 and book_extend_viability(filtered_info,due_date) == True:
        while True:
                LCD.lcd_display_string("You have Fines due",1)
                LCD.lcd_display_string("Extension Available",2)
                time.sleep(5)
                LCD.lcd_display_string("1.Pay Fines",1)
                LCD.lcd_display_string("2.Exit",2)
                time.sleep(2)
                LCD.lcd_display_string("3.Extend Loan",1)

                keyvalue = None
                while keyvalue not in [1, 2, 3]:
                    keyvalue= keypad_queue.get()

                if keyvalue == 1:
                    LCD.lcd_clear()
                    LCD.lcd_display_string("Scan RFID",1)
                    RFID = read_rfid()
                    if RFID == True:
                        # buzzer.turn_on_with_timer(0.5)
                        deduct_fines(filtered_info, overdue_fines_due, extension_cost=0)
                        break
                if keyvalue == 2:
                    break       
    
    book_dispensal()
    update_status(filtered_info,account_id)
"""
def keypad_interrupt():
    global keyvalue
    keyvalue = keypad.get_key()
    return keyvalue"""

def main_system():
    # There was some error with this function for getList()
    getList()
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


# Main Function
def main():

    keypad.init(key_pressed)
    keypad_thread = threading.Thread(target=keypad.get_key)

    main_system_thread = threading.Thread(target=main_system)
   # keypad_thread = threading.Thread(target=keypad_interrupt)
    main_system_thread.start()
    keypad_thread.start()



if __name__ == '__main__':
    main()



################################################################################
# RPi Testing Code
"""
#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()




#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)


def main():
    #initialization of HAL modules
    led.init()
    adc.init()
    buzzer.init()
  
    moisture_sensor.init()
    input_switch.init()
    ir_sensor.init()
    reader = rfid_reader.init()
    servo.init()
    temp_humid_sensor.init()
    usonic.init()
    dc_motor.init()
    accelerometer = accel.init()

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Dignostic Tests", 2)

    time.sleep(3)

    print("press 0 to test accelerometer")
    print("press 1 to test LED")
    print("press 2 to test potentiometer")
    print("press 3 to test buzzer")
    print("press 4 to test moizture sensor")
    print("press 5 to test ultrasonic sensor")  
    print("press 6 to test rfid reader") 
    print("press 7 to test LDR") 
    print("press 8 to test servo & DC motor") 
    print("press 9 to test temp & humidity")   
    print("press # to test slide switch")  
    print("print * to test IR sensor")


    while(True):
        lcd.lcd_clear()
        lcd.lcd_display_string("press any key!", 1)
     

        print("wait for key")
        keyvalue= shared_keypad_queue.get()

        print("key value ", keyvalue)
        

        if(keyvalue == 1): 
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)
            lcd.lcd_display_string("LED TEST ", 2)
            led.set_output(1, 1)
            time.sleep(2)
            led.set_output(1, 0)
            time.sleep(2)

        elif (keyvalue == 2):
            pot_val = adc.get_adc_value(1)
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)
            lcd.lcd_display_string("potval " +str(pot_val), 2)
            time.sleep(2)

        elif (keyvalue == 3):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)
            lcd.lcd_display_string("Buzzer TEST ", 2)
            buzzer.beep(0.5, 0.5, 1)

        elif (keyvalue == 4):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)
            sensor_val = moisture_sensor.read_sensor()
            lcd.lcd_display_string("moisture " +str(sensor_val), 2)
            time.sleep(2)

        elif (keyvalue == 5):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)            
            sensor_val = usonic.get_distance()
            lcd.lcd_display_string("distance " +str(sensor_val), 2)
            time.sleep(2)   

        elif (keyvalue == 6):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)           
            id = reader.read_id_no_block()
            id = str(id)
        
            if id != "None":
                print("RFID card ID = " + id)
                # Display RFID card ID on LCD line 2
                lcd.lcd_display_string(id, 2) 
            time.sleep(2)   

        elif (keyvalue == 7):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)            
            pot_val = adc.get_adc_value(0)
            lcd.lcd_display_string("LDR " +str(pot_val), 2)
            time.sleep(2)

        elif (keyvalue == 8):
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)     
            lcd.lcd_display_string("servo/DC test ", 2)  
            servo.set_servo_position(20)
            time.sleep(1)  
            servo.set_servo_position(80)
            time.sleep(1)     
            servo.set_servo_position(120)
            time.sleep(1)            
            dc_motor.set_motor_speed(50)
            time.sleep(4)   
            dc_motor.set_motor_speed(0)
            time.sleep(2) 

        elif (keyvalue == 9):
            temperature, humidity = temp_humid_sensor.read_temp_humidity()
            lcd.lcd_display_string("Temperature "  +str(temperature), 1)  
            lcd.lcd_display_string("Humidity "  +str(humidity), 2) 
            time.sleep(2)  

        elif (keyvalue == "#"):
            sw_switch = input_switch.read_slide_switch()
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)    
            lcd.lcd_display_string("switch "  +str(sw_switch), 2) 
            time.sleep(2)  
        
        elif (keyvalue == "*"):
            ir_value = ir_sensor.get_ir_sensor_state()
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1)    
            lcd.lcd_display_string("ir sensor "  +str(ir_value), 2) 
            time.sleep(2)  
        
        elif (keyvalue == 0):
            x_axis, y_axis, z_axis = accelerometer.get_3_axis_adjusted()
            lcd.lcd_display_string("key pressed "  +str(keyvalue), 1) 
            lcd.lcd_display_string("x " +str(x_axis), 2) 
            time.sleep(2) 
            lcd.lcd_clear()
            lcd.lcd_display_string("y " +str(y_axis), 1) 
            lcd.lcd_display_string("z " +str(z_axis), 2) 
            print(x_axis)
            print(y_axis)
            print(z_axis)  

            time.sleep(2)  
       


        time.sleep(1)





if __name__ == '__main__':
    main()
    """