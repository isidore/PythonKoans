#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutInheritance(Koan):
    class Dog:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        def bark(self):
            return "WOOF"

    class Chihuahua(Dog):
        def wag(self):
            return "happy"

        def bark(self):
            return "woof woof"


    def test_dogs_are_still_dogs(self):
        boef = self.Dog('Boef')
        self.assertEqual(self.Dog, __)

    def test_but_what_are_chihuahuas(self):
        tinkerbell = self.Chihuahua('Tinkerbell')
        self.assertEqual(__, type(tinkerbell))

    def test_subclasses_have_the_parent_as_an_ancestor(self):
        self.assertEqual(__, issubclass(self.Chihuahua, self.Dog))

    def test_all_defined_classes_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(self.Chihuahua, object))

    def test_all_built_in_classes_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(str, object))

#TODO: also do isinstance not only issubclass!


    def test_instances_inherit_behavior_from_parent_class(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.name)

    def test_subclasses_add_new_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.wag())

        fido = self.Dog("Fido")
        with self.assertRaises(___): fido.wag()

    def test_subclasses_can_modify_existing_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.bark())

        fido = self.Dog("Fido")
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    class BullDog(Dog):
        def bark(self):
            return super().bark() + ", GRR"

    def test_subclasses_can_invoke_parent_behavior_via_super(self):
        ralph = self.BullDog("Ralph")
        self.assertEqual(__, ralph.bark())

    # ------------------------------------------------------------------

    class GreatDane(Dog):
        def growl(self):
            return super().bark() + ", GROWL"

    def test_super_works_across_methods(self):
        george = self.GreatDane("George")
        self.assertEqual(__, george.growl())

    # ---------------------------------------------------------

    class Pug(Dog):
        def __init__(self, name):
            pass

    class Greyhound(Dog):
        def __init__(self, name):
            super().__init__(name)

    def test_base_init_does_not_get_called_automatically(self):
        snoopy = self.Pug("Snoopy")
        with self.assertRaises(___): name = snoopy.name

    def test_base_init_has_to_be_called_explicitly(self):
        boxer = self.Greyhound("Boxer")
        self.assertEqual(__, boxer.name)
