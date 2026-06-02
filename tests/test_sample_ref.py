from src.ref_splitter import RefSplitter

sample_path = './mouse_drop_sample.txt'


def test_parse_sample_page() -> None:
    with open(sample_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    splitter = RefSplitter(content)
    splitter.build_ref_entries()