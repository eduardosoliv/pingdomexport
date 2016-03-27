from pingdomexport import checks
from pingdomexport import configuration

class TestPicker:
    def test_get_strategy_all(self):
        picker = checks.Picker(
            configuration.Checks('all', []),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == [{'id': 1}, {'id': 2}]

    def test_get_strategy_include(self):
        picker = checks.Picker(
            configuration.Checks('include', [2]),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == [{'id': 2}]

    def test_get_strategy_include_none(self):
        picker = checks.Picker(
            configuration.Checks('include', [3]),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == []

    def test_get_strategy_exclude(self):
        picker = checks.Picker(
            configuration.Checks('exclude', [2]),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == [{'id': 1}]

    def test_get_strategy_exclude_none(self):
        picker = checks.Picker(
            configuration.Checks('exclude', [5]),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == [{'id': 1}, {'id': 2}]

    def test_get_strategy_exclude_all(self):
        picker = checks.Picker(
            configuration.Checks('exclude', [1, 2]),
            {"checks": [{"id":1}, {"id":2}]}
        )
        assert picker.filter() == []
