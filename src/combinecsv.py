import csv

def merge_csv():
    # Converting CSVs to dictionaries we can use
    Account_Info = 'passwords.csv'
    # Convert CSV dictionary from website into dictionary

    with open(Account_Info, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        Account_Info = [row for row in csv_reader]

    Reservation_Info = 'reserveList.csv'
    # Convert CSV dictionary for book borrowing information into dictionary

    with open(Reservation_Info, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        Reservation_Info = [row for row in csv_reader]

    
    combined_data = {}

    for row in Account_Info:
        user_id = row['id']
        if user_id not in combined_data:
            combined_data[user_id] = {
                'books': []
            }
        combined_data[user_id]['books'].append({
            'bookId': row['bookId'],
            'location': row['location'],
            'date': row['date']
        })

    for row in Reservation_Info:
        user_id = row['username']
        if user_id in combined_data:
            combined_data[user_id].update({
                'password': row['password'],
                'account_balance': row['account_balance'],
                'fines': row['fines'],
                'extensions': row['extensions'],
                'rfid': row['rfid'],
                'return_date': row['return_date']
            })
        else:
            combined_data[user_id] = {
                'password': row['password'],
                'account_balance': row['account_balance'],
                'fines': row['fines'],
                'extensions': row['extensions'],
                'rfid': row['rfid'],
                'return_date': row['return_date'],
                'books': []
            }

    # Final merged csv into python dictionary
    merged_dictionary = []
    for user_id, details in combined_data.items():
        for book in details['books']:
            output_row = {
                'id': user_id,
                'rfid': details.get('rfid', 'NoRFID'),
                'password': details.get('password', ''),
                'account_balance': details.get('account_balance', ''),
                'fines': details.get('fines', ''),
                'extensions': details.get('extensions', ''),
                'return_date': details.get('return_date', ''),
                'bookId': book['bookId'],
                'location': book['location'],
                'date': book['date']
            }
            merged_dictionary.append(output_row)

        return merged_dictionary



# Sample of how combined CSV would look 
"""
id_rfid,password,account_balance,fines,extensions,return_date,bookId,location,date
123_RFID1,pass1,150.0,2,5,2024-01-15,14,location1,2024-07-19 00:37:58
123_RFID1,pass1,150.0,2,5,2024-01-15,9,location1,2024-07-19 00:57:42
123_RFID1,pass1,150.0,2,5,2024-01-15,3,location1,2024-07-19 00:57:47
123_RFID1,pass1,150.0,2,5,2024-01-15,14,location1,2024-07-19 00:57:52
123_RFID1,pass1,150.0,2,5,2024-01-15,12,location1,2024-07-19 00:57:55
456_RFID2,pass2,40.0,1,4,20224-01-14,2,location1,2024-07-19 00:58:08
456_RFID2,pass2,40.0,1,4,20224-01-14,666,location1,2024-07-19 00:58:14
456_RFID2,pass2,40.0,1,4,20224-01-14,13,location1,2024-07-19 00:58:18
789_RFID3,pass3,20.0,0,0,2024-02-01,,,
147_NoRFID,pass4,0,,,,,,
159_NoRFID,pass5,0,,,,,,
"""

def update_csv(Updated_Data):
    Account_Info = 'passwords.csv'
    Reservation_Info = 'reserveList.csv'
    
    # Initialize dictionaries to store data to be written back to CSVs
    updated_account_info = []
    updated_reservation_info = []

    for entry in Updated_Data:
        user_id = entry['id']
        book_info = {
            'id': user_id,
            'bookId': entry['bookId'],
            'location': entry['location'],
            'date': entry['date']
        }
        
        account_info = {
            'username': user_id,
            'password': entry['password'],
            'account_balance': entry['account_balance'],
            'fines': entry['fines'],
            'extensions': entry['extensions'],
            'rfid': entry['rfid'],
            'return_date': entry['return_date']
        }

        updated_account_info.append(book_info)
        updated_reservation_info.append(account_info)
    
    # Remove duplicates from updated_reservation_info
    updated_reservation_info_unique = {entry['username']: entry for entry in updated_reservation_info}.values()

    # Write back to passwords.csv
    with open(Account_Info, mode='w', newline='') as file:
        fieldnames = ['id', 'bookId', 'location', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_account_info)
    
    # Write back to reserveList.csv
    with open(Reservation_Info, mode='w', newline='') as file:
        fieldnames = ['username', 'password', 'account_balance', 'fines', 'extensions', 'rfid', 'return_date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_reservation_info_unique)


