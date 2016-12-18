from lang import Env, evaluate


def test_lang():
    env = Env()
    sample1 = '定義これは1です'
    sample2 = '関数定義ほげの引数はaとbでa+bを返す'
    sample3 = '関数ほげを1と2で呼び出す'
    sample4 = 'これを評価'
    sample5 = '10+20'

    assert evaluate(sample1, env)[0] == '"これ"を"1"で定義しました'
    assert evaluate(sample2, env)[0] == '"aとb"を引数に"a+b"を返す関数を定義しました'
    assert evaluate(sample3, env)[0] == '結果は"ほげ"です'
    assert evaluate(sample4, env)[0] == '"これ"は"1"です'
    assert evaluate(sample5, env)[0] == '"30"です'
