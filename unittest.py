#!/usr/bin/python3

import calculator

def test_add():
    calculator.equal(str(2+3)) == 5
    calculator.equal(str(-2+3)) == 1
    calculator.equal(str(2+-3)) == -1
    calculator.equal(str(-2+-3)) == -5

def test_subtract():
    calculator.equal(str(5-3)) == 2
    calculator.equal(str(-5-3)) == -8
    calculator.equal(str(5--3)) == 8
    calculator.equal(str(-5--3)) == -2

def test_multiply():
    calculator.equal(str(2*3)) == 6
    calculator.equal(str(-2*3)) == -6
    calculator.equal(str(2*-3)) == -6
    calculator.equal(str(-2*-3)) == 6

if __name__ == '__main__':
    test_add()
    test_subtract()
    test_multiply()
    print('All tests passed!')