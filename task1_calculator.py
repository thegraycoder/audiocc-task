class Calculator(object):
    def __init__(self, expression: str):
        self.expression = expression.replace(' ', '')
        self.index = 0

    def calculate(self):
        if not self.expression or self.expression == '':
            return 0
        return self._calculate(self.expression)

    def _calculate(self, expression):
        previous_value = 0
        current_value = 0
        result = 0
        sign = '+'
        while self.index <= len(expression):
            c = expression[self.index] if self.index < len(expression) else '#'
            if c == '(':
                self.index += 1
                current_value = self._calculate(expression)
                continue
            if c.isdigit():
                current_value = 10 * current_value + int(c)
            if not c.isdigit() or c == '#' or c == ')':
                if sign == '+':
                    result += previous_value
                    previous_value = current_value
                elif sign == '-':
                    result += previous_value
                    previous_value = -current_value
                elif sign == '*':
                    previous_value = previous_value * current_value
                elif sign == '/':
                    previous_value = previous_value / current_value
                sign = c
                current_value = 0
            self.index += 1
            if c == ')' or c == '#':
                result += previous_value
                return result
        return result


if __name__ == '__main__':
    equation = input('Enter an expression to be calculated: ')
    calculator = Calculator(equation)
    print(f'The answer is: {calculator.calculate()}')
