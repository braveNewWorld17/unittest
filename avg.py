import sys

def compute_average(numbers):
    if not numbers:
        return 0
    sum = 0
    for number in numbers:
        sum += number
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

