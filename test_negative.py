from selenium import webdriver
from driver import Base
import pytest
from Actions import Contact_us
from time import sleep
import re

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    
    @pytest.mark.parametrize("email_adress,password_text",[("aaa1111111222mail.ru","Aa@123aA"),("aaa1111111222mailru","Aa@123aA"),
    ("aaa1111111222@mailru","Aa@123aA")])
    def test_acount_create_wrong_email_format(self,email_adress,password_text,error_config):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.create_acount_failed_email(email_adress,password_text)
        if "@" or "." not in email_adress:
            assert El_item==error_config[1],"no message about wrong email type"

    @pytest.mark.parametrize("email_adress,password_text",[("aaa1111111222@mail.ru","Aa@123"),("aaa1111111222@mail.ru","AAAAAAAAAAaA"),
    ("aaa1111111222@mailru","AaaaaaaaaA"),("aaa1111111222@mailru","A@@@@@@@@@@@A")])
    def test_acount_create_wrong_password_format(self,email_adress,password_text,error_config):
        driver=self.driver
        element=Contact_us(driver)
        El_item=element.create_acount_failed_password(email_adress,password_text)
        if len(password_text)<8:
            assert El_item==error_config[0],"No error message"
        else:
            count_lower=0
            count_upper=0
            count_digit=0
            count_symbol=0
            for char in password_text:
                if char.islower():
                    count_lower+=1
                elif char.isupper():
                    count_upper+=1
                elif char.isdigit():
                    count_digit+=1
                else:
                    count_symbol+=1
            lst=[count_upper,count_digit,count_lower,count_symbol]
            count_0=0
            for num in lst:
                if num==0:
                    count_0+=1
            if count_0>=2:
                assert El_item==error_config[0],"No error message"






