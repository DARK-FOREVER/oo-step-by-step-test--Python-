#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Class类
"""


class Klass:
    _leader = None

    def __init__(self, **kw) -> None:
        self._number = kw.get('number', None)
        self._teacher = kw.get('teacher', None)

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher) -> None:
        self._teacher = teacher

    @property
    def leader(self):
        return self._leader

    @leader.setter
    def leader(self, leader) -> None:
        self._leader = leader

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Klass):
            if self._teacher:
                return self._number == other._number and self._teacher == other._teacher
            else:
                return self._number == other._number
        return False

    def is_in(self, student) -> bool:
        return self == student.my_class

    def get_display_name(self) -> str:
        return f"Class {self.number}"

    def append_member(self, student) -> None:
        student.my_class = self
        if self.teacher:
            self.teacher.print_if_student_join(student, self)

    def assign_leader(self, student) -> None:
        if self.is_in(student):
            self.leader = student
            if self.teacher:
                self.teacher.print_if_student_become_leader(student, self)
        else:
            print("It is not one of us.")
