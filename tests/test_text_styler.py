from dublib.cli.text_styler import TextStyler

styler = TextStyler()

def test_html_to_rich():

	assert styler.html_to_rich("<b>text</b>") == "[bold]text[/bold]"
	assert styler.html_to_rich("<i>text</i>") == "[italic]text[/italic]"
	assert styler.html_to_rich("<s>text</s>") == "[strike]text[/strike]"
	assert styler.html_to_rich("<u>text</u>") == "[underline]text[/underline]"

	rich_link: str = styler.html_to_rich("<a href=\"https://example.com\" style=\"color: red\">text</a>")
	open_tag, close_tag = rich_link.split("text")
	open_tag = open_tag.strip("[]")
	close_tag = close_tag.strip("/[]")
	open_parts: list[str] = open_tag.split(" ")
	close_parts: list[str] = close_tag.split(" ")

	assert set(open_parts) == {"red", "link=https://example.com"}
	assert set(close_parts) == {"red", "link"}

	assert styler.html_to_rich("<span style=\"font-weight: bold\">text</span>") == "[bold]text[/bold]"
	assert styler.html_to_rich("<span style=\"font-style: italic\">text</span>") == "[italic]text[/italic]"
