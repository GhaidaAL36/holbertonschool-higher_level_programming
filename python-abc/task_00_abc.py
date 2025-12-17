#!/usr/bin/env python3
"""
Module that defines an abstract class Animal
and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal"""

    @abstractmethod
    def sound(self):
        """Abstract method return the sound of the animal."""
        pass

class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return dog sound"""
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return cat sound"""
        return "Meow"
