import sys

def cal_case(input):
    
    # 1로 만드는 케이스
    # 1과 2로 만드는 케이스
    # 1과 3으로 만드는 케이스
    # 2와 3으로 만드는 케이스
    # 1과 2와 3으로 만드는 케이스
    
    # 1, 2, 3
    # 1 : 1
    # 2 : 1+1,         2
    # 3 : 1+1+1,       2+1,       1+2,                                                                                                     3
    # 4 : 1+1+1+1,     2+1+1,     1+2+1,     1+1+2,                           2+2                                                          3+1,     1+3
    # 5 : 1+1+1+1+1,   2+1+1+1,   1+2+1+1,   1+1+2+1,   1+1+1+2,              2+2+1,          2+1+2,            1+2+2,                     3+1+1,   1+3+1,   1+1+3,            3+2,          2+3
    # 6 : 1+1+1+1+1+1, 2+1+1+1+1, 1+2+1+1+1, 1+1+2+1+1, 1+1+1+2+1, 1+1+1+1+2, 2+2+1+1, 2+2+2, 2+1+2+1, 2+1+1+2, 1+2+2+1, 1+2+1+2, 1+1+2+2, 3+1+1+1, 1+3+1+1, 1+1+3+1, 1+1+1+3, 3+2+1, 3+1+2, 2+3+1, 2+1+3, 3+3 
    # 1 : 1개
    # 2 : 2개
    # 3 : 4개
    # 4 : 7개
    # 5 : 13개
    # 6 : 24개

    if input == 1:
        return 1
    elif input == 2:
        return 2
    elif input == 3:
        return 4
    else:
        return cal_case(input-1) + cal_case(input-2) + cal_case(input-3)


N = int(sys.stdin.readline())
for _ in range(N):
    i = int(input())
    # print(케이스의 합) 
    print(cal_case(i))