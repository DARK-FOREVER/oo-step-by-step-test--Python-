#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teacher类
"""
from typing import List

import Person


class TeacherClass(Person.PersonClass):
    def __init__(self, p_id: int, name: str, age: int, classes: List=[]) -> None:
        super().__init__(p_id, name, age)
        self._classes = classes
        for my_class in self._classes:
            my_class.teacher = self

    @property
    def classes(self):
        return self._classes

    def get_class_info(self) -> str:
        class_numbers = []
        for my_class in self.classes:
            class_numbers.append(str(my_class.number))

        return ', '.join(class_numbers)

    def display_class_info(self) -> str:
        if self.classes:
            output = f'I am a Teacher. I teach Class {self.get_class_info()}.'
        else:
            output = "I am a Teacher. I teach No Class."

        return output

    def introduce(self) -> str:
        return super().introduce() + " " + self.display_class_info()

    def introduce_with(self, sc) -> str:
        if sc.my_class in self.classes:
            return super().introduce() + " " + "I am a Teacher. I teach " + sc.name + "."
        else:
            return super().introduce() + " " + "I am a Teacher. I don't teach " + sc.name + "."

    def is_teaching(self, sc) -> bool:
        return sc.my_class in self.classes

    def print_if_student_join(self, sc, my_class) -> None:
        print(f"I am {self.name}. I know {sc.name} has joined Class {my_class.number}.")

    def print_if_student_become_leader(self, sc, my_class) -> None:
        print(f"I am {self.name}. I know {sc.name} become Leader of Class {my_class.number}.")
