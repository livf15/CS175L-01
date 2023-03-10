
def main():
    try:
        file=open('numbers.txt','r')
        num1=int(file.readline())
        num2=int(file.readline())
        num3=int(file.readline())
        print(line)
    
for line in file:
    print('I read in 1 number(s)','Current number is:',f'{num1:>.3f}','Total is:', f'{num1:>.3f}')
    print('I read in 2 number(s)','Current number is:',f'{num2>.3f}','Total is:',f'{num2:>.3f}')
    print('I read in 3 number(s)','Current number is:',f'{num3>.3f}','Total is:',f'{num3:>.3f}')
    avg=(num1+num2+num3)/3
    print('The average of the numbers is:', avg)
        
        
    
    




if __name__=='__main__':
    main()



