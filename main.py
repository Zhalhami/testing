class Calculator:
    def Add (self, a, b):
        return a + b

    def Subtract (self, a, b):
        return a - b

    def multiply (self, a, b):
        return a * b

    def divide (self, a, b):
        return a / b


cal = Calculator()

while True:
    print('1: Add')
    print('2: subtract')
    print('3: multiply')
    print('4: divide')
    print('5: exit')

    info = int(input('Choose number: '))

    if info in (1, 2, 3, 4, 5):

        if (info == 5):
          break

        a = int(input('Enter digit: '))
        b = int(input('Enter digit: '))
        if (info == 1):
            print(a, '+', b, '=', cal.Add(a, b))

        elif(info == 2):
            print(a, '-', b, '=', cal.Subtract(a, b))

        elif (info == 3):
            print(a, '*', b, '=', cal.multiply(a, b))

        elif (info == 4):
            print(a, '/', b, '=', cal.divide(a, b))


    else:
        print('Invalid digit')