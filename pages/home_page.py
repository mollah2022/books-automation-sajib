from dataclasses import dataclass
from typing import List
from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.config import Config


@dataclass
class BookCard:
    """Represents a single book item on the homepage."""
    title: str
    price: str
    index: int


class HomePage(BasePage):
    """Page object for the Books to Scrape homepage."""

    _BOOKS_SECTION = "section"
    _BOOK_ITEMS = "article.product_pod"
    _BOOK_TITLE = "h3 > a"
    _BOOK_PRICE = "p.price_color"
    _HEADINGS = "h1, h2, h3, h4, h5, h6"
    _NEXT_BUTTON = "li.next > a"
    _PRODUCT_IMAGES = "article.product_pod img"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> "HomePage":
        self.navigate(Config.BASE_URL)
        return self

    def get_url(self) -> str:
        return self.current_url

    def get_page_title(self) -> str:
        return self.title

    def get_all_headings(self) -> List[str]:
        heading_locators = self._page.locator(self._HEADINGS).all()
        return [h.inner_text().strip() for h in heading_locators if h.is_visible()]

    def is_books_section_visible(self) -> bool:
        return self.is_visible(self._BOOKS_SECTION)

    def get_book_count(self) -> int:
        return len(self._page.locator(self._BOOK_ITEMS).all())

    def get_all_book_cards(self) -> List[BookCard]:
        book_elements = self._page.locator(self._BOOK_ITEMS).all()
        cards: List[BookCard] = []
        for idx, book in enumerate(book_elements):
            title_elem = book.locator(self._BOOK_TITLE)
            price_elem = book.locator(self._BOOK_PRICE)
            title = title_elem.get_attribute("title") or title_elem.inner_text().strip()
            price = price_elem.inner_text().strip()
            cards.append(BookCard(title=title, price=price, index=idx))
        return cards

    def click_book_by_index(self, index: int) -> None:
        self._page.locator(self._BOOK_ITEMS).nth(index).locator(self._BOOK_TITLE).click()
        self._page.wait_for_load_state("networkidle")

    def has_next_page(self) -> bool:
        return self._page.locator(self._NEXT_BUTTON).count() > 0

    def click_next_page(self) -> None:
        self._page.locator(self._NEXT_BUTTON).click()
        self._page.wait_for_load_state("networkidle")

    def get_product_images(self) -> list:
        return self._page.locator(self._PRODUCT_IMAGES).all()

    def get_all_hrefs(self) -> List[str]:
        anchors = self._page.locator("a[href]").all()
        hrefs = set()
        for anchor in anchors:
            href = anchor.get_attribute("href")
            if href and href.strip():
                hrefs.add(href.strip())
        return list(hrefs)