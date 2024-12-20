import re

def main():
    # Prompt the user to input a time range and process it
    time = input("Hours: ")
    print(convert(time))

def convert(time):
    """
    Convert a time range in the format 'HH:MM AM to HH:MM PM'
    into a 24-hour format, handling various cases for hour and minute inputs.
    """
    # Validate and parse the input using a regular expression
    if valid := re.search(r"^(?P<am_hour>\d|1[0-2]):?(?P<am_minutes>[0-5][0-9])? (AM) to (?P<pm_hour>\d|1[0-2]):?(?P<pm_minutes>[0-5][0-9])? (PM)$", time.strip()):
        # Extract AM hour and PM hour, converting PM hour to 24-hour format
        am_hour = int(valid.group("am_hour"))
        pm_hour = int(valid.group("pm_hour"))
        pm_hour_twentyfour = pm_hour + 12

        # Extract minutes if they exist; otherwise, set them to None
        if am_minutes := valid.group("am_minutes"):
            am_minutes = int(am_minutes)
        if pm_minutes := valid.group("pm_minutes"):
            pm_minutes = int(pm_minutes)

        # Handle various formatting cases based on the presence of hours and minutes
        # Case 1: AM hour < 10, no AM or PM minutes provided
        if am_hour < 10 and am_minutes == 0 and pm_minutes == 0:
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 2: AM hour >= 10, no AM or PM minutes provided
        elif am_hour > 9 and am_minutes == 0 and pm_minutes == 0:
            return f"{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 3: AM hour >= 10, no AM minutes, and PM minutes are absent
        elif am_hour > 9 and am_minutes == 0 and valid.group("pm_minutes") == None:
            return f"{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 4: AM hour < 10, no AM minutes, and PM minutes are absent
        elif am_hour < 10 and am_minutes == 0 and valid.group("pm_minutes") == None:
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 5: AM hour >= 10, no AM minutes, but PM minutes are 0
        elif am_hour > 9 and valid.group("am_minutes") == None and pm_minutes == 0:
            return f"{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 6: AM hour < 10, no AM minutes, but PM minutes are 0
        elif am_hour < 10 and valid.group("am_minutes") == None and pm_minutes == 0:
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:00"

        # Case 7: AM hour < 10, both AM and PM minutes provided
        elif am_hour < 10 and valid.group("am_minutes") and valid.group("pm_minutes"):
            return f"0{am_hour}:{am_minutes} to {pm_hour_twentyfour}:{pm_minutes}"
        
        # Case 8: AM hour >= 10, both AM and PM minutes provided
        elif am_hour > 9 and valid.group("am_minutes") and valid.group("pm_minutes"):
            return f"{am_hour}:{am_minutes} to {pm_hour_twentyfour}:{pm_minutes}"
        
        # Case 9: AM hour < 10, no AM minutes, and no PM minutes provided
        elif am_hour < 10 and am_minutes == 0 and valid.group("pm_minutes") == None:
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:00"

        # Case 10: AM hour < 10, AM minutes provided, but no PM minutes
        elif am_hour < 10 and valid.group("am_minutes") and valid.group("pm_minutes") == None:
            return f"0{am_hour}:{am_minutes} to {pm_hour_twentyfour}:00"

        # Case 11: AM hour < 10, no AM minutes, but PM minutes are provided
        elif am_hour < 10 and valid.group("am_minutes") == None and valid.group("pm_minutes"):
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:{pm_minutes}"

        # Case 12: AM hour >= 10, no AM minutes, but PM minutes are 0
        elif am_hour > 9 and valid.group("am_minutes") == None and pm_minutes == 0:
            return f"{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Case 13: AM hour >= 10, no AM minutes, but PM minutes are provided
        elif am_hour > 9 and valid.group("am_minutes") == None and valid.group("pm_minutes"):
            return f"{am_hour}:00 to {pm_hour_twentyfour}:{pm_minutes}"
        
        # Case 14: AM hour < 10, no AM or PM minutes provided
        elif am_hour < 10 and valid.group("am_minutes") == None and valid.group("pm_minutes") == None:
            return f"0{am_hour}:00 to {pm_hour_twentyfour}:00"
        
        # Default case: Catch any other scenarios
        else:
            return f"{am_hour}:{am_minutes} to {pm_hour_twentyfour}:00"

if __name__ == "__main__":
    main()
