import urllib.request
from bs4 import BeautifulSoup

base_url = 'http://e-liquid-recipes.com/?q=&exclsingle=0&flavorIds=&sort=recipe.created&direction=desc&page='
recipe_urls = []

def get_html(url):
    response = urllib.request.urlopen(url)
    return response

def get_last_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    paggination_class = soup.find('div', class_='pagination')
    last_page = paggination_class.findAll('li')[-2].text
    return last_page

last_page = int(get_last_page(get_html('http://e-liquid-recipes.com')))


def add_links_to_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_="recipelist")

    for a in table.find_all('a', href=True)[4:]:
        if r'http://e-liquid-recipes.com/recipe/' in a['href']:
            recipe_urls.append(a['href'])

def get_links():
    i = 1
    while(i <= last_page):
        add_links_to_list(get_html(base_url + str(i)))
        i +=1

def main():
    get_links()
    print (len(recipe_urls))


if __name__ == '__main__':
    main()

