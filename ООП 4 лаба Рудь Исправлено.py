if __name__ == "__main__":
    # Write your solution here
    class ConiferousTree:
        """
        Базовый класс для хвойных деревьев.

        Атрибуты:
            name (str): Название дерева.
            height (float): Высота дерева в метрах.
            crown_width (float): Ширина кроны дерева в метрах.
        """

        def __init__(self, name: str, height: float, crown_width: float) -> None:
            """
            Конструктор класса ConiferousTree.

            Аргументы:
                name (str): Название дерева.
                height (float): Высота дерева в метрах.
                crown_width (float): Ширина кроны дерева в метрах.
            """
            self.name = name
            self.height = height
            self.crown_width = crown_width

        # Свойство для получения имени дерева
        @property
        def name(self):
            return self._name

        # Сеттер для изменения имени дерева
        @name.setter
        def name(self, value):
            if not isinstance(value, str):
                raise ValueError("Имя должно быть строкой")
            self._name = value

        # Свойство для получения высоты дерева
        @property
        def height(self):
            return self._height

        # Сеттер для изменения высоты дерева
        @height.setter
        def height(self, value):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("Высота должна быть положительным числом")
            self._height = value

        # Свойство для получения ширины кроны дерева
        @property
        def crown_width(self):
            return self._crown_width

        # Сеттер для изменения ширины кроны дерева
        @crown_width.setter
        def crown_width(self, value):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("Ширина кроны должна быть положительным числом")
            self._crown_width = value

        def __str__(self) -> str:
            """Магический метод для вывода строки, представляющей объект ConiferousTree."""
            return f"{self.name} is a coniferous tree with height {self.height}m and crown width {self.crown_width}m."

        def __repr__(self) -> str:
            """Магический метод для представления объекта ConiferousTree."""
            return f"ConiferousTree(name='{self.name}', height={self.height}, crown_width={self.crown_width})"

        def grow(self, years: int) -> None:
            """
            Метод, имитирующий рост дерева за указанный период лет.

            Аргументы:
                years (int): Количество лет роста.
            """
            self.height += 0.25 * years  # Примерный прирост высоты дерева
            self.crown_width += 0.15 * years  # Примерный прирост ширины кроны

    class Fir(ConiferousTree):
            """
            Класс для описания ели.

            Атрибуты:
                needle_length (float): Длина иголок в сантиметрах.
            """

            def __init__(self, name: str, height: float, crown_width: float, needle_length: float) -> None:
                """
                Конструктор класса Fir.

                Аргументы:
                    name (str): Название дерева.
                    height (float): Высота дерева в метрах.
                    crown_width (float): Ширина кроны дерева в метрах.
                    needle_length (float): Длина иголок в сантиметрах.
                """
                super().__init__(name, height, crown_width)
                self.needle_length = needle_length

            def __str__(self) -> str:
                """Перегрузка метода __str__ для вывода информации об ели."""
                return f"{super().__str__()} with needle length {self.needle_length}cm."

            def __repr__(self) -> str:
                """Перегрузка метода __repr__ для представления объекта Fir."""
                return f"Fir(name='{self.name}', height={self.height}, crown_width={self.crown_width}, needle_length={self.needle_length})"

            def grow(self, years: int) -> None:
                """
                Перегрузка метода grow для ели.

                Ель растет быстрее, чем обычные хвойные деревья.

                Аргументы:
                    years (int): Количество лет роста.
                """
                self.height += 0.35 * years  # Ель растет быстрее
                self.crown_width += 0.20 * years  # Увеличение ширины кроны
    class Pine(ConiferousTree):
            """
            Класс для описания сосны.

            Атрибуты:
                needle_length (float): Длина иголок в сантиметрах.
            """

            def __init__(self, name: str, height: float, crown_width: float , needle_length: float) -> None:
                """
                Конструктор класса Pine.

                Аргументы:
                    name (str): Название дерева.
                    height (float): Высота дерева в метрах.
                    crown_width (float): Ширина кроны дерева в метрах.
                    needle_length (float): Длина иголок в сантиметрах.
                """
                super().__init__(name, height)
                self.needle_length = needle_length

            def __str__(self) -> str:
                """Перегрузка метода __str__ для вывода информации об сосне."""
                return f"{super().__str__()} with needle length {self.needle_length}cm."

            def __repr__(self) -> str:
                """Перегрузка метода __repr__ для представления объекта Pine."""
                return f"Pine(name='{self.name}', height={self.height}, crown_width={self.crown_width}, needle_length={self.needle_length})"

            def grow(self, years: int) -> None:
                """
                Перегрузка метода grow для сосны.

                Сосна растет медленнее, чем обычные хвойные деревья.

                Аргументы:
                    years (int): Количество лет роста.
                """
                self.height += 0.5 * years  # Сосна растет быстрее
                self.crown_width += 0.1 * years  # Увеличение ширины кроны


    pass
