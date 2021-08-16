

def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name="Selenium"
    title="Selenium is for web automation"
    assert name in title

def test_3():
    name="jenkins"
    title="Jenkins is CI server"
    assert name in title, "Title doesn't match"

#pytest
#py.test
#pytest -rA :for summary of all reports

#pytest -h
#pytest -rA :full summary
#pytest -k "String"
#pytest -v :verbose