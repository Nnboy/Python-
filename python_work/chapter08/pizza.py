def make_pizza(size, *toppings):
    """[做披萨]

    Args:
        size ([int]): [披萨的大小]
    """
    print('\nMaking a ' + str(size) +
          "-inch pizza with the: ")
    for topping in toppings:
        print("- " + topping)
