# config.py

class Config:
    URL = "https://www.kikar.co.il/"
    BASE_URL = "https://www.kikar.co.il"
    HEADLESS = False
    MAX_CONCURRENT_REQUESTS = 5
    JSON_DIR = "json_files"
    IMAGE_DIR = "images"
    SCREENSHOT_DIR = "screenshots"
    IMAGE_SELECTOR = "img.MuiBox-root.css-8fjtk0"
    AUTOHR_INFO = (
        ".MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary."
        "MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-root.MuiButton-text."
        "MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.css-1mx6moy"
    )
    ARTICLE_CONTENT = ".article-content.MuiBox-root.css-1b737da"
    ARTICLE_DATE_OR_TIME = ".almoni-tzar.MuiBox-root.css-19f8y51"
    ALL_ARTICLE_HREFS = "a.text-decoration-none"

    
  
