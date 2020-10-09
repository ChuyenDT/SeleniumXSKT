
from howday import get_data_from_brower
from probability import probability_one
from probability2 import probability_two
from number import number_max
import os
def remover_file():
    os.remove('30day.txt')
    os.remove('probability.txt')
    os.remove('probability2.txt')
def main():
    remover_file()
    get_data_from_brower()
    probability_one()
    probability_two()
    number_max()
if __name__ == "__main__":
    main()