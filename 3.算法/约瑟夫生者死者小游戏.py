#Python 约瑟夫生者死者小游戏
# 30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。报数，从 1 开始，数到 9 的人下船。
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
people=list(range(1,31))
while len(people)>15:
    i=1
    while i<9:
        people.append(people.pop(0))
        i+=1
        print(people)
    print('{:2d}号下船了'.format(people.pop(0)))