import os
import shutil
import pypandoc
import cProfile

"""
 DM Reference Defucker 2000, by F0lak.
 
 Here's my little script for splitting the DM Reference into markdown files
 
 HOW TO USE:
  All that you need to do is run the script
  
 HOW IT WORKS:
  The script finds info.dm in the same folder as this script
  First it splits the html file into a list of strings using horizontal rules (<hr>) as the delimiter
  It loops through all of the strings and does the following:
  - parses the file names and relative paths from the string
  - cleans up the file path and file names to prep for writing to disk
  - reformats the strings from html to markdown
  - cleans up the markdown for display on github.com
  - writes the files to disk, mimicking the tree that the original reference uses
  
  After that, you're left with a big ol' tree of files that you can do what you want with.
	
 (I'm a humble cook, not a programmer, so my apologies if the code isn't up to snuff!)
"""

BUILD_HTML : bool = False
BUILD_FILE_TREE : bool = False
SOURCE_FILE : str = "info.html"

'''
	Directory Stuff
'''

def make_files() -> None:
	'''
		Converts a Page object into a file on disk and index it if BUILD_HTML is enabled
	'''
	for page in pages:
		page.write_to_file()

	if BUILD_HTML:
		write_file(index, f"{script_directory}\\index.html")

def write_file(text, file_name) -> None:
	'''
		Writes a file to the disk
	'''
	output_file = os.path.join(f'{file_name}')
	with open(output_file, 'w', encoding='utf-8') as file:
		file.write(text)  
  
def clean_file(file_name) -> None:
	'''
		Checks if a file exists and runs a markdown cleanup on it
	'''
	if os.path.exists(file_name):
		with open(file_name, "r+", encoding = "utf-8") as file:
			file_text = file.read()
			file_text = clean_markdown_file(file_text)
			file.seek(0)
			file.write(file_text)
			file.truncate()
   
def clean_subdirectories(root_dir) -> None:
	'''
		Organizes the file and folder tree to mimic the BYOND reference
	'''
	for dir_path, dir_names, files in os.walk(root_dir, topdown = False):
		if dir_path != root_dir:
			clean_directory(dir_path)

def clean_directory(directory) -> None:
	'''
		Checks if a file is the only one in a folder, if so, moves it up and deletes the folder
	'''
	items = os.listdir(directory)
	files = [file for file in items if os.path.exists(os.path.join(directory, file))]
	
	if len(files) == 1:
		file_to_move = os.path.join(directory, files[0])
		parent_dir = os.path.dirname(directory)
		shutil.move(file_to_move, parent_dir)
		
		if not os.listdir(directory):
			os.rmdir(directory)
	
	elif len(files) == 0:
		os.rmdir(directory)

def make_dir(directory) -> None:
	'''
		Makes a new directory on the disk
	'''
	if not os.path.exists(directory):
		try:
			os.makedirs(directory, exist_ok=True)
		except:
			Exception(f"Invalid Path: Could not write {directory}")

def build_file_tree() -> None:
	'''
		Converts the reference to markdown and separates the pages into separate files
		if BUILD_HTML is enabled it will also create html pages, which are written to a different folder
	'''
	print("Building file tree")
	for html_text in parts:
		
		html_title: str = set_title(html_text, "html")
		md_text = pypandoc.convert_text(prep_html_file(html_text), "md", format="html")
		md_title: str = set_title(md_text, "md")
		if md_title != None and html_title != None:
			
			md_title = clean_filenames(md_title)
			html_title = clean_filenames(html_title)
	
			dirty_file_path: str = copytext(md_text, "[]{#/", "}")
	
			clean_file_path: str = clean_filenames(dirty_file_path)

			pruned_file_path: str = ""
			slash_index = clean_file_path.rfind("\\")
			if slash_index != -1:
				pruned_file_path = clean_file_path[0:slash_index]
			else:
				pruned_file_path = clean_file_path
			print(f"{clean_file_path}\\{md_title}")

			link_dict[f"{dirty_file_path}/{md_title}"] = f"{pruned_file_path}\\{md_title}.md"
			pages.append(Page(f"{markdown_directory}\\{pruned_file_path}", f"{md_title}", "md", "THIS IS NEW" + md_text))
			
			if BUILD_HTML == True:
				pages.append(Page(f"{html_directory}\\html\\{pruned_file_path}", f"{md_title}", "html", html_text))

				global index
				index += f"<a href = \"html\\{pruned_file_path}\\{md_title}.html\">{md_title}</a></ br>\n"
 
