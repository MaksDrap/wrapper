text = input("Введіть текст: ")
result = ""
longword = ""

for char in text:
    if char.isupper():
        result += char.lower()
    else:
        result += char

words = result.split()
golosni = ['a', 'e', 'i', 'o', 'u']
even_golosni = lambda word: sum(1 for letter in word if letter in golosni) % 2 == 0

for word in words:
    if len(word) > len(longword):
        longest_word = word
    if even_golosni(word):
        result = result.replace(word, '')

print("Замінений текст:", result)
print("Найдовше слово:", longword)
