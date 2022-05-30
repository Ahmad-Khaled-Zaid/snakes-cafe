def intro_message():
    return """$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""


menu = [{"name": "Wings", "counter": 0}, {"name": "Cookies", "counter": 0},
        {"name": "Spring Rolls", "counter": 0},
        {"name": "Entrees", "counter": 0}, {"name": "Salmon", "counter": 0}, {"name": "Steak", "counter": 0},
        {"name": "Meat Tornado", "counter": 0}, {"name": "A Literal Garden", "counter": 0},
        {"name": "Ice Cream", "counter": 0},
        {"name": "Cake", "counter": 0},
        {"name": "Pie", "counter": 0}, {"name": "Coffee", "counter": 0}, {"name": "Tea", "counter": 0},
        {"name": "Unicorn Tears", "counter": 0}
        ]

print(intro_message())
customer_input = ""

# keep asking about the order until entering quit
while customer_input != "quit":
    customer_input = input("> ")

    # check if the customer order available
    for element in menu:
        if customer_input == element["name"]:
            element["counter"] += 1

    # print the customer order
    for element in menu:
        if element["counter"] > 0:
            print(f'\n** {element["counter"]} order of {element["name"]} have been added to your meal **')
