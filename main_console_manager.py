import sys,os.path
from Functions_manager.module_for_manager import create_file, create_folder, get_list, del_file, copy_file, save_info, datetime, change_dir, direct_
from Pract_6 import game
command=''
while command!='stop':


    current_time = str(datetime.datetime.now())
    try:
        with open('log.txt', 'r', encoding='UTF-8') as f:
            last_opening = f.readlines()[-1]
        if current_time[0:9]==last_opening[0:9]:
            pass
        else:
            print('Привет я консольный менеджер, введи help чтобы посмотреть какие команды тебе доступны')
            save_info()
    except FileNotFoundError:
        save_info()
        print('Привет я консольный менеджер, введи help чтобы посмотреть какие команды тебе доступны')

    command = input()
    first_ = command.find(' ')
    if first_==-1:
        first_=len(command)
        save_info(command)
            #print(type(sys.argv[1]))


    if command[:first_] == 'list':
        save_info(command[:first_])
        get_list()

    elif command[:first_] == 'create_file': # checked
        try:
            second_ = command.find(' ', first_ + 1)
            if second_!=-1:
                name = command[first_+1:second_]
            else:
                name = command[first_ + 1:]
        except IndexError:
            print ('Отсутствует название файла, введи название')
        else:
            if second_!=-1:
                text = command[second_+1:]
            else:
                text=''
        save_info(command[:first_])
        create_file(name, text)  ## #


    elif command[:first_] == 'create_folder':#checked
            try:

                    name = command[first_+1:]
                    save_info(command[:first_])
                    create_folder(name)

            except IndexError:
                    create_folder()
                    save_info(command)

    elif command[:first_] == 'delete': #checked
        try:

                name = command[first_+1:]
                save_info(command[:first_])
                del_file(name)

        except IndexError:
            print ('Укажите название удаляемого файла или папки')
    elif command[:first_] == 'copy': #checked


            second_=command.find(' ',first_+1)
            if second_!=-1:
                name = command[first_+1:second_]
                new_name = command[second_+1:]
                save_info(command[:first_])
                copy_file(name, new_name)
            else:
                name = command[first_ + 1:]
                title, ext =name.split('.')
                new_name=title+'_1.'+ext
                save_info(command[:first_])
                copy_file(name, new_name)
    elif command[:first_] == 'help':
            print ("list - список файлов и папок")
            print('create_file - cоздание файла ')
            print('create_folder - cоздание папки ')
            print('delete - удаление файла или папки ')
            print('copy - копирование файла или папки ')
            print('change_dir - сменить рабочую директорию директорию ')
            print ('game - запустить игру')
            save_info(command)
    elif command[:first_]=='change_dir':
            #print(os.getcwd())
        change_dir()
        save_info(command[:first_])
            #print(os.getcwd())
                #os.system("/bin/bash")

    elif command[:first_]=='game':
        game()
        save_info(command[:first_])

    save_info('Конец')


    #except Exception as e:
        #if isinstance(e,IndexError) and isinstance(e,IndexError):
            #print ('Привет я консольный менеджер, введи help чтобы посмотреть какие команды тебе доступны')
            #save_info()
        #elif isinstance(e, FileNotFoundError):
                #save_info()