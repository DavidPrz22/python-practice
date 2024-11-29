
def main():
    fraction = input("fraction: ").split("/") # separate fraction
    
    #turn strings to int
    while True:
        try:
            for i in range(len(fraction)):
                fraction[i] = int(fraction[i])
            
            if fraction[0] > fraction[1]:
                raise ValueError()
            
        except ValueError:
                fraction = input("fraction: ").split("/")
        else:
            break
    #handle zerodivisionerror
    try:
        fuel = fraction[0]/fraction[1]
        fuel = fuel * 100 # round fuel to the nearest decimal
        
        if fuel >= 99:
            print("F")
        elif fuel <= 1:
            print("E")
        else:
            print(f"your fuel is at {fuel:.2f}%")
    except ZeroDivisionError:
        print("Cant divide by zero")


main()