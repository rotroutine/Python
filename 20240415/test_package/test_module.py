# add = lambda x , y : x + y

# def test(x, y) -> int:
#     """
#     This function returns the sum of two numbers.
#     :param x: int
#     :param y: int
#     :return: int
#     """
#     return x + y

__all__ = ['add']

def add(x: int | float, y: int | float) -> int | float:
    return x + y

