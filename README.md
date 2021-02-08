# Audio CC - Application test

This project is a solution to the coding challenge solved by Kshitij Saxena as a part of interview process for `Audio CC`. The programming language of choice is `Python 3.7` and the dependencies are mentioned in `requirements.txt` file.

### How to run the program:
It is recommended to run the program using a virtualenv

```
$ cd audiocc-task
$ virtualenv venv
$ source venv/bin/activate

# Install requirements after activating the virtual environment
$ (venv) ➜ pip install -r requirements.txt

# Run unit tests
$ (venv) ➜ python -m unittest tests
 ..
 ----------------------------------------------------------------------
 Ran 2 tests in 0.020s
 
 OK

```

## Task 1 - Calculator
```
$ (venv) ➜ python task1_calculator.py 

Enter an expression to be calculated:  (5 + 8) * 3/8 +3
The answer is: 7.875

Enter an expression to be calculated: 8+9 + (3*6)  
The answer is: 35
```

## Task 2 - Peter Meditation
```
$ (venv) ➜ python task2_peter.py

Enter the number: 23245
Last number written down by Peter is: 22999

Enter the number: 11235888
Last number written down by Peter is: 11235888
```

## Task 3 - Simple X-Y Graph
```
$ (venv) ➜ python task3_graph.py

Enter an expression to be plotted: (5+x) * (x/3+8)
                       Simple X-Y Graph
┌────────────────────────────────────────────────────────────┐
│                                                          ▄▀│ 121,754
│                                                        ▄▛▘ │ 
│                                                      ▄▛▘   │ 
│                                                    ▄▛▘     │ 
│                                                  ▄▛▘       │ 92,248
│                                                ▄▛▘         │ 
│                                             ▗▟▀            │ 
│                                           ▄▞▀              │ 
│                                        ▗▄▀▘                │ 62,741
│                                      ▄▛▀                   │ 
│                                   ▄▟▀                      │ 
│                               ▗▄▞▀▘                        │ 
│                            ▄▄▛▀                            │ 33,234
│                        ▄▄▞▀▘                               │ 
│                   ▗▄▄▛▀▘                                   │ 
│             ▗▄▄▟▀▀▀                                        │ 
│▄▄▄▄▄▄▄▄▄▛▀▀▀▘                                              │ 3,728
└────────────────────────────────────────────────────────────┘
 1                                                        600

```