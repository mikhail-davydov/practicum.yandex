import pandas as pd


def fill_na_with_median(df: pd.DataFrame):
    """
    Найдет все колонки датасета, содержащие пустые значения (NaN), и заполнит их медианой каждой колонки.

    Parameters:
    -----------
    df: pandas.DataFrame
        Входной датасет.

    Returns:
    --------
    filled_df: pandas.DataFrame
        Датасет с заполненными пустыми значениями.
    """
    # Сначала найдем все колонки, содержащие NaN
    nan_columns = df.columns[df.isnull().any()]

    # Для каждой колонки с пустыми значениями заполним их медианой
    for col in nan_columns:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    return df


def prepare_data(df: pd.DataFrame):
    """
    Подготовит датасет к использованию с обученной моделью

    Parameters:
    -----------
    df: pandas.DataFrame
        Входной датасет.

    Returns:
    --------
    filled_df: pandas.DataFrame
        Подготовленный датасет.
    """
    # Переименуем столбцы
    df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

    # Заполним пропуски
    df = fill_na_with_median(df)

    # Поменяем значения для признака gender
    df.loc[df['gender'] == 'Male', 'gender'] = '1.0'
    df.loc[df['gender'] == 'Female', 'gender'] = '0.0'

    return df