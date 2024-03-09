from date_create import*

def create_contact():# Вызываем функции и получаем от пользователя всю требуемую информацию
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n' #Вид сформированной строки контакта
                                                            # в конце добавляем \n\n, чтобы вывод след контакта был через строку

def add_contact(): # Создание контакта
    '''Вызываем функцию create_contact(), и сохраняем ее в новую переменную contact_str
    Далее открываем файл на дозапись и обращаемся к файловому дискриптору.
    След. строка непосредственно дозаписывает информацию в файл
    '''
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str)


def print_contacts(): # Выводим контакт
    '''Открываем файл на считывание, считываем длинный список из строк.
    В переменную contacts_list записывает список контактов, переделанный из строки контактов
    '''
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    # print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):#нумерация контактов будет начинаться с 1
        print(n, contact) # Выводится номер контакта и сам контакт


def search_contact(): #Поиск контакта по параметрам
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчеству\n'
            '4. По телефону\n'
            '5. По адресу(городу)'
            )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод!')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1 #Получаем индекс каждого контакта

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read() #Считываем данные для поиска
    # print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n') #Преобразуем строку в список
    #print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()# сплитуем по каждому элементу, получаем каждую позицию в отдельной "подстроке"
        if search in lst_contact[i_var]: #проверяем наличие введенных данных в имеющемся списке
            print(str_contact)# если ДА, то выводим найденный контакт, один или несколько

def copy_contact(): # 4. Копирование выбранного контакта в др файл по его номеру
    
    print('Список доступных контактов для копирования: ')
    print()
    
    # Считываем данные с файла
    with open("phonebook.txt", 'r', encoding='utf-8') as file: 
        date_contacts_str = file.read() # Считываем все контакты ввиде одной строки
    #каждый контакт делаем отдельным элементом списка:
    date_contacts_list = date_contacts_str.rstrip().split('\n\n') 
    
    i_number = [] # Запишем номера контактов в отдельный список

    for number, contact in enumerate(date_contacts_list, 1):#нумерация контактов будет начинаться с 1
        i_number.append(number)
        print(number, contact) # Выводится номер контакта и сам контакт
    # print(i_number) # Возможные варианты поиска

    print()
    number_contact = int(input('Введите номер контакта: '))
    print()

    for number, contact in enumerate(date_contacts_list, 1):#нумерация контактов будет начинаться с 1
        if number == number_contact:
            # print(number_contact, contact)
            print(contact)
                # Записываем полученный контакт в новый файл:
            with open("phonebook_copy.txt", 'a', encoding='utf-8') as file:
                file.write(f'{contact} \n\n') #записываем, либо дозаписываем данные котакта в файл
    print()
    print('Копирование произведено. Проверьте файл phonebook_copy.txt на изменения.')