from task1_calculator import Calculator
from uniplot import plot


def plot_expression(equation):
    y = []
    expressions = [equation.replace('x', str(i)) for i in range(600)]
    for expression in expressions:
        calc = Calculator(expression)
        y.append(calc.calculate())
    plot(y, title="Simple X-Y Graph")


if __name__ == '__main__':
    e = input('Enter an expression to be plotted: ')
    plot_expression(e)
