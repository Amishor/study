def the_calc():
    formula = input()
    for i in formula:
        if i.isalpha():
            print('Use numbers or operation signs!')
            the_calc()
        elif i.isnumeric():
            pass
    else:
        print(eval(formula))


the_calc()
