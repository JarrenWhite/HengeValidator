from typing import List

from skills import Skills
from attributes import Attributes


class Character:

    def __init__(
            self,
            attributes: Attributes,
            skills: Skills,
            attunement: int,
            feats: int,
            purchased_feats: int
        ):
        self._attributes = attributes
        self._skills = skills
        self._attunement = attunement
        self._feats = feats
        self._purchased_feats = purchased_feats

        self._level = self._get_level()


    def _get_level(self):
        level_points = self._attributes.get_level_points()
        level_points += self._skills.get_level_points()

        if level_points < 10:
            return 1

        return 2 + (level_points - 10) // 5


    def get_light(self) -> List[int]:
        return self._attributes.get_light_levels(self._get_level())

