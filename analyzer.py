import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args()

if args.command == 'config':
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
