
class Attributes:


    def __init__(self, red: int, green: int, blue: int, gold: int):
        self._red = red
        self._green = green
        self._blue = blue
        self._gold = gold


    def get_level_points(self) -> int:
        points = self._red + self._green + self._blue + self._gold

        return points


    def get_exp_spent(self) -> int:

        sorted_attrs = sorted([self._red, self._green, self._blue, self._gold], reverse=True)

        total_costs = 0

        total_costs += self._determine_cost(2, sorted_attrs[0])
        total_costs += self._determine_cost(2, sorted_attrs[2])
        total_costs += self._determine_cost(1, sorted_attrs[3])
        total_costs += self._determine_cost(1, sorted_attrs[4])

        return total_costs


    def _determine_cost(self, starting: int, final: int) -> int:
        exp_cost = 0
        current = starting

        while current < final:
            exp_cost += (current + 1) *4

        return exp_cost
