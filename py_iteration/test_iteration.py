import math

import iteration


def test_0():
    assert math.isclose(iteration.sin_(0), 0)


def test_pi_2():
    assert math.isclose(iteration.sin_(math.pi/2), 1)


def test_pi_6():
    assert math.isclose(iteration.sin_(math.pi/6), 0.5)