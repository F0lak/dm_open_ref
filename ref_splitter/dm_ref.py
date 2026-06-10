'''
Data Class to fetch the DM Reference from the BYOND web server
loads the file into into a DMRef object,
which can then be passed to the RefSplitter class for processing
'''

from dataclasses import dataclass
import requests

@dataclass
class DMRef:
    '''Grabs and stores info.html from the byond webserver'''

    dm_ref_url: str = "https://www.byond.com/docs/ref/info.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    timeout_seconds: int = 10
    timeout_error_message = "Timeout exceeds maximum value (10 seconds)"

    ref_info: str = ""

    def __post_init__(self) -> None:
        if self.timeout_seconds > 10:
            raise ValueError(self.timeout_error_message)

    def fetch_web_ref(self) -> str:
        '''
        Attempts to fetch the reference from the BYOND webserver
        
        Raises:
            requests.RequestException if the network request fails or times out
        '''
        response = requests.get(self.dm_ref_url, headers=self.headers, timeout=self.timeout_seconds)
        response.raise_for_status()
        self.ref_info = response.text
        return self.ref_info
