import csv
import time

actions = []
dataset1 = "./csv/dataset1_Python+P7.csv"

with open(dataset1) as csv_file:
    csv_list = list(csv.reader(csv_file))
    for action in csv_list[1:]:
        if float(action[1]) <= 0 or float(action[2]) <= 0:
            pass
        else:
            sum_prices_profits = round(float(action[1]) * float(action[2])) / 100
            actions.append([action[0], round(float(action[1])), sum_prices_profits])


def optimized_algorithm(budget, elements):
    nb_elements = len(elements)
    matrice = [[0 for x in range(budget + 1)] for y in range(nb_elements + 1)]

    for i in range(nb_elements + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                matrice[i][w] = 0
            elif elements[i - 1][1] <= w:
                matrice[i][w] = max(
                    elements[i - 1][2] + matrice[i - 1][w - elements[i - 1][1]],
                    matrice[i - 1][w],
                )
            else:
                matrice[i][w] = matrice[i - 1][w]

    profit = matrice[nb_elements][budget]
    final_elements = []
    for i in range(nb_elements, 0, -1):
        if profit - elements[i - 1][2] < 0:
            break
        if profit == matrice[i - 1][budget]:
            continue
        else:
            if elements[i - 1][1] < budget and elements[i - 1][2] > 0:
                final_elements.append(elements[i - 1])
                budget -= elements[i - 1][1]

    actions_names = [x[0] for x in final_elements]
    investissement = sum([(x[1]) for x in final_elements])

    """ RÉSULTATS """
    print(f"\nIl faut choisir les {len(final_elements)} actions suivantes:\n")
    print(actions_names)
    print(f"")
    print(f"\nPour un investissement de {investissement}€")
    print(f"\nVous gagnerez : {round(profit, 2)}€")
    print(
        f"\nCela équivaut à un retour sur investissement de {round(profit / investissement * 100, 2)}%"
    )

    with open("./rapports/decision_investissement_christophe.txt", "a") as exp:
        exp.write("From the dataset1_Python+P7.csv dataset, Christophe bought:\n\n")
        for count, value in enumerate(final_elements):
            exp.write(
                f"{value[0]} - {round(value[2], 2)}\n"
            )
        exp.write("\n\nTotal Cost: {} Euros\n".format(investissement))
        exp.write("Total Profit: {} Euros\n".format(round(profit, 2)))
        exp.write(f"So a {round(profit / investissement * 100, 2)}% ROI\n")
        exp.write('\n')
        exp.write('------------------------------------------------------')
        exp.write('\n\n')

if __name__ == "__main__":
    start_time = time.time()
    optimized_algorithm(500, actions)
    print("\nProgram executed in %s seconds" % (round(time.time() - start_time, 2)))