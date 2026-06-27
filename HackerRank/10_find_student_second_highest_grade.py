if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    print(records)
    score_list = sorted(set(student[1] for student in records))
    second_lowest = score_list[1]
    # name_second_lowest = []
    # for names in records:
    #     if names[1] == second_lowest:
    #         name_second_lowest.append(names[0])

    # name_second_lowest = sorted(name_second_lowest)
    # for n in name_second_lowest:
    #     print(n)
    
    names = sorted(
    student[0]
    for student in records
    if student[1] == second_lowest)

    for name in names:
        print(name)
