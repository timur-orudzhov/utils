import functools
from typing import Any, List, Mapping, Tuple, Union


def partial_class(cls, *args, **kwargs):
    """Partial для класса."""

    class NewCls(cls):
        __init__ = functools.partialmethod(cls.__init__, *args, **kwargs)

    return NewCls


def nearest_value(source_numbers: List[Union[int, float]],
                  value: Union[int, float]) -> int:
    """Возвращает ближайшее значение из переданого списка значений.

    :param source_numbers: источник значений, в котором будет осуществляться
    поиск
    :param value: значение, относительно которого будет выбрано ближайшее
    значение

    Example:
    nearest_value([2, 4, 8], 3) -> 2
    nearest_value([2.4, 3.5], 3) -> 3.5
    """

    return min(source_numbers, key=lambda x: abs(x - value))


def nearest_value_from_map(source_mapping: Mapping[Union[int, float], Any],
                           value: Union[int, float]) -> Any:
    """Возвращает ближайшее значение из переданого mapping-а.

    :param source_mapping: mapping, в котором будет осуществляться
    поиск
    :param value: значение, относительно которого будет выбрано ближайшее
    значение

    Example:
    nearest_value_from_map({2: 'foo', 4: 'bar', 8: 'baz'}, 3) -> 'foo'
    nearest_value_from_map({2.4: 'foo', 3.5: 'bar'}, 3) -> 'bar'
    """

    return source_mapping[min(source_mapping, key=lambda x: abs(x - value))]


def get_nested_value(source: Mapping, key: str):
    """Get nested value from composite dict.

    :param source:
    :param key: supports composite keys like foo.bar or foo.0.bar
    :return: value
    """
    def _try_convert_to_int(value):
        try:
            return int(value)
        except ValueError:
            return value

    keys = key.split('.')

    return functools.reduce(lambda x, y: x[_try_convert_to_int(y)], keys, source)
