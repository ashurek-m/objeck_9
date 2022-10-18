import pandas as pd

exped = pd.read_excel(
    r'W:\Theoretical Planning\03 - План отгрузки (Planification)\План отгрузки\EXPED. IDM-Direct.xlsb',
    sheet_name='Текущий',
    header=4
)


def filter(df, item: int):
    df_item = df[df['N° ITEM'] == item].reset_index(drop=True)
    df_item = df_item.loc[:, ['Индекс RTB',
                              'Наименование детали',
                              'Кол-во',
                              'Неделя Отгрузки',
                              'Примечания',
                              'Отметка о выполнении',
                              'Потенциальные проблемы',
                              'N° ITEM'
                              ]].astype({'Индекс RTB': 'int64', 'Кол-во': 'int64', 'N° ITEM': 'int64'})
    return df_item
