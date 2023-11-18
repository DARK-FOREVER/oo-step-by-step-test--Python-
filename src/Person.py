#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Person类
"""


class PersonClass:
    def __init__(self, p_id: int, name: str, age: int) -> None:
        self._p_id = p_id
        self._p_name = name
        self._age = age

    @property
    def id(self) -> int:
        return self._p_id

    @id.setter
    def id(self, p_id: int) -> None:
        self._p_id = p_id

    @property
    def name(self) -> str:
        return self._p_name

    @name.setter
    def name(self, name: str) -> None:
        self._p_name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def introduce(self) -> str:
        return f"My name is {self.name}. I am {self.age} years old."
