"""
Sum of even Fibonacci Sequence
"""

n=int(input("Enter the number of fibonacci sequence: "))
f_num=0
s_num=1
even_sum=0
for i in range(0,n):
    nx_num=f_num+s_num
    f_num=s_num
    s_num=nx_num
    if nx_num%2==0:
        even_sum+=nx_num
        print(nx_num)
print("The sum of even fibonacci sequence is :", even_sum)

