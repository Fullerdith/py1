a=1
while a <= 9:#此处循环控制的是整体的行数，即每一行
    b = 1
    while b <= a:#约束b在a内，此处引入另一个 while意在控制每一行内的每个元素
        print(f"{a}×{b}={a*b}",end="\t")
        b += 1
    a += 1
    print()#每一行的循环结束后进行换行
