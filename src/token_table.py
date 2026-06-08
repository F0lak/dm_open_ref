    
INLINE_TOKEN_TABLE = [
    {"TOKEN" : "BOLD",        "html" : "b",     "md" : "*"  },
    {"TOKEN" : "ITALIC",      "html" : "i",     "md" : "**" },
    {"TOKEN" : "UNDERLINE",   "html" : "u",     "md" : "__" },
    {"TOKEN" : "CODE",        "html" : "tt",    "md" : "`"  },
    {"TOKEN" : "CODE",        "html" : "var",   "md" : "`"  },
    {"TOKEN" : "DESC_TERM",   "html" : "dt",    "md" : "**" },
    {"TOKEN" : "DESC_DETAIL", "html" : "dd",    "md" : "DD" }

    # this is handled in the ref_splitter; the standard tokenizer destroys the code inside the block
    #{"TOKEN" : "CODEBLOCK",   "html" : "xmp",   "md" : "```" },
]

P_CLASS_TOKEN_TABLE = [
    {"TOKEN" : "P_COMPATIBILITY", "html" : "compatibility",   "md" : "TIP"},
    {"TOKEN" : "P_PERFORMANCE",   "html" : "performance",     "md" : "TIP"},
    {"TOKEN" : "P_TIP",           "html" : "tip",             "md" : "TIP"},
    {"TOKEN" : "P_NOTE",          "html" : "note",            "md" : "NOTE"},
    {"TOKEN" : "P_DIDYOUKNOW",    "html" : "didyouknow",      "md" : "TIP"},
    {"TOKEN" : "P_DEPRECTATED",   "html" : "deprecated",      "md" : "WARNING"},
    {"TOKEN" : "P_SECURITY",      "html" : "security",        "md" : "CAUTION"}
]