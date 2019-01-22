var { Given, When, Then } = require('cucumber')
const { After, BeforeAll, Before, AfterAll, setDefaultTimeout } = require('cucumber');
const { driver } = require('./get_driver');
const assert = require('assert');

//设置缺省超时时间
setDefaultTimeout(60 * 1000);

BeforeAll(function() {
   return driver.init();
})

//Before Scenario Hook
Before(async function() {
    //return driver.timeoutImplicitWait(60 * 1000)
})

//After Scenario Hook
After(async function() {
    //每个场景结束时截屏
    let screenshot = await driver.saveScreenshot();
    this.attach(screenshot, 'image/png');
});

AfterAll(async function() {
    //关闭应用
    await driver.end();
})



Given(/^\*\*\*点击左上角设置图标，弹出侧边栏$/, async function () {
    
    //className定位元素
    await driver.click('android=new UiSelector().className("android.widget.ImageButton").index(0)')
    
    //X PATH 定位元素
    //await driver.click('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.ImageButton')
    let text = await driver.getText('android=new UiSelector().className("android.widget.CheckedTextView").index(2)')
    console.log(text)
    return assert.equal(text, "全部")
});

When(/^点击精华版块，跳转至精华页面$/, async function () {
    //resource-id定位元素
    await driver.click('android=new UiSelector().resourceId("org.cnodejs.android.md:id/btn_nav_good")')
    let text1 = await driver.elements('android=new UiSelector().resourceId("org.cnodejs.android.md:id/icon_good")')
    console.log(text1)
    
});
