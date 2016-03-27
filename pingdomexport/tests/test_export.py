import pytest
from pingdomexport import export

class TestExport:
    def test_export_path_unrecognized(self):
        with pytest.raises(ValueError):
            export.Export("unrecognized")
