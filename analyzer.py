import sys
import xml.etree.ElementTree as ET
from urllib.request import urlopen 
import json

def parse_arguments():
    if len(sys.argv) < 2:
        print("Ошибка: не указана команда")
        sys.exit(1)
    command = sys.argv[1]
    return command

command = parse_arguments()

if command == 'config':
    try:
        tree = ET.parse('config.xml')
        root = tree.getroot()
        
        package_name = root.find('package_name').text
        if package_name is None:
            print("Тег не найден")
        elif not package_name:
            print("Тег пустой")
        elif package_name.isspace():
            print("Тег состоит из пробела(ов)")
        else:
            print(f"package_name: {package_name}")

        repo_url = root.find('repository_url').text
        if  repo_url  is None:
            print("Тег не найден")
        elif not  repo_url :
            print("Тег пустой")
        elif  repo_url .isspace():
            print("Тег состоит из пробела(ов)")
        elif not repo_url.startswith(('http://', 'https://')):
            print("URL: не начинается с http/https")
        elif ' ' in repo_url:
            print("URL с пробелами")
        else:
            print(f"repository-url: {repo_url}")
        

        test_mode = root.find('test_repo_mode').text
        if  test_mode is None:
            print("Тег не найден")
        elif not  test_mode:
            print("Тег пустой")
        elif  test_mode.isspace():
            print("Тег состоит из пробела(ов)")   
        elif test_mode not in ['true', 'false']:
            print("Режим работы с тестовым репозиторием должен быть true либо false")
        else:
            print(f"test-repo-mode: {test_mode}")

        version = root.find('version').text
        if  version is None:
            print("Тег не найден")
        elif not version:
            print("Тег пустой")
        elif  version.isspace():
            print("Тег состоит из пробела(ов)")
        else:
            print(f"version: {version}")

        ascii_tree = root.find('ascii_tree').text
        if  ascii_tree is None:
            print("Тег не найден")
        elif not ascii_tree:
            print("Тег пустой")
        elif  ascii_tree.isspace():
            print("Тег состоит из пробела(ов)")
        else:
             print(f"ascii-tree: {ascii_tree}")
        

        max_depth = root.find('max_depth').text
        if   max_depth is None:
            print("Тег не найден")
        elif not  max_depth:
            print("Тег пустой")
        elif   max_depth.isspace():
            print("Тег состоит из пробела(ов)")
        elif not max_depth.isdigit() or int(max_depth) < 0:
            print("Максимальная глубина анализа зависимостей отрицательна")
        else:
             print(f"max-depth: {max_depth}")
    except Exception as e:
         print(f"Ошибка при работе с config.xml: {e}")

#gdd - get dependency data
elif command == 'gdd':
    tree = ET.parse('config.xml')
    root = tree.getroot()

    package_name = root.find('package_name').text
    repo_url = root.find('repository_url').text
    version = root.find('version').text

    full_url = F"{repo_url}/{package_name}/{version}"
    response = urlopen(full_url)

    res1 = response.read() #получаем в байтах
    res2 = res1.decode('utf-8')

    # Берем только первую строку (она содержит все ключи верхнего уровня)
    first_line = res2.split('\n')[0]
    
    # Убираем фигурные скобки
    clean_content = first_line.strip().strip('{}')
    
    # Счетчик для отслеживания вложенности
    brace_count = 0
    current_key = "" #текущий найденный ключ
    keys = [] #список всех найденных ключей
    
    i = 0
    while i < len(clean_content):
        if clean_content[i] == '"' and brace_count == 0:
            # Начало ключа
            start = i + 1
            end = clean_content.find('"', start) #5-первый
            if end != -1:
                current_key = clean_content[start:end] #name
                i = end #=5
        elif clean_content[i] == ':': 
            if current_key and brace_count == 0: #если верхний уровень и слово(name)
                keys.append(current_key) # keys = ["name"]
                current_key = "" #очищаем
        elif clean_content[i] == '{':
            brace_count += 1
        elif clean_content[i] == '}':
            brace_count -= 1
        elif clean_content[i] == '[':
            brace_count += 1
        elif clean_content[i] == ']':
            brace_count -= 1
            
        i += 1

    # Выводим на экран
    has_dependencies = False
    for key in keys:
        if key != "name":
            print(f"{package_name} -> {key}")
            has_dependencies = True
    
    if not has_dependencies:
        print(f"Пакет {package_name} не имеет зависимостей")
else:
    print(f"неизвестная команда: {command}")
    print("Доступные команды: config")


