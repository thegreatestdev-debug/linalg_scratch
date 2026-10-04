from __future__ import annotations
import math


class Vector:
    """A vector of floats, implemented without NumPy."""

    def __init__(self, components: list[float]) -> None:
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components: list[float] = [float(c) for c in components]

    def __len__(self) -> int:
        return len(self.components)

    def __getitem__(self, i: int) -> float:
        return self.components[i]

    def __repr__(self) -> str:
        return f"Vector({self.components})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        if len(self) != len(other):
            return False
        return all(
            math.isclose(a, b, abs_tol=1e-9)
            for a, b in zip(self.components, other.components)
        )

    def _check_same_dim(self, other: Vector) -> None:
        if len(self) != len(other):
            raise ValueError(f"Dimension mismatch: {len(self)} vs {len(other)}")

    def __add__(self, other: Vector) -> Vector:
        self._check_same_dim(other)
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other: Vector) -> Vector:
        self._check_same_dim(other)
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar: float) -> Vector:
        return Vector([c * scalar for c in self.components])

    def __rmul__(self, scalar: float) -> Vector:
        return self * scalar

    def dot(self, other: Vector) -> float:
        self._check_same_dim(other)
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        return math.sqrt(self.dot(self))