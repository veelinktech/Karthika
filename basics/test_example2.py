from selenium import webdriver


def test_Fb():
    driver = webdriver.Chrome()
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Facebook"
    driver.close()