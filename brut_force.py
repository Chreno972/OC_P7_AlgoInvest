"""
Brute force algorithm
"""
#Python installed library
from itertools import combinations as cbts

# Python native libraries
import csv
import time


class DataSet:
    """Represents an action object.

    Returns:
        tuple: an action object to a tuple.
    """

    liste_dataset = []

    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.liste_dataset.append(self)

    def serialize_dataset(self):
        """converts actions to a list of tuples.

        Returns:
            tuple: a tuple of all the attributes of the action object.
        """
        dataset = (self.name, int(float(self.price)), float(self.profit))
        return dataset

    def __repr__(self):
        """Return a string representation of this object.

        Returns:
            tuple : (name, price, profit)
        """
        return "{} {} {}".format(self.name, self.price, self.profit)


def brute_force_algo(money):
    """Brute force function"""

    # CSV_DATA actions
    data_set = []
    # .csv dataset
    the_csv_file = "./csv/BruteForce.csv"
    # final selected actions
    the_combinations = []

    # extracting the data from the .csv file to the data_set list
    with open(the_csv_file, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for elem in reader:
            action_percentage = float(elem["price"]) * float(elem["profit"]) / 100
            # each action is a DataSet instance or object
            data_set.append(
                DataSet(
                    elem["name"], elem["price"], action_percentage
                ).serialize_dataset()
            )


    # Creates all possible combinations
    for i in range(1, len(data_set) + 1):  # O(n)
        for combination in cbts(data_set, i):  # O(n)
            for elem in combination:  # O(n)
                if elem[1] <= 0:
                    pass
                elif sum(elem[1] for elem in combination) <= money:  # O(n)
                    the_combinations.append(combination)  # O(1)

    best_combination = max(
        the_combinations, key=lambda x: sum(elem[2] for elem in x)  # O(n)
    )

    total_investment = sum(x[1] for x in best_combination)
    total_profit = sum(x[2] for x in best_combination)

    # Reports the results in the terminal
    print("\nThe best combination is:\n")
    print("NAME      |PRICE|PROFIT")
    for elem in best_combination:  # O(n)
        print("______________________")  # O(1)
        print(f"{elem[0]} | {elem[1]} | {elem[2]}   ")  # O(1)
    print(f"\nFor a total investment of {total_investment}€")
    print(f"You'll get a profit of {round(total_profit, 2)}€ after 2 years")

    # Reports my results to a .txt file in order to compare with Sienna's
    with open("./rapports/decision_investissement_christophe.txt", "a") as exp:
        exp.write("From the BruteForce.csv dataset, Christophe bought:\n\n")
        for count, value in enumerate(best_combination):
            exp.write(
                f"{value[0]} - {round(value[2], 2)}\n"
            )
        exp.write("\n\nTotal Cost: {} Euros\n".format(total_investment))
        exp.write("Total Profit: {} Euros\n".format(round(total_profit, 2)))
        exp.write(f"So a {round(total_profit / total_investment * 100, 2)}% ROI\n")
        exp.write('\n')
        exp.write('------------------------------------------------------')
        exp.write('\n\n')


if __name__ == "__main__":
    start_time = time.time()
    brute_force_algo(500)  # O(n)
    print("\nProgram executed in %s seconds" % (round(time.time() - start_time, 2)))
