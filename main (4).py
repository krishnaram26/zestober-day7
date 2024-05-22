date = int(input())

if date % 400 == 0 or date % 100 != 0 and date % 4 == 0:
  print("true")
else:
  print("false")