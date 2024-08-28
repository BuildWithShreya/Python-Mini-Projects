import webbrowser as wb


def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    urls ={
        "http://google.com",
        "http://youtube.com",
        "http://gmail.com"
    }

    for url in urls:
        print(f'Opening the URL: {url}')
        wb.get(chrome_path).open(url)


webauto()

