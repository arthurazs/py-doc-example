"""Example module.

Classes:
    UFFClass: an example class.

Functions:
    print_greetings: an example function.
"""


class UFFClass:
    """Example class.

    Attributes:
        name: student's name.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def greetings(self, message: str = 'Hi') -> str:
        """Example function inside a class.

        Args:
            message: message that comes before the student's name.

        Returns:
             message followed by the student's name.
        """
        return message + ', ' + self.name + '!'


def print_greetings(obj: UFFClass) -> None:
    """Prints a greeting for the student.

    Args:
        obj: an object of UFFClass type;
    """
    print(obj.greetings('Hello'))
