vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

poem = input("Введите стихотворение Винни-Пуха: ").split()
syllables = [sum([True for _ in word if _ in vowels]) for word in poem]

print(*syllables)

if all(syllables) and len(set(syllables)) == 1:
    print("Парам пам-пам")
else:
    print( "Пам парам")





