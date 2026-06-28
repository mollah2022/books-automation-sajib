from playwright.sync_api import Page
from pages.base_page import BasePage


class BookDetailPage(BasePage):
    """Page object for individual book detail page."""

    _H1_TITLE = "article.product_page h1"
    _PRICE = "p.price_color"
    _PRODUCT_INFO = "table.table-striped"
    _PRODUCT_GALLERY = "div.item.active img"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_title(self) -> str:
        self.wait_for_selector(self._H1_TITLE)
        return self.get_text(self._H1_TITLE)

    def get_price(self) -> str:
        self.wait_for_selector(self._PRICE)
        return self._page.locator(self._PRICE).first.inner_text().strip()

    def is_product_info_visible(self) -> bool:
        return self.is_visible(self._PRODUCT_INFO)

    def is_image_visible(self) -> bool:
        return self.is_visible(self._PRODUCT_GALLERY)

    def go_to_homepage(self) -> None:
        self.go_back()