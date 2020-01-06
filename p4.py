'''
Использование декоратора, выполняющего необходимые вычисления

Если вернуться к исходному примеру,
то для подсчёта числа вызовов функции будет также может быть удобно использовать декораторы.
Это позволит в том числе и переиспользовать код.

При желании вы можете скомбинировать этот способ с каким-нибудь из описанных ранее.
'''

# Для Python 3 код может выглядеть, например, так:
from functools import wraps


def call_count(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(count)

    return wrapper


# Использоваться это будет следующим образом:
@call_count
def f():
    pass


f()  # 1
f()  # 2
f()
f()

'''
В Python 2 нет nonlocal, но можно использовать изменяемые переменные:

from functools import wraps


def call_count(func):
    count = [0]
    @wraps(func)
    def wrapper(*args, **kwargs):
        count[0] += 1
        func(*args, **kwargs)
        print(count[0])
    return wrapper

'''
