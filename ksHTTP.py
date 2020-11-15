from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep


''' Sebourn Web Helper is a class that uses the Selenium Module 

    The Intent of this class is to have methods that help the user quickly make automated scripts for web scraping.
    
    All methods have try and except blocks 
    When the exception of ElementNotVisibleException occurs the method that catches it is called again. This creates a 
    recursive loop that has the potential of going on forever if the html element is never found.
    
    common parameters include "index" and "show_tries" and "seconds"
     
    index is either a string or integer
    if "index" is a string it will find the html element that has element.text equal to the "index"
    if "index" is a interger then it will interact with that index in the array of html elements
    
    "show_tries" is a boolean variable that is set to false when not specified. When set to true it allows a print() to 
    be called this is intended for debugging purpose in case the program is not working as intended
    
    "seconds" is an float or interger varible that controls how quickly a method is triggered in the recusive loop
    it is set to loop every 1 second unless changed
     
     Methods are also in alphabetical order for ease of finding them
     
'''


class ksHTTP:

    def __init__(self, http):
        self.driver = webdriver.Chrome()
        self.driver.get(http)

    def click_atag(self, index, show_tries=False, seconds=1):
        try:
            atags = self.driver.find_elements_by_tag_name('a')
            webdriver.ActionChains(self.driver).click_and_hold(atags[index]).perform()
            webdriver.ActionChains(self.driver).release().perform()
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find an atag with '+str(index)+'. ')
            self.click_atag(index)

    def press_atag(self, index, show_tries=False, seconds=1):
        try:
            atags = self.driver.find_elements_by_tag_name('a')
            if type(index) == int:
                atags[index].send_keys(Keys.RETURN)
            elif type(index) == str:
                for tag in atags:
                    if tag.text == index:
                        tag.send_keys(Keys.RETURN)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find an atag with '+str(index)+'. ')
            self.press_atag(index)

    def press_button(self, index, show_tries=False, seconds=1):
        try:
            buttons = self.driver.find_elements_by_tag_name('button')
            if type(index) == int:
                buttons[index].send_keys(Keys.RETURN)
            elif type(index) == str:
                for b in buttons:
                    print(b.text)
                    if b.text == index:
                        b.send_keys(Keys.RETURN)
            else:
                print('Buttons did nothing')
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find a button to press with '+str(index)+'. ')
            self.press_button(index)

    def print_atags(self, show_tries=False, seconds=1):
        try:
            atags = self.driver.find_elements_by_tag_name('a')
            for n in range(len(atags)):
                print(n, end=' : Ahref : ')
                print(atags[n].text)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find atags')
            self.print_atags()

    def print_buttons(self, show_tries=False, seconds=1):
        try:
            buttons = self.driver.find_elements_by_tag_name('button')
            for n in range(len(buttons)):
                print(n, end=' : Button : ')
                print(buttons[n].text)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to print buttons but none were found')
            self.print_buttons()

    def print_classes(self, class_name, show_tries=False, seconds=1):
        try:
            classes = self.driver.find_elements_by_class_name(class_name)
            for n in range(len(classes)):
                print(n, end=' : Class : ')
                print(classes[n].text)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find '+class_name+' classes to print out.')
            self.print_classes(class_name)

    def print_selects(self, show_tries=False, seconds=1):
        try:
            selects = self.driver.find_elements_by_tag_name('select')
            for n in range(len(selects)):
                print(n, end=' : Select : ')
                print(selects[n].text)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to find selects to print out.')
            self.print_selects()

    def print_inputs(self, show_tries=False, seconds=1):
        try:
            inputs = self.driver.find_elements_by_tag_name('input')
            for n in range(len(inputs)):
                print(n, end=' : Input : ')
                print(inputs[n].text)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Trying to print out inputs but none where found.')
            self.print_inputs()

    def print_web_info(self, show_tries=False, seconds=1):
        self.print_atags(show_tries=show_tries, seconds=seconds)
        self.print_buttons(show_tries=show_tries, seconds=seconds)
        self.print_inputs(show_tries=show_tries, seconds=seconds)

    def send_to_class(self, class_name, index, key, show_tries=False, seconds=1):
        try:
            elements = self.driver.find_elements_by_tag_name(class_name)
            if type(index) == int:
                elements[index].send_keys(key)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to send keys to class '+class_name+' but it was not found.')
            self.send_to_class(class_name, index, key)

    def send_to_id(self, element_id, key, show_tries=False, seconds=1):
        try:
            self.driver.find_element_by_id(element_id).send_keys(key)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to find id '+element_id+' but it was not found.')
            self.send_to_id(element_id, key)

    def send_to_input(self, index, key, show_tries=False, seconds=1):
        try:
            inputs = self.driver.find_elements_by_tag_name('input')
            if type(index) == int:
                inputs[index].send_keys(key)
            elif type(index) == str:
                for i in inputs:
                    if i.text == index:
                        i.send_keys(key)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to send keys to input but none were found.')
            self.send_to_input(index, key)

    def send_to_select(self, index, key, show_tries=False, seconds=1):
        try:
            selects = self.driver.find_elements_by_tag_name('select')
            if type(index) == int:
                selects[index].send_keys(key)

        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to send input to selects but none were found.')
            self.send_to_select(index, key)

    def send_to_text_area(self, index, key, show_tries=False, seconds=1):
        try:
            areas = self.driver.find_elements_by_tag_name('textarea')
            if type(index) == int:
                areas[index].send_keys(key)
            else:
                print('Index type not supported')
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to send input to text area but none were found.')
            self.send_to_text_area(index, key)

    def switch_to_iFrame(self, frame_id, show_tries=False, seconds=1):
        try:
            iframe = self.driver.find_element_by_id(frame_id)
            self.driver.switch_to(iframe)
        except exceptions.ElementNotVisibleException:
            sleep(seconds)
            if show_tries:
                print('Tried to switch to jFrame id '+frame_id+' but it was not found.')
            self.switch_to_iFrame(frame_id)