# Algoritms-and-Big-Data

Проект реализован в рамках учебного курса Algoritms and Big data.

Здесь реализованы:
- Data set cleaning
- Feature engeneering and feature selection
- Data analysis and dimension reduction
- Clustering algorithms
- Regression algorithms

Более подробное описание ниже

Файлы в репозитории разделены по логике выполнения работы над датасетом.

## Папка 1
Код для создания выборки в 20 000 строк из начального датасета - дз 1.

## Папка 2
Код для подгрузки дескрипторов из библиотек (descriptors.ipynb) и проведения feature selection (feature_selection.ipynb). 
Этой папке соответствуют:
- Задание 2: дескрипторы из библиотек RDkit и Mordred.
- Выбор фичей с помощью следующих методов: 
  - Drop incomplete features
  - Drop features with (near-)zero variance
  - Pearson’s r
- Частично задание 3: перед feature selection проведена начальная чистка:
  - Проверка на дубликаты
  - Проверка на некорректные данные
  - Проверка на очевидно бесполезные характеристики
  - Проверка на отсутствующие значения.

## Папка 3
Код для снижения размерности и некоторого анализа данных, что соответствует заданию 4. 
Так как снижение размерности с помощью использованного (PCA и kernel-PCA) метода предполагает нормализацию, именно здесь она проведена, что соответствует оставшейся части задания 3.

## Папка 4
Код для кластеризации - дз 5.

## Папка 5
Код для регрессии - дз 6.

Промежуточные датасеты слишком тяжелые для загрузки в репозиторий и доступны по ссылке:
[Data](https://drive.google.com/drive/folders/1fjpVS04FBtO_KILVdLUMh7wdKe6K2rIK?usp=sharing)

## Примечания
Целевой характеристикой обозначена 'gap'. Она является разностью характеристик LUMO и HOMO. Так как целевая характеристика напрямую вычисляется из них, логично убрать хотя бы один из связанных дескрипторов.

Однако мне известно, что значения HOMO, LUMO и gap получают в результате квантово-химических расчетов. Можно предположить, что мы хотим предсказывать gap, так как расчеты слишком затратны.

Исходя из этого предположения из датасета были удалены HOMO и LUMO, так как для получения их значений требуются расчеты, которых мы хотим избежать.
