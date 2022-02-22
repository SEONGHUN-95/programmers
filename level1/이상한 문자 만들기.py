def solution(s):
    idx = 0
    answer = ''
    for i in s:
        if i == ' ':
            idx = 0
            answer = answer + ' '
        else: 
            if idx % 2 == 0: 
                answer = answer + i.upper()
            else:
                answer = answer + i.lower()
            idx = idx +1
    return answer