from utils import  numberAdder, print_plays_data


#to do list
#
# reading from XML
# python coding 
# github actions


if __name__ == "__main__":
    print("This is the main entry point of the program.")
    print_plays_data(True, "plays.xml")
    print('------------------------------')
    print_plays_data(False, "newPlays.xml")