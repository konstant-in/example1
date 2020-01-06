"""
Использование изменяемого объекта, как значение по умолчанию для параметра

Этот способ заключается в том, чтобы создать функцию, у которой будет необязательный параметр, использующий изменяемое значение в качестве состояния:

В качестве объекта состояния можно использовать любой изменяемый объект. Это использует то, что все значения по умолчанию присваиваются один раз.
"""
def func7(state=[]):
    if not state:
        state.append(1)
    print(state[0])
    state[0] += 1


func7()  # 0
func7()  # 1
func7()
func7()
func7([])
func7()

