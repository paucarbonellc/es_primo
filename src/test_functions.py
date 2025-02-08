import pytest
import functions

def test_primo_1():
    assert functions.es_primo(1) == False

def test_es_primo_numero_primo():
    assert functions.es_primo(2) == True

def test_es_primo_negativo():
    assert functions.es_primo(-10) == False

def test_es_primo_numero_primo_mayor_2():
    assert functions.es_primo(29) == True

def test_es_primo_numero_compuesto():
    assert functions.es_primo(30) == False
