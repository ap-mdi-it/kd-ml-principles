"""Test ML Principles."""

import ml_principles


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(ml_principles.__name__, str)
