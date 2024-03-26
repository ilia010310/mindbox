import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        if any(side <= 0 for side in (side1, side2, side3)):
            raise ValueError("Длины сторон должны быть положительными")
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

# Пример использования:
if __name__ == "__main__":
    # Вычисление площади круга
    radius = 5
    circle_area = ShapeCalculator.circle_area(radius)
    print(f"Площадь круга с радиусом {radius}: {circle_area:.2f}")

    # Вычисление площади треугольника
    side1, side2, side3 = 3, 4, 5
    triangle_area = ShapeCalculator.triangle_area(side1, side2, side3)
    print(f"Площадь треугольника со сторонами {side1}, {side2}, {side3}: {triangle_area:.2f}")

    # Проверка на прямоугольный треугольник
    is_right_triangle = ShapeCalculator.is_right_triangle(side1, side2, side3)
    print(f"Треугольник со сторонами {side1}, {side2}, {side3} является прямоугольным: {is_right_triangle}")

