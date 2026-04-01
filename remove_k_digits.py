#402
#Input: num = "1432219", k = 3
#Output: "1219"


def remove_k_digits(num,k):
    stack=[]
    for digit in num:
        while k > 0 and stack and stack[-1] >digit:
            stack.pop()
            k-=1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result= ''.join(stack).lstrip('0')
    return result if result else "0"
num=input()
k=int(input())
print(remove_k_digits(num, k))

