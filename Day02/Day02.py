def part1(numbers):
    safe = 0
    for line in numbers:
        row = []
        row = (line.split())
        directon = "none"
        for i in range(len(row) - 1):
            num = int(line.split()[i])
            num2 = int(line.split()[i + 1])
            if abs(num - num2) <= 3 and abs(num - num2) >= 1:
                if i == 0 and num > num2:
                    directon = "down"
                elif i == 0 and num < num2:
                    directon = "up"
                elif num > num2 and directon != "down":
                    break
                elif num < num2 and directon != "up":
                    break
                elif i == len(row) - 2:
                    safe = safe + 1
            else:
                break
    return safe


# def part2(numbers):
#     column1 = []
#     column2 = []
#     finalnum = 0
#     for line in numbers:
#         first_numbers = int(line.split()[0])
#         second_numbers = int(line.split()[1])
#         column1.append(first_numbers)
#         column2.append(second_numbers)
#     for i in range(len(column1)):
#         num = column1[i]
#         numT = 0
#         for j in range(len(column2)):
#             if num == column2[j]:
#                 numT = numT + 1
#         finalnum += num * numT
#     return finalnum


def main():
    numbers = open("numberjunk.txt").readlines()
    print(part1(numbers))
    #print(part2(numbers))


main()
