pol = True
word = input('Please enter word: ').lower()
# while True:
#     word = input('Please enter word: ').lower()
#     if len(word) % 2 == 0:
#         print('not polindrom')
#         continue
#     for i, d in enumerate(word):
#         if word[i] != word[-i - 1]:
#             pol = False
#     break
word1 = reversed(word)
''.join(word1)
if word == word1:
    print(pol)
else:
    print(pol)

# word = input("Enter word: ")
# print(word == ''.join(reversed(word)))