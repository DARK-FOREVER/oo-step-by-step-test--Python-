#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试用例"""

import io
import sys

import src.Person as sp
import src.MyClass as sclass
import Student as sd
import Teacher as t


class TestOOStep:

    def setup_class(self) -> None:
        self.klass = sclass.Klass(number=2)
        print("\n开始执行测试用例")

    @staticmethod
    def teardown_class() -> None:
        print("\n执行测试用例完毕")

    def test_should_person_have_id_name_and_age(self) -> None:
        person = sp.PersonClass(1, 'Tom', 21)
        assert person.name == 'Tom'
        assert person.age == 21

    def test_should_person_with_same_id_be_same_one(self) -> None:
        person1 = sp.PersonClass(1, 'Tom', 21)
        person2 = sp.PersonClass(1, 'Tom', 21)
        assert person1.id == person2.id and person1.name == person2.name and person1.age == person2.age

    def test_should_person_have_an_introduce_method_which_introduce_person_with_name_and_age(self) -> None:
        tom = sp.PersonClass(1, 'Tom', 21)
        intro = tom.introduce()
        assert "My name is Tom. I am 21 years old." == intro

    def test_should_class_have_a_number(self) -> None:
        assert self.klass.number == 2

    def test_should_class_get_display_name(self) -> None:
        assert self.klass.get_display_name() == "Class 2"

    def test_should_class_not_assign_a_student_as_leader_when_student_is_not_a_member(self) -> None:
        jerry = sd.StudentClass(1, "Jerry", 8, sclass.Klass(number=5))

        stdout = sys.stdout
        sys.stdout = io_obj = io.StringIO()
        self.klass.assign_leader(jerry)
        sys.stdout = stdout
        result = io_obj.getvalue()

        assert result == "It is not one of us.\n"

    def test_should_class_assign_a_member_student_as_leader(self) -> None:
        jerry = sd.StudentClass(1, "Jerry", 8, self.klass)
        self.klass.append_member(jerry)
        self.klass.assign_leader(jerry)
        assert self.klass.leader == jerry

    def test_should_student_have_name_age_and_class_number(self) -> None:
        tom = sd.StudentClass(1, "Tom", 21, self.klass)
        assert tom.name == "Tom"
        assert tom.age == 21
        assert tom.my_class == self.klass

    def test_should_student_introduce_with_class(self) -> None:
        tom = sd.StudentClass(1, "Tom", 21, self.klass)
        assert tom.introduce() == "My name is Tom. I am 21 years old. I am a Student. I am at Class 2."

    def test_should_student_introduce_itself_as_class_leader(self) -> None:
        tom = sd.StudentClass(1, "Tom", 21, self.klass)
        self.klass.append_member(tom)
        self.klass.assign_leader(tom)
        assert tom.introduce() == "My name is Tom. I am 21 years old. I am a Student. I am Leader of Class 2."

    def test_should_teacher_have_name_and_age_and_classes(self) -> None:
        class_list = [self.klass]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        assert tom.name == "Tom"
        assert tom.age == 21
        assert len(tom.classes) == 1
        assert tom.classes[0] == self.klass

    def test_should_teacher_introduce_itself_with_which_classes_it_teaches(self) -> None:
        class_list = [self.klass, sclass.Klass(number=3)]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        assert tom.introduce() == "My name is Tom. I am 21 years old. I am a Teacher. I teach Class 2, 3."

    def test_should_teacher_introduce_itself_with_no_class_teaching(self) -> None:
        tom = t.TeacherClass(1, "Tom", 21)
        assert tom.introduce() == "My name is Tom. I am 21 years old. I am a Teacher. I teach No Class."

    def test_should_teacher_isTeaching_return_true_when_the_student_is_in_any_classes_the_teacher_teaches(self) -> None:
        class_list = [self.klass, sclass.Klass(number=3)]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, self.klass)
        assert tom.is_teaching(jerry)

    def test_should_teacher_isTeaching_return_false_when_the_student_is_not_in_all_the_classes_the_teacher_teaches(self) -> None:
        class_list = [self.klass]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, sclass.Klass(number=3))
        assert not tom.is_teaching(jerry)

    def test_should_teacher_introduce_a_student_it_teaches(self) -> None:
        class_list = [self.klass]
        tom = t.TeacherClass(1, 'Tom', 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, self.klass)
        assert tom.introduce_with(jerry) == "My name is Tom. I am 21 years old. I am a Teacher. I teach Jerry."

    def test_should_teacher_introduce_a_student_it_does_not_teach(self) -> None:
        class_list = [sclass.Klass(number=1)]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, sclass.Klass(number=2))
        assert tom.introduce_with(jerry) == "My name is Tom. I am 21 years old. I am a Teacher. I don't teach Jerry."

    def test_should_teacher_be_notified_when_student_join_any_classes_it_teaches(self) -> None:
        class_list = [self.klass]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, sclass.Klass(number=3))

        stdout = sys.stdout
        sys.stdout = io_obj = io.StringIO()
        self.klass.append_member(jerry)
        sys.stdout = stdout
        result = io_obj.getvalue()

        assert result.endswith("I am Tom. I know Jerry has joined Class 2.\n")

    def test_should_teacher_be_notified_when_any_class_it_teaches_assigned_a_leader(self) -> None:
        class_list = [self.klass]
        tom = t.TeacherClass(1, "Tom", 21, class_list)
        jerry = sd.StudentClass(1, "Jerry", 8, sclass.Klass(number=3))

        stdout = sys.stdout
        sys.stdout = io_obj = io.StringIO()
        self.klass.append_member(jerry)
        self.klass.assign_leader(jerry)
        sys.stdout = stdout
        result = io_obj.getvalue()

        assert result.endswith("I am Tom. I know Jerry become Leader of Class 2.\n")
