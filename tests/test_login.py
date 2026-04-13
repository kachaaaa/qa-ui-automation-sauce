from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "wrong_pass")

    error_text = login_page.get_error_text()
    assert "Username and password do not match" in error_text


def test_empty_username(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("", "secret_sauce")

    error_text = login_page.get_error_text()
    assert "Username is required" in error_text

def test_login_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.enter_username("standard_user")
    login_page.enter_password("")  

    login_page.click_login()

    error_text = login_page.get_error_text()

    assert "Password is required" in error_text
    
def test_empty_fields(driver):
    login_page = LoginPage(driver)


    login_page.open()

    
    login_page.enter_username("")
    login_page.enter_password("")

  
    login_page.click_login()

    
    error_text = login_page.get_error_text()

    
    assert "Username is required" in error_text

def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_text()

    assert "Sorry, this user has been locked out." in error_text
    assert "inventory" not in driver.current_url 

def test_successful_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_inventory_page_is_visible(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    title = driver.find_element(By.CLASS_NAME, "title").text

    assert title == "Products"
