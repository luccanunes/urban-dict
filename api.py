def get_term(term: list):
    import requests
    from bs4 import BeautifulSoup

    URL = "https://www.urbandictionary.com/define.php?term="

    for word in term:
        URL += word 
        if word != term[-1]:
            URL += '+'

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        meaning = soup.select('.meaning')[0].text
    except:
        return { "Error": "Failed to find term meaning" }
    else:
        return meaning