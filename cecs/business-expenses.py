# Comment on main()
def main():
    total = 0
    total_excess = 0
    days = get_days()
    departure = get_time()
    airfare = get_airfare()
    car_rental = get_car_rental(days)
    miles = get_miles()
    parking_fees = get_parking_fees(days)
    taxi_fees = get_taxi_fees(days)
    registration_fees = get_registration_fee()
    hotel_fees = get_hotel_fees(days)
    breakfast = get_breakfast(days, departure)
    lunch = get_lunch(days, departure)
    dinner = get_dinner(days, departure)
    # After all the functions are finished, main() prints summary using the returned value from each function.
    print("Here is a summary:")

    print("You were away for", days, "Days.")

    print("The time was", departure[0], "when you departed from home and", departure[1], "when you arrived home.")

    print("Your total was", "$"+str(airfare), "for the airfare.")

    print("Your total was", "$"+str(car_rental), "for your rented vehicle.")

    print("You accrued", "$"+str(miles[0]), "worth of driving fees during your trip at 27 cents a mile. Overall, you"
          " traveled", miles[1], "miles.")

    if parking_fees[0] > 0:
        print("Your total was", "$"+str(parking_fees[0]), "for parking,", "$"+str(parking_fees[1]), "was the total"
              " excess you accumulated from the company at $6 a day.")
    else:
        print("Your total was,", "$"+str(parking_fees[0]), "for parking and the company covered",
              "$"+str(parking_fees[1]), "meaning you don't owe anything.")

    if taxi_fees[0] > 0:
        print("Your total was", "$"+str(taxi_fees[0]), "for taxi fees,", "$"+str(taxi_fees[1]), "was the total excess"
              " you accumulated from the company at $10 a day.")
    else:
        print("Your total was", "$"+str(taxi_fees[0]), "for taxi fees and your company covered",
              "$"+str(taxi_fees[1]), "meaning you don't owe anything.")

    print("Your total was", "$"+str(registration_fees), "for conference/seminar registration fees.")

    if hotel_fees[0] > 0:
        print("Your total was", "$"+str(hotel_fees[0]), "for your hotel,", "$"+str(hotel_fees[1]), "was the total"
              " excess you accumulated from the company at $90 a day.")
    else:
        print("Your total was", "$"+str(hotel_fees[0]), "for your hotel and your company covered",
              "$"+str(hotel_fees[1]), "meaning you don't owe anything.")

    if breakfast[0] > 0:
        print("Your total was", "$"+str(breakfast[0]), "for breakfast,", "$"+str(breakfast[1]), "was the total excess"
              " you accumulated from the company at $9 a day.")
    else:
        print("Your total was", "$" + str(breakfast[0]), "for breakfast and your company covered",
              "$" + str(breakfast[1]), "meaning you don't owe anything.")

    if lunch[0] > 0:
        print("Your total was", "$"+str(lunch[0]), "for lunch,", "$"+str(lunch[1]), "was the total excess you"
              " accumulated from the company at $12 a day.")
    else:
        print("Your total was", "$" + str(lunch[0]), "for lunch and your company covered",
              "$" + str(lunch[1]), "meaning you don't owe anything.")

    if dinner[0] > 0:
        print("Your total was", "$"+str(dinner[0]), "for dinner,", "$"+str(dinner[1]), "was the total excess you"
              " accumulated from the company at $16 a day.")
    else:
        print("Your total was", "$" + str(dinner[0]), "for dinner and your company covered",
              "$" + str(dinner[1]), "meaning you don't owe anything.")

    total += airfare + car_rental + miles[0] + parking_fees[0] + taxi_fees[0] + registration_fees + hotel_fees[0] \
                     + breakfast[0] + lunch[0] + dinner[0]

    print("Overall, including deductibles, you spent", "$"+str(total)+".")

    total_excess += parking_fees[1] + taxi_fees[1] + hotel_fees[1] + breakfast[1] + lunch[1] + dinner[1]
    print("Overall, your company covered", "$"+str(total_excess)+".")

    no_deductible_total = total - total_excess
    if no_deductible_total > 0:
        print("Overall, not including deductibles, you spent", "$"+str(no_deductible_total)+".")
    else:
        print("Overall, not including deductibles, you saved", "$"+str((abs(no_deductible_total))))

# Function gets input and returns it to main() if it is >= 1
def get_days():
    days = int(input("Enter the amount of days the trip lasted:" + "\n"))
    # Input validation
    while days < 1:
        days = int(input("The trip must be at least one day long." + "\n"))

    return days

# Function gets time in (HH.MM) format for 2 variables, restricts them between 0-24, then returns them to main()
def get_time():
    departure = float(input("Enter the time you departed from home in the 24-hour format (HH.MM)." + "\n"))
    # Input validation with relation to departure
    while departure > 23.59 or departure < 0:
        departure = float(input("Invalid departure, enter departure time in 24-hour format (HH.MM)." + "\n"))

    arrival = float(input("Enter the time you arrived home in the 24-hour format (HH.MM)." + "\n"))
    # Input validation with relation to arrival
    while arrival > 23.59 or arrival < 0:
        arrival = float(input("Invalid arrival, enter departure time in 24-hour format (HH.MM)." + "\n"))

    return departure, arrival

# Function gets input then returns it to main() if > 0
def get_airfare():
    airfare = float(input("Enter your round-trip airfare." + "\n"))
    # Input validation
    while airfare < 0:
        airfare = float(input("Airfare must be at least 0." + "\n"))

    return airfare

# Function gets input and restricts the input to n or y. If n is input, 0 is returned to main() and if y is input, the
# user is then prompted to answer details about the price/fees. Then the function calculates the total and returns it to
# main() assuming it is >= 0
def get_car_rental(max_days):
    total = 0

    car = input("Did you rent a vehicle for this trip? Enter y/n" + "\n")
    # Input Validation
    while car not in ["y", "n"]:
        car = input("Invalid Input. Did you rent a vehicle for this trip? Enter y/n" + "\n")

    if car == "y":
        fee = float(input("Enter the daily fee for the vehicle." + "\n"))
        # Input validation
        while fee < 0:
            fee = float(input("Invalid Input. The fee must be at least 0." + "\n"))

        days = int(input("Enter the total days you rented the vehicle for." + "\n"))
        # Input validation
        while days < 1 or days > max_days:
            days = int(input("Invalid input. The total days must be greater than 0 and less than days you"
                             " were on the trip." + "\n"))

        total += fee * days
    elif car == "n":
        total = 0
    return total

# Function gets input and restricts the input to n or y. If n is input, 0 is returned to main() and if y is input, the
# user is then prompted to answer certain questions. Then the function calculates the total and returns it to main()
# assuming it is >= 0 along with company excess
def get_miles():
    total_cost = 0.27
    miles_driven = 0
    car = input("Did you use a private vehicle for this trip? Enter y/n" + "\n")
    # Input validation
    while car not in ["y", "n"]:
        car = input("Invalid Input. Did you use a private vehicle for this trip? Enter y/n" + "\n")

    if car == "y":
        miles = float(input("How many miles did you drive?" + "\n"))
        # Input validation
        while miles < 1:
            miles = float(input("Invalid Input. Miles must be at least 1." + "\n"))

        miles_driven += miles
        total_cost *= miles
    elif car == "n":
        total_cost *= 0
    return total_cost, miles_driven

# Function gets input and restricts the input to n or y. If n is input, 0 is returned to main() and if y is input, the
# user is then prompted to answer certain questions. Then the function calculates the total and returns it to main()
# assuming it is >= 0 along with company excess
def get_parking_fees(max_days):
    total_parking = 0
    total_excess = 6
    car = input("Did you accrue any parking fees during your trip? y/n" + "\n")
    # Input validation
    while car not in ["y", "n"]:
        car = input("Invalid Input. Did you accrue any parking fees during your trip? y/n" + "\n")

    if car == "y":
        days = int(input("How many days did you park?" + "\n"))
        # Input validation
        while days < 1 or days > max_days:
            days = int(input("Invalid input. Days must be greater than 0 and less than the days you were on the trip."
                             + "\n"))

        parking = float(input("How much was parking overall? The company's excess will automatically be deducted."
                                 + "\n"))
        # Input validation
        while parking < 1:
            days = float(input("Invalid input. Parking must be greater than 0." + "\n"))

        total_excess *= days
        total_parking += parking - total_excess
    elif car == "n":
        total_parking = 0
    return total_parking, total_excess

# Function gets input and restricts the input to n or y. If n is input, 0 is returned to main() and if y is input, the
# user is then prompted to answer certain questions. Then the function calculates the total and returns it to main()
# assuming it is >= 0 along with company excess
def get_taxi_fees(max_days):
    total_cost = 0
    total_excess = 10
    taxi = input("Did you use a taxi during this trip? Enter y/n" + "\n")
    while taxi not in ["y", "n"]:
        # Input validation
        taxi = input("Invalid Input. Did you use a taxi during this trip? Enter y/n" + "\n")

    if taxi == "y":
        days = int(input("How many days did you use a taxi?" + "\n"))
        while days < 1 or days > max_days:
            # Input validation
            days = int(input("Invalid input. Days must be greater than 0 and less than the amount of days you"
                             " were on the trip." + "\n"))

        cost = float(input("How much were the taxi fees overall? The company's excess will automatically be deducted." +
                           "\n"))
        while cost < 1:
            # Input validation
            float(input("Invalid input. Cost must be greater than 0." + "\n"))

        total_excess *= days
        total_cost += cost - total_excess
    elif taxi == "n":
        total_cost = 0
    return total_cost, total_excess

# Function gets input and returns it if its an integer
def get_registration_fee():
    fees = float(input("Enter and conference/seminar fees if any." + "\n"))
    # Input validation
    while fees < 0:
        fees = float(input("Invalid Input. Enter and conference/seminar fees or 0 if there were no fees." + "\n"))

    return fees

# Function gets input on user hotel the calculates the total and returns along with company excess
def get_hotel_fees(max_days):
    total_cost = 0
    total_excess = 90
    fees = float(input("Enter how much you spent overall during your stay at your hotel." + "\n"))
    # Input validation
    while fees < 0:
        fees = float(input("Invalid input. Fees must be at least 0." + "\n"))

    days = int(input("Enter how many days you stayed at your hotel." + "\n"))
    # Input validation
    while days < 0 or days > max_days:
        days = int(input("Invalid Input. Days must greater than 0 and the days you were on the trip." + "\n"))

    total_excess *= days
    total_cost += fees - total_excess
    return total_cost, total_excess

# Gets user input depending on what time the departed to their destination/arrived home. Gets the cost of each meal
# then returns the total with company excess.
def get_breakfast(days, departure):
    breakfast_total = 0
    breakfast_excess = 9
    if departure[0] < 7.0:
        if departure[1] >= 8.0:
            # departure < 7 a.m + arrival home > 8 a.m
            print("Since you departed before 7 a.m and returned home after 8 a.m, 2 meals are covered by company"
                  " expenses. Enter the prices of all breakfast meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                breakfast_total += meals
            breakfast_excess *= days
            breakfast_total -= breakfast_excess
            return breakfast_total, breakfast_excess
        elif departure[1] < 8.0:
            # departure < 7 a.m + arrival home < 8 a.m
            print("Since you departed before 7 a.m but returned home before 8 a.m, only your departure breakfast is"
                  " covered by the company. Enter the prices of all breakfast meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                breakfast_total += meals
            breakfast_excess *= days - 1
            breakfast_total -= breakfast_excess
            return breakfast_total, breakfast_excess
    if departure[0] >= 7.0:
        if departure[1] >= 8.0:
            # departure > 7 a.m + arrival home > 8 a.m
            print("Since you departed after 7 a.m but returned home after 8 a.m, only your arrival breakfast is covered"
                  " by company expenses. Enter the prices of all breakfast meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                breakfast_total += meals
            breakfast_excess *= days - 1
            breakfast_total -= breakfast_excess
            return breakfast_total, breakfast_excess
        elif departure[1] < 8.0:
            # departure > 7 a.m + arrival < 8 a.m
            print("Since you departed after 7 a.m and returned home before 8 a.m, 2 meals are NOT covered by company"
                  " expenses. Enter the prices of all breakfast meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                breakfast_total += meals
            breakfast_excess *= days - 2
            breakfast_total -= breakfast_excess
            return breakfast_total, breakfast_excess


# Gets user input depending on what time the departed to their destination/arrived home. Gets the cost of each meal
# then returns the total with company excess.
def get_lunch(days, departure):
    lunch_total = 0
    lunch_excess = 12
    if departure[0] < 12.0:
        if departure[1] >= 13.0:
            # departure < 12 p.m + arrival home > 1 p.m
            print("Since you departed before 12 p.m and returned home after 1 p.m, 2 meals are covered by company"
                  " expenses. Enter the prices of all lunch meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                lunch_total += meals
            lunch_excess *= days
            lunch_total -= lunch_excess
            return lunch_total, lunch_excess
        elif departure[1] < 13.0:
            # departure < 12 p.m + arrival home < 1 p.m
            print("Since you departed before 12 p.m but returned home before 1 p.m, only your departure lunch is"
                  " covered by the company. Enter the prices of all lunch meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                lunch_total += meals
            lunch_excess *= days - 1
            lunch_total -= lunch_excess
            return lunch_total, lunch_excess
    if departure[0] >= 12.0:
        if departure[1] >= 13.0:
            # departure > 12 p.m + arrival home > 1 p.m
            print("Since you departed after 12 p.m but returned home after 1 p.m, only your arrival lunch is covered by"
                  " company expenses. Enter the prices of all lunch meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                lunch_total += meals
            lunch_excess *= days - 1
            lunch_total -= lunch_excess
            return lunch_total, lunch_excess
        elif departure[1] < 13.0:
            # departure > 12 p.m + arrival home < 1 p.m
            print("Since you departed after 12 p.m and returned home before 1 p.m, 2 meals are NOT covered by company"
                  " expenses. Enter the prices of all lunch meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                lunch_total += meals
            lunch_excess *= days - 2
            lunch_total -= lunch_excess
            return lunch_total, lunch_excess


# Gets user input depending on what time the departed to their destination/arrived home. Gets the cost of each meal
# then returns the total with company excess.
def get_dinner(days, departure):
    dinner_total = 0
    dinner_excess = 16
    if departure[0] < 18.0:
        if departure[1] >= 19.0:
            # departure < 6 p.m + arrival home > 7 p.m
            print("Since you departed before 6 p.m and returned home after 7 p.m, 2 meals are covered by company"
                  " expenses. Enter the prices of all dinner meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                dinner_total += meals
            dinner_excess *= days
            dinner_total -= dinner_excess
            return dinner_total, dinner_excess
        elif departure[1] < 19.0:
            # departure < 6 p.m + arrival home < 7 p.m
            print("Since you departed before 6 p.m but returned home before 7 p.m, only your departure dinner is"
                  " covered by the company. Enter the prices of all dinner meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                dinner_total += meals
            dinner_excess *= days - 1
            dinner_total -= dinner_excess
            return dinner_total, dinner_excess
    if departure[0] >= 18.0:
        if departure[1] >= 19.0:
            # departure > 6 p.m + arrival home > 7 p.m
            print("Since you departed after 6 p.m but returned home after 7 p.m, only your arrival dinner is covered by"
                  "company expenses. Enter the prices of all dinner meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                dinner_total += meals
            dinner_excess *= days - 1
            dinner_total -= dinner_excess
            return dinner_total, dinner_excess
        elif departure[1] < 19.0:
            # departure > 6 p.m + arrival home < 7 p.m
            print("Since you departed after 6 p.m and returned home before 7 p.m, 2 meals are NOT covered by company"
                  " expenses. Enter the prices of all dinner meals during your trip.")
            for b in range(days):
                print("Day", b + 1)
                meals = float(input(""))
                dinner_total += meals
            dinner_excess *= days - 2
            dinner_total -= dinner_excess
            return dinner_total, dinner_excess


main()
