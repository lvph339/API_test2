from utils.jsonschema_utils import JSONSchemaUtils

def test_Schem():
    json_y = {"code": 200, "message": "ok", "list": [{"name": "tom", "age": 18, "ishappy": True},{"name": "jey", "age": 28, "ishappy": False}], "createTime": "2024-02-23 11:08:44"}
    json_r = {"code": 200, "message": "ok", "list": [{"name": "tom", "age": 18, "ishappy": True},{"name": "jey", "age": 28, "ishappy": False}], "createTime": "2024-02-23 11:08:44"}
    result = JSONSchemaUtils.validate_schema(json_r, json_y)
    assert result is True
