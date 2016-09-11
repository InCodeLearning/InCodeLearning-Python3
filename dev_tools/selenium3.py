from selenium import webdriver
from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    '''
        Page Object Model sample code package (page_objects)
        https://page-objects.readthedocs.io/en/latest/tutorial.html
        https://media.readthedocs.org/pdf/page-objects/latest/page-objects.pdf

        <html>
            <head>
                <title>Login Page</title>
            </head>
            <body>
                <form type="POST" action="/login">
                    <input type="text" name="username" id="user-input"></input>
                    <input type="password" name="password"></input>
                    <input type="submit">Submit</input>
                </form>
            </body>
        </html>
    '''
    username = PageElement(id_='user-input')
    password = PageElement(name='password')
    login = PageElement(css='input[type="submit"]')
    form = PageElement(tag_name='form')


driver = webdriver.PhantomJS()
driver.get("http://example.com")
page = LoginPage(driver)
page.username = 'secret'
page.password = 'squirrel'
assert page.username.text == 'secret'
page.login.click()
