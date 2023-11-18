#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Student类
"""

import Person as ps
from typing import NoReturn


class StudentClass(ps.PersonClass):
    def __init__(self, p_id: int, name: str, age: int, my_class) -> NoReturn:
        super().__init__(p_id, name, age)
        self._my_class = my_class

    @property
    def my_class(self) -> type:
        return self._my_class

    @my_class.setter
    def my_class(self, my_class) -> NoReturn:
        self._my_class = my_class

    def introduce(self) -> str:
        if self == self.my_class.leader:
            output = f"I am Leader of Class {self.my_class.number}."
        else:
            output = f"I am at Class {self.my_class.number}."

        return f"{super().introduce()} I am a Student. {output}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StudentClass):
            is_equal = (self.id == other.id and self.name == other.name and self.age == other.age
                        and self.my_class == other.my_class)
            return is_equal
        return False
