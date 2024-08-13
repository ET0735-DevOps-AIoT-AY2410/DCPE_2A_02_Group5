import main
import csv
import os
def main():
   global location
   location = "location1"
   update_status('2302931')

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