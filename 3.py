import re

text = 'lat = 5, lon=7'
match = re.findall(r'\w+\s*=\s*\d+', text)  # но это работает не только для lat и lon (a = 5, b=7)


text = 'lat = 5, lon=7, a=5'
match = re.findall(r'(lat|lon)\s*=\s*(\d+)', text)  # использовать можно только lat | lon (lat или lon); сохраняется то что в скобках (ключ, значение)


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)  # значение в кавычках len>=1 минорное; но если src="bg.jpg' - то все равно сработает, ща исправим


text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text)  # \1 - то же значение что хранит первая сохраняющая скобка


# Имя сохраняющей скобки
#  (?P<name>...) - (?P=name)


print(match)
