import pydantic
from pybwi import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_pydantic_cython_compiled():
    # REFERENCE https://pydantic-docs.helpmanual.io/install/#compiled-with-cython
    assert pydantic.compiled
