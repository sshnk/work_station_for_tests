from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # url должен соответствовать ожидаемому
        assert "login" in self.browser.current_url,   "word 'Login' not in link  or is not presented"

    def should_be_login_form(self):
        # форма для логина должна присутствовать
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # форма регистарации должна присутствовать
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        pass1.send_keys(password)
        pass2.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        link.click()
