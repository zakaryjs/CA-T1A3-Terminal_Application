import pytest
import csv
from calendar_functions import add_calendar, get_date, delete_calendar

test_file_name = "tests/test_calendar.csv"
test_file_name2 = "tests/test_calendar2.csv"


def test_add(monkeypatch):
   inputs = iter(['Test', 'March', '11', ''])
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   add_calendar(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length + 1

   inputs = iter(['Test 2', 'April', '12', ''])
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   add_calendar(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length + 1

def test_get_date(monkeypatch):
    inputs = iter(['' ''])
    assert get_date

def test_delete(monkeypatch):
   inputs = iter(['Test', ''])
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   delete_calendar(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length - 1

   inputs = iter(['Test3', ''])
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   delete_calendar(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length - 1