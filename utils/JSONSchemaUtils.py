from genson import SchemaBuilder
import json
from jsonschema.validators import validate


class JSONSchemaUtils:

    #生成对应的 JSONSchema 数据结构
    @classmethod
    def generate_jsonschema(cls,obj):
        # 实例化 SchemaBuilder 类
        builder = SchemaBuilder()
        # 调用 add_object 方法，将要转换成jsonschema的数据传入进去，python对象obj，格式为字典
        builder.add_object(obj)
        # 转换成 schema 数据
        return builder.to_schema()

    #把对应的JSONSchema存储成文件
    @classmethod
    def generate_jsonschema_by_file(cls, obj, file_path):
        json_schema_data = cls.generate_jsonschema(obj)
        with open(file_path, "w") as f:
            # json_schema_data 需要传的对象，f 文件形式
            json.dump(json_schema_data, f)

    #读取JSONSchema文件并对比json结构
    @classmethod
    def validate_schema_by_file(cls, josn_r, json_y):
        cls.generate_jsonschema_by_file(json_y,"validate.json")
        with open("validate.json") as f:
            json_schema_data = json.load(f)
        # 不直接抛出错误，直接返回是否成功的标志 T 或 F
        try:
            validate(josn_r, schema=json_schema_data)
            return True
        except Exception as e:
            # 打印异常，也可以使用日志形式
            # log()
            print(f"结构体验证失败，失败原因是{e}")
            return False


  #结果获取生成的JSONSchema结构，不存储文件，直接对比
    @classmethod
    def validate_schema(cls, josn_r, json_y):
        json_schema_data = cls.generate_jsonschema(json_y)
        # 不直接抛出错误，直接返回是否成功的标志 T 或 F
        try:
            validate(josn_r, schema=json_schema_data)
            return True
        except Exception as e:
            # 打印异常，也可以使用日志形式
            # log()
            print(f"结构体验证失败，失败原因是{e}")
            return False
