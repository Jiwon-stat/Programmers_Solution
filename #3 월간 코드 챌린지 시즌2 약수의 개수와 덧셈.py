def solution(left, right):

    answer = 0

    def factorization(n):
        num = 0
        for i in range(2,n+1) :
            if n % i == 0 :
                num += 1
        number = num+1
        return number

    for i in range(left, right+1):
            if factorization(i)%2 ==0 : #짝수일 때
                answer += i
            else :
                answer -= i

    return answer
