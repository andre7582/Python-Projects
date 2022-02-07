def xfile(*grades):
    """
    > Function to analyze the grades, grade average and situation of a student.
    :param grades: arquive one or more grades.
    :return: dictionary with various information related to the student.
    """
    if grades[-1]:
        sit = True
    else:
        sit = False

    values = dict()
    highest = 0
    lowest = 10
    tsum = 0

    for cont in range(0, len(grades) - 1, 1):
        if cont < len(grades) - 1:
            if float(grades[cont]) > highest:
                highest = float(grades[cont])
            if float(grades[cont]) < lowest:
                lowest = float(grades[cont])
            tsum += float(grades[cont])
    average = float(tsum / (len(grades) - 1))

    if average <= 5:
        situacao = 'BAD'
    elif 5 < average <= 7.5:
        situacao = 'GOOD'
    elif 7.5 < average < 9.5:
        situacao = 'EXCELLENT'
    else:
        situacao = 'GREAT'

    values['Total grades'] = len(grades) - 1
    values['Higest grade'] = highest
    values['Lowest grade'] = lowest
    values['Average grade'] = average

    if sit:
        values['Situation'] = situacao

    return values


# main program

tgrades = list()
count = 1
print()

while True:
    start = str(input('- Do you want to get start [S/start] or ask for help [H/help]? ').strip().upper())
    print()
    if start != 'S' and start != 'H':
        print("'S/start' for start the program or 'H/help' for ask for help.")
        print()
    elif start == 'S':
        break
    elif start == 'H':
        help(xfile)
        break
    else:
        print('ERROR 404')

while True:
    grade = input(f'- Input grade nº{count}: ')
    if grade.isalpha() or grade == '':
        print('> Input a number!')
    elif float(grade) < 0 or float(grade) > 10:
        print('> Enter a grade between 0 e 10!')
    else:
        tgrades.append(float(grade))
        count += 1
        print()
    while True:
        questionyn = str(input('- More grades? [Y/N]: ').strip().upper())
        print()
        if questionyn != 'Y' and questionyn != 'N':
            print("Enter [Y/yes] or [N/no]")
            print()
        else:
            break
    if questionyn == 'N':
        while True:
            questionyn2 = str(input('- Do you want to show the situation? [Y/N]: ').strip().upper())
            print()
            if questionyn2 != 'Y' and questionyn2 != 'N':
                print('- Enter [Y/yes] or [N/no]')
                print()
            else:
                break
        if questionyn2 == 'Y':
            situation = True
        else:
            situation = False
        break

finalresult = xfile(*tgrades, situation)
print(finalresult)
print()
print('=' * 120)
