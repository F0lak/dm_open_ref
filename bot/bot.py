# bot.py
import os
import discord
import requests
from github import Github, Auth
from discord.ext import commands
from dotenv import load_dotenv 
import difflib
import asyncio

load_dotenv()
DIS_TOKEN	= str(os.getenv("DISCORD_TOKEN"))
GIT_TOKEN	= str(os.getenv("GITHUB_TOKEN"))
CHANNEL_ID	= int(os.getenv("CHANNEL_ID"))
REPO		= str(os.getenv("REPO"))
RAW			= str(os.getenv("RAW"))

github = Github(auth = Auth.Token(GIT_TOKEN))

user = github.get_user()
repo = user.get_repo("dm_open_ref")
    
intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!o", intents = intents)

OVERRIDE_QUERIES = {
	'.' : 'ref/proc/..md',
	'#' : 'ref/DM/preprocessor/define.md',
	'!' : 'ref/operator/!.md',
	'?' : 'ref/operator/?.md',
	'/' : 'ref/operator/SLASH.md',
	'^' : 'ref/operator/^.md'
}

def ping_via_http(url) -> str:
	status = "NO_STATUS"
	try:
		response = requests.get(url, timeout=5)
		print(f"{response.status_code}")
		if response.status_code == 200:
			status = f"repo is reachable."
		else:
			status = f"repo returned status code: {response.status_code}"
	except requests.ConnectionError:
		status = f"repo is not reachable."
	except requests.Timeout:
		status = f"repo request timed out."

	print(status)

web_connection_status : str = ping_via_http(REPO)

@bot.event
async def on_ready():
    
    custom_activity = discord.Activity(
        type=discord.ActivityType.custom, 
        state="Lummox has me locked up!"
    )
    
    await bot.change_presence(status=discord.Status.online, activity=custom_activity)
    print(f"\n{bot.user} is online")
    await bot.sync_commands()
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        #await channel.send(f"open-ref Bot is now online and {web_connection_status}.\nI accept the following commands:{commands}")
        print(f"Active in main channel! ({CHANNEL_ID})")
    else:
        print(f"Could not find main channel ({CHANNEL_ID})")
        
class MyView(discord.ui.View):
    def __init__(self, ref_text = "", timeout_time=120):
        super().__init__(timeout = timeout_time)
        self.ref_text = ref_text
        
    @discord.ui.button(label="Click to View", style=discord.ButtonStyle.primary)
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(self.ref_text, ephemeral=True, embed=None)
        
        
def write_file(text, file_name) -> None:
	'''
		Writes a file to the disk
	'''
	output_file = os.path.join(f'{file_name}')
	with open(output_file, 'w', encoding='utf-8') as file:
		file.write(text)  
  
def clean_query(filename, replace_with=""):
    # Define illegal characters based on the operating system
    illegal_chars = '\\/*?:"<>|'
    
    # Build the cleaned filename by replacing illegal characters
    cleaned = ''.join(char if char not in illegal_chars else replace_with for char in filename)
    
    return cleaned

def special_characters(text) -> str: 
	'''
		Strips illegal characters from file names
		Also performs minor cleanup of the file name
	'''
	text = text.replace("#", "preprocessor/")
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
	text = text.replace("/ ", "SLASH ")
	text = text.replace("%", "PERCENT")
	text = text.replace("``` dm", "``` cs")
	return text

@bot.command(
    aliases=['penref'],
    brief="Displays a reference file",
    help="""Searches reference files on open-ref using your input.
    		It will first search file names and paths, and if no matches are found, it will search file contents.
       		It displays the best match to your search."""
    )

