if __name__ == "__main__":
    # Write your solution here
    class ConiferousTree:
        def __init__(self, name: str, age: int, height: float) -> None:
            self.name = name
            self.age = age
            self.height = height
            self._id = hash(f"{name}{age}")

        def grow(self) -> str:
            return f"{self.name} растет"

        def shed_needles(self) -> str:
            return f"{self.name} сбрасывает хвою"

        def __str__(self) -> str:
            return f"Хвойное дерево: {self.name}, возраст: {self.age} лет, высота: {self.height} м"

        def __repr__(self) -> str:
            return f"ConiferousTree(name={self.name!r}, age={self.age}, height={self.height})"

    class Spruce(ConiferousTree):

        def __init__(self, name: str, age: int, height: float, cone_length: float, has_pyramidal_crown: bool) -> None:
            super().__init__(name, age, height)
            self.cone_length = cone_length
            self.has_pyramidal_crown = has_pyramidal_crown

        def grow(self) -> str:
            crown_description = "с пирамидальной кроной" if self.has_pyramidal_crown else "с обычной кроной"
            return f"Ель {self.name} {crown_description} растет в высоту и ширину"

        def shed_needles(self) -> str:
            return super().shed_needles()

        def produce_cones(self) -> str:
            return f"Ель {self.name} образует шишки длиной {self.cone_length} см"

        def __str__(self) -> str:
            crown_info = ", пирамидальная крона" if self.has_pyramidal_crown else ""
            return f"Ель: {self.name}, возраст: {self.age} лет, высота: {self.height} м, шишки: {self.cone_length} см{crown_info}"

        def __repr__(self) -> str:
            return (f"Spruce(name={self.name!r}, age={self.age}, height={self.height}, "
                    f"cone_length={self.cone_length}, has_pyramidal_crown={self.has_pyramidal_crown})")


    class Pine(ConiferousTree):

        def __init__(self, name: str, age: int, height: float, needle_length: float, resin_content: int) -> None:
            super().__init__(name, age, height)
            self.needle_length = needle_length
            self.resin_content = resin_content

        def grow(self) -> str:
            return f"Сосна {self.name} быстро растет в высоту, особенно в первые годы жизни"

        def shed_needles(self) -> str:
            return super().shed_needles()

        def produce_resin(self) -> str:
            resin_level = "высокое" if self.resin_content > 7 else "среднее" if self.resin_content > 4 else "низкое"
            return f"Сосна {self.name} выделяет смолу ({resin_level} содержание)"

        def __str__(self) -> str:
            return f"Сосна: {self.name}, возраст: {self.age} лет, высота: {self.height} м, длина хвои: {self.needle_length} см"

        def __repr__(self) -> str:
            return (f"Pine(name={self.name!r}, age={self.age}, height={self.height}, "
                    f"needle_length={self.needle_length}, resin_content={self.resin_content})")
    pass
