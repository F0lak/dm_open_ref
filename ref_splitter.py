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
  - cleans up the markdown for the following criteria:
   - fix links to other files
   - removes empty lines
  - writes the files to disk, mimicking the tree that the original reference uses
  
  After that, you're left with a big ol' tree of markdown files that you can do what you want with.
	
 (I'm a humble cook, not a programmer, so my apologies if the code isn't up to snuff!)
"""

def write_file(text, file_name):
	output_file = os.path.join(f'{file_name}')
	with open(output_file, 'w', encoding='utf-8') as file:
		file.write(text)
		print(f"New file: {output_file}")
  
def clean_empty_lines(text):
	lines = text.splitlines()
	non_empty_lines = [line for line in lines if line.strip()]
	text = "  \n".join(line + "  " for line in non_empty_lines)

	return text

def copytext(text, start_delimiter, end_delimiter, start_closer=""):
		start_index = text.find(start_delimiter)
		end_index = text.find(end_delimiter, start_index)
		start_index_close = text.find(start_closer, start_index, end_index)

		if start_index != -1 and end_index != -1:
			start_index += len(start_delimiter)
			if start_index_close != 0:
				start_index += start_index_close - start_index + 1
			text = text[start_index:end_index]
			return text

def set_title(text, extension):
		global stubs
		if extension == "html":
			text = copytext(text, "<h2", "</h2>", start_closer=">") or None
   
		elif extension == "md":
			text = lines = text.splitlines()[0]
			if text != None:
				slash_index = text.rfind("/")
				text = text[slash_index+1:len(text)-1]
			print(text)
   
	#	print("=-=-=-=-=-=")
		if text != None:
			text = text.replace("/","_")
			return text#[0:len(text)-1]
		else:
			return None

def clean_markdown_file(text):
		text = clean_empty_lines(text)
		text = fix_links(text)
		return text

def clean_filenames(text):
		text = text.replace(".", "DOT")
		text = text.replace(">", "RIGHT")
		text = text.replace("<", "LEFT")
		text = text.replace("*", "STAR")
		text = text.replace(":", "COLON")
		text = text.replace("|", "PIPE")
		text = text.replace("?", "QMARK")
		text = text.replace("{", "")
		text = text.replace("}", "")
		text = text.replace("toc", "")
		text = text.replace("toc=", "")
		text = text.replace("\"", "")
		text = text.replace(" =mouse", "")
		text = text.replace("/", "\\")
		text = text.replace("%", "PERCENT")

		return text

def fix_links(text):
	result = []
	i = 0
	while i < len(text):
		# Find the start of a link
		start_index = text.find('](#', i)
		if start_index == -1:
			# No more links found
			result.append(text[i:])
			break
		
		# Append text before the link
		result.append(text[i:start_index + 1])
		
		# Find the end of the path
		end_index = text.find(')', start_index)
		if end_index == -1:
			break
		
		# Extract the path
		path = text[start_index + len('](#'):end_index]
		new_link = f'({path})'
		if path in link_dict:
			new_link = f'({link_dict[path]})'
		
		# Append the new link
		result.append(new_link)
		
		# Move the index past this link
		i = end_index + 1
	
	return ''.join(result)
	
def clean_subdirectories(root_dir):
	for dir_path, dir_names, files in os.walk(root_dir, topdown = False):
		if dir_path != root_dir:
			clean_directory(dir_path)

def clean_directory(directory):
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

def make_dir(directory):
	if not os.path.exists(directory):
   		os.makedirs(directory, exist_ok=True)

def build_file_tree():
	for text in parts:
		
		html_title = set_title(text, "html")
		text = pypandoc.convert_text(text, "md", format="html")
		md_title = set_title(text, "md")
		if md_title != None and html_title != None:
			
			md_title = clean_filenames(md_title)
			html_title = clean_filenames(html_title)
	
			dirty_file_path = copytext(text, "[]{#/", "}") or "stubs"
	
			text = text.replace(dirty_file_path, html_title + ".md")
			clean_file_path = clean_filenames(dirty_file_path)
			full_dir = f"{output_directory}\\{clean_file_path}\\{html_title}"

			print("md: " + md_title)
			print(clean_file_path)
			pruned_file_path = ""
			slash_index = clean_file_path.rfind("\\")
			if slash_index != -1:
				pruned_file_path = clean_file_path[0:slash_index]
			else:
				pruned_file_path = clean_file_path
			print(pruned_file_path)
			print("fd: " + full_dir)

			#make_dir(full_dir)
			link_dict[dirty_file_path] = f"{pruned_file_path}\\{md_title}.md"
			pages.append(Page(f"{output_directory}\\{pruned_file_path}", f"{md_title}.md", text))

def make_files():
	for page in pages:
		page.write_to_file()
  
class Page:
    def __init__ (self, path, title, text): 
        self.title = title
        self.path = path
        self.text = text
    
    def write_to_file(self):
        make_dir(self.path)
        self.text = clean_markdown_file(self.text)
        write_file(self.text, f"{self.path}\\{self.title}")
        
        
if __name__ == "__main__":
	profiler = cProfile.Profile()
	profiler.enable()
    
	script_directory = os.path.dirname(os.path.abspath(__file__))
	input_file = os.path.join(script_directory, 'info.html')
	output_directory = os.path.join(script_directory, 'ref')

	if os.path.exists(output_directory):
		shutil.rmtree(output_directory)

	link_dict = {}
	pages = []

	text = ""
	with open(input_file, 'r', encoding='utf-8') as file:
		text = file.read()

	delimiter = "<hr>"
	parts = text.split(delimiter)
	stubs = 0

	print("Building file tree")
	build_file_tree()

	print("Making Files")
	make_files()

	#print("Cleaning Subdirs")
	#clean_subdirectories(output_directory)

	input("All done, press Enter to exit...")
 
	profiler.disable()
	profiler.dump_stats("profile.prof")
		