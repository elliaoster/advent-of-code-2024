def part1(numbers):
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
    return totadiff


def part2(numbers):
    column1 = []
    column2 = []
    finalnum = 0
    for line in numbers:
        first_numbers = int(line.split()[0])
        second_numbers = int(line.split()[1])
        column1.append(first_numbers)
        column2.append(second_numbers)
    for i in range(len(column1)):
        num = column1[i]
        numT = 0
        for j in range(len(column2)):
            if num == column2[j]:
                numT = numT + 1
        finalnum += num * numT
    return finalnum


def main():
    numbers = open("numberjunk.txt").readlines()
    totadiff = part1(numbers)
    print(totadiff)
    print(part2(numbers))


main()
