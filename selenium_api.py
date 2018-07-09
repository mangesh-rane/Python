from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import free_port

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

"""

print(free_port())
