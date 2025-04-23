# Termina Pygments Lexer

This repository provides a custom [Pygments](https://pygments.org/) syntax highlighter for the [Termina](#about-termina) programming language. It support syntax highlighting of keywords, types, constants, operators, and identifiers

## Installation

The following commands install the lexer into a Python environment in editable mode.

```bash
git clone https://github.com/termina-lang/termina-lexer.git
cd termina-lexer
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Using with MkDocs

To enable Termina syntax highlighting in [MkDocs](https://www.mkdocs.org/), you need to configure your mkdocs.yml to enable Pygments highlighting:


```yaml
markdown_extensions:
  - pymdownx.highlight:
      use_pygments: true
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
```

## Contribute

If you are interested in collaborating with us and would like more information, please contact us at the following e-mail address: team@termina-lang.org.
