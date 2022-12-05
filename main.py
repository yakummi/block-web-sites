import platform
path_to_hosts = ''

if platform.system() == 'Windows':
    path_to_hosts = r'C:\Windows\System32\drivers\etc\hosts'
elif platform.system() == 'Linux':
    path_to_hosts = r'/etc/hosts'


redirect = '127.0.0.1'
websites = []

def block():
    while True:
        site = input('Введите сайт для блокировки: ')
        if site == 'exit':
            break
        websites.append(site)
        print(f'Ссылка {site} добавлена!')
        print('Если Вы добавили все сайты, для выхода отправьте "exit"')

    with open(path_to_hosts, 'r+') as file:
        content = file.read()
        for site in websites:
            if site in content:
                pass
            else:
                file.write(f'{redirect} {site}\n')

def unblock():
    while True:
        site = input('Введите сайт для разблокировки: ')
        if site == 'exit':
            break
        websites.append(site)
        print(f'Ссылка {site} удалена!')
        print('Если Вы разблокировали все сайты, для выхода отправьте "exit"')

    with open(path_to_hosts, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in websites):
                file.write(line)
        file.truncate()


while True:
    choosing_action = input('1 - Заблокировать сайт\n2 - разблокировать сайт\n')
    if choosing_action == '1' or choosing_action == '2':
        break
    print('Выберите вариант ответа!')

if choosing_action == '1':
    block()
elif choosing_action == '2':
    unblock()
