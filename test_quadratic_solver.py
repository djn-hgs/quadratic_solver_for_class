import quadratic_solver
import pytest

test_data = [
    (1, 3, 1, 5),
    (1, 2, 1, 0)
]


@pytest.mark.parametrize("a, b, c, D", test_data)
def test_discriminant(a, b, c, D):
    assert quadratic_solver.calc_discriminant(a, b, c) == D


test_data = [
    (1, 3, 2, (-2, -1)),
    (1, 5, 6, (-3, -2))
]

@pytest.mark.parametrize("a, b, c, solutions", test_data)
def test_solve_quadratic(a, b, c, solutions):
    assert quadratic_solver.solve_quadratic(a, b, c) == solutions

def test_negative_discriminant():
    with pytest.raises(ValueError):
        quadratic_solver.solve_quadratic(-1, -1, -1)
