"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

class StackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        # if len(self.elems) < self.max_size:
        #     self.elems.append(el)
        # elif len(self.elems) == self.max_size:
        #     self.elems.append([])
        #     self.elems[len(self.elems) - 1].append(el)
        if len(self.elems[len(self.elems) - 1]) <= self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

        # def push_in(self, el):
        #     """Предполагаем, что верхний элемент стека находится в конце списка"""
        #     for i in range(0, len(self.elems) - 1, 1):
        #         if len(self.elems[i]) < self.max_size:
        #             self.elems[i].append(el)
        #             break

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)



if __name__ == '__main__':


    stack_1 = StackClass(5)
    print(len(stack_1.elems))

    i = 0
    while i < 40:
        stack_1.push_in(i)
        i += 1

    print(stack_1.elems)

    i = 0
    while i < 48:
        stack_1.pop_out()
        i += 1

    print(stack_1.elems)
