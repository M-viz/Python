# Function to arrange arithmetic problems vertically.
# Funzione per organizzare problemi aritmetici verticalmente.

def arithmetic_arranger(problems, show_answers=False):
    # Initialize flag variables.
    # Inizializzazione delle variabili flag.
    sign_check = 0
    char_check = 0
    width_check = 0 

    # Check if operator is valid in each problem.
    # Verifica se l'operatore è valido in ogni problema.
    for problem in problems: 
        if  '+' not in problem and '-' not in problem:
            sign_check = 1
            break

    # Check the width of numbers in each problem.
    # Verifica la larghezza dei numeri in ogni problema.   
    for problem in problems: 
        left = problem.split()[0]
        right=problem.split()[-1]
        if len(left) > 4 or len(right) > 4:
            width_check = 1
            break

    # Check if any non-numeric characters are present in any problem.
    # Verifica se sono presenti caratteri non numerici in un problema.    
    for problem in problems: 
        for char in problem:
            if char.isalpha():
                char_check = 1
                break

    # Error checks.
    # Controlli degli errori.
    if len(problems)>5:
        return "Error: Too many problems."
    if sign_check == 1:
        return "Error: Operator must be '+' or '-'."
    if char_check == 1:
        return 'Error: Numbers must only contain digits.'
    if width_check == 1:
        return 'Error: Numbers cannot be more than four digits.'
    else:
        # Initialize lists to store arranged parts of problems.
        # Inizializza liste per memorizzare le parti dei problemi organizzati.
        pt1=[]          # Store the left operands.
                        # Conserva gli operandi sinistri.
        pt2=[]          # Store the right operands.
                        # Conserva gli operandi destri.
        signs=[]        # Store the operators.
                        # Conserva gli operatori.
        answers=[]      # Store the results of calculations.
                        # Conserva i risultati dei calcoli.
        underscores=[]  # Store the lines of underscores.
                        # Conserva le linee di trattini.
        final_pt1=[]    # Store the left operands after alignment.
                        # Conserva gli operandi sinistri dopo l'allineamento.
        final_pt2=[]    # Store the right operands after alignment.
                        # Conserva gli operandi destri dopo l'allineamento.

        # Loop through each problem to arrange and calculate.
        # Cicla attraverso ogni problema per organizzare e calcolare.
        for i in range(len(problems)): 
            if problems[i].find('+')!=-1:
                # Split the problem into left and right parts.
                # Dividi il problema in parti sinistra e destra.
                signs.append('+')
                pt1.append(problems[i][:problems[i].find('+')-1])
                pt2.append(problems[i][problems[i].find('+')+2:])

                # Convert left and right parts to integers and calculate sum.
                # Converti le parti sinistra e destra in interi e calcola la somma.
                sum_pt1=int(pt1[i])
                sum_pt2=int(pt2[i])
                final_sum=sum_pt1+sum_pt2

                # Determine width of underscores and align numbers.
                # Determina la larghezza dei trattini e allinea i numeri.
                if int(pt1[i]) > int(pt2[i]):
                    underscores.append('-'*(len(pt1[i])+2))
                else:
                    underscores.append('-'*(len(pt2[i])+2))
                final_pt1.append(pt1[i].rjust(len(underscores[i])))
                final_pt2.append(pt2[i].rjust(len(underscores[i])))
                final_pt2[i] = "+" + final_pt2[i][1:]
                answers.append(str(final_sum).rjust(len(underscores[i])))

            elif problems[i].find('-')!=-1:
                # Split the problem into left and right parts.
                # Dividi il problema in parti sinistra e destra.
                signs.append('-')
                pt1.append(problems[i][:problems[i].find('-')-1])
                pt2.append(problems[i][problems[i].find('-')+2:])

                # Convert left and right parts to integers and calculate difference.
                # Converti le parti sinistra e destra in interi e calcola la differenza.
                diff_pt1=int(pt1[i])
                diff_pt2=int(pt2[i])
                final_diff=diff_pt1-diff_pt2

                # Determine width of underscores and align numbers.
                # Determina la larghezza dei trattini e allinea i numeri.
                if int(pt1[i]) > int(pt2[i]):
                    underscores.append('-'*(len(pt1[i])+2))
                else:
                    underscores.append('-'*(len(pt2[i])+2))
                final_pt1.append(pt1[i].rjust(len(underscores[i])))
                final_pt2.append(pt2[i].rjust(len(underscores[i])))
                final_pt2[i] = "-" + final_pt2[i][1:]
                answers.append(str(final_diff).rjust(len(underscores[i])))

        # Check if answers need to be shown.
        # Controlla se è necessario mostrare le risposte.        
        if show_answers==False:
            return f"{'    '.join(final_pt1)}\n{'    '.join(final_pt2)}\n{'    '.join(underscores)}"
        if show_answers==True:
            return f"{'    '.join(final_pt1)}\n{'    '.join(final_pt2)}\n{'    '.join(underscores)}\n{'    '.join(answers)}"
    

# Print the arranged arithmetic problems.
# Stampa i problemi aritmetici organizzati.
print(f'\n{arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"],show_answers=True)}')

