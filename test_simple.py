import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args()

if args.command == 'config':
    tree = ET.parse('config.xml')
    root = tree.getroot()
    
    package_name = root.find('package_name').text
    repo_url = root.find('repository_url').text
    test_mode = root.find('test_repo_mode').text
    version = root.find('version').text
    ascii_tree = root.find('ascii_tree').text
    max_depth = root.find('max_depth').text
    
    print(f"package_name: {package_name}")
    print(f"repository-url: {repo_url}")
    print(f"test-repo-mode: {test_mode}")
    print(f"version: {version}")
    print(f"ascii-tree: {ascii_tree}")
    print(f"max-depth: {max_depth}")
