from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    #iphone X, Nokia Edge -> verify 2 items are showing in cart.
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        #step1
        #step2
        page.locator(".blinkingText").click()  # new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") #0 -> Please email us ,  1->mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0]    #0->mentor@rahulshettyacademy.com 1->
        assert email == "mentor@rahulshettyacademy.com"















