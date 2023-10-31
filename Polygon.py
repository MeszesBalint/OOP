class Polygon:
    id_counter = 0

    def __init__(self, sides, color="sárga"):
        self.sides = sides
        self.color = color
        self.counter = Polygon.id_counter
        Polygon.id_counter += 1


my_polygon = Polygon(sides=4, color="piros")

print(f"Ennek a polygonnak {my_polygon.sides} oldal van és {my_polygon.color} és a számom {my_polygon.id_counter}")

your_polygon = Polygon(sides=3, color="kék")

print(f"Ennek a polygonnak {your_polygon.sides} oldal van és {your_polygon.color}és a számom {your_polygon.id_counter}")

their_polygon = Polygon(sides=3, color="kék")

print(f"Ennek a polygonnak {their_polygon.sides} oldal van és {their_polygon.color}és a számom {their_polygon.id_counter}")

their_polygon = Polygon(5)

print(f"Ennek a polygonnak {their_polygon.sides} oldal van és {their_polygon.color}és a számom {their_polygon.id_counter}")

their_polygon.sides = 6

print(f"Ennek a polygonnak {their_polygon.sides} oldal van és {their_polygon.color}és a számom {their_polygon.id_counter}")

print(f"A counter állása: {Polygon.id_counter}")
