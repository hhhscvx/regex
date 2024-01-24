import re

text = 'Google, Gooogle, Goooooogle'
match = re.findall(r'o{2,5}', text)  # {min,max}, по возможности берет большее (5)


text = 'Google, Gooogle, Goooooogle'
match = re.findall(r'o{2,5}?', text)  # {min,max}?, берет наименьшее (2)


# {m} - повторение выражения ровно m раз
# {m,} - повторение от m и более
# {,n} - повторение не более n раз


text = 'Google, Gooogle, Goooooogle'
match = re.findall('Go{2,}gle', text)


phone = '89826546664'
match = re.findall(r'8\d{10}', phone)


# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности ({0,})
# + - от единицы до бесконечности ({1,})


text = 'стеклянный, стекляный'
match = re.findall(r'стеклянн?ый', text)  # вторая н может быть, а может ее и не быть


text = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001'
match = re.findall(r'\w+\s*=\s*[^;]+', text)  # \w - атрибут длиной от 1 до беск; \s* - может быть пробел а может и не быть; = \s*; [^;] - все слова кроме ; от 1 до беск;


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r'<img.*>', text)  # - этот чел жадный и т.к. в конце так же есть >, он возьмет как можно больше, до туда


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r'<img.*?>', text)  # рабочий вариант, берет самую короткую последовательность


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r'<img[^>]*>', text)  # еще рабочий


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'  # проверка на src
match = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]+>', text)  # после img должен быть пробел -> src -> мб пробел -> = -> мб пробел -> все значения до >;


print(match)
