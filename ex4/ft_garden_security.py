class SecurePlant:
    """represent a plant with protected and validated attributes
        atributtes:
        __name:str => name of the plant (private),
        __height:int => height of the plant in cm (private)
        __age:int => age of the plant in days (private)
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a new SecurePlant instance"""
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        """return the plant name"""
        return self.__name

    def get_height(self) -> int:
        """return the plant height"""
        return self.__height

    def set_height(self, height: int) -> None:
        """Set the plant's height if valid"""
        if isinstance(height, int) and height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted:"
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_age(self) -> int:
        """return the plant age"""
        return self.__age

    def set_age(self, age: int) -> None:
        """Set the plant's age if valid"""
        if isinstance(age, int) and age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self) -> None:
        """Display the plant's information in a formatted way."""
        print(f"\nCurrent plant: {self.__name} ({self.__height}cm,"
              f"{self.__age} days)")


def main() -> None:
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    p1.set_height(-5)
    p1.get_info()


if __name__ == "__main__":
    main()
