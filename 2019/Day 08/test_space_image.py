"""Day N Tests"""

import pytest
from space_image import part1, part2


def test_parts():
    assert part1() == 2375
    # RKHRY
    assert (
        part2()
        == "###  #  # #  # ###  #   #\n#  # # #  #  # #  # #   #\n#  # ##   #### #  #  # # \n###  # #  #  # ###    #  \n# #  # #  #  # # #    #  \n#  # #  # #  # #  #   #  "
    )
