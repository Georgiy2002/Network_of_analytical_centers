# загружаем библиотеки
import pandas as pd
from pyvis.network import Network
from legend import legend_html


# загружаем данные из эксель-файла
data=pd.read_excel('ссылка на данные')

# создаем граф
pyvis_graph = Network(height="800px", width="100%", layout=None)

# определяем тип раксладки графа
pyvis_graph.force_atlas_2based()

# в points хранится список уникальных организаций
points = set(list(data['Организация'])+list(data['Партнёр']))

# для каждой организации создаем определенный тип вершины,
# цветом определяя страну организации
for i in points:
    if i in set(data['Организация']): 
        pyvis_graph.add_node(i, shape='triangle')
    else:
        if data.loc[data['Партнёр']==i,'Страна партнёра'].values[0] == 'Китай':
            pyvis_graph.add_node(i, color='#FFFF00')
            
        if data.loc[data['Партнёр']==i,'Страна партнёра'].values[0] == 'США':
            pyvis_graph.add_node(i, color='#00008B')
            
        if data.loc[data['Партнёр']==i,'Страна партнёра'].values[0] == 'РФ':
            pyvis_graph.add_node(i, color='#FF0000')

            
        if data.loc[data['Партнёр']==i,'Страна партнёра'].values[0] == 'ООН':
            pyvis_graph.add_node(i, color='#48D1CC')
            
        if data.loc[data['Партнёр']==i,'Страна партнёра'].values[0] == 'ФРГ':
            pyvis_graph.add_node(i, color='#708090')
            
        else:
            pyvis_graph.add_node(i)

# создаем парные связи между вершинами      
for z in range(data.shape[0]):
    pyvis_graph.add_edge(*data[['Организация', 'Партнёр']].iloc[z].to_list())

# настраиваем масштаб графа  
options = {
    "minHeight": "500px",
    "minWidth": "500px"
    }
pyvis_graph.set_options(options)

# считываем html-код графа в отдельную переменную
html = pyvis_graph.generate_html()  


# присоединяем html-разметку легенды, которую мы импортировали из отдельного файла,
#  к основному html-коду
html += legend_html
    
# записываем созданный html-код в отдельный файл
with open('ссылка на файл', 'w') as f: 
    f.write(html)