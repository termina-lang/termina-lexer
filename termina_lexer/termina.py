from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class TerminaLexer(RegexLexer):
    name = 'Termina'
    aliases = ['termina']
    filenames = ['*.fin']
    case_sensitive = True

    # Categorized language elements
    KEYWORDS = (
        "match", "case", "for", "if", "else",
        "return", "continue", "while", "reboot",
        "as", "is", "in", "self"
    )

    DECLARATIONS = (
        "struct", "enum", "class", "emitter",
        "task", "function", "handler", "resource",
        "channel", "const", "constexpr", "var", "let",
        "interface", "provides", "extends",
        "procedure", "viewer", "method", "action",
    )

    IMPORTS = (
        "import"
    )

    BUILTIN_TYPES = (
        "u8", "u16", "u32", "u64",
        "i8", "i16", "i32", "i64",
        "usize", "bool", "char", "unit",
        "access", "sink", "out", "triggers", 
        "box", "loc"
    )

    CONSTANTS = ("true", "false", "null")

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Single-line and multi-line comments
            (r'//.*?\n', Comment.Single),
            (r'/\*', Comment.Multiline, 'comment'),

            # Strings and chars
            (r'"(\\\\|\\"|[^"])*"', String),
            (r"'(\\.|[^'])'", String.Char),

            # Numbers
            (r'\b\d+\.\d+\b', Number.Float),
            (r'\b0x[0-9a-fA-F]+\b', Number.Hex),
            (r'\b\d+\b', Number.Integer),

            (
                r'\b(import)(\s+)'
                r'([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)'  # dotted module path
                r'(\s*)(;)',
                bygroups(Keyword.Namespace, Text.Whitespace, Name.Namespace, Text.Whitespace, Punctuation)
            ),

            # Built-in types
            (r'\b(?:' + '|'.join(BUILTIN_TYPES) + r')\b', Keyword.Type),

            # Declarations
            (r'\b(?:' + '|'.join(DECLARATIONS) + r')\b', Keyword.Declaration),

            # Constants (true, false)
            (r'\b(?:' + '|'.join(CONSTANTS) + r')\b', Keyword.Constant),

            # Keywords
            (r'\b(?:' + '|'.join(KEYWORDS) + r')\b', Keyword),

            # Operators & punctuation
            (r'(\.\.|\&mut|\&priv|->|=>|::|<<|>>|<=|>=|==|!=|&&|\|\||<->|<-|:=|\?)', Operator),
            (r'[\+\-\*/%<>=\^\|\&!#@]', Operator),
            (r'[:\[\]\{\}\(\)\.,;]', Punctuation),

            # Identifiers
            (r'[A-Z][A-Za-z0-9_]*', Name.Class),
            (r'[a-z_][A-Za-z0-9_]*', Name)
        ],

        'comment': [
            (r'[^*/]+', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline),
        ]
    }


