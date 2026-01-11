import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage

import os




class Test_001_Login:

    @pytest.mark.sanity
    def test_home_page(self, setup, pytestconfig):
        self.driver = setup

        baseUrl = pytestconfig.getini("baseUrl")


        self.driver.get(baseUrl)
        exp_title = 'Vaastu For All'
        act_title = self.driver.title

        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            time.sleep(10)

            path = os.path.join("Screenshots", "test_hompage_title_failure.png")
            print(path)



            self.driver.save_screenshot(path)
            self.driver.close()
            assert False, "Wrong title displayed"


    @pytest.mark.peetha
    def test_login_check(self, setup, pytestconfig):
        self.driver = setup


        baseUrl = pytestconfig.getini("baseUrl")
        username = pytestconfig.getini("username")
        password = pytestconfig.getini("password")

        self.driver.get(baseUrl)

        self.lp = Loginpage(self.driver)
        self.lp.clickStarted()
        self.lp.setusername(username)
        self.lp.setpassword(password)
        self.lp.clicklogin()

        act_title = self.driver.title
        exp_title = 'Vaastu For All'

        self.driver.close()

        assert act_title == exp_title, 'Failed wrong title wrong page loaded'

