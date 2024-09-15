# Scrapy parser PEP

PEP Parser — это проект, предназначенный для извлечения и анализа информации о PEP (Python Enhancement Proposals) с официального сайта (<https://peps.python.org/>). Проект использует Scrapy для парсинга данных и сохранения их в CSV файлы.

## Установка

1.**Клонируйте репозиторий:**

```bash
git@github.com:Alexander-Klp/scrapy_parser_pep.git
```

2.**Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate  # Для Unix систем
venv\Scripts\activate  # Для Windows
```

3.**Установите необходимые зависимости:**

```bash
pip install -r requirements.txt
```

## Структура проекта

```bash
scrapy_parser_pep
 ├── pep_parse/
     ├── spiders/
         ├── __init__.py
         └── pep.py
     ├── __init__.py
     ├── items.py
     ├── middlewares.py
     ├── pipelines.py
     └── settings.py
 ├── results/ 
 │ └── (содержит CSV файлы с результатами парсинга)
 ├── tests/
   └── <содержимое tests>
 ├── .flake8
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── scrapy.cfg
```

## Использование

```bash
scrapy crawl pep
```

Эта команда запустит парсер и сохранит собранные данные в файлы CSV в директорию results/

