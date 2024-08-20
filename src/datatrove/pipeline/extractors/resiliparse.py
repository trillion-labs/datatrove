from .base import BaseExtractor


class Resiliparse(BaseExtractor):
    """Resiliparse extractor, it uses https://github.com/chatnoir-eu/chatnoir-resiliparse.

    Args:
        preserve_formatting: Preserve basic block-level formatting.
        main_content: Apply simple heuristics for extracting only "main-content" elements.
        list_bullets: Insert bullets or numbers for list items.
        alt_texts: Preserve alternative text descriptions.
        links: Extract link target URLs.
        form_fields: Extract form fields and their values.
        noscript: Extract contents of <noscript> elements.
        comments: Treat comment sections as main content.
    """

    name = "⛏ Resiliparse"
    _requires_dependencies = ["resiliparse"]

    def __init__(
        self,
        main_content: bool = True, 
        preserve_formatting: bool = True, 
        list_bullets: bool = False,
        alt_texts: bool = False, 
        links: bool = False,
        form_fields: bool = False,
        noscript: bool = False,
        comments: bool = False,
        timeout: float = 0.1,
        **kwargs,
    ):
        super().__init__(timeout)
        self.main_content = main_content 
        self.preserve_formatting = preserve_formatting
        self.list_bullets = list_bullets
        self.alt_texts = alt_texts
        self.links = links
        self.form_fields = form_fields
        self.noscript = noscript
        self.comments = comments
        self.kwargs = kwargs

    def extract(self, text: str) -> str:
        """

        Args:
          text: str: html content

        Returns: plain text extracted text

        """
        from resiliparse.extract.html2text import extract_plain_text

        return extract_plain_text(
            text,
            main_content=self.main_content, 
            preserve_formatting=self.preserve_formatting, 
            list_bullets=self.list_bullets,
            alt_texts=self.alt_texts,
            links=self.links,
            form_fields=self.form_fields,
            noscript=self.noscript, 
            comments=self.comments,
        )
