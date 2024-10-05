
#אשתמש ב try, except אם אני רוצה להגן על התכנית שלי מלקרוס במקרה בו הוזנה שגיאה

#כדאי לתפוס שגיאות בפייטון כדי שבמקרה שטעינו בקוד נדע איפה הטעות ואיפה יש שגיאה שהיא בסדר להרצת התכנית

x: int = 0
try:
    print(88 / x)
except ZeroDivisionError:
    print("can't divide by zero")

###

height: float = float(input("Enter your height in m: "))
if height > 2.0:
    raise ValueError
print("value is ok")

try:
    print(height)
except ValueError:
    print("value is ok")

###

numbers: list[int] = [2, 9, 0, 7]
index: int = int(input("Enter index: "))

while index != -999:
    if index <= len(numbers):
        index: int = int(input("Enter index: "))
        print(numbers.pop(index))
    try:
        index is str
    except ValueError:
        print("value is not a number")