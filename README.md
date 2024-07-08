# Gilded Rose Refactoring Kata Fork

I have written two solutions to this refactoring challenge. This is because I found the stdout of the texttests
did not meet all the requirements of the challenge, so rather than change the stdout, I chose to write a solution
which passed the texttests and then another solution to meet the requirements of the challenge, which I tested
with my own unit tests. If the stdout of the texttests did meet the requirements of the challenge, I would have
written one solution to be tested with both texttests and unit tests.

### 1. To pass the sdtout of the texttests
The ```update_quality``` method which has been refactored is in [python_texttests/gilded_rose.py](python_texttests/gilded_rose.py)

This passes the texttest. However the stdout of the texttest does not meet all the requirements of [info/GildedRoseRequirements.md](info/GildedRoseRequirements.md),
 most notably that Conjured items do not decrease in quality twice as fast as normal items.

To test it, run [start_texttest.sh](start_texttest.sh)

The input is in [python_texttests/texttest_fixture.py](python_texttests/texttest_fixture.py)

The stdout is in [texttests/ThirtyDays/stdout.gr](texttests/ThirtyDays/stdout.gr)

### 2. To meet the requirements in [info/GildedRoseRequirements.md](info/GildedRoseRequirements.md) tested with unit tests
The ```update_quality``` method which has been refactored is in [python_unittests/gilded_rose_2.py](python_unittests/gilded_rose_2.py)

The unit tests I have written to test it are in [python_unittests/test_gilded_rose_2.py](python_unittests/test_gilded_rose_2.py)
