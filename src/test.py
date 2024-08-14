import main
import csv
import os
import datetime
def main():
    global location
    location = "location1"
    update_extension('1234567', datetime.datetime.now())

def update_extension(account_id, new_due_date):
    global location
    global reserveList

    current_dir = os.getcwd()  # This will get the current working directory
    file_path = os.path.join(current_dir, 'website', 'reserveList.csv')

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        reserveList = list(reader)

    new_due_date_str = new_due_date.strftime("%Y-%m-%d %H:%M:%S")

    for item in reserveList:
        if item['id'] == account_id and item['location'] == location:
            item['date'] = new_due_date_str

    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['id', 'bookId', 'location', 'date']  
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reserveList)

def update_status(account_id):
    global location
    global reserveList

    current_dir = os.getcwd()  # This will get the current working directory
    file_path = os.path.join(current_dir, 'website', 'reserveList.csv')

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        reserveList = list(reader)

    for item in reserveList:
        print(item['id'] == account_id and item['location'] == location)
        print(item['id'] == account_id)
        print(item['location'] == location)
        if item['id'] == account_id and item['location'] == location:
             item['location'] = 'borrowed'
        print (item)

    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['id', 'bookId', 'location', 'date']  
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reserveList)



if __name__ == '__main__':
    main()
