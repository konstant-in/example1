'''Использование класса с поведением функции

Этот способ заключается в создании класса с поведением функции. Это наиболее удобный и безопасный, по моему мнению,
способ реализации подобного поведения. Просто создайте класс и перегрузите его метод __call__:

Это увеличивает объём кода, но добавляет удобств от использования функциональности класса.
'''

class FuncCreator:
    def __init__(self, start_state):
        self.state = start_state

    def __call__(self):
        print(self.state)
        self.state += 1


func6 = FuncCreator(1)
#print(func6.state)
func6()
#print(func6.state)
func6()
#print(func6.state)
func6()
#print(func6.state)
func6()
