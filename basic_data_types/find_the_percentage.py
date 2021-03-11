if __name__ == '__main__':
    sum = 0
    count = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_list = student_marks[query_name]
    for i in score_list:
        count += 1
        sum = float(sum + i)
    average_score = sum/count
    formatted_average_score = "{:.2f}".format(average_score)
    print(formatted_average_score)