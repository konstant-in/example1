'''
Способ с использованием объекта функции для хранения состояния функции

Стоит быть осторожным, давая имена подобным полям функции, так как в Python 2 у функции есть стандартные поля
с названиями, не начинающимися с двух подчёркиваний, например, func_closure, func_code и т.п.
Все они начинаются с func_, поэтому главное не использовать этот префикс и не начинать название поля с __,
в остальных случаях шанс коллизии имён практически равен нулю.
'''

def func5():
    if not hasattr(func5, '_state'):  # инициализация значения
        func5._state = 1
    print('Функция вызывается ',func5._state, 'раз')
    func5._state = func5._state + 1

func5()
func5()
func5()
func5()
