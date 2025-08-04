from db.mysql_repository import *

repo = MysqlRepository();

def test_count_ingredients():
    result = repo.load_ingredients()
    assert result == 14
