class Solution(object):
    def deserialize(self, s):
        from ast import literal_eval
        def build(x):
            obj = NestedInteger()
            if isinstance(x, int):
                obj.setInteger(x)
            else:
                for i in x:
                    obj.add(build(i))
            return obj
        return build(literal_eval(s))