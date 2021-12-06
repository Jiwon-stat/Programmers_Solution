def solution(dartResult):
    
    n = ""
    answer = []
    
    for i in dartResult :
        if i.isnumeric() :
            n += i
            
        elif i == "S" :
            a = int(n) ** 1
            answer.append(a)
            n = ""
        elif i == "D" :
            a = int(n) ** 2
            answer.append(a)
            n = ""
        elif i == "T" :
            a = int(n) ** 3
            answer.append(a)
            n = ""
            
        elif i == "*" : 
            if len(answer) == 1:
                answer[0] = answer[0]*2
            elif len(answer) == 2:
                answer[0] = answer[0]*2
                answer[1] = answer[1]*2
            elif len(answer) == 3:
                answer[1] = answer[1]*2
                answer[2] = answer[2]*2
        elif i == "#" :
            answer[-1] = answer[-1]*(-1)
        
    ans = sum(answer)
    return ans
    
