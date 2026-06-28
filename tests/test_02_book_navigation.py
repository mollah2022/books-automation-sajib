# Third-party imports
import allure
import pytest
from playwright.sync_api import Page

# Internal imports
from pages.home_page import HomePage, BookCard
from pages.book_detail_page import BookDetailPage
from utils.config import Config
from utils.helpers import pick_random_items


@allure.feature("Book Navigation")
@allure.story("TC-02: Random Book Navigation")
@pytest.mark.regression
@pytest.mark.navigation
class TestRandomBookNavigation:
    """Test suite for random book selection and detail page validation."""

    @allure.title("5 randomly selected books open correct detail pages")
    def test_random_book_navigation(self, page: Page) -> None:
        """Click 5 random books and verify the detail page title and product info."""
        home = HomePage(page).open()

        with allure.step("Collect all book cards from homepage"):
            all_books = home.get_all_book_cards()
            assert all_books, "No books found on the homepage"

        with allure.step(f"Randomly select {Config.RANDOM_BOOK_COUNT} books"):
            selected: list[BookCard] = pick_random_items(all_books, Config.RANDOM_BOOK_COUNT)
            allure.attach(
                "\n".join([b.title for b in selected]),
                name="Selected Book Titles",
                attachment_type=allure.attachment_type.TEXT,
            )

        detail = BookDetailPage(page)

        for book in selected:
            with allure.step(f"Validate book: '{book.title}'"):

                with allure.step("Click the book on homepage"):
                    home.click_book_by_index(book.index)

                with allure.step("Verify detail page H1 title matches"):
                    actual_title = detail.get_title()
                    assert actual_title == book.title, (
                        f"Title mismatch!\n"
                        f"  Homepage : '{book.title}'\n"
                        f"  Detail   : '{actual_title}'"
                    )

                with allure.step("Verify product information table is visible"):
                    assert detail.is_product_info_visible(), (
                        f"Product info table not visible for book '{book.title}'"
                    )

                with allure.step("Navigate back to homepage"):
                    detail.go_to_homepage()
                    home = HomePage(page)