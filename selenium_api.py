from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import free_port
from selenium.webdriver.support.wait import WebDriverWait

"""
Packages:
    1. selenium.common.exception
        This package includes all the exception that could occure in the selenium code
    2. selenium.webdriver.common
        a. selenium.webdriver.common.action_chains
            click(on_element=None)
            click_and_hold(on_element=None)
            context_click(on_element=None)
            double_click(on_element=None)
            drag_and_drop(source, target)
            drag_and_drop_by_offset(source, xoffset, yoffset)
            key_down(value, element=None)
            key_up(value, element=None)
            move_by_offset(xoffset, yoffset)
            move_to_element(to_element)
            move_to_element_with_offset(to_element, xoffset, yoffset)
            pause(seconds)
            perform()
            release(on_element=None)
            reset_actions()
            send_keys(*keys_to_send)
            send_keys_to_element(element, *keys_to_send)
        b. selenium.webdriver.common.utils
            find_connectable_ip(host, port=None)
            free_port()
        c. selenium.webdriver.common.alert
        d. selenium.webdriver.common.by
        e. selenium.webdriver.common.keys
        f. selenium.webdriver.common.service
        g. selenium.webdriver.common.desired_capabilities
        h. selenium.webdriver.common.touch_action
        i. selenium.webdriver.common.proxy
        j. selenium.webdriver.common.html5.application_cache

------------------------------------------------------------------------------------------------------------------------
Decorator to override implicit wait for specific method

def no_wait(func):
    @wraps(func)
    def without_wait(*args, **kwargs):
        try:
            driver.get_driver().implicitly_wait(0)
            return func(*args, **kwargs)
        finally:
            driver.get_driver().implicitly_wait(config.implicit_timeout)

    return without_wait
    
------------------------------------------------------------------------------------------------------------------------
cookie builder to return cookie to add

WEBDRIVER_COOKIES_MAP={
    'domain': 'domain',
    'expiry': 'expiry',
    'httpOnly': False,
    'name': 'name',
    'path': 'path',
    'secure': 'False',
    'value': 'value',' 
}
    

-> data generators
-> providers
        mysql_provider
        sqlite_provider
        csv_provider
        xls_provider
        yml_provider
-> assertions
-> utils
        email
        locator_
        ----------------------------------------------------------------------------------------------------------------
        @staticmethod
        def find_element_by_selectors(webdriver, *selectors):
            '''
            Utility method makes it easier to find an element using multiple selectors. This is 
            useful for problematic elements what might works with one browser, but fail in another.
            (Like different page elements being served up for different browsers)
    
            Args:
                selectors - var arg if N number of selectors to match against.  Each selector should 
                            be a Selenium 'By' object.
    
            Usage::
                my_element = XXXX.find_element_by_selectors(webdriver,
                                                                        (By.ID, "MyElementID"),
                                                                        (By.CSS, "MyClassSelector") )
    
            '''
            # perform initial check to verify selectors are valid by statements.
            selectors_used = []
            for selector in selectors:
                (by_method, value) = selector
                if not WebElementSelector.__is_valid_by_type(by_method):
                    raise BadSelectorError(
                        u("Selectors should be of type selenium.webdriver.common.by.By"))
                if type(value) != str:
                    raise BadSelectorError(
                        u("Selectors should be of type selenium.webdriver.common.by.By"))
                selectors_used.append(
                    u("{by}:{value}").format(by=by_method, value=value))
                try:
                    return webdriver.find_element(by=by_method, value=value)
                except:
                    pass
    
            raise ElementNotSelectableException(
                u("Unable to find elements using:") + u(",").join(selectors_used))
        
        @staticmethod
        def __is_valid_by_type(by_type):
            for attr, value in By.__dict__.iteritems():
                if "__" not in attr:
                    if by_type == value:
                        return True
    
            return False
        
        @staticmethod
        def is_image_loaded(webdriver, webelement):
            '''
            Check if an image (in an image tag) is loaded.
            Note: This call will not work against background images.  Only Images in <img> tags.
    
            Args:
                webelement (WebElement) - WebDriver web element to validate.
    
            '''
            script = (u("return arguments[0].complete && type of arguments[0].naturalWidth != \"undefined\" ") + 
                     u("&& arguments[0].naturalWidth > 0"))
            try:
                return webdriver.execute_script(script, webelement)
            except:
                return False  # Img Tag Element is not on page.
        
        driver_factory
            
"""



# import unittest
#
# class Test_suite(unittest.TestCase):
#
#     # @beforeClass
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome("/home/mrane/Downloads/chromedriver")
#
#     # @beforeTest
#     def setUp(self):
#         self.driver = webdriver.Chrome("/home/mrane/Downloads/chromedriver")
#
#     def test_case(self):
#         print("test case 1")
#
#     def test_case_1(self):
#         print("test case 2")
#
#     # @afterTest
#     def tearDown(self):
#         self.driver.quit()
#
#     # @afterClass
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# from selenium.webdriver.support import wait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome("/home/mrane/Downloads/chromedriver")
# driver.get("http://10.200.10.74:8080")
# driver.set_network_conditions()
# driver.implicitly_wait(10)
# wait.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_username"))).send_keys("mrane")
# wait.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_password")), "Not Found").send_keys("__python__")
# driver.find_element_by_id("yui-gen1-button").click()

import pytest
#
#
# @pytest.mark.xfail(raises=ZeroDivisionError)
# def test_case_1():
#     a = 1 / 0

# @pytest.fixture(scope='session')
# def connect_to_databse():
#     # higher order fixture than module and function
#     driver = webdriver.Chrome("/home/mrane/Downloads/chromedriver")
#
#
# @pytest.fixture(scope='module')
# def query_to_return_something():
#     # code which needs to called at once per module
#     driver.get("url")
#
# @pytest.fixture(scope='module')
# def test_setup_teardown():
#     driver = webdriver.Chrome("/home/mrane/Downloads/chromedriver")
#     yield driver
#     driver.quit()
#
# def test_google():
#     test_setup_teardown().get("http://google.com"
import pysel

def setup_module(pysel):
    """ setup any state specific to the execution of the given module."""
    print("setup statements")

def teardown_module(pysel):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print("tear Down statements")
