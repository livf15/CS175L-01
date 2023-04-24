


def winners():
    file=open('/Users/oliviafranczykowski/Documents/WorldSeriesWinners.txt','r')
    winner=[]
    for infile in file:
        infile=infile.rstrip('\n')
        winner.append(infile)
    file.close()
    return winner

def search(winner):
    file=open('/Users/oliviafranczykowski/Documents/WorldSeriesWinners.txt','r')
    name=[]
    while name !='quit':
        name=('Enter name of a team or quit')
        name=name.lower()
        if name!='quit':
            search=[look for look in winner if look.lower()==name]
            times=(len(search))
            if times>0:
                print(f'The{name} won the world series {times} between 1901 to 2009')
            else:
                print('Team not found')
                
        else:
            print('Goodbye')
        file.close()
                    

    




def main():
    file=open('/Users/oliviafranczykowski/Documents/WorldSeriesWinners.txt','r')
    line=file.readline()
    winner=winners()
    search(winner)
   
    
    

    
    

main()
