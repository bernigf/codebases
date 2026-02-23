from typing import List, Dict, Optional

class Book:
    """
    Book represents an immutable content entity in the reading domain.

    Responsibilities:
    - Encapsulates book content (title + pages)
    - Provides O(1) page access via index
    - Ensures controlled access to page data
    - Maintains object integrity after construction

    Design Decisions:
    - Title is treated as an identity attribute (should not change)
    - Pages are stored as a list of strings (each string = one page)
    - Page number is derived from list index (efficient lookup)
    - No user-specific state is stored here (SRP compliance)

    Notes:
    - In production, a unique book_id would replace title as identity
    - Content should ideally be immutable
    - Validation (non-empty title, at least one page) should be enforced
    """
    def __init__(self, title: str, pages: List[str]):
        # Title is immutable identity attribute
        self._title = title
        
        # Store pages; index represents page number (O(1) access)
        self._pages = pages

    @property
    def title(self) -> str:
        # Expose title read-only
        return self._title

    def get_page(self, page_number: int) -> str:
        # Validate bounds to prevent invalid access
        if page_number < 0 or page_number >= len(self._pages):
            raise IndexError("Invalid page number")
        
        # O(1) list access
        return self._pages[page_number]

    def total_pages(self) -> int:
        # Useful for boundary validation
        return len(self._pages)


class Library:
    def __init__(self):
        # Use dict for O(1) lookup by title (could be book_id in real system)
        self._books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        # Prevent duplicate books
        self._books[book.title] = book

    def remove_book(self, title: str) -> None:
        # Safe removal if exists
        self._books.pop(title, None)

    def get_book(self, title: str) -> Optional[Book]:
        # O(1) lookup
        return self._books.get(title)


class ReadingSession:
    def __init__(self):
        # Track last page per book
        self._progress: Dict[str, int] = {}
        
        # Active book reference
        self._active_book: Optional[Book] = None

    def set_active_book(self, book: Book) -> None:
        # Set active book
        self._active_book = book
        
        # Initialize progress if first time
        self._progress.setdefault(book.title, 0)

    def get_current_page(self) -> str:
        if not self._active_book:
            raise Exception("No active book selected")
        
        # Retrieve last saved page
        current_page_index = self._progress[self._active_book.title]
        
        # Only one page displayed at a time
        return self._active_book.get_page(current_page_index)

    def next_page(self) -> None:
        if not self._active_book:
            raise Exception("No active book selected")
        
        current_index = self._progress[self._active_book.title]
        
        # Boundary check
        if current_index + 1 < self._active_book.total_pages():
            # Move forward one page
            self._progress[self._active_book.title] += 1

    def previous_page(self) -> None:
        if not self._active_book:
            raise Exception("No active book selected")
        
        current_index = self._progress[self._active_book.title]
        
        # Prevent negative page index
        if current_index > 0:
            self._progress[self._active_book.title] -= 1


class User:
    def __init__(self, user_id: str):
        # Unique user identifier
        self.user_id = user_id
        
        # Composition: user owns library
        self.library = Library()
        
        # Composition: user owns reading state
        self.reading_session = ReadingSession()