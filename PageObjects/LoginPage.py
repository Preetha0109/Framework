from selenium.webdriver.common.by import By


class Loginpage:
    get_started_css = 'button[class="navbar-cta-btn"]'
    text_box_email_css = "input[type='email']"
    text_box_password_css = "input[type='password']"
    login_button_css = 'button[type="submit"]'
    logout_button_xpath = "//span[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickStarted(self):
        self.driver.find_element(By.CSS_SELECTOR, self.get_started_css).click()

    def setusername(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.text_box_email_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.text_box_email_css).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.text_box_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.text_box_password_css).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()


