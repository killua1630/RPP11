
"""env_check.py — „Кой Python работи в момента?“

Изпълнете програмата два пъти: веднъж с глобалния Python и веднъж
от активирана виртуална среда. Сравнете реда „Текущ префикс“.
"""

import os
import platform
import sys
import site
from importlib.metadata import distributions


def in_virtualenv() -> bool:
    """Връща True, ако програмата се изпълнява във виртуална среда."""
    return sys.prefix != sys.base_prefix


def report() -> None:
    print("=" * 52)
    print("ДОКЛАД ЗА СРЕДАТА")
    print("=" * 52)

    print(f"Версия на Python : {platform.python_version()}")
    print(f"Изпълним файл    : {sys.executable}")
    print(f"Базов префикс    : {sys.base_prefix}")
    print(f"Текущ префикс    : {sys.prefix}")
    print(f"Работна папка    : {os.getcwd()}")

    print("Папки с инсталирани пакети:")
    for path in site.getsitepackages():
        print(f"  {path}")

    broi_paketi = len(list(distributions()))
    print(f"Брой инсталирани пакети: {broi_paketi}")

    print("=" * 52)

    if in_virtualenv():
        print("СТАТУС: РАБОТИМ ВЪВ ВИРТУАЛНА СРЕДА.")
    else:
        print("ПРЕДУПРЕЖДЕНИЕ: РАБОТИМ С ГЛОБАЛЕН PYTHON!")
        print("ВНИМАВАЙ КАКВИ ПАКЕТИ ИНСТАЛИРАШ!")

    print("=" * 52)


if __name__ == "__main__":
    report()

