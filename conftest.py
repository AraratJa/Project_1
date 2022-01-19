import pytest
import allure

@pytest.fixture
def error_config():
    error_rgb="#d00e17"
    email_invalid="Адрес электронной почты недействителен."
    
    return error_rgb,email_invalid

