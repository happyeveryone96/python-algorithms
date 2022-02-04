def solution(answers):
    answer = []
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == man1[i % len(man1)]:
            score[0] += 1
    for i in range(len(answers)):
        if answers[i] == man2[i % len(man2)]:
            score[1] += 1
    for i in range(len(answers)):
        if answers[i] == man3[i % len(man3)]:
            score[2] += 1
    max_num = max(score)
    for i in range(len(score)):
        if max_num == score[i]:
            answer.append(i+1)
    return answer
