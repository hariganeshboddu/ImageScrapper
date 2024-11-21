**Pinterest Image Scraper**

This project is a Pinterest image scraper that uses Selenium and BeautifulSoup to search for images based on a user-provided query and download them to a specified directory.

**Requirements**

To install the required packages, run:

pip install -r requirements.txt

**Configuration**

The scraper uses a configuration file (config.ini) to store settings. Below is an example configuration:

```
[selenium]
driver_path = /path/to/chromedriver
scroll_count = 10
scroll_delay = 2

[directories]
download_dir = downloads
```

-driver_path: Path to the ChromeDriver executable.
-scroll_count: Number of times to scroll the page to load more images.
-scroll_delay: Delay (in seconds) between scrolls.
-download_dir: Directory where images will be saved.

**Usage**

Ensure you have the required packages installed.
Update the config.ini file with the appropriate settings.
Run the scraper script:

python scrapper.py

Enter the search query when prompted (e.g., "blonde man").

**Script Overview**

The main script (scrapper.py) performs the following steps:  

Loads configuration from config.ini.
Sets up the Selenium WebDriver.
Opens the Pinterest search URL based on the user-provided query.
Scrolls the page to load images.
Parses the page source with BeautifulSoup to extract image URLs.
Downloads the images to the specified directory.