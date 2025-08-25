from db.mysql_repository import *

repo = MysqlRepository();

def test_count_ingredients():
    result = repo.load_ingredients()
    #assert result == 14

def test_check_mealtype():
    valid_ids = set(mt.value for mt in MealType)
    result = repo.check_mealtype()
    assert all(id_ in valid_ids for id_ in result)