async def ref(ctx, *, query="DM"):
	print(query)
	query = special_characters(query)

	SEARCH_URL = "https://api.github.com/search/code"

	headers = {'Authorization': f'Token {GIT_TOKEN}'}
 
	if query in OVERRIDE_QUERIES:
		match = OVERRIDE_QUERIES[query]
	#	await ctx.send(f"Override Query: {query} : {match}")
		await ref_info(ctx, (get_page(match), f"{REPO}/{match}"))
		return

	filename_params = {'q': f'filename:{query} repo:F0lak/dm_open_ref path:ref', 'order': 'desc'}
	path_params = {'q': f'{query} in:path repo:F0lak/dm_open_ref path:ref', 'order': 'desc'}
	code_params = {'q': f'{query} in:file repo:F0lak/dm_open_ref path:ref', 'order': 'desc'}

	# we will fix you later
	#query = clean_query(query)
	content =  await search(ctx, query, SEARCH_URL, headers, filename_params)
	if content:
		await ref_info(ctx, content)
	else:
		print(f"No matches in files for {query} , searching paths")
		content = await search(ctx, query, SEARCH_URL, headers, path_params)
		if content:
			await ref_info(ctx, content)
		else:
			print(f"No matches in paths for {query}, searching content")
			content = await search(ctx, query, SEARCH_URL, headers, code_params)
			if content:
				await ref_info(ctx, content)
			else:
				await ctx.send(f"Could not find anything for: {query} :disappointed_relieved:")

async def search(ctx, query, url, header, params):
	response = requests.get(url, headers=header, params=params)

	if response.status_code == 200:
		search_results = response.json()
	#	write_file(str(search_results), "search_results.json")
		print(f"Query = {query}")
		if 'items' in search_results and len(search_results['items']) > 0:
			unsorted_items = []
			for item in search_results['items']:
				unsorted_items.append(item['path'])
    
			print(f"Pre-Sort:\n{[unsorted_items]}")

			if len(unsorted_items) > 0:
				match = unsorted_items[0]

				sorted_items = difflib.get_close_matches(query, [item for item in unsorted_items], n = len(unsorted_items), cutoff = 0.5)
    
				if len(sorted_items) > 0:
					match = sorted_items[0]
		
					print(f"Sorted:\n{[sorted_items]}")

				page = get_page(match)
				lines = page.splitlines()
				title = lines[0]
				lines.remove(lines[0])
				page = "\n".join(line + "" for line in lines)

				return page, title, f"{REPO}/{match}"
	else:
		print(f"Error: {response.status_code}")

	return None

async def ref_info(ctx, content):
		ref_content = content[0]
		ref_title = content[1]
		ref_link = content[2]
		timeout = 300
		ref_view = MyView(ref_content, timeout)
		bot_message = await ctx.send(embed=prettify(ref_content, ref_title, ref_link), view=ref_view)
  
		await asyncio.sleep(timeout)
		await bot_message.edit(view=None)
  
def prettify(content, page_title, link):
    
    content = content[0:4000] + ("..." if len(content) > 4000 else "")
    page_title = page_title.replace("#","")
    page_title = page_title.replace("\\","")
    embed = discord.Embed(
        title= "🔗 " + page_title,
        url=link,
        #description=cleanup_output(content),
        color=discord.Color.orange()  # Set color of the embed
    )
    #embed.add_field(name="", value = link, inline = False)
    embed.set_footer(text="BYOND Version 516.1644")
    
    return embed
	# use: send(embed = prettify(content))
    
def get_page(item):
	markdown_response = requests.get(f"{RAW}/{item}")
	markdown_content = markdown_response.text

	if len(markdown_content) > 1900:
		markdown_content = markdown_content[0:1900] + f"...\n\n*Character limit reached, check out the full page on Github* "

	return cleanup_output(markdown_content)

def fix_links(text) -> str:
	'''
		Fixes the links on the page to align with the file tree
	'''
	result = []
	i = 0
	while i < len(text):
		start_marker = "](/"
		start_index = text.find(start_marker, i)
		if start_index == -1:
			result.append(text[i+1:])
			break
		result.append(text[i:start_index])
		end_index = text.find(")", start_index)
		if end_index == -1:
			break
		path = text[start_index + len(start_marker):end_index]
		new_link = f"]"
		result.append(new_link)
		
		i = end_index + 1
	return ''.join(result)

def cleanup_output(text):
    text = text.replace("######","")
    text = text.replace("<!-- -->","")
    text = text.replace("> [!TIP]", "")
    text = text.replace("+  ", "-  ")
    text = fix_links(text)
    
    text = text[0:text.find("> **See also:**")]
    
    return text

bot.run(DIS_TOKEN) # run the bot with the token
