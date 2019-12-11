"""Day 11 Tests"""

# import pytest
from space_police import part1, part2


def test_parts():
    assert part1() == 1967
    assert (
        part2()
        == " #  # ###  #  # ####  ##  #### ###  #  #   \n # #  #  # #  # #    #  #    # #  # # #    \n ##   ###  #  # ###  #      #  ###  ##     \n # #  #  # #  # #    # ##  #   #  # # #    \n # #  #  # #  # #    #  # #    #  # # #    \n #  # ###   ##  ####  ### #### ###  #  #   "
    )
