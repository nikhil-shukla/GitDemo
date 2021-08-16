import pytest

@pytest.mark.skip
def test_login():
    print("login done")

@pytest.mark.skipif()
def test_addProduct():
    print("add product")

@pytest.mark.smoke
def test_logout():
    print("logout done")