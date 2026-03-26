def test_calculator_add(page):
    page.goto("http://127.0.0.1:8000/calculator")

    page.fill("#a", "5")
    page.fill("#b", "3")

    page.click("text=Add")

    page.wait_for_timeout(1000)

    result = page.inner_text("#result")

    assert "Addition Result" in result
    assert "8" in result