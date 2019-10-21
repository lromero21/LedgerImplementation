import argparse
import sys
import re
import click


class Resources:
    date = []
    transaction = []
    posting = []
    postingSource = []
    moneyQ = []
    posting2 = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation', type=str, default='print',
                        help='What operation? Can choose, register, balance, print')
    parser.add_argument('--flag', type=str, default='sort',
                        help='What flag? Can choose, sort, price-db, file')
    args = parser.parse_args()
    options(args)
    #sys.stdout.write(str(options(args)))


#tokens = []
def readAll(file):
    f = open (file,'r')
    message = ''
    try:
        for lines in f:           
            if lines.startswith(';'):
                continue
            if lines.startswith('!include'):
                message += readAll(lines.split(' ')[1][:-1])
            else:
                message += lines    
    finally:
        f.close()
        #tokens = re.findall(r'(.+\n.+\n.+)', message)
        #print(len(tokens))            
        return message

## REGISTER
def options(args):
    if args.operation == 'print' or 'pri':  # I USE THIS OPTION FOR PRINTING ALL THE INFORMATION -PRINT-
        message = readAll('index.ledger')
        tokens = re.findall(r'(.+\n.+\n.+)', message)   
        for token in tokens:
            # I ADD THE INFORMATION TO EACH LIST
            tokensSplitted = re.search(r'(\d{4}\/\d{1,2}\/\d{1,2})\s+(.+)\n\s+([\w ]+(:[ \w]+)*)[ \t]+([\$\d\-\.]+[ A-Z]*)\n\s+([\w ]+(:[ \w]+\t*[\$\d\-\.]+[ A-Z]*)*)',token)
            Resources.date.append(tokensSplitted.group(1))
            Resources.transaction.append(tokensSplitted.group(2))
            Resources.posting.append(tokensSplitted.group(3))
            Resources.postingSource.append(tokensSplitted.group(4))
            Resources.moneyQ.append(tokensSplitted.group(5))
            Resources.posting2.append(tokensSplitted.group(6))
        # I WILL PRINT ALL THE INFORMATION CHUNKED THAT I HAVE
    elif args.operation == 'register' or 'reg': # I WANT TO USE THIS OPTION FOR THE REGISTER COMMAND
        message = readAll('index.ledger')           
        tokens = re.findall(r'(.+\n.+\n.+)', message)    
    # THIS WORKS FOR PRINTING
    balanceMoney = 0
    balanceBitcoins = 0
    for i in range(len(Resources.date)):
        if Resources.moneyQ[i].startswith('$'):
            #splittedResult = Resources.moneyQ[i].split('$')[1]
            #print ('THIS'+splittedResult)
            balanceMoney += float (Resources.moneyQ[i].split('$')[1])
            #print (Resources.posting2[i])
            if '$' in Resources.posting2[i]:
                # PRINT IT
                print ('into posting2 find $ ')
                print (Resources.posting2[i])
                balanceMoney = 0                
                pass
            elif 'BTC' in Resources.posting2[i]:
                print('into posting2 find BTC')
                print (Resources.posting2[i])
                balanceMoney = 0
                # PRINT 
                pass
            else:
                print (Resources.date[i] +' '+ Resources.transaction[i]+'\n\t'+ Resources.posting[i]+''+ Resources.postingSource[i]+'\t\t'+Resources.moneyQ[i]+'\t'+'$'+str (balanceMoney)+'\n\t '+Resources.posting2[i]+'\t\t\t'+'-'+Resources.moneyQ[i]+'\t'+'0')
                balanceMoney = 0
        # elif Resources.moneyQ[i].startswith('-$'):
        #     Resources.moneyQ[i].split('-$')
        #     balanceMoney -= int (Resources.moneyQ[i][1])
        # Disscomment later
        # elif re.search(r'BTC',Resources.moneyQ[i]):
        #     if(Resources.moneyQ[i].startswith('-')):                                
        #         Resources.moneyQ[i].split('BTC')
        #         balanceBitcoins -= int (Resources.moneyQ[i][0])
        #     else:
        #         Resources.moneyQ[i].split('BTC')
        #         balanceBitcoins += int (Resources.moneyQ[i][0])
        # else:
        #     print('Something went wrong and I didn\'t go inside the conditions')

       # print (Resources.date[i] +' '+ Resources.transaction[i]+'\n\t'+ Resources.posting[i]+''+ Resources.postingSource[i]+'\t\t'+ Resources.moneyQ[i]+'\n\t '+Resources.posting2[i])






# PRINT
# def options(args):
#     if args.operation == 'print' or 'pri':  # I USE THIS OPTION FOR PRINTING ALL THE INFORMATION -PRINT-
#         message = readAll('index.ledger')
#         tokens = re.findall(r'(.+\n.+\n.+)', message)   
#         for token in tokens:
#             # I ADD THE INFORMATION TO EACH LIST
#             tokensSplitted = re.search(r'(\d{4}\/\d{1,2}\/\d{1,2})\s+(.+)\n\s+([\w ]+(:[ \w]+)*)[ \t]+([\$\d\-\.]+[ A-Z]*)\n\s+([\w ]+(:[ \w]+)*)',token)
#             Resources.date.append(tokensSplitted.group(1))
#             Resources.transaction.append(tokensSplitted.group(2))
#             Resources.posting.append(tokensSplitted.group(3))
#             Resources.postingSource.append(tokensSplitted.group(4))
#             Resources.moneyQ.append(tokensSplitted.group(5))
#             Resources.posting2.append(tokensSplitted.group(6))
#         # I WILL PRINT ALL THE INFORMATION CHUNKED THAT I HAVE
#     elif args.operation == 'register' or 'reg': # I WANT TO USE THIS OPTION FOR THE REGISTER COMMAND
#         message = readAll('index.ledger')           
#         tokens = re.findall(r'(.+\n.+\n.+)', message)    
#     # THIS WORKS FOR PRINTING
#     for i in range(len(Resources.date)):
#         print (Resources.date[i] +' '+ Resources.transaction[i]+'\n\t'+ Resources.posting[i]+''+ Resources.postingSource[i]+'\t\t'+ Resources.moneyQ[i]+'\n\t '+Resources.posting2[i])
            
if __name__ == '__main__':
    main()