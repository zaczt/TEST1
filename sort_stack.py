from enum import Enum

class Stacks(Enum):
    REJECTED = "REJECTED"
    SPECIAL = "SPECIAL"
    STANDARD = "STANDARD"


def sort(width, height, length, mass):
    """
    Assigns a stack type based on given dimensions

    Parameters:
    - width (int/float): Package width in cm.
    - height (int/float): Package height in cm.
    - length (int/float): Package length in cm.
    - mass (int/float): Package mass in kg.

    Returns:
    - str: Stack type such as "STANDARD", "SPECIAL" or "REJECTED"
    """
    if not (isinstance(width, (int, float)) and width > 0 and
            isinstance(height, (int, float)) and height > 0 and
            isinstance(length, (int, float)) and length > 0 and
            isinstance(mass, (int, float)) and mass >= 0):
        raise ValueError("Dimensions should be a positive number.")

    # Calculate volume and largest dimension
    volume = width * height * length
    max_dimension = max(width, height, length)
    print(f"Volume: {volume}, max dimension: {max_dimension}")

    # Validate if the package is bulky
    is_bulky = volume >= 1000000 or max_dimension >= 150

    # Validate if the package is heavy
    is_heavy = mass >= 20

    # Assign the correct stack
    if is_bulky and is_heavy:
        return Stacks.REJECTED.value
    elif is_bulky or is_heavy:
        return Stacks.SPECIAL.value
    else:
        return Stacks.STANDARD.value


if __name__ == "__main__":
    assert sort(100, 100, 100, 10) == "SPECIAL"
