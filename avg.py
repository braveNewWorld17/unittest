import sys

def compute_average(numbers):
    sum = 0
    if not numbers:
        return 0
    for number in numbers:
        try :
            sum += number
        except TypeError:
            print("Value is not number type.")

    return sum/len(numbers)    

def main():
    list = []

# sys.argv[0] is file name
    print(sys.argv[0])

    for argv in sys.argv[1:]:
        list.append(int(argv))
    print("Average :" +   
         str(compute_average(list)))

# entry point definition
if __name__ == "__main__":
    main()

