"""
Домашнее задание для лекции "Задачки на собеседованиях для продвинутых,
с тонкостями языка"

Описание
    1. Перестроить заданный связанный список (LinkedList) в обратном порядке.
    Для этого использовать метод `LinkedList.reverse()`, представленный
    в данном файле.
    2. Определить сложность алгоритма.
    3. Определить потребление памяти в big-O notation.

Примечание
    Проверить работоспособность решения можно при помощи тестов,
    которые можно запустить следующей командой:

    python3 -m unittest linked_list_reverse.py
"""

import unittest

from typing import Iterable


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def reverse(self):
        """Переопределяем в связаном списке элементы next и заголовки
        для 1 (текущ. заголов.)- next будет None т.е.делаем последним элементом (end).Заголовком становится 2 (head_new)
        берем 2, next будет 1, end = 2, заголовком становится 3 (head_new)
        берем 3, next будет 2, end = 3, заголовком становится 4 (head_new)
        берем 4, next будет 3, end = 4, заголовком становится None (head_new) - тут цикл while останавливается (False)
        """

        head_new = self.head
        end = None

        while head_new:
            head_new.next, end, head_new = end, head_new, head_new.next

        self.head = end  # Переопределяем заголовок на подходящий параметр (head)

        return self.head


class LinkedListTestCase(unittest.TestCase):

    def test_reverse(self):
        cases = dict(
            empty=dict(
                items=[],
                expected_items=[],
            ),
            single=dict(
                items=[1],
                expected_items=[1],
            ),
            double=dict(
                items=[1, 2],
                expected_items=[2, 1],
            ),
            triple=dict(
                items=[1, 2, 3],
                expected_items=[3, 2, 1],
            ),
        )
        for case, data in cases.items():
            with self.subTest(case=case):
                linked_list = LinkedList(data['items'])
                linked_list.reverse()
                self.assertListEqual(
                    data['expected_items'],
                    list(linked_list),
                )


test = LinkedList([1, 2, 3, 4])
print('Первый next {}'.format(test.head.next.data))
print('Второй next {}'.format(test.head.next.next.data))
print('Третий next {}'.format(test.head.next.next.next.data))

test.reverse()
print('Сделали реверс связаного списка')
print('Первый next {}'.format(test.head.next.data))
print('Второй next {}'.format(test.head.next.next.data))
print('Третий next {}'.format(test.head.next.next.next.data))
