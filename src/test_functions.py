"""Modulo para tests"""
import pytest
"""Modulo para funciones"""
import functions

def test_primo_1():
    """
    Test
    """
    assert functions.es_primo(1) == False
