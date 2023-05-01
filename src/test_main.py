import pytest
import csv
from calendar_functions import add_calendar

test_file_name = "tests/test_calendar.csv"


def test_add(monkeypatch):
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: "Calendar 1")
   add_calendar(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length + 1