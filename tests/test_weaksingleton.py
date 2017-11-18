import gc

from unittest import TestCase, mock

from singlepy import WeakSingleton


class Number(metaclass=WeakSingleton):

    def __init__(self, number):
        self.value = number


class NumberSum(metaclass=WeakSingleton):

    def __init__(self, *numbers):
        self.value = numbers

    @staticmethod
    def _make_singleton_key(*numbers):
        return sum(numbers)


class ResourceManager(metaclass=WeakSingleton):

    def __init__(self, resource):
        self.resource = resource
        self.resource.open()

    def __del__(self):
        self.resource.close()


class TestWeakSingleton(TestCase):

    def _do_singleton_test(self, cls, args_a, value_a, args_b, value_b, args_c, value_c):
        a = cls(*args_a)
        b = cls(*args_b)
        c = cls(*args_c)
        id_a = id(a)
        id_c = id(c)

        assert a.value == value_a
        assert b.value == value_b
        assert c.value == value_c

        assert a is b
        assert a is not c
        assert id_a == id(cls(*args_a))
        assert id_c == id(cls(*args_c))

        del c
        gc.collect()

        assert id_c != id(cls(*args_c))

        del a
        gc.collect()
        assert id(b) == id_a
        del b
        gc.collect()
        assert id_a != id(cls(*args_a))

    def test_simple_case(self):
        self._do_singleton_test(Number, (1,), 1, (1,), 1, (2,), 2)

    def test_custom_singleton_key(self):
        self._do_singleton_test(NumberSum, (1, 2, 3), (1, 2, 3), (3, 3), (1, 2, 3), (3, 4, 5), (3, 4, 5))

    def test_custom_del(self):
        mock_resource = mock.Mock()
        instance = ResourceManager(mock_resource)
        mock_resource.open.assert_called_once_with()
        del instance
        gc.collect()
        mock_resource.close.assert_called_once_with()
