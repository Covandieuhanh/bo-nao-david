"""Kiểm tập con JSON Schema đang dùng trong khuon/, không phụ thuộc gói ngoài."""
def kiem(value, schema, path="$ "):
    kind = schema.get("type")
    tests = {"object":lambda v:isinstance(v,dict), "array":lambda v:isinstance(v,list),
             "string":lambda v:isinstance(v,str), "boolean":lambda v:type(v) is bool,
             "number":lambda v:type(v) in (int,float), "integer":lambda v:type(v) is int,
             "null":lambda v:v is None}
    if kind and not any(tests[k](value) for k in (kind if isinstance(kind,list) else [kind])):
        raise ValueError(f"{path}: phải là {kind}")
    if "enum" in schema and value not in schema["enum"]: raise ValueError(f"{path}: ngoài enum")
    if isinstance(value,dict):
        for name in schema.get("required",[]):
            if name not in value: raise ValueError(f"{path}: thiếu {name}")
        props=schema.get("properties",{})
        for name, v in value.items():
            if name in props: kiem(v,props[name],path+"."+name)
            elif schema.get("additionalProperties") is False: raise ValueError(f"{path}: khoá thừa {name}")
            elif isinstance(schema.get("additionalProperties"),dict):kiem(v,schema["additionalProperties"],path+"."+name)
    if isinstance(value,list):
        if len(value)<schema.get("minItems",0) or len(value)>schema.get("maxItems",float("inf")): raise ValueError(f"{path}: sai số phần tử")
        for i,v in enumerate(value):kiem(v,schema.get("items",{}),f"{path}[{i}]")