def clean_markdown_files() -> list:
	'''
		Cleans up the formatting on every markdown file.
		* Does not overwrite data
	'''
	for root, dirs, files in os.walk(markdown_directory):
		for file in files:
			print(file)
			if file.endswith(".md"):
				full_path = os.path.join(root, file)
				clean_file(full_path)

'''
	File Cleanup
'''

def copytext(text, start_delimiter, end_delimiter, start_closer="") -> str:
	'''
		Returns the text found between two delimiters
	'''
	start_index = text.find(start_delimiter)
	end_index = text.find(end_delimiter, start_index)
	start_index_close = text.find(start_closer, start_index, end_index)

	if start_index != -1 and end_index != -1:
		start_index += len(start_delimiter)
		if start_index_close != 0:
			start_index += start_index_close - start_index + 1
		text = text[start_index:end_index]
		return text
	else:
		return ""
 
def set_title(text, extension) -> str | None:
	'''
		Sets the title of the file, based on the extension, using some data in the file to generate the filename
	'''
	if extension == "html":
		text = copytext(text, "<h2", "</h2>", start_closer=">") or None

	elif extension == "md":
		text = lines = text.splitlines()[0]
		if text != None:
			slash_index = text.rfind("/")
			text = text[slash_index+1:len(text)-1]
		# print(text)

#	print("=-=-=-=-=-=")
	if text != None:
		text = text.replace("/","_")
		return text#[0:len(text)-1]
	else:
		return None

def clean_filenames(text) -> str: 
	'''
		Strips illegal characters from file names
		Also performs minor cleanup of the file name
	'''
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

	if text.find("operator") == -1:
		start_marker = " ="
		start_index = text.find(start_marker)
		if start_index != -1:
			end_index = text.find("(", start_index)
			if end_index == -1:
				end_index = len(text)
			else:
				start_index += 1
			text = text.replace(text[start_index:end_index], "")

	return text
   
def clean_markdown_file(text) -> str:
	'''
		Cleans up and finalizes the formatting of markdown files
	'''
	text = clean_empty_lines(text)
	text = fix_links(text)
	text = clean_version(text)
	text = clean_inline_code(text)
	text = text.replace("\n: ", "\n+ ")
	text = text.replace("PARAGRAPH", "\n\n")
	text = text.replace("CODE_TICKS_DM", "\n``` dm\n")
	text = text.replace("CODE_TICKS", "\n```\n")
	text = text.replace("NOTE", "\n> [!NOTE]\n> ")
	text = text.replace(" .code}", "")
	text = text.replace("{.code}", "")
	text = move_see_also(text)
	return text
  
def clean_empty_lines(text) -> str:
	'''
		Removes empty lines
	'''
	lines = text.splitlines()
	lines.remove(lines[0])
	non_empty_lines = [line for line in lines if line.strip()]
	text = "\n".join(line + "" for line in non_empty_lines)

	return text

def fix_links(text) -> str:
	'''
		Fixes the links on the page to align with the file tree
	'''
	result = []
	i = 0
	while i < len(text):
		start_marker = "](#/"
		start_index = text.find(start_marker, i)
		if start_index == -1:
			result.append(text[i+1:])
			break
		result.append(text[i:start_index])
		end_index = text.find(")", start_index)
		if end_index == -1:
			break
		path = text[start_index + len(start_marker):end_index]
		new_link = f"{path}"
		if f"/{path}" in link_dict:
			new_link = f"](/ref{link_dict[path]}.md)"
		else:
			new_link = f"](/ref/{path}.md) "
		result.append(new_link)
		
		i = end_index + 1
	
	return ''.join(result)

def clean_version(text) -> str:
	'''
		Checks for BYOND version tags and converts them to a markdown-friendly format
	'''
	version_index = text.find("byondver=")
	if version_index:
		start_index = text[0:version_index].rfind("{#")
		end_index = text.find("\"}")

		if start_index != -1 and end_index != -1:
			version: str = text[version_index+10:end_index]
			version = f"\n###### BYOND Version {version}"

			text = text.replace(text[start_index:end_index+2], version)

	return text

def clean_inline_code(text) -> str:
	'''
		Cleans up inline code
	'''
	fixed_text = ""
	i = 0
	while i < len(text):
		if text[i] == '[':
			close_bracket_index = text.find(']', i)
			if close_bracket_index != -1:
				path = text[i+1:close_bracket_index]
				if text[close_bracket_index+1:close_bracket_index+2] == '(':
					close_paren_index = text.find(')', close_bracket_index)
					code_index = close_paren_index + 1
					
					if text[code_index:code_index+7] == '{.code}':
						link_name = text[close_bracket_index+2:close_paren_index]
						fixed_text += f'[`{path}`]({link_name})'
						i = code_index + 7
						continue
		fixed_text += text[i]
		i += 1

	return fixed_text

def move_see_also(text) -> str:
	'''
		Moves the "See Also" section to the bottom of the file
	'''
	start = "**See also:**"
	start_index = text.find(start)
	i = start_index
	end_index = None
	while i < len(text):
		if text[i] == "\n":
			if text[i:i+3] != "\n+ ":
				end_index = i
				break
		i = i + 1
	if end_index:
		replacement_text = text[start_index:end_index]
		tiptext = replacement_text.replace("\n", "\n> ")
		if replacement_text:
			text = text.replace(replacement_text, "") + f"\n\n> [!TIP] \n> {tiptext}"
  
	return text
        
def prep_html_file(text) -> str:
	'''
		Preps an html file for conversion to markdown by converting tags that would otherwise be
  		stripped into tokens that will not be removed during conversion
	'''
	text = text.replace("<p>", "PARAGRAPH")
	text = text.replace("<xmp>", "CODE_TICKS_DM")
	text = text.replace("</xmp>", "CODE_TICKS")
	text = text.replace("<p class=note>", "NOTE")
	return text
  
class Page:
	'''
		Page object that represents a new file to be written to disk
	'''
	def __init__ (self, path, title, extension, text): 
		self.title: str = title
		self.path: str = path
		self.text: str = text
		self.extension = extension

	def write_to_file(self) -> None:
		make_dir(self.path)
		if self.extension == "md":
			self.text = clean_markdown_file(self.text)
		write_file(self.text, f"{self.path}\\{self.title}.{self.extension}")

	def add_to_index(self) -> None:
		global index
		index += f"<a href = \"f\"{self.path}\\{self.title}.{self.extension}\"{self.title}</a></ br>\n"
        
if __name__ == "__main__":
	profiler = cProfile.Profile()
	profiler.enable()
    
	script_directory = os.path.dirname(os.path.abspath(__file__))
	input_file = os.path.join(script_directory, SOURCE_FILE)
	markdown_directory = os.path.join(script_directory) + "\\ref"
	html_directory = os.path.join(script_directory) + "\\html"

	if BUILD_FILE_TREE:
		if os.path.exists(markdown_directory):
			shutil.rmtree(markdown_directory)
		if os.path.exists(html_directory):
			shutil.rmtree(html_directory)

		link_dict	: dict = {}
		pages	: list = []
		index	: str = ""
	
		if os.path.exists("index.html"):
			os.remove("index.html")

		text: str = ""
		with open(input_file, 'r', encoding='utf-8') as file:
			text = file.read()

		delimiter: str = "<hr>"
		parts = text.split(delimiter)

		build_file_tree()

		make_files()
  
	else:
		clean_markdown_files()

	print("All done")
 
	profiler.disable()
	profiler.dump_stats("profile.prof")
		