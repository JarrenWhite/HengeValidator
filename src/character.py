from typing import List

from src.skills import Skills
from src.attributes import Attributes


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

        self._level = self._get_level()


    def _get_level(self):
        level_points = self._attributes.get_level_points()
        level_points += self._skills.get_level_points()

        if level_points < 10:
            return 1

        return 2 + (level_points - 10) // 5


    def get_light(self) -> List[int]:
        return self._attributes.get_light_levels(self._get_level())


    def get_spent_exp(self) -> int:

        total_exp = 0

        total_exp += self._attributes.get_exp_spent()
        total_exp += self._skills.get_exp_spent()

        purchased_feats = self._feats - self._level
        total_exp += purchased_feats * 4

        current_attunement = 4
        while current_attunement < self._attunement:
            total_exp += (current_attunement + 1) *2

        return total_exp


    def get_focus_roll(self) -> int:
        return self._level + self._attunement
