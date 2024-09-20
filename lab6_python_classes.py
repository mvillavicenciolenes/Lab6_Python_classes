"""

Michael Villavicencio
Sep 20, Python Classes

"""

print(f"\n ------------ Example 1: Exception Handling ----------- ")
def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide to 24: "))

        hours /= h # hours = hours / h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} cant be divided by 24. Result is undefined")
    except ValueError:
        print(f"{h} is not a number")
    except:
        print("PROGRAM ERROR")

print(hour_ratio())
print("\n ================= End of program 1 ==================")


print(f"\n ------------ Example 2: Classes ----------- ")
