import requests

BASE_URL = 'http://127.0.0.1:5000'

def getReserve():
    try:
        url = f'{BASE_URL}/reservations'
        response = requests.get(url)
        bookList = response.json()
    except:
        return [{}, {}]
    
    return bookList

def main():
    print(getReserve())

if __name__ == '__main__':
    main()