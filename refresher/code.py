#pylint: disable-all

def age_to_months():
    age = input('Hello what is your age? >> ')
    months = 12*int(age)
    print(f"Your age: {age} years is equivalent to {months} months")
    print('BYE')
    return

if __name__ == '__main__':
    print('hello')
    age_to_months()