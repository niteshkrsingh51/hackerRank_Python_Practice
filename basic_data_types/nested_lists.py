#Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students,
#order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    my_list = []
    scores = set()
    second_lowest_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        item = name,score
        my_list.append([name, score])
        scores.add(score)
    second_lowest = sorted(scores) [1]
    for name, score in my_list:
        if score == second_lowest:
            second_lowest_names.append(name)
    for name in sorted(second_lowest_names):
        print(name, end='\n')