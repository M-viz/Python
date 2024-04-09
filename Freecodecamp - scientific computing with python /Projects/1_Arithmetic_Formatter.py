def arithmetic_arranger(problems, show_answers=False):
    pt1=[]
    pt2=[]
    signs=[]
    answers=[]
    underscores=[]
    for i in range(len(problems)): 
        if problems[i].find('+')!=-1:
            signs.append('+')
            pt1.append(problems[i][:problems[i].find('+')-1])
            pt2.append(problems[i][problems[i].find('+')+2:])
            sum_pt1=int(pt1[i])
            sum_pt2=int(pt2[i])
            final_sum=sum_pt1+sum_pt2
            answers.append(final_sum)
            if pt1[i] > pt2[i]:
                underscores.append(len(pt1[i])+2)
            else:
                underscores.append(len(pt2[i])+2)
        elif problems[i].find('-')!=-1:
            signs.append('-')
            pt1.append(problems[i][:problems[i].find('-')-1])
            pt2.append(problems[i][problems[i].find('-')+2:])
            diff_pt1=int(pt1[i])
            diff_pt2=int(pt2[i])
            final_diff=diff_pt1-diff_pt2
            answers.append(final_diff)
            if pt1[i] > pt2[i]:
                underscores.append(len(pt1[i])+2)
            else:
                underscores.append(len(pt2[i])+2)
    #return pt1,pt2,signs,answers,underscores
    return f"{' '.join(pt1)}\n{' '.join(signs+pt2)} {' '.join(pt2)}\n{'_' * max(underscores)}"
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')