import pytest
from pingdomexport import export

class TestExport:
    def test_export_path_unrecognized(self):
        with pytest.raises(ValueError):
            export.Export("unrecognized")            

    def test_config_not_found(self):
        with pytest.raises(FileNotFoundError):
            export.Export(config_path = "absent")
