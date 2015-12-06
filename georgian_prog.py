f = open('geor.csv', 'r', encoding='utf-8') # груз.алфавит с IPA
letters = {}
for row in f:
    wordsinline = row.split()
    key = wordsinline[0]
    letters[key]=wordsinline[2] #груз. букв с их IPA в значении
f.close()
file = open('hymn.txt', 'r', encoding = 'utf-8') #файл с текстом на грузинском
writefile = open('translation.txt', 'w', encoding = 'utf-8') #файл для перевода грузинского текста в IPA
for line in file:
        for letter in str(line):
            if letter in letters:
                writefile.write(letters[letter])
            else:
                writefile.write(letter)
            
writefile.close()
file.close()
print('The end')
