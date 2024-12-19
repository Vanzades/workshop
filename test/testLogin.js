const { Builder, By, until } = require("selenium-webdriver");
const assert = require("assert");

async function loginTest() {
  let driver = await new Builder().forBrowser("chrome").build();

  try {
    await driver.get("https://www.saucedemo.com/");
    await driver.findElement(By.id("user-name")).sendKeys("standard_user");
    await driver.findElement(By.id("password")).sendKeys("secret_sauce");
    await driver.findElement(By.name("login-button")).click();

    await driver.wait(until.urlContains("inventory.html"), 1000);
    const pageTitle = await driver.findElement(By.className("title")).getText();
    assert.strictEqual(pageTitle, "Products");
  } finally {
    await driver.quit();
  }
}

loginTest();
