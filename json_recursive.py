#!/usr/bin/python3
#递归json，输出所有的key-value，每层key用_连接
def json_recursive(injson):
    json_rst={}
    for key in injson.keys():
        if isinstance(injson[key], dict):
            #json_rst.update(json_recursive(injson[key]))
            tmpjson=json_recursive(injson[key])
            for subkey in tmpjson.keys():
                json_rst[key+"_"+subkey] = tmpjson[subkey]
        else:
            json_rst[key]=injson[key]
    return json_rst

#Test
if __name__ == '__main__':
    a={"a0": 1, "a1": {"b0":2, "b1":3}, "a2":{"b0":{"c0":4, "c1":5}}
    print(json_recursive(a))
