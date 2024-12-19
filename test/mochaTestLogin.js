const { Builder, By, until } = require("selenium-webdriver");
const assert = require("assert");

describe("Test Login Scenario", function () {
    this.timeout(20000);
    let driver;

    before(async () => {
        driver = new Builder().forBrowser("chrome").build();
    });

    after(async () => {
        await driver.quit();
    });

    it("Should have redirect to product page if login success", async () => {
        await driver.get("https://www.saucedemo.com/");
        await driver.findElement(By.id("user-name")).sendKeys("standard_user");
        await driver.findElement(By.id("password")).sendKeys("secret_sauce");
        await driver.findElement(By.id("login-button")).click();

        await driver.wait(until.urlContains("inventory.html"), 10000);
        const pageTitle = await driver.findElement(By.className("title")).getText();
        assert.strictEqual(pageTitle, "Products");
    });
});
