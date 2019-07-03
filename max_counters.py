'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
'''

N = 5
A = [3, 4, 4, 6, 1, 4, 4]

N = 1
A = [2, 1, 1, 2, 1]



def solution(N, A):
    # write your code in Python 3.6
    D = { i+1: 0 for i in range(N)}
    
    for idx, i in enumerate(A):
        if i == N + 1:
            max_counter = D[idx+1]
            D = { i+1: max_counter for i in range(N)}
        else:
            D[i] = D[i] + 1
        print(D)
    
    return [D[i+1] for i in range(N)]


def solution_t(N, A):
    result = [0] * N
    minValue = 0
    maxValue = 0
    for number in A:
        index = number - 1
        if(index == N):
            minValue = maxValue
            continue
        result[index] = max(result[index], minValue) + 1
        maxValue = max(maxValue, result[index])
    for i in range(N):
        result[i] = max(result[i], minValue)
    return result


# print(solution(N, A))
print(solution_t(N, A))

