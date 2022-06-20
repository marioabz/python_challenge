from utils import check_integrity, MIN_VALUE, MAX_VALUE
from custom_exceptions import OutOfRangeException, StatsNotUpdated


class Node(object):
    def __init__(self, value: int):
        self._number = value
        self._quantity = 0
        self._cumulative = 0

    def get_value(self) -> int:
        return self._number

    def add_number(self) -> None:
        self._quantity += 1

    def set_cumulative(self, value: int) -> None:
        self._cumulative = value

    def get_cumulative(self) -> None:
        return self._cumulative

    def get_quantity(self) -> int:
        return self._quantity


class DataCapture(object):

    OFFSET = 1

    def __init__(self):
        self._array = [Node(i) for i in range(MIN_VALUE, MAX_VALUE + 1)]
        self._updated = False
        self.min_updated_node = self._get_node(1)

    def _set_update(self, value: bool) -> None:
        self._updated = value

    def _get_update(self) -> bool:
        return self._updated

    @check_integrity
    def _get_node(self, value: int):
        return self._array[value - DataCapture.OFFSET]

    @check_integrity
    def add(self, value: int) -> None:

        node = self._get_node(value)
        node.add_number()

        if node.get_value() < self.min_updated_node.get_value():
            self.min_updated_node = node

        if self._get_update():
            self._set_update(False)

    @check_integrity
    def less(self, value: int) -> int:

        if not self._get_update():
            raise StatsNotUpdated()

        if value == MIN_VALUE:
            return 0

        node = self._get_node(value - 1)
        return node.get_cumulative()

    @check_integrity
    def greater(self, value: int) -> int:

        if not self._get_update():
            raise StatsNotUpdated()

        node = self._get_node(value)
        last_node = self._get_node(MAX_VALUE)

        return last_node.get_cumulative() - node.get_cumulative()

    @check_integrity
    def between(self, min_value: int, max_value: int) -> int:

        if not self._get_update():
            raise StatsNotUpdated()

        min_node = self._get_node(min_value)
        max_node = self._get_node(max_value)
        min_quantity = min_node.get_quantity()
        inclusive_amount = (
            max_node.get_cumulative() - min_node.get_cumulative() + min_quantity
        )

        return inclusive_amount

    @check_integrity
    def build_stats(self) -> None:

        if self._get_update():
            return

        min_number = self.min_updated_node.get_value()

        for node in self._array[min_number - DataCapture.OFFSET :]:

            if node.get_value() == 1:
                node.set_cumulative(node.get_quantity())
                continue

            past_node = self._get_node(node.get_value() - 1)
            past_cumulative = past_node.get_cumulative()
            ideal_cumulative = node.get_quantity() + past_cumulative
            real_cumulative = node.get_cumulative()
            if ideal_cumulative != real_cumulative:
                node.set_cumulative(ideal_cumulative)

        self.min_updated_node = self._get_node(MAX_VALUE)
        self._set_update(True)
