

import matplotlib.pyplot as plt

def main():
    try:
        names=[]
        exp=[]
        file=open('expenses.txt','r')
        x=0
        for line in file:
            name=line.split('\t')[0]
            number=line.split('\t')[1].rstrip('\n')
            if number.isdigit():
                names.append(name)
                exp.append(int(number))
                x+=1
        plt.pie(exp,labels=names)
        plt.title('monthly expenses')
        plt.show()

    except IOError:
        print('Error occured trying to read the file')


main()
