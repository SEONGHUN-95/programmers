def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    save = 0
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            save = save+1
            continue
        if i-1 in reserve:
            reserve.remove(i-1)
            save = save + 1 
        elif i+1 in reserve:
            reserve.remove(i+1)
            save = save + 1
    answer = n - len(lost) + save
    return answer