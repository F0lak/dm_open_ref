'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from src.ref_splitter import RefEntry, TOKEN_TABLE
import pathlib


class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry
    
    def __init__(self, entry, id: int) -> None:
        self.entry = entry
        self.id = id

class RefTree:
    '''manages the tree of reference nodes
    and supports exporting files in various formats'''
    _instance = None
    
    export_path: str

    nodes: list[RefNode] = []
    links: dict[str, str]
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            raise ValueError("RefTree Singleton already created")
        return cls._instance
    
    def __init__(self) -> None:
        print("RefTree created")
        
    def set_export_path(self, exp_path: str) -> None:
        export_path = exp_path
        
    def build_tree_from_entries(self, entries: list[RefEntry]) -> None:
        for entry in entries:
            new_node = self.create_node(entry)
            self.append(new_node)
            
        print(f"RefTree built with {len(self.nodes)} nodes")
            
    def append(self, node: RefNode) -> None:
        self.nodes.append(node)
    
    def create_node(self, entry: RefEntry) -> RefNode:
        new_node = RefNode(entry, len(self.nodes))
        return new_node
    
    def clean_filepath(self, text: str) -> str:
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

    def export_markdown(self) -> None:
        for node in self.nodes:
            clean_ref_id = node.entry.ref_id.lstrip("\\/")
            clean_filepath = self.clean_filepath(clean_ref_id)
            
            export_file = pathlib.Path("_md_export") / "ref" / f"{clean_filepath}.md"
            print(f"Writing {export_file}")
            export_file.parent.mkdir(parents=True, exist_ok=True)
            
            md_content: str = f'##{node.entry.title}\n\n'
            
            # We'll end up swapping this out for a properly referenced group of variables
            top_desc_keys = ["Format:", "Args:", "Default action:"]
            top_desc_lists: dict[str, list[str]] = {
                k: node.entry.desc_lists.pop(k) 
                for k in top_desc_keys 
                if k in node.entry.desc_lists
            }

            see_also_list = node.entry.desc_lists.pop("See also:", None)
            
            for desc in top_desc_lists:
                md_content += f'**{desc}**\n'
                for n in top_desc_lists[desc]:
                    md_content += f'+   {n}\n'
                md_content += '\n'
            md_content += '\n'
            
            for p in node.entry.content:
                md_content += p+'\n\n'
            
            # reformat this into a parsed inline list.  no need to extract it I think
            for desc in node.entry.desc_lists:
                md_content += f'**{desc}**\n'
                for n in node.entry.desc_lists[desc]:
                    md_content += f'+   {n}\n'
                md_content += '\n'
            md_content += '\n'
            
            if see_also_list:
                md_content += "**See also:**\n"
                for n in see_also_list:
                    md_content += f'+   {n}\n'
                md_content += '\n\n'
            
            for row in TOKEN_TABLE:
                token = row["TOKEN"]
                tag = row["md"]
                md_content = md_content.replace(f"[{token}] ", f"{tag}")
                md_content = md_content.replace(f" [/{token}]", f"{tag}")
                
            md_content = self.format_md_links(md_content)
            
            #print("Markdown File Created:")
            #print(md_content)
            with open(export_file, "w", encoding="utf-8") as file:
                file.write(md_content)
                
    def format_md_links(self, text: str) -> str:
        start_token = "[LINK]"
        end_token = "[/LINK]"
        
        while True:
            start_idx = text.find(start_token)
            if start_idx == -1:
                break
                
            end_idx = text.find(end_token, start_idx)
            if end_idx == -1:
                raise ValueError("Malformed link")
                
            path_start = start_idx + len(start_token)
            link_path = text[path_start:end_idx]
            
            link_text = self.links.get(link_path, link_path)
            
            markdown_link = f"[{link_text}]({link_path})"
            text = text[:start_idx] + markdown_link + text[end_idx + len(end_token):]
            
        return text