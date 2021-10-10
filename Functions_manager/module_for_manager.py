import sys
import os
import shutil, datetime, os.path


def create_file(name, text=None):
    f = open(name, 'w', encoding='utf-8')
    if text:
        f.write(text)


def create_folder(name="Новая папка"):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует, пожалуйста придумайте другое имя')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]

    if not result:
        print("Папки отсутствуют")
    print(result)


def del_file(*name):
    try:
        for item_name in name:
            if os.path.isfile(item_name) == True:
                os.remove(item_name)
            else:
                os.rmdir(item_name)
    except FileNotFoundError:
        print ('такого объекта не существует, введите другое имя')

def copy_file(name, new_name):
    try:
        if os.path.isfile(name) == True:
            shutil.copyfile(name, new_name)
        else:
            shutil.copytree(name, new_name)
    except FileExistsError:
        print('Папка с таким именем существует, добавь другое имя')


def save_info(message='Старт'):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(result + '\n')

#написать функцию, которая при аргументе Up поднимает на одну директорию вверх, а при вводе названия папки из текущей директории опускается на диреторию ниже
def direct_(directiva):
    try:
        if directiva != 'up':
           new_path=os.path.join(os.getcwd(), directiva)
           return os.chdir(new_path)




        elif directiva== 'up':
            new_path = os.getcwd()[:os.getcwd().rfind('\\')]

            return os.chdir(new_path)

    except:
        print ('Такого пути не существует, введите up либо имя папки в текущей директории')


def change_dir():
    print('текущая рабочая директория:', os.getcwd() )
    print ('папки в текущей директории:')
    get_list(True)
    directiva = input('Введите up чтобы подняться на один уровень вверх, либо название папки из текущей директории ') # попробовать прикрутить нажатие стрелок, в противном случае либо Up вверх по директории, либо название папки - вниз
    direct_(directiva)

#if __name__ == '__main__':
    #print(os.getcwd())
    #direct_('up')
    #print(os.getcwd())
    #change_dir()
    #    create_file('check', 'some text')
    #create_folder()
    #get_list(False)
    #del_file('Test_case')
    #   copy_file('Новая папка', 'Новая папка2')
    #save_info('abs')
    #create_file('test4.txt', 'ya pytayus)
    #direct_()