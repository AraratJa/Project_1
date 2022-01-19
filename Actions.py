from typing import Text
from locators import Locators,Er_locators
from driver import Base
from time import sleep
import re
from selenium.webdriver.support.color import Color
from selenium.webdriver import ActionChains


class Contact_us:
    def __init__(self,driver):
        self.driver=driver
        self.input=Locators.input__password_field
        self.message=Locators.input__email_field
        self.submit_button=Locators.submit_button
        self.clear_button=Locators.create_acount_button
            
    def create_acount(self,email_adress,password_text):
        create_acount=self.driver.find_element_by_xpath(Locators.create_acount_button).click()
        sleep(3)
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        email_field=self.driver.find_element_by_xpath(Locators.input__email_field)
        email_field.send_keys(email_adress)
        password_field=self.driver.find_element_by_xpath(Locators.input__password_field)
        password_field.send_keys(password_text)
        submit_button_click=self.driver.find_element_by_xpath(Locators.submit_button).click()
        sleep(5)
        self.driver.switch_to.window(original_window)
        check_acount=self.driver.find_element_by_xpath(Locators.created_acount_checker)
        acount_name=check_acount.get_attribute('alt')
        return acount_name

    def create_acount_failed_email(self,email_adress,password_text):
        create_acount=self.driver.find_element_by_xpath(Locators.create_acount_button).click()
        sleep(3)
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        email_field=self.driver.find_element_by_xpath(Locators.input__email_field)
        email_field.send_keys(email_adress)
        password_field=self.driver.find_element_by_xpath(Locators.input__password_field)
        password_field.send_keys(password_text)
        submit_button_click=self.driver.find_element_by_xpath(Locators.submit_button).click()
        error_message=self.driver.find_element_by_xpath(Er_locators.wrong_email_format).text
        return error_message
    
    def create_acount_failed_password(self,email_adress,password_text):
        create_acount=self.driver.find_element_by_xpath(Locators.create_acount_button).click()
        sleep(3)
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        email_field=self.driver.find_element_by_xpath(Locators.input__email_field)
        email_field.send_keys(email_adress)
        password_field=self.driver.find_element_by_xpath(Locators.input__password_field)
        password_field.send_keys(password_text)
        submit_button_click=self.driver.find_element_by_xpath(Locators.submit_button).click()
        sleep(2)
        rgb=self.driver.find_element_by_xpath(Er_locators.wrong_password_format).value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        return hex
        
    def login_acount(self,email_adress,password_text):
        login_acount_valid=self.driver.find_element_by_xpath(Locators.Login_button).click()
        sleep(3)
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        email_field=self.driver.find_element_by_xpath(Locators.login_email_field)
        email_field.send_keys(email_adress)
        password_field=self.driver.find_element_by_xpath(Locators.input__password_field)
        password_field.send_keys(password_text)
        submit_button_click=self.driver.find_element_by_xpath(Locators.submit_button).click()
        sleep(5)
        self.driver.switch_to.window(original_window)
        check_acount=self.driver.find_element_by_xpath(Locators.created_acount_checker)
        acount_name=check_acount.get_attribute('alt')
        return acount_name

    def create_new_project(self,project_name):
        iframe_close=self.driver.find_element_by_xpath(Locators.iframe_button).click()
        create_new_pr=self.driver.find_element_by_xpath(Locators.create_project).click()
    
        projectname_input_field=self.driver.find_element_by_xpath(Locators.project_name_input)
        projectname_input_field.send_keys(project_name)
        project_creat_button=self.driver.find_element_by_xpath(Locators.project_create_button).click()
        created_project=self.driver.find_element_by_xpath(Locators.check_project).text
        return created_project

    def invite_friends(self,friend_email_adress):
        iframe_close=self.driver.find_element_by_xpath(Locators.iframe_button).click()
        friend_add=self.driver.find_element_by_xpath(Locators.friend_invite_start_button).click()
        friend_invite_button=self.driver.find_element_by_xpath(Locators.friend_invite_button).click()
        friend_email=self.driver.find_element_by_tag_name(Locators.friend_invite_email_input)
        sleep(5)
        friend_email.send_keys(friend_email_adress)
        sleep(5)
        friend_role_set=self.driver.find_element_by_xpath(Locators.friend_role).click()
        friend_add_to_project=self.driver.find_element_by_xpath(Locators.friend_invite_add_button).click()
        sleep(5)
        friend_list=self.driver.find_elements_by_xpath(Locators.members_check)
        friends_in_project=self.driver.find_elements_by_xpath(Locators.members_list)
        lst1=[]
        for ttx in friend_list:
            lst1.append(ttx.text)
        return lst1
