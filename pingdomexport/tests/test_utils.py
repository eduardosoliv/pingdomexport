from pingdomexport import utils

class TestIntervals:
    def test_regular(self):
        assert utils.intervals(1, 12000) == [[1, 3601], [3601, 7201], [7201, 10801], [10801, 12000]]
    def test_match_end(self):
        assert utils.intervals(1, 2001, 1000) == [[1, 1001], [1001, 2001]]
