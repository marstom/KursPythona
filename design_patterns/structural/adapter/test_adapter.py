import pytest
import unittest

from hole import RoundHole, RoundPeg, SquarePeg, SquarePegAdapter


@pytest.mark.parametrize("peg_radius, hole_radius, fits_hole",
                         [
                             (13, 3, False),
                             (10, 9, False),
                             (10, 10, True),
                             (10, 11, True),
                             (3, 3, True),
                             (3, 10, True),
                             (0, 0, True),
                         ])
def test_round_peg(peg_radius, hole_radius, fits_hole):
    round_hole = RoundHole(radius=hole_radius)
    round_peg = RoundPeg(radius=peg_radius)
    assert round_hole.fits(round_peg) is fits_hole


def test_square_peg_to_round_hole_is_not_compatibile():
    round_hole = RoundHole(radius=10)
    square_peg = SquarePeg(width=10)

    # SquarePeg' object has no attribute 'get_radius'
    with pytest.raises(AttributeError) as e:
        round_hole.fits(square_peg)


def test_square_peg_to_round_hole_adapter():
    round_hole = RoundHole(radius=10)
    square_peg = SquarePegAdapter(SquarePeg(width=11))
    print(round_hole.get_radius(), square_peg.get_radius())
    assert round_hole.fits(square_peg) is True