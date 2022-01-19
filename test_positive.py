from selenium import webdriver
from driver import Base
import pytest
from Actions import Contact_us
from time import sleep
import re

@pytest.mark.usefixtures('set_up')
class TestPozitive(Base):
    
    @pytest.mark.parametrize("email_adress,password_text",[("aaa2222277777@mail.ru","Aa@123aA")])
    def test_create_acount(self,email_adress,password_text):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.create_acount(email_adress,password_text)
        print(len(El_item))
        acount_name=""
        for char in email_adress:
            if char!="@":
                acount_name=acount_name+char
            else:
                break
        assert acount_name==El_item,"User is not created"
        print("User created succesfully and acount name is the same,as email adress name until '@' character")
    
    @pytest.mark.parametrize("email_adress,password_text",[("aaa2222277777@mail.ru","Aa@123aA")])
    def test_log_in(self,email_adress,password_text):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.login_acount(email_adress,password_text)
        acount_name=""
        for char in email_adress:
            if char!="@":
                acount_name=acount_name+char
            else:
                break
        assert acount_name==El_item,"User is not logged in"
        print("User logged in succesfully")
    
    @pytest.mark.parametrize("email_adress,password_text,project_name",[("aaa2222277@mail.ru","Aa@123aA","first_project")])
    def test_new_project(self,email_adress,password_text,project_name):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.login_acount(email_adress,password_text)
        El_item2=element.create_new_project(project_name)
        assert El_item2==project_name,"Project cant be created or name does not much"
    
    @pytest.mark.parametrize("email_adress,password_text,friend_email_adress",[("aaa2222277@mail.ru","Aa@123aA","a1a1a1a@mail.ru")])
    def test_add_member(self,email_adress,password_text,friend_email_adress):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.login_acount(email_adress,password_text)
        El_item2=element.invite_friends(friend_email_adress)
        assert friend_email_adress in El_item2,"friend was not added"