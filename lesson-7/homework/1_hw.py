import math

class Vector:
    def __init__(self, *components):
        """Initialize a vector with any number of components."""
        self.components = tuple(components)
    
    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector{self.components}"
    
    def __add__(self, other):
        """Add two vectors of the same dimension."""
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        """Subtract one vector from another (same dimension required)."""
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        """Multiply by a scalar or compute the dot product with another vector."""
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication must be with a scalar or another vector of the same dimension")
    
    def __rmul__(self, scalar):
        """Allow scalar multiplication from the left side."""
        return self * scalar
    
    def magnitude(self):
        """Return the magnitude (length) of the vector."""
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        """Return a unit vector (vector with length 1)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a / mag for a in self.components))
    
    def __eq__(self, other):
        """Check if two vectors are equal."""
        return isinstance(other, Vector) and self.components == other.components