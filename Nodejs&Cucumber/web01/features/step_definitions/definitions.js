const { Given, When, Then } = require('cucumber');
const assert = require('assert');
const { driver } = require('../support/web_driver');

Given(/^浏览到搜索网站 "([^"]*)"$/, async function(url) {
   
    this.url = url
    await driver.get(this.url);
});

When(/^\.\.\.点击搜索框输入内容，显示所输入的内容 "([^"]*)"$/, async function (arg1) {

    await driver.findElement({ id:'sb_form_q'}).sendKeys(arg1)
});

When(/^\.\.\.点击搜索图标，跳转至搜索结果页面$/, async function () {

    await driver.findElement({ id:'sb_form_go'}).click()
    cur_url = driver.getCurrentUrl()
    console.log(cur_url)

    console.log(this.url)
    assert.notEqual(cur_url,this.url)
});