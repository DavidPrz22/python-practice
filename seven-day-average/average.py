import csv
import requests
import sys

states_data = [ "Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming" ]

def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    csv_reader = []

    for i in reader:
        csv_reader.append(i)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(csv_reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in states_data:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    length = len(reader)
    days = 14 + 1               # 14 days plus a day before to calculate new cases for first day
    range_reader = days * 56    # data of 56 states during 56 days
    
    new_recorded_cases = []

    for state in states_data:

        previous_case = None
        count = 0

        for cases in reader[length - range_reader: length]:

            if state == cases["state"]:
                if count == 0 and previous_case == None:
                    previous_case = int(cases["cases"])
                    count += 1
                    continue
                else:
                    new_cases = int(cases["cases"]) - previous_case
                    previous_case = int(cases["cases"])

                    new_recorded_cases.append({"state": state, "cases": new_cases, "day": count})
                    count += 1

    return new_recorded_cases
    

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    
    print(states)
    for state in states:

        states_avg = [case for case in new_cases if case["state"] == state]

        try:
            length = len(states_avg)

            previous_week_avg = round(sum(int(state["cases"]) for state in states_avg[0 : int(length / 2)]) / 7, 3)
            last_week_avg = round(sum(int(state["cases"]) for state in states_avg[int(length / 2) : length]) / 7, 3)
            
            diff = previous_week_avg - last_week_avg

            if diff < 0:
                decrease = (abs(diff) / last_week_avg) * 100
                print(f"In {state} was a {decrease:.2f}% decrease in cases")
            else:
                increase = (abs(diff) / last_week_avg) * 100
                print(f"In {state} was a {increase:.2f}% increase in cases")

        except ZeroDivisionError:
            print("Can't divide by zero")


main()
