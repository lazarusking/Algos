def newtonDiff(x, fi):
    """ 
        f(t)=∑ ai(t-tj)
             i=0
             j=0
    """ 
    fx0 = []
    a = []
    a.append(fi[0])
    inc = 0
    result = a[0]
    for j in range(len(x)-1):
    # f[ti]-f[t0]/ti-t0
        for i in range(len(fi)-1):
            # print(i, "now", f" {i}-{i-1}",
            #       f"{fi[i]}-{fi[i-1]}", f"{x[i+inc]}-{x[i-1]}")
            # print(fx0)
            fx0.append((fi[i+1]-fi[i])/(x[i+1+inc]-x[i]))
        inc += 1
        fi = fx0[:]
        a.append(fi[0])
        fx0 = []
    for i in range(1,len(a)):
        prod=1
        for j in range(i):
            prod *= (t-x[j])
        result += a[i]*prod
    print("Δfο=",a)
    print(f"f({t})=", result)



x = [0, 1, 3, 4, 7]
fi = [1, 3, 49, 129, 813]
# x = [1, 2, 3]
# fi = [86, 84, 89]

t = 1.4

newtonDiff(x, fi)




# for i in range(1, len(x)):
#     # f[ti]-f[t0]/ti-t0
#     print(i, "now", f" {i}-{i-1}", f"{fi[i]}-{fi[i-1]}", f"{x[i]}-{x[i-1]}")
#     fx0.append((fi[i]-fi[i-1])/(x[i]-x[i-1]))
#     print(fx0)
#     print(a)
#     if (i % 2 == 0):
#         for j in range(1):
#             # print(j, "j", f" {i}-{i-1}",
#             #       f"{fi[i]}-{fi[i-1]}", f"{x[j+1]}-{x[j-1]}")
#             # fx0.append((fi[i]-fi[i-1])/(x[j+1]-x[j-1]))
#             print(i, "now", f" {i}-{i-1}",
#                   f"{fx0[i-1]}-{fx0[i-2]}", f"{x[i]}-{x[i-2]}")

#             print((fx0[i-1]-fx0[i-2])/(x[i]-x[i-2]))
#             a.append((fx0[i-1]-fx0[i-2])/(x[i]-x[i-2]))
#             pass
# print(fx0)
# print(a)
