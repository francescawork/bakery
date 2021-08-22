# time
day_count = 1

# counts
money_count = 1.5
dough_count = 0
bread_count = 0

# costs
dough_cost = 1.5
bread_cost = 1
bread_sell_cost = 3


def main():
    global day_count
    global money_count
    global dough_count
    global bread_count

    while True:
        # start of day - print summary
        print(f"This is day #{day_count} of your bakery. You have ${money_count} dollars, {dough_count} dough, and {bread_count} bread.")
        input()

        # display options
        print_options()
        process_choice()

        # if statement for option 1, 2, 3. Else goes back to original question
        # print consequence of player input
        day_count += 1


# This function will display all the options available to the player
def print_options():
    global dough_cost
    global bread_cost
    global bread_sell_cost

    print("What would you like to do for the day? Type the number next to the option.")
    print()
    print(f"1 - Buy some dough. Cost: ${dough_cost}")
    print()
    print(f"2 - Make some bread. Requires at least {bread_cost} dough.")
    print()
    print(f"3 - Sell some bread. You will receive ${bread_sell_cost}.")
    print()


def process_choice():
    global dough_count, bread_count, money_count

    while True:
        choice = input("")
        if choice == "1":
            # buy dough, subtract $1.5
            if money_count < dough_cost:
                print(f"You don't have enough money, you need at least ${dough_cost}. Please select another option.")
            else:
                dough_count += 1
                money_count -= dough_cost
                print(f"Dough was purchased for ${dough_cost}. You now have {dough_count} dough, and ${money_count}")
                break
        elif choice == "2":
            # subtract 1 dough, add 1 bread
            if dough_count < 1:
                print(f"You have {dough_count} dough, and require at least {bread_cost}. "
                      f"Please select another option.")
            else:
                dough_count -= bread_cost
                bread_count += 1
                print(f"A loaf of bread was baked. You now have {bread_count} bread, and {dough_count} dough.")
                break
        elif choice == "3":
            # minus 1 bread, add #3
            if bread_count < 1:
                print("You don't have enough bread to sell! You need at least 1 bread. Please select another option.")
            else:
                bread_count -= 1
                money_count += bread_sell_cost
                print(f"A loaf of bread was sold for ${bread_sell_cost}. You now have {bread_count} bread, and ${money_count}.")
                break
        else:
            print(f"'{choice}' is an incorrect option. Please select another option.")


if __name__ == "__main__":
    main()
