def checkio(number):
    if number % 16 == 0:
        return 'Fizz Buzz'
    if number % 6 == 0:
        return 'Buzz'
    if number % 4 == 0:
        return 'Fizz'
    return str(number)