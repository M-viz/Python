def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return "Error: Too many problems."
    else:
        pt1=[]
        pt2=[]
        signs=[]
        answers=[]
        underscores=[]
        final_pt1=[]
        final_pt2=[]
        for i in range(len(problems)): 
            if problems[i].find('+')!=-1:
                signs.append('+')
                pt1.append(problems[i][:problems[i].find('+')-1])
                pt2.append(problems[i][problems[i].find('+')+2:])
                sum_pt1=int(pt1[i])
                sum_pt2=int(pt2[i])
                final_sum=sum_pt1+sum_pt2
                if pt1[i] > pt2[i]:
                    underscores.append('-'*(len(pt1[i])+2))
                else:
                    underscores.append('-'*(len(pt2[i])+2))
                final_pt1.append(pt1[i].rjust(len(underscores[i])))
                final_pt2.append(pt2[i].rjust(len(underscores[i])))
                final_pt2[i] = "+" + final_pt2[i][1:]
                answers.append(str(final_sum).rjust(len(underscores[i])))
            elif problems[i].find('-')!=-1:
                signs.append('-')
                pt1.append(problems[i][:problems[i].find('-')-1])
                pt2.append(problems[i][problems[i].find('-')+2:])
                diff_pt1=int(pt1[i])
                diff_pt2=int(pt2[i])
                final_diff=diff_pt1-diff_pt2
                if pt1[i] > pt2[i]:
                    underscores.append('-'*(len(pt1[i])+2))
                else:
                    underscores.append('-'*(len(pt2[i])+2))
                final_pt1.append(pt1[i].rjust(len(underscores[i])))
                final_pt2.append(pt2[i].rjust(len(underscores[i])))
                final_pt2[i] = "-" + final_pt2[i][1:]
                answers.append(str(final_diff).rjust(len(underscores[i])))
        if show_answers==False:
            return f"{'    '.join(final_pt1)}\n{'    '.join(final_pt2)}\n{'    '.join(underscores)}"
        if show_answers==True:
            return f"{'    '.join(final_pt1)}\n{'    '.join(final_pt2)}\n{'    '.join(underscores)}\n{'    '.join(answers)}"
    
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

