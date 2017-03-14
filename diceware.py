words={}
with open('diceware.wordlist.asc') as f:
    for line in f:
        dice,word = line.split('\t')
        words[dice]=word.strip()
     
h=''
while h != 'q':
    n = int(raw_input('How many words?'))
    d = [raw_input('5d6\n') for _ in range(n)]
     
    for x in d:
        print words[x],
         
    print ''
    h = raw_input('q to quit')
