
import pytest
from ref_splitter.ref_splitter import RefSplitter
from ref_splitter.ref_tree import RefTree
from ref_splitter.export import ExportMD

@pytest.mark.e2e
def test_export_file_structure(tmp_path, client_sample_path):
    # Run your export logic pointing to the temp directory
    with open(client_sample_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ref_splitter = RefSplitter(content)
    ref_splitter.prep_pages()
    ref_splitter.build_ref_entries()
    
    ref_tree = RefTree()
    ref_tree.build_tree_from_entries(ref_splitter.entries, ref_splitter.links)
    
    export = ExportMD(tmp_path)
    export.format_tree(ref_tree)
    export.export_pages()

    expected_dir = export.export_root / "ref" / "client"
    index_file = expected_dir / "index.md"

    assert expected_dir.is_dir()
    assert index_file.exists()
    assert not (tmp_path / "some_node_folder.md").exists()
    
    #technically unecessary, but confirms that this functions at the correct time
    export.clear_export_dir()
    assert not export.export_root.exists(), "export temp folder was not cleaned up!"