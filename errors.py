try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    assert age > 0
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value.')
except AssertionError:
    print("age can't be negative.")

