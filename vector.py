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
        # TODO: return False if other is not a Vector or lengths differ;
        # compare components with math.isclose (never == on floats)
        raise NotImplementedError

    def _check_same_dim(self, other: Vector) -> None:
        if len(self) != len(other):
            raise ValueError(f"Dimension mismatch: {len(self)} vs {len(other)}")

    def __add__(self, other: Vector) -> Vector:
        # TODO: call _check_same_dim, then add component-wise
        raise NotImplementedError

    def __sub__(self, other: Vector) -> Vector:
        # TODO
        raise NotImplementedError

    def __mul__(self, scalar: float) -> Vector:
        # TODO: scalar multiplication, so Vector([1,2]) * 3
        raise NotImplementedError

    def __rmul__(self, scalar: float) -> Vector:
        # TODO: makes 3 * Vector([1,2]) work. Reuse __mul__.
        raise NotImplementedError

    def dot(self, other: Vector) -> float:
        # TODO: sum of products of matching components
        raise NotImplementedError

    def magnitude(self) -> float:
        # TODO: sqrt of dot with itself
        raise NotImplementedError