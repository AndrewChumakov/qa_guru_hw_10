import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "achumakov")
@allure.feature("Задачи в репозитории")
@allure.story("Задача видна в репозитории")
@allure.link("https://github.com", name="Testing")
def test_without_steps():
    browser.open("/qa-guru/allure-notifications")
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("Instruction")).should(be.visible)
