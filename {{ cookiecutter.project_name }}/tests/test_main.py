from {{ cookiecutter.project_name }}.main import foo


def test_foo():
    assert foo()
