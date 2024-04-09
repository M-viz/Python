def arithmetic_arranger(problems, show_answers=False):
    pt1=[]
    pt2=[]
    sign=[]
    for i in range(len(problems)): 
        if problems[i].find('+')!=-1:
            sign.append('+')
            pt1.append(problems[i][:problems[i].find('+')-1])
            pt2.append(problems[i][problems[i].find('+')+2:])
        elif problems[i].find('-')!=-1:
            sign.append('-')
            pt1.append(problems[i][:problems[i].find('-')-1])
            pt2.append(problems[i][problems[i].find('-')+2:])
        else:
            return '"Error: Operator must be '+' or '-'."' 
    return pt1,pt2,sign
x=arithmetic_arranger("32 + 698", "3801 - 2", "45 + 43", "123 + 49")
print(x)
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
