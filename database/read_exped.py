import pandas as pd

exped = pd.read_excel(
    r'W:\Theoretical Planning\03 - План отгрузки (Planification)\План отгрузки\EXPED. IDM-Direct.xlsb',
    sheet_name='Текущий',
    header=4
)


def filter_item(df, item: int):
    df_item = df[df['N° ITEM'] == item].reset_index(drop=True)
    df_item = df_item.loc[:, ['Индекс RTB',
                              'Наименование детали',
                              'Кол-во',
                              'Неделя Отгрузки',
                              'Примечания',
                              'Отметка о выполнении',
                              'Потенциальные проблемы',
                              'N° ITEM',
                              'Приоритет'
                              ]].astype({'Индекс RTB': 'int64', 'Кол-во': 'int64', 'N° ITEM': 'int64'})
    inform = df_item.loc[0, ['Индекс RTB',
                             'Наименование детали',
                             'Кол-во',
                             'Приоритет',
                             'Примечания',
                             'Потенциальные проблемы'
                             ]].values
    return inform


def filter_detal(df, detal: str):
    df_t = df['Наименование детали'].str.contains(detal, regex=True)
    df['search'] = df_t
    df_detal = df[df['search'] == True]
    df_detal = df_detal.loc[:, ['Индекс RTB',
                                'Наименование детали',
                                'Кол-во',
                                'Неделя Отгрузки',
                                'Примечания',
                                'Отметка о выполнении',
                                'Потенциальные проблемы',
                                'N° ITEM',
                                'Приоритет'
                                ]].astype({'Индекс RTB': 'int64', 'Кол-во': 'int64', 'N° ITEM': 'int64'})
    inform = df_detal.loc[:, ['Индекс RTB',
                              'Наименование детали',
                              'Кол-во',
                              'Приоритет',
                              'Примечания',
                              'Потенциальные проблемы'
                              ]].values
    return inform


def filter_order(df, order):
    df_t = df['Индекс RTB'].astype(dtype='str').str.contains(order, regex=True)
    df['search'] = df_t
    df_order = df[df['search'] == True]
    df_order = df_order.loc[:, ['Индекс RTB',
                                'Наименование детали',
                                'Кол-во',
                                'Неделя Отгрузки',
                                'Примечания',
                                'Отметка о выполнении',
                                'Потенциальные проблемы',
                                'N° ITEM',
                                'Приоритет'
                                ]].astype({'Индекс RTB': 'int64', 'Кол-во': 'int64', 'N° ITEM': 'int64'})
    inform = df_order.loc[:, ['Индекс RTB',
                              'Наименование детали',
                              'Кол-во',
                              'Приоритет',
                              'Примечания',
                              'Потенциальные проблемы'
                              ]].values
    return inform
