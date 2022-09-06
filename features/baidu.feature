Feature: 一个简单的sample演示自动化测试

  Scenario: 打开百度网页并输入关键字
    Given: 打开百度网页http://www.baidu.com
    When: 输入关键字pytest
    Then：验证返回的搜索结果标题是pytest_百度搜索
