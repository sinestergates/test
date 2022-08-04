#вводим начальный список
list_name=['wad3asw','3s14234212345321312','4d21q42343423423c23rfsdgter']
list_name_no_duplicate=[]
def name_file():

    #избавляемся от дубликатов
    for i in range(len(list_name)):
        read="".join(set(list_name[i]))
        list_name_no_duplicate.append(read)
    lens = max(len(i) for i in list_name_no_duplicate)
    #счетаем строки и делаем файлы

    for i in range(len(list_name_no_duplicate)):
        iter=list_name_no_duplicate[i]
        if len(iter) < lens:
            diff=lens-len(iter)
            s =  iter+'_' * diff

        else:
            s=iter
        with open(f'{s}.txt', "w") as file:
            file.write("Your text goes here")



if __name__ == '__main__':
    try:
        name_file()
    except:
        pass