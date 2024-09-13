#1 with 2 task
def find_max_str(string, seperated: str = ' ', desc=False):
    words = string.split(seperated)
    if not words:
        print('Нет данных')
        return 
    
    findstr = ''
    if desc:
        findstr = min(words, key=len)
        
    else:
        max = -1
        for word in words:
            length = len(word)
            if  length > max:
                max = length
                findstr = word

    print(f'Response: {findstr}')

string = input('Введите строку: ')
separetad_value = input('Введите разделитель: ')
find_max_str(string, seperated=separetad_value, desc=True)



# 4 Task
def find_word_in_sentence(word, sentence):
    if word in sentence:
        return f"Слово '{word}' найдено в строке."
    else:
        return f"Слово '{word}' не найдено в строке."

sentence = input("Введите строку: ")
word = input("Введите слово для поиска: ")
print(find_word_in_sentence(word, sentence))

# 5 Task
print(len(str(input('Введите строку'))))
