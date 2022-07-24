
import random
import time

import allure

from locators.alertrs_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.switch_to_win(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.switch_to_win(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    # # check new window message
    # def check_new_window_message(self):
    #     self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE).click()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     text_message = self.element_is_present(self.locators.TEXT_MESSAGE).text
    #     print(text_message)
    #     return text_message


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('get text from alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        # alert_window = self.driver.switch_to.alert
        alert_window = self.switch_to_alert()
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.switch_to_alert()
        return alert_window.text

    @allure.step('check confirm alert')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        # alert_window = self.driver.switch_to.alert
        alert_window = self.switch_to_alert()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('check prompt alert')
    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        # alert_window = self.driver.switch_to.alert
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('check frame')
    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.PARENT_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('check modal dialogs')
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        tittle_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        tittle_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        return [tittle_small, len(body_small_text)], [tittle_large, len(body_large_text)]
