#program sporoci True, ce je seznam narascujoc, drugace vrne False

input_list = 1, 2, 3, 4, 5
def strictly_ascending(input_list):

    previous = input_list[0]
    for el in input_list[1:]:
        if el <= previous:
            return False
        previous = el
    return True

print strictly_ascending(input_list)