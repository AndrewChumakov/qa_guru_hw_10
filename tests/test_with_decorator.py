import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "achumakov")
@allure.feature("Задачи в репозитории")
@allure.story("Задача видна в репозитории")
@allure.link("https://github.com", name="Testing")
def test_with_decorator():
    open_page("/qa-guru/allure-notifications")
    open_tab("#issues-tab")
    should_have_issue("Instruction")

@allure.step("Открыть страницу с репозиторием")
def open_page(page):
    browser.open(page)

@allure.step("Перейти на вкладку Issues")
def open_tab(tab):
    browser.element(tab).click()

@allure.step("Проверить наличие Issue")
def should_have_issue(issue):
    browser.element(by.partial_text(issue)).should(be.visible)