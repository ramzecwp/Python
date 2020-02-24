import os
import time # мы использовали модули os и time (импортировали их)
source = ['"E:\python"'] # можно еще через запятую дописать source - это список
target_dir = 'E:\Backup' # target_dir -- переменная и каталог назначекния
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip' # стр 93 имя нашего архива (target) будет все, что в '' ('%Y%m%d%H%M%S' -- название архов это сегоднейшая дата )
 #+ расширение .zip -- хранится все в каталолге target_dir os.sep -- это разделитель пути (для винды \ для линукса /) -- нужна для работы на всех операционных системах strftime* -- справочник python
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) # zip_command содержит команду которую мы хотим выполнить -- команда zip имеет параметры -- -q значит тихо -r значит рекурсивно
# -- включает все каталоги и файлы, далее идет имя файла (target) за которым следует источник файлов (source) -- метод join превращает список в строку
# имя конечного зип- файла мы создаем при помощи оператора, который соединяет строки
if os.system(zip_command) == 0: # мы выполняем команду с помощью функции os.system -- она запускает прогу из системы
    print('Резевная копия создана в ', target)
else:
    print('Создание резервной копии не удалось')
