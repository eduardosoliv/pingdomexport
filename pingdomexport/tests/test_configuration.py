from unittest.mock import patch
import pytest
from pingdomexport import configuration

class TestConfiguration:
    def test_config_not_found(self):
        with patch('os.path.isfile') as isfile:
            with pytest.raises(FileNotFoundError):
                isfile.return_value = False
                configuration.Configuration('config.yml.dist')

    def test_config_default(self):
        with patch('os.path.dirname') as dirname, patch('os.path.isfile') as isfile:
            with pytest.raises(FileNotFoundError) as exc:
                dirname.return_value = "pathtest"
                isfile.return_value = False
                configuration.Configuration()
            assert "pathtest/../config.yml" in str(exc)

class TestPingdomAccess:
    def test_from_dict(self):
        config = configuration.PingdomAccess.from_dict(
            {
                "username": 'u',
                "password": 'p',
                "account_email": 'ae',
                "app_key": "akey"
            }
        )
        assert config.username() == 'u'
        assert config.password() == 'p'
        assert config.account_email() == 'ae'
        assert config.app_key() == 'akey'

    def test_from_dict_missing_key(self):
        with pytest.raises(KeyError):
            configuration.PingdomAccess.from_dict({})

class TestChecks:
    def test_strategy_unrecognized(self):
        with pytest.raises(ValueError):
            configuration.Checks('t', [])
    def test_strategty_all_with_ids(self):
        with pytest.raises(ValueError):
            configuration.Checks('all', [1, 2])
    def test_from_dict_missing_key(self):
        with pytest.raises(KeyError):
            configuration.Checks.from_dict({})
    def test_is_strategy_all(self):
        checks = configuration.Checks('all', [])
        assert checks.is_strategy_all()
        checks = configuration.Checks('include', [])
        assert not checks.is_strategy_all()
    def test_is_strategy_include(self):
        checks = configuration.Checks('include', [123])
        assert checks.is_strategy_include()
        checks = configuration.Checks('all', [])
        assert not checks.is_strategy_include()
    def test_is_strategy_exclude(self):
        checks = configuration.Checks('exclude', [123])
        assert checks.is_strategy_exclude()
        checks = configuration.Checks('all', [])
        assert not checks.is_strategy_exclude()

class TestLoad:
    def test_type_unrecognized(self):
        with pytest.raises(ValueError):
            configuration.Load('t', {})
    def test_output_with_parameters(self):
        with pytest.raises(ValueError):
            configuration.Load('output', {'db_url': 'test'})
    def test_mysql_without_db_url(self):
        with pytest.raises(ValueError):
            configuration.Load('mysql', {})
    def test_postgres_without_db_url(self):
        with pytest.raises(ValueError):
            configuration.Load('postgres', {})
    def test_output(self):
        load = configuration.Load('output', {})
        assert load.type() == 'output'
        assert load.params() == {}
        assert load.is_type_output()
        assert not load.is_type_mysql()
        assert not load.is_type_postgres()
        assert not load.is_type_db();
    def test_mysql(self):
        load = configuration.Load('mysql', {'db_url': 'test'})
        assert load.type() == 'mysql'
        assert load.params() == {'db_url': 'test'}
        assert not load.is_type_output()
        assert load.is_type_mysql()
        assert not load.is_type_postgres()
        assert load.is_type_db();
    def test_postgres(self):
        load = configuration.Load('postgres', {'db_url': 'test'})
        assert load.type() == 'postgres'
        assert load.params() == {'db_url': 'test'}
        assert not load.is_type_output()
        assert not load.is_type_mysql()
        assert load.is_type_postgres()
        assert load.is_type_db();
    def test_output_from_dict(self):
        load = configuration.Load.from_dict({'type': 'output', 'parameters': {}})
        assert load.type() == 'output'
        assert load.params() == {}
    def test_mysql_from_dict(self):
        load = configuration.Load.from_dict({'type': 'mysql', 'parameters': {'db_url': 'test'}})
        assert load.type() == 'mysql'
        assert load.params() == {'db_url': 'test'}
    def test_postgres_from_dict(self):
        load = configuration.Load.from_dict({'type': 'postgres', 'parameters': {'db_url': 'test'}})
        assert load.type() == 'postgres'
        assert load.params() == {'db_url': 'test'}
