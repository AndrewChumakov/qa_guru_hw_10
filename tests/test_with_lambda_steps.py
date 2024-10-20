import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "achumakov")
@allure.feature("Задачи в репозитории")
@allure.story("Задача видна в репозитории")
@allure.link("https://github.com", name="Testing")
def test_with_lambda_steps():
    with allure.step("Открыть страницу с репозиторием"):
        browser.open("/qa-guru/allure-notifications")
    with allure.step("Перейти на вкладку Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверить наличие Issue"):
        browser.element(by.partial_text("Instruction")).should(be.visible)