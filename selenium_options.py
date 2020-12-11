from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument('--disable-gpu')  # Last I checked this was necessary.
CHROME_OPTIONS.add_argument('--disable-notifications')
prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
CHROME_OPTIONS.add_experimental_option('prefs', prefs)
CHROME_OPTIONS.add_argument('--ignore-certificate-errors')
CHROME_OPTIONS.add_argument("--test-type")
CHROME_OPTIONS.add_argument('--disable-infobars')
CHROME_OPTIONS.add_argument('--disable-extensions')
CHROME_OPTIONS.add_argument('--profile-directory=Default')
CHROME_OPTIONS.add_argument('--incognito')
CHROME_OPTIONS.add_argument('--disable-plugins-discovery')
CHROME_OPTIONS.add_argument('--start-maximized')

########### Additional options #########################################################################################

def build_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    # chrome configuration
    # More: https://github.com/SeleniumHQ/docker-selenium/issues/89
    # And: https://github.com/SeleniumHQ/docker-selenium/issues/87
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-impl-side-painting")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-seccomp-filter-sandbox")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-cast")
    chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
    chrome_options.add_argument("--disable-cloud-import")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-ipv6")
    chrome_options.add_argument("--allow-http-screen-capture")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

    return chrome_options