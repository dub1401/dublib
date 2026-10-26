# TextStyler
Provides [Rich](https://github.com/Textualize/rich) markup into ANSI-styled string conversion and HTML-Rich-ANSI conversion. The main goal is capture Rich console output and make powerful stylization libruary easy-to-run, also add base HTML support instead Rich own markup.

All instances use one common `rich.console.Console` with always captured output. No reinitialization required. No printed text in terminal. If you need console, `TextStyler` provides `console` read-only property.

## How to use
```Python
from dublib.cli.text_styler import TextStyler

styler = TextStyler()

# Rich markup and HTML gives identical result.
assert styler.convert("[bold]bold text[/bold]") == styler.convert_from_html("<b>bold text</b>")

text: str = styler.richify("bold text", "bold") # Returns ANSI-styled bold text.

preset = styler.make_preset("bold red")
preset("bold red text") # Returns ANSI-styled bold red text. Simple reusable.
```

## Methods
```{eval-rst}
.. autoclass:: dublib.cli.text_styler.TextStyler
    :members:
```