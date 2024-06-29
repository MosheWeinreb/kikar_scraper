

class Config:
    URL = "https://www.kikar.co.il/"
    BASE_URL = "https://www.kikar.co.il"
    HEADLESS = False
    MAX_CONCURRENT_REQUESTS = 11
    JSON_DIR = "json_files"
    IMAGE_DIR = "images"
    SCREENSHOT_DIR = "screenshots"
    IMAGE_SELECTOR = "img.MuiBox-root.css-8fjtk0"
    
    ARTICLE_CONTENT = ".article-content.MuiBox-root.css-1b737da"
    AUTOHR_INFO = (".MuiButtonBase-root.css-1mx6moy" )
    ARTICLE_DATE_OR_TIME = ".almoni-tzar.MuiBox-root.css-19f8y51"
    ALL_ARTICLE_HREFS = "a.text-decoration-none"
    
    def __init__(self):
        print(f"Loaded Config: {self.__dict__}")
 

    
  
