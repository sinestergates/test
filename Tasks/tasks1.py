list = []
list_results = []
arr = []
technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
           ('Смартфон', 500, 'Анна', '89202202325'),
           ('Проектор ', 300, 'Андрей', '89505205656'),
           ('Принтер', 750, 'Игорь', '89303303236'),
           ('Планшет', 2300, 'Игорь', '89303303236'),
           ('Смартфон', 1000, 'Андрей', '89505205656'),
           ('Ноутбук', 4800, 'Татьяна', '89002001020'),
           ('Наушники', 780, 'Марина', '89562002350'),
           ('Сканер', 550, 'Сергей', '89808564559'),
           ('Планшет', 1200, 'Анна', '89202202325'),
           ('Ноутбук', 1100, 'Игорь', '89303303236'),
           ('Смартфон', 3500, 'Татьяна', '89002001020')]


def optimization()1:
    # получаем все индексы совпадений
    for i in range(len(technic)):

        optim = technic[i][2]
        a = [i for i, x in enumerate(technic) if optim in x]
        list.append(a)
        for j in list:
            if j not in arr:
                arr.append(j)


def results():
    # формируем массив с верным расположением элементов
    for i in range(len(arr)):

        a = (f'{technic[arr[i][0]][2]} {technic[arr[i][0]][3]}:')

        list_results.append([])
        list_results[i].append(a)
        for j in arr[i]:
            c = (f'{technic[j][0]}-{technic[j][1]};')
            list_results[i].append(c)

    # выводим на печать верные данные
    for i in range(len(list_results)):
        iter = list_results[i]
        print(" ".join(iter))


def main():
    optimization()
    results()


if __name__ == '__main__':
    try:
        main()
    except:
        pass

