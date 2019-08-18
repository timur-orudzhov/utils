from typing import Any, List, Mapping, Tuple, Union


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
