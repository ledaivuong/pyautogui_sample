from behave import *

from helpers import helper as hp
import pyautogui as pag
from helpers.env import Env
from unittest import TestCase as tc
from helpers.env import Env
import time

import sys
# Add the parent directory of mypackage to the Python path
sys.path.append("d:\\Chongyeu\\pyautogui_sample")


@given('User click on "{string_path_image}"')
def step_impl(context, string_path_image):
    hp.click_on_img_subject(
        string_path_image, duration=Env.DURATION)


@given('User double click on "{string_path_image}"')
def step_impl(context, string_path_image):
    hp.double_click_on_img_subject(
        string_path_image, duration=Env.DURATION)


@given('User click on search button by image "{string_path_image}"')
def step_impl(context, string_path_image):
    hp.click_on_img_subject(
        string_path_image, duration=Env.DURATION)


@when('User type "{text}"')
def step_impl(context, text):
    pag.typewrite(text)


@when('User open notepad by click on it by image "{string_path_image}"')
def step_impl(context, string_path_image):
    hp.click_on_img_subject(
        string_path_image, duration=Env.DURATION)


@when('User maximize window')
def step_impl(context):
    string_path_image = "./images/maximize.png"
    hp.click_on_img_subject(
        string_path_image, duration=Env.DURATION)

# This step require an array of item


@Then('User should see')
def step_impl(context):
    array_images = hp.conver_string_array(context.text)
    for image in array_images:
        tc.assertTrue(tc, hp.get_locator_of_image(image))


@When('User press hot key "{hot_key}"')
def step_impl(context, hot_key):
    array_hotkey = hp.conver_string_array(hot_key)
    pag.hotkey(array_hotkey)


@when('User perform save action with path "{string_path}" and file name "{string_file_name}"')
def step_impl(context, string_path, string_file_name):
    locator_refresh = hp.get_locator_of_image(
        "./images/note_pad_images/refresh.png")
    pag.moveTo(locator_refresh[0]-30,
               locator_refresh[1], duration=Env.DURATION)
    pag.click()
    pag.write(string_path)
    pag.press('enter')
    locator_file_name = hp.get_locator_of_image(
        "./images/note_pad_images/file_name.png")
    pag.moveTo(locator_file_name[0]+120,
               locator_file_name[1], duration=Env.DURATION)
    pag.click()
    pag.write(string_file_name)
    hp.click_on_img_subject(
        "./images/note_pad_images/save.png", duration=Env.DURATION)


@When('User open "{string_path}"')
def step_ipml(context, string_path):
    locator_search = hp.get_locator_of_image("./images/search.png")
    pag.moveTo(locator_search[0]+50, locator_search[1], duration=Env.DURATION)
    pag.click()
    pag.write(string_path)
    pag.press('enter')


@when('Delete file "{string_path}"')
def step_ipml(context, string_path):
    hp.delete_file(string_path)
