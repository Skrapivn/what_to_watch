### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Skrapivn/what_to_watch.git
```

```
cd what_to_watch
```

Cоздать и активировать виртуальное окружение:

```python
python -m venv venv
```

```python
source venv/bin/activate
```

Активировать виртуальное окружение, обновить версию ```pip``` и установить зависимости из ```requirements.txt```:

```python
source venv/bin/activate
```

```python
python -m pip install -–upgrade pip.
```

```python
pip install -r requirements.txt
```

Функция загрузки мнений в базу данных из **opinions.csv**:

```
flask load_opinions  
```

Запустить проект:

```
flask run
```

[Sergey K.](https://github.com/skrapivn/)
