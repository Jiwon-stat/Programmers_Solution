def solution(lottos, win_nums) :
    
    same_num = []
    smallwin = 0
    bigwin = 0
    
    for i in range(len(lottos)) :
        for j in range(len(win_nums)) :
            if lottos[i] == win_nums[j] :
                same_num += [(i,j)]
    
    smallwin += len(same_num)
    if smallwin == 0 :
        smallwin = 6
    else :
        smallwin = 7-smallwin 
    
    bigwin = lottos.count(0)
    if bigwin == 6 :
        bigwin = 1
    else :
        bigwin = smallwin-bigwin
    
    answer = []
    answer += [bigwin, smallwin]
    return answer
