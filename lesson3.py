
'''
if isinstance(1.0, (int, float)):
    print('ok')
else:
    print('false')
'''
a = "dddd"
b = 'gggg\n hhh'\
    'mmmm'
c = '''
nnnn
mmmm
'''
"""
"d = f"text {c}"
print(d)

print(a)
print(b)
print(c)
"""

a_initial = 123
b_digit = 0
d_digit = 0
e_digit = 0
f_reverse = 0

b_digit = a_initial // 100
_c_ = 0
_c_ = a_initial % 100
d_digit = _c_ // 10
e_digit = a_initial % 10
f_reverse = e_digit*100 + d_digit*10 + b_digit
print(a_initial)
print(f_reverse)

additional_str = input('Введите что-нибудь:')
existing_str = "Это строка, в которую {} новую строку".format(additional_str)
new_add = 'замена в строке'
new_str = "Это строка, в которую {} новую строку".format(new_add)
print(existing_str)
print(new_str)
print(len(new_str))

if "строка" in new_str:
    print("Да")
else:
    print("Нет")