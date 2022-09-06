from behave import *
from pages.BaiduPage import BaiduPage

@given('打开百度网页"{baidu}"')
def step_imp1(context, baidu):
    context.driver.get(baidu)

@when('输入关键字"{keyword}"')
def step_imp1(context, keyword):
    page = BaiduPage(context.driver)
    page.search_input = keyword
    page.search_button.click()

@then('验证返回的搜索结果标题是"{keyword}"')
def step_impl(context, keyword):
    assert context.driver.title == keyword
