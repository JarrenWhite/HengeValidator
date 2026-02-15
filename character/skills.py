from typing import List


class Skills:

    def __init__(self, skills: List[int]):
        self._all_skills = skills


    def get_level_points(self) -> int:
        points = 0

        for skill in self._all_skills:
            if skill == 3:
                points += 1

        return points


    def get_exp_spent(self) -> int:

        sorted_skills = sorted(self._all_skills, reverse=True)

        total_costs = 0

        total_costs += self._determine_cost(2, sorted_skills[0])
        total_costs += self._determine_cost(1, sorted_skills[1])
        total_costs += self._determine_cost(1, sorted_skills[2])

        for skill in sorted_skills[3:]:
            total_costs += self._determine_cost(0, skill)

        return total_costs


    def _determine_cost(self, starting: int, final: int) -> int:
        exp_cost = 0
        current = starting

        while current < final:
            current += 1
            exp_cost += current *2

        return exp_cost
