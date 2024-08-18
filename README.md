
# Automated Book Loan and Return System

This is an automated system designed to promote reading by streamlining the process of borrowing and returning books.

## Description

The Automated Book Loan and Return System is designed to encourage and increase the number of people reading and borrowing books from public libraries. The system allows users to reserve, borrow, and return books seamlessly via an online platform or mobile app. Users can manage their book reservations and loans efficiently, making library visits more convenient.

[Watch Demo Video](https://drive.google.com/file/d/1fgF0ec8k3hH4ev1GFfw3ZyXC4f_n21cS/view?usp=sharing)

## Features

- **Online Book Reservation**: Users can select and reserve books online via a website.
- **Branch Selection**: Users can choose the library branch from which they would like to collect their books.
- **Automatic Reservation Cancellation**: Reservations not collected within 5 days are automatically canceled.
- **Loan Period Management**: Books can be borrowed for 18 days with an option to renew once for an additional 7 days.
- **Borrowing Limit**: Users can borrow a maximum of 10 books at any time.
- **Fine Calculation**: A fine of $0.15 per book per day is imposed for late returns.
- **Fine Payment**: Users must clear any outstanding fines using an RFID card reader before collecting new book reservations.
- **Automated Book Dispensing**: After scanning their NRIC or SP Student Card, authenticated users can collect their reserved books from the automated system.

## Prerequisites

- Web server (HTML)
- Keypad
- RFID card
- RFID reader
- Barcode
- Pi camera (to scan barcode)

## Usage

### 1. User Registration
Users must register on the platform using their NRIC or SP Student Card details.

### 2. Book Search and Reservation
Users can search for books and reserve them online.

### 3. Branch Selection
During reservation, users select the library branch for book collection.

### 4. Collection of Books
Users must collect their reserved books within 5 days by scanning their card at the library.

### 5. Return and Renewal
Books must be returned within 18 days, with an option to renew once for an additional 7 days.

## Book Reservation

- Search for the book you wish to borrow.
- Select the book and choose your preferred library branch for collection.
- Confirm your reservation.

## Book Collection

- Visit the selected library branch within 5 days of reservation.
- Scan your NRIC or SP Student Card at the automated system.
- After authentication, collect your reserved books from the dispenser.

## Loan Period and Renewals

- The standard loan period for each book is 18 days.
- You can renew a book once for an additional 7 days if no other reservations exist for the book.
- Failure to return books on time will result in a fine.

## Fines and Payments

- A fine of $0.15 per book per day will be charged for late returns.
- Users must pay any outstanding fines at the library's machine using the RFID card reader.
- Only after clearing fines will users be allowed to collect new book reservations.

## Docker Commands

```bash
cd ET0735/DCPE_2A_02_Group5/
docker build -t library .
docker run -it -p 5000:5000 --privileged=true library
docker exec -it [container_name] sh
docker ps
docker exec -it [container_name] sh
cat reserveList.csv
```

## Distribution of Tasks

- **Xin Jun**: Website, integration, troubleshooting
- **Joel**: RFID reader, calculate fines, integration, calculate extension
- **Jaslyn**: Pi camera, Readme document
- **Jia Yi**: Pytest, SRS, Readme document
