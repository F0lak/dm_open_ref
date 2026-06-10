
import pathlib
from .ref_tree import RefTree
from .token_table import INLINE_TOKEN_TABLE, P_CLASS_TOKEN_TABLE
from enum import Enum
import logging
from tqdm import tqdm
import shutil

logger = logging.getLogger(__name__)

class MDFlavour(Enum):
    NOTE = "NOTE"
    TIP = "TIP"
    IMPORTANT = "IMPORTANT"
    WARNING = "WARNING"
    CAUTION = "CAUTION"
    
class MDPage:
    def __init__(self, ref_id: str, content: str, is_index: bool):
        self.id = ref_id
        self.content = content
        self.is_index = is_index

class ExportMD:
    '''Exports the RefTree into a collection of md files'''
    
    export_root: pathlib.Path
    export_format: str = "md"
    
    def __init__(self, exp_path: pathlib.Path | str) -> None:
        self.export_root = pathlib.Path(exp_path)
        self.prepared_pages: list[MDPage] = []
    
    def clean_filepath(self, text: str) -> str:
        '''removes invalid characters from filepaths'''
        text = text.replace("%2e", ".")
        text = text.replace("%3e", ">")
        text = text.replace("%3c", "<")
        text = text.replace("%3f", "?")
        text = text.replace("%25", "%")
        text = text.replace(">", "RIGHT")
        text = text.replace("<", "LEFT")
        text = text.replace("*", "STAR")
        text = text.replace(":", "COLON")
        text = text.replace("|", "PIPE")
        text = text.replace("?", "QMARK")
        text = text.replace("{", "")
        text = text.replace("}", "")
        text = text.replace("toc", "")
        text = text.replace("\"", "")
        text = text.replace("/", "\\")
        text = text.replace("%", "PERCENT")
        return text
    
    def format_tree(self, tree: RefTree) -> None:
        '''exports all of the pages that the reftree contains'''
        
        for node in tqdm(tree.nodes, desc="Processing Pages", bar_format="{l_bar}{r_bar}"):
            
            meta_header: str = "" # the content of the header metadata.  This will be assigned based on the GithubPages framework
            content: str = "" # the content of the markdown file
            
            # Compile page content
            source_content: str = self.format_source_content(node.entry.content)
            
            proc_format: str = self.format_string_list(node.entry.format, "Format")
            returns: str = self.format_string_list(node.entry.returns, "Returns")
            args: str = self.format_string_list(node.entry.args, "Arguments")
            called_when: str = self.format_string_list(node.entry.when, "Called When")
            default_action: str = self.format_string_list(node.entry.default_action, "Default Action")
            default_value: str = self.format_string_list(node.entry.default_value, "Default Value")
            related_pages: str = self.format_string_list(node.entry.see_also, "Related Pages")
            
            # build and format page content
            content += meta_header + '\n'
            content += f'## {node.entry.title} ({node.entry.entry_type})\n'
            content += proc_format
            content += args
            content += returns
            content += called_when
            content += default_action
            content += default_value
            content += "***"
            content += source_content
            content += "***"
            content += related_pages
            content = self.format_tokens(content)
            content = self.format_codeblocks(content)
            content = self.format_links(tree.links, content)
            
            self.prepared_pages.append(MDPage(node.entry.ref_id, content, node.is_index))
    
    def format_string_list(self, str_list: list[str], header: str) -> str:
        '''parses a list of strings from the RefEntry
        uses <header> as the header, if specified
        returns an empty string is str_list is empty'''
        parsed: str = ""
        if len(str_list) > 0:
            if header == "":
                raise ValueError("Header cannot be an empty string")
            parsed += f'\n**{header}:**'
            for l in str_list:
                parsed += f'\n+   {l}'
            parsed += '\n'
        return parsed
    
    def format_source_content(self, content: list[str]) -> str:
        '''parses the content list into a string of paragraphs
        returns an empty string is content is empty'''
        parsed = ""
        if len(content) > 0:
            for p in content:
                parsed += '\n'+p+'\n'
        return parsed
    
    def season_string(self, content: str, flavour: MDFlavour) -> str:
        '''
        seasons a string with a markdown alert
        to season a list, format it to a string first using format_string_list
        '''
        seasoned: str = f'\n> [!{flavour.value}]'
        seasoned += content.replace('\n', '\n> ')
        return seasoned
        
    def format_tokens(self, content: str) -> str:
        '''replaces tokens with their markdown counterparts from the TOKEN_TABLE'''
        for row in INLINE_TOKEN_TABLE:
            token = row["TOKEN"]
            tag = row["md"]
            # removes whitespace added during parsing.  This can be removed when that is fixed
            content = content.replace(f"[{token}] ", f"{tag}")
            content = content.replace(f" [/{token}]", f"{tag}")
            # once we've cleared the spaced out tokens, we can clear out non-spaced tokens
            content = content.replace(f"[{token}]", f"{tag}")
            content = content.replace(f"[/{token}]", f"{tag}")
            
        for row in P_CLASS_TOKEN_TABLE:
            token = row["TOKEN"]
            tag = row["md"]
            
            start_token = f'[{token}]'
            end_token = f'[/{token}]'
            
            while True:
                start_idx = content.find(start_token)
                if start_idx == -1:
                    break
                    
                end_idx = content.find(end_token, start_idx)
                if end_idx == -1:
                    raise ValueError(f'p class token ({token}) at index {start_idx} does not close')
                    
                paragraph_start = start_idx + len(start_token)
                format_content = '\n' + content[paragraph_start:end_idx]
                seasoned_paragraph = self.season_string(format_content, MDFlavour(tag))
                
                content = content[:start_idx] + seasoned_paragraph + content[end_idx + len(end_token):]
                
        return content
    
    def format_codeblocks(self, content: str) -> str:
        '''converts codeblock tokens into markdown codeblocks with the dm annotation'''
        content = content.replace("[CODEBLOCK]", "\n```dm\n")
        content = content.replace("[/CODEBLOCK]", "\n```\n")
        return content
                
    def format_links(self, tree_links: dict[str, str], text: str) -> str:
        '''replaces link tokens with their proper markdown links provided by the RefTree's link LUT'''
        start_token = "[LINK]"
        end_token = "[/LINK]"
        
        while True:
            start_idx = text.find(start_token)
            if start_idx == -1:
                break
                
            end_idx = text.find(end_token, start_idx)
            if end_idx == -1:
                    raise ValueError(f'Link token ({start_token}) at index {start_idx} does not close')
                
            path_start = start_idx + len(start_token)
            link_path = text[path_start:end_idx]
            
            link_text = tree_links.get(link_path, link_path)
            
            ## adding a space because links don't respect whitespace for some reason.
            ##TODO: look into why
            markdown_link = f" [{link_text}](/ref{link_path})"
            text = text[:start_idx] + markdown_link + text[end_idx + len(end_token):]
            
        return text
    
    def clear_export_dir(self) -> None:
        '''Wipes the export root folder before writing fresh'''
        target_dir = self.export_root
        
        if target_dir.exists():
            logger.info(f"Clearing export directory: {target_dir}")
            shutil.rmtree(target_dir)
        
    def export_pages(self):
        '''exports all of the prepared pages to disk'''
        if len(self.prepared_pages) == 0:
            raise ValueError("Cannot export pages: No pages prepared.")
        
        self.export_root.mkdir(parents=True, exist_ok=True)
        
        current_page = None
        try:
            for page in tqdm(self.prepared_pages, desc="Writing Pages", bar_format="{l_bar}{r_bar}"):
                current_page = page
                self.export_page(page)
        except Exception as e:
            self.clear_export_dir()
            page_info = f" (Page ID: {current_page.id})" if current_page else ""
            raise RuntimeError(f'Export Aborted{page_info}, temp folder has been cleared.\nError: {e}') from e
    
    def export_page(self, page: MDPage):
        '''exports the page content to a markdown file'''
        clean_ref_id = page.id.lstrip("\\/")
        clean_filepath = self.clean_filepath(clean_ref_id)
        
        if page.is_index:
            export_file = self.export_root / "ref" / clean_filepath / "index.md"
        else:
            export_file = self.export_root / "ref" / f"{clean_filepath}.md"
            
        #logger.info(f"Writing {export_file}")
        export_file.parent.mkdir(parents=True, exist_ok=True)
        with open(export_file, "w", encoding="utf-8") as file:
            file.write(page.content)
            
    def move_to_main_folder(self):
        '''Safely replaces the repo's main ref folder.
        If this fails, the old ref is reinstated'''
        repo_ref_dir = pathlib.Path("./ref").resolve()
        temp_ref_dir = (self.export_root / "ref").resolve()
        backup_ref_dir = pathlib.Path("./ref_backup_twp").resolve()

        if not temp_ref_dir.exists():
            raise FileNotFoundError(f"Source temp directory not found at {temp_ref_dir}")
        if repo_ref_dir.exists():
            shutil.move(str(repo_ref_dir), str(backup_ref_dir))

        try:
            shutil.move(str(temp_ref_dir), str(repo_ref_dir))
            if backup_ref_dir.exists():
                shutil.rmtree(backup_ref_dir)
                
        except Exception as e:
            if backup_ref_dir.exists():
                if repo_ref_dir.exists():
                    shutil.rmtree(repo_ref_dir)
                shutil.move(str(backup_ref_dir), str(repo_ref_dir))
            
            raise RuntimeError(f"Something went terribly wrong moving the folders.  Rollin' back.\nError: {e}") from e