import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

# Створюємо парсер командного рядка:
parser = argparse.ArgumentParser(description="Sorting folder")
# Аргумент для вказання вихідної папки:
parser.add_argument("--source", "-s", help="Source folder", required=True)
# Аргумент для вказання папки виводу (за замовчуванням - 'dist'):
parser.add_argument("--output", "-o", help="Output folder", default="dist")

# Отримуємо аргументи командного рядка та зберігаємо їх у словник args:
args = vars(parser.parse_args())

# Визначаємо шляхи до вихідної та вихідної папок на основі аргументів командного рядка:
source = Path(args.get("source"))
output = Path(args.get("output"))

# Створюємо порожній список для збереження списку папок, які потребують обробки:
folders = []


# Функція для рекурсивного обходу та додавання папок у список folders:
def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


# Функція для копіювання файлів:
def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]  # Отримуємо розширення файлу
            ext_folder = output / ext  # Формуємо шлях до папки з відповідним розширенням
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)  # Створюємо папку з розширенням, якщо її немає
                copyfile(el, ext_folder / el.name)  # Копіюємо файл у відповідну папку
            except OSError as err:
                logging.error(err)  # Логуємо помилку

if __name__ == '__main__':
    # Встановлюємо рівень логування та формат повідомлень:
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(source)  # Додаємо вихідну папку до списку folders
    grabs_folder(source)  # Запускаємо обробку всіх папок

    threads = []

    # Створюємо потоки для обробки кожної папки:
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    # Очікуємо завершення роботи всіх потоків:
    [th.join() for th in threads]

    print(f"Можна видаляти {source}")  # Виводимо повідомлення про готовність видалення вихідної папки
