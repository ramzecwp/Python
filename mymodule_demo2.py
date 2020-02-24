from mymodule import sayhi, __version__

sayhi()
print('Версия', __version__)
# файл такой же, как и mymodule
# можно было написать from mymodule import * -- тогда все публичные имена (например sayhi) импортируются, но не __version__, тк она начинается с двойного подчеркивания

# import sys # получим список атрибутов модуля sys
# dir(sys) -- все ввести в компиляторе

# Пакеты - способ иерархии модулей (__int__.py) 78 стр
