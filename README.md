# Rodin Helpers
Библиотека с набором функций для наглядного вывода данных в Jupyter Notebook

## Установка 

```shell
pip install -U git+https://github.com/madiedinro/rodin_helpers_py
```

```python
import rodin_helpers as rh
```
В jupyer перед командой добавляется префикс `!`


## Вывод ссылки в заданном формате
```python
rh.show_link('https://digitalgod.be')
```
Результат:
> Click [Authorize](https://digitalgod.be) or open https://digitalgod.be in your browser

## Вывод YouTube видео по id

```python
rh.video('2-gboBo3MtY')
```

## Отображение структурированных данных с указанием типов

```python
data = [
    {
        'date': '2019-01-11',
        'metrics': {
            'visits':1534,
            'impressions':2345
        }
    },
    {
        'date': '2019-01-12',
        'metrics': {
            'visits':1324,
            'impressions':2132
        }
    }
]
rh.walk(data)
```
Результат:
```bash
[list
[dict  0
|      0 > date=2019-01-11
[dict  0 > metrics
|      0 > metrics > visits=1534
|      0 > metrics > impressions=2345
[dict  1
|      1 > date=2019-01-12
[dict  1 > metrics
|      1 > metrics > visits=1324
|      1 > metrics > impressions=2132
```
## Представление построчных данных (к примеру, из бд)
```python
rh.print_rows(data)
```
Результат:

campaign_id|date|utm_term|utm_source|account_id|spent|utm_campaign|clicks|utm_content|impressions|ad_id|reach
---|---|---|---|---|---|---|---|---|---|---|---
1010819423|2019-01-20|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|12|49726084|8
1010819423|2019-01-21|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|15|49726084|13
1010819423|2019-01-22|retarg-mob|vk|1603421955|13.00|dr4|None|kiborg-vid|7|49726084|7
1010819423|2019-01-23|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|9|49726084|8
1010819423|2019-01-24|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-25|retarg-mob|vk|1603421955|4.60|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-26|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-27|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|6|49726084|5
1010819423|2019-01-28|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|3|49726084|3
1010819423|2019-01-29|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-30|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|2|49726084|2

```bash
campaign_id|date|utm_term|utm_source|account_id|spent|utm_campaign|clicks|utm_content|impressions|ad_id|reach
---|---|---|---|---|---|---|---|---|---|---|---
1010819423|2019-01-20|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|12|49726084|8
1010819423|2019-01-21|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|15|49726084|13
1010819423|2019-01-22|retarg-mob|vk|1603421955|13.00|dr4|None|kiborg-vid|7|49726084|7
1010819423|2019-01-23|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|9|49726084|8
1010819423|2019-01-24|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-25|retarg-mob|vk|1603421955|4.60|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-26|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|4|49726084|3
1010819423|2019-01-27|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|6|49726084|5
1010819423|2019-01-28|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|3|49726084|3
1010819423|2019-01-29|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|5|49726084|5
1010819423|2019-01-30|retarg-mob|vk|1603421955|None|dr4|None|kiborg-vid|2|49726084|2
```
