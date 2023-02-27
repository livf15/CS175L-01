

    
def determine_grade(numeric_grade):
    if numeric_grade>=90 and numeric_grade<=100:
        return 'A'
    elif numeric_grade>=80:
        return 'B'
    elif numeric_grade>=70:
        return 'C' 
    elif numeric_grade>=60:
        return 'D'
    else:
        return 'F'

def calc_average():
    score1=float(input('Enter score 1: '))
    score2=float(input('Enter score 2: '))
    score3=float(input('Enter score 3: '))
    score4=float(input('Enter score 4: '))
    score5=float(input('Enter score 5: '))
    avg=(score1+score2+score3+score4+score5)/5
    return score1,score2,score3,score4,score5
    
    
    

    
def main():
    repeat='yes'
    while repeat=='yes':
        score1,score2,score3,score4,score5=calc_average()
        determine_grade(score1)
        determine_grade(score2)
        determine_grade(score3)
        determine_grade(score4)
        determine_grade(score5)
        print('Score        Numeric Grade    Letter Grade')
        print('---------------------------------------------')
        print('Score 1:',f'{score1:>10}', f'{determine_grade(score1):>16}')
        print('Score 2:',f'{score2:>10}', f'{determine_grade(score2):>16}')
        print('Score 3:',f'{score3:>10}', f'{determine_grade(score3):>16}')
        print('Score 4:',f'{score4:>10}', f'{determine_grade(score4):>16}')
        print('Score 5:',f'{score5:>10}', f'{determine_grade(score5):>16}')
        total=score1+score2+score3+score4+score5
        avg=total/5
        print('Average score:',avg, determine_grade(avg))
        repeat=input('Enter "yes" if you wold like to do another calculation:')
        

main()
    
