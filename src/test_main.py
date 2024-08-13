from datetime import datetime
import main as main


def test_filter_info():
  #Tests the filter_info function for various scenarios.

  # Scenario 1: Filter by account_id with matches
  reserveList = [
      {"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:37:58"},
      {"id": 123, "bookId": 9, "location": "location2", "date": "2024-07-19 00:57:42"},
      {"id": 456, "bookId": 2, "location": "borrowed", "date": "2024-07-19 00:58:08"},
  ]
  account_id = 123
  location = "location1"
  expected_result = [{"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:37:58"}]
  assert main.filter_info(account_id, location, reserveList) == expected_result

  # Scenario 2: Filter by account_id with no matches
  account_id = 789
  expected_result = []
  assert main.filter_info(account_id, location, reserveList) == expected_result

  # Scenario 3: Filter by location with matches
  account_id = 123
  location = "location2"
  expected_result = [{"id": 123, "bookId": 9, "location": "location2", "date": "2024-07-19 00:57:42"}]
  assert main.filter_info(account_id, location, reserveList) == expected_result

  # Scenario 4: Filter by both account_id and location with matches
  account_id = 123
  location = "location1"
  expected_result = [{"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:37:58"}]
  assert main.filter_info(account_id, location, reserveList) == expected_result

  # Scenario 5: Filter by both account_id and location with no matches
  account_id = 789
  location = "location3"
  expected_result = []
  assert main.filter_info(account_id, location, reserveList) == expected_result

  # Scenario 6: Empty reserveList
  reserveList = []
  account_id = 123
  location = "location1"
  expected_result = []
  assert main.filter_info(account_id, location, reserveList) == expected_result
    
def test_calculate_due_date():
    #Tests the calculate_due_date function for various scenarios.

    # Scenario 1: Normal calculation
    filtered_info = [{"id": 123, "bookId": 14, "location": "location1", "date": "2023-11-20"}]
    expected_due_date = datetime(2023, 11, 30)
    due_date, _ = main.calculate_due_date(filtered_info)
    assert due_date == expected_due_date

    # Scenario 2: Date parsing error
    filtered_info = [{"id": 123, "bookId": 14, "location": "location1", "date": "invalid_date"}]
    try:
        main.calculate_due_date(filtered_info)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    # Scenario 3: Empty filtered_info list
    filtered_info = []
    try:
        main.calculate_due_date(filtered_info)
        assert False, "Expected ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    test_calculate_due_date()

def test_calculate_fines():
    #Tests the calculate_fines function for various scenarios.

    # Scenario 1: No fines
    due_date = datetime(2024, 8, 1) #today's date
    expected_fines = 0.0
    fines = main.calculate_fines(due_date)
    assert fines == expected_fines

    # Scenario 2: Fines due
    due_date = datetime(2024, 7, 25)
    expected_fines = 0.9  # 6 days overdue * 0.15/day
    fines = main.calculate_fines(due_date)
    assert fines == expected_fines

    # Scenario 3: Negative days overdue (should be zero fines)
    due_date = datetime(2024, 8, 5)
    expected_fines = 0.0
    fines = main.calculate_fines(due_date)
    assert fines == expected_fines

if __name__ == "__main__":
    test_calculate_fines()

def test_book_extend_viability():
    filter_info =  [
    {"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:37:58"},
    {"id": 123, "bookId": 9, "location": "location2", "date": "2024-07-19 00:57:42"},
    {"id": 123, "bookId": 3, "location": "location2", "date": "2024-07-19 00:57:47"},
    {"id": 123, "bookId": 14, "location": "location1", "date": "2024-07-19 00:57:52"},
    {"id": 123, "bookId": 12, "location": "location1", "date": "2024-07-19 00:57:55"},
    {"id": 456, "bookId": 2, "location": "borrowed", "date": "2024-07-19 00:58:08"},
    {"id": 456, "bookId": 666, "location": "location1", "date": "2024-07-19 00:58:14"},
    {"id": 456, "bookId": 13, "location": "borrowed", "date": "2024-07-19 00:58:18"}
    ]
    # Scenario 1: Book can be extended (borrow date is within 18 days)
    filtered_info = [{"id": 123, "date": "2024-07-20 00:00:00"}]
    due_date = datetime.strptime("2024-07-27", "%Y-%m-%d").date()
    assert main.book_extend_viability(filtered_info, due_date) == True
"""
    # Scenario 2: Book cannot be extended (borrow date is more than 18 days)
    filtered_info = [{"id": 123, "date": "2024-07-06 00:00:00"}]
    due_date = datetime.strptime("2024-07-27", "%Y-%m-%d").date()
    assert main.book_extend_viability(filtered_info, due_date) == False

    # Scenario 3: Empty filtered_info list
    filtered_info = []
    due_date = datetime.strptime("2024-07-27", "%Y-%m-%d").date()
    assert main.book_extend_viability(filtered_info, due_date) == False"""

def test_book_extend():
    #Tests the book_extend function for various scenarios.

    # Scenario 1: Normal extension
    account_info = {"id": 123, "balance": 10.0}
    due_date = datetime(2024, 8, 1)
    expected_new_due_date = datetime(2024, 8, 8)
    new_due_date, _ = main.book_extend(account_info, due_date)
    assert new_due_date == expected_new_due_date

    # Scenario 2: Insufficient balance
    account_info = {"id": 123, "balance": 0.5}
    due_date = datetime(2024, 8, 1)
    try:
        main.book_extend(account_info, due_date)
        assert False, "Expected ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    test_book_extend()
