import os
import re
from bs4 import BeautifulSoup

def reformat_link(link):
    # Regular expression for <a> tags
    pattern_a = re.compile(r'([^/]+)%20(.+)%20([0-9a-f]{32})\.html')
    match_a = pattern_a.match(link)
    if match_a:
        print("match group 1: ", match_a.group(1))
        print("match group 2: ", match_a.group(2))
        if len(match_a.group(2).split('/')) > 1:
            output = f"{match_a.group(1)}/{match_a.group(2).split('/')[1]}.html"
        else:
            output = f"{match_a.group(1)}/{match_a.group(2)}.html"
        print("output: \n", output)
        return output
        # return f"{match_a.group(2)}.html"

    # Regular expression for <img> tags
    pattern_img = re.compile(r'(.+)%20([0-9a-f]{32})/(.+)')
    match_img = pattern_img.match(link)
    if match_img:
        return f"{match_img.group(1)}/{match_img.group(3)}"

    return link

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Process <a> tags
    for a in soup.find_all('a', href=True):
        a['href'] = reformat_link(a['href'])

    # Process <img> tags
    for img in soup.find_all('img', src=True):
        img['src'] = reformat_link(img['src'])

    # Write the modified HTML back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def process_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file))

# Replace 'your_directory_path' with the path to the directory you want to process
process_directory('output')
