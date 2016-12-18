import re
import json


class Syntax:
    pass


class DefSyntax(Syntax):
    name = 'def'
    matcher = re.compile("定義(.*)は(.*)です")

    @classmethod
    def eval(cls, input, env):
        match = cls.matcher.search(input)
        if match:
            var = match.group(1)
            value = match.group(2)
            env.set(var, value)
            return '"{0}"を"{1}"で定義しました'.format(var, value)
        else:
            return


class PlusSyntax(Syntax):
    name = '+'
    matcher = re.compile("([0-9]*).*\+([0-9]*)")

    @classmethod
    def eval(cls, input, env):
        match = cls.matcher.search(input)
        if match:
            print(match.groups())
            front = match.group(1)
            back = match.group(2)
            result = int(front) + int(back)
            return '"{0}"です'.format(result)
        else:
            return


class Function:
    def __init__(self, args, expression, outer_env):
        self._env = Env(outer_env)
        self._args = args
        self._expression = expression


class DefnSyntax(Syntax):
    name = 'defn'
    matcher = re.compile('関数定義(.*)の引数は(.*)で(.*)を返す')

    @classmethod
    def eval(cls, input, env):
        match = cls.matcher.search(input)
        if match:
            var = match.group(1)
            args = match.group(2)
            expression = match.group(3)
            function = Function(args.split("と"), expression, env)
            env.set(var, function)
            return '"{1}"を引数に"{2}"を返す関数を定義しました'.format(var, args, expression)
        else:
            return


class CallSyntax(Syntax):
    name = 'call'
    matcher = re.compile('関数(.*)を(.*)で呼び出す')

    @classmethod
    def eval(cls, input, env):
        match = cls.matcher.search(input)
        if match:
            var = match.group(1)
            args = match.group(2)
            return '結果は"{0}"です'.format(var)
        else:
            return


class EvalSyntax(Syntax):
    name = 'eval'
    matcher = re.compile('(.*)を評価')

    @classmethod
    def eval(cls, input, env):
        match = cls.matcher.search(input)
        if match:
            var = match.group(1)
            print(var)
            found_env = env.find(var)
            if found_env:
                return '"{0}"は"{1}"です'.format(var, found_env.get(var))
            else:
                return "{0}は定義されていません".format(var)
        else:
            return


class Env(dict):
    def __init__(self, outer_env=None):
        self._outer_env = outer_env

    def serialize(self):
        return json.dump(self)

    @classmethod
    def deserialize(self, str):
        return json.load(str)

    def find(self, var):
        return self if var in self else (self._outer_env.find(var) if self._outer_env else None)

    def set(self, key, value):
        self[key] = value


def evaluate(input, env):
    syntax_list = [DefSyntax, DefnSyntax, CallSyntax, EvalSyntax, PlusSyntax]
    for syntax in syntax_list:
        result = syntax.eval(input, env)
        if result:
            return (result, env)
    return ("結果が返りませんでした", env)
