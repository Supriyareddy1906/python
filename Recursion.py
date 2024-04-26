def recursion(start, end):
    if start <= end:
        print(start)
        recursion(start + 1, end)

recursion(1, 100)
