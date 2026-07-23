"""Teste de fumaça do módulo principal (sem executar o crew)."""

import importlib


def test_main_module_imports_and_exposes_main():
    main_module = importlib.import_module("main")
    assert callable(main_module.main)
