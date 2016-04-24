f = open('Pismennost.csv', 'r', encoding='utf-8') # amharskiy.алфавит
letters = {}
letters1 =[]
letters2 =[]
y = 0
for row in f:
    if y == 0:
        letters2 += row.split()
        y +=1
    else:
        wordsinline = row.split() 
        x = 0
        for letter in wordsinline:
            if letter == wordsinline[0]:
                letter1 = letter
                letters1.append(letter1)
            else:
                key = letter
                letters[key]=letter1 + letters2[x] #амхар. букв с их лат. в значении
                x += 1
    
f.close()
file = open('text.txt', 'r', encoding = 'utf-8') #файл с текстом на amharskom
writefile = open('translation.txt', 'w', encoding = 'utf-8') #файл для перевода амхарского текста
for line in file:
        for letter in str(line):
            if letter in letters:
                writefile.write(letters[letter])
            else:
                writefile.write(letter)
            
writefile.close()
file.close()
print('The end')
