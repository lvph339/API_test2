from utils.JSONSchemaUtils import JSONSchemaUtils

def test_Schem():
    #期望返回数据类型
    json_y = {"code": 200, "message": "ok", "list": [{"name": "tom", "age": 18, "ishappy": True}, {"name": "jey", "age":28, "ishappy": False}], "createTime": "2024-02-23 11:08:44"}
    #接口实际返回值
    json_r = {"code": 200, "message": "ok", "list": [{"name": "tom", "age": 18, "ishappy": True}, {"name": "jey", "age":28, "ishappy": False}], "createTime": "2024-02-23 11:08:44"}
    result = JSONSchemaUtils.validate_schema(json_r, json_y)
    assert result is True
