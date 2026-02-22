from typing import List

from .skills import Skills
from .attributes import Attributes


class Character:

    def __init__(
            self,
            attributes: Attributes,
            skills: Skills,
            attunement: int,
            feats: int
        ):
        self._attributes = attributes
        self._skills = skills
        self._attunement = attunement
        self._feats = feats
        self._level = None


    def get_level(self):
        if self._level:
            return self._level

        level_points = self._attributes.get_level_points()
        level_points += self._skills.get_level_points()

        if level_points < 10:
            self._level = 1
        else:
            self._level = 2 + (level_points - 10) // 5

        return self._level


    def get_light(self) -> List[int]:
        return self._attributes.get_light_levels(self.get_level())


    def get_river(self) -> int:
        return self.get_level() + 1


    def get_spent_exp(self) -> int:

        total_exp = 0

        total_exp += self._attributes.get_exp_spent()
        total_exp += self._skills.get_exp_spent()

        purchased_feats = self._feats - self.get_level() - 1
        total_exp += purchased_feats * 4

        current_attunement = 4
        while current_attunement < self._attunement:
            current_attunement += 1
            total_exp += current_attunement *2

        return total_exp


    def get_focus_roll(self) -> int:
        return self.get_level() + self._attunement


    def get_health(self) -> int:
        return self._attributes.get_health()
