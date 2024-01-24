import re

text = '+7(123)456-78-90'
m = re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', text)
# print(m)


text = """<point lon="40.8412" lat="52.3425" />
<point lon="40.6324" lat="52.6432" />; <point lon="40.6342" lat="52.641" />
<point lon="40.6342" lat="64.4132" />, <point lon="25.6452" lat=53.4123" />
"""

ar = re.split(r'[\n;,]+', text)  # сплит по нескольким параметрам
# print(ar)


text = """Москва
Казань
Тверь
Самара
Уфа"""


list = re.sub(r'\s*(\w+)\s*', r'<option>\1</option>\n',
              text)  # оборачиваем в <option> все города


count = 0


def replFind(m):  # Match
    global count
    count += 1
    # m.group(1) - name of city
    return f'<option value="{count}">{m.group(1)}</option>\n'


list = re.sub(r'\s*(\w+)\s*', replFind, text)
# print(list)


list, total = re.subn(r'\s*(\w+)\s*', r'<option>\1</option>\n', text)  # подсчитываем сколько раз выполнялось число произведенных замен


rx = re.compile(r'\s*(\w+)\s*')  # компиляция шаблона заранее
list, total = rx.subn(r'<option>\1</option>\n', text)
list2 = rx.subn(replFind, text)
print(list, total, list2, sep="\n")


# print(list, total)
