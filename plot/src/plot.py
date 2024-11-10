import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Создаём бесконечный цикл
while True:
    try:
        # Чтение данных с указанием заголовков
        df = pd.read_csv('./logs/metric_log.csv', header=None, names=['id', 'y_true', 'y_pred', 'absolute_error'])
        
        # гистограмма ошибок
        sns_plot = sns.histplot(df['absolute_error'], kde=True, color="yellow", bins=30)
        
        # сохранение графика в файл
        plt.savefig('./logs/error_distribution.png')
        plt.close()
        print('Файл успешно сохранен')

        time.sleep(40)
    except Exception as e:
        print(f'Не удалось считать таблицу metric_log.csv: {e}')
