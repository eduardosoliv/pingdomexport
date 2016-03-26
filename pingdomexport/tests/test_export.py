import pytest
from pingdomexport import export

class TestExport:
    def test_config_not_found(self):
        with pytest.raises(SystemExit):
            export.Export(config_path = "absent")
