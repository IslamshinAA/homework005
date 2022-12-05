# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'фывфывабв зыдвыфв абвфывф абв фывфыв фывфабфыф'
# list = text.split() # старый способ
search_str = "абв"
my_list = [i for i in text.split() if search_str not in i]
print(f'{" ".join(my_list)}')
# for i in range(len(list)):
#     if search_str not in list[i]:
#         print(list[i])
