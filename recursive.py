"""
Recursive algorithm
"""
import csv
import time

# CSV_DATA actions
actions = []
# .csv dataset
CSV_DATA = "./csv/BruteForce.csv"
# final selected actions (func call)
sel = []

# extracting the data from the .csv file to the actions list
with open(CSV_DATA) as csv_file:
    csv_list = list(csv.reader(csv_file))

    # drop unusable actions, sum action's price with profit %
    for action in csv_list[1:]:
        if float(action[1]) > 0 and float(action[2]) > 0:
            sum_prices_profits = round(float(action[1]) * float(action[2])) / 100
            actions.append([action[0], round(float(action[1])), sum_prices_profits])


def solution_recursive(capacite, elements, elements_selection):
    """
    Recursive solution

    Args:
        capacite (int): the max budget
        elements (list of tuples): the actions list
        elements_selection (list): the best combination list.

    Returns:
        string templates: two strings templates containing the results
    """

    if elements:
        val1, lstvalone = solution_recursive(capacite, elements[1:], elements_selection)
        val = elements[0]

        if val[1] <= capacite:
            val2, lstvaltwo = solution_recursive(
                capacite - val[1], elements[1:], elements_selection + [val]
            )

            if val1 < val2:
                return val2, lstvaltwo

        return val1, lstvalone

    choix = [i[0] for i in elements_selection]
    total = round(sum([i[1] for i in elements_selection]), 2)
    profit_total = (
        f"Profit {round(sum([i[2] for i in elements_selection]), 2)}€ sur 2 ans"
    )
    actions_choisies = f"Choix: {choix} Gains: {total}€"

    return profit_total, actions_choisies


if __name__ == "__main__":
    start_time = time.time()
    print(solution_recursive(500, actions, sel))
    print("\nProgram executed in %s seconds" % (round(time.time() - start_time, 2)))
    
