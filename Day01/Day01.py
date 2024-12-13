def main():
    numbers = open("numberjunk.txt").readlines()
    column1 = []
    column2 = []
    for line in numbers:
        first_numbers = int(line.split()[0])
        second_numbers = int(line.split()[1])
        column1.append(first_numbers)
        column2.append(second_numbers)
    totadiff = 0
    for i in range(len(column1)):
        small1 = min(column1)
        small2 = min(column2)
        totadiff = totadiff + abs(small2 - small1)
        column1.remove(small1)
        column2.remove(small2)
    print(totadiff)

main()