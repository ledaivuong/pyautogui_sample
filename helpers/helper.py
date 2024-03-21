import pyautogui as pag
from helpers.env import Env
from ast import literal_eval
import os


def get_locator_of_image(string_path_image, min_search_time=Env.WAITING_TIME_OUT, confidence=Env.IMG_CONFIDENCE):
    return pag.locateCenterOnScreen(string_path_image, minSearchTime=min_search_time, confidence=confidence)


def click_on_img_subject(string_path_image, confidence=Env.IMG_CONFIDENCE, duration=Env.DURATION):
    locator = get_locator_of_image(string_path_image, confidence=confidence)
    pag.click(locator, duration=duration)


def double_click_on_img_subject(string_path_image, confidence=Env.IMG_CONFIDENCE, duration=Env.DURATION):
    locator = get_locator_of_image(string_path_image, confidence=confidence)
    pag.doubleClick(locator, duration=duration)


def conver_string_array(string_array):
    return literal_eval(string_array)


def delete_file(string_path):
    if os.path.exists(string_path):
        os.remove(string_path)
    else:
        print(string_path)
