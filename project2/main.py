#!/usr/bin/python3

def reminder_two_numbers(a, b):
   try:
    return a % b
  except ZeroDivisionError:
  
    return None
