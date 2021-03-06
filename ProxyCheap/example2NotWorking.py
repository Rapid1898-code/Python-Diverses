# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os,sys

# PROXY = "21.65.32.65:3124"
# PROXY = "34.88.40.44:3128"
# path = os.path.abspath (os.path.dirname (sys.argv[0]))
# cd = '/chromedriver.exe'

# options = Options()
# print(f"Try to access with Proxy {PROXY}...")
# options.add_argument(f"--proxy-server={PROXY}")
# driver = webdriver.Chrome (path + cd, options=options)
# driver.get("https://whatismyipaddress.com")

from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv()) 
PROXY_CHEAP_USER = os.environ.get("PROXY_CHEAP_USER")
PROXY_CHEAP_PW= os.environ.get("PROXY_CHEAP_PW")



url = f"http://{PROXY_CHEAP_USER}:{PROXY_CHEAP_PW}@proxy.proxy-cheap.com:31112 https://ifconfig.co/json"
data = requests.get(url).json
print(data)
exit()


import os
import zipfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_HOST = 'proxy.proxy-cheap.com'  # rotating proxy or host
PROXY_PORT = 31112 # port
PROXY_USER = PROXY_CHEAP_USER # username
PROXY_PASS = PROXY_CHEAP_PW # password

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.Options()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options)
    return driver

def main():
    driver = get_chromedriver(use_proxy=True)
    #driver.get('https://www.google.com/search?q=my+ip+address')
    driver.get('https://httpbin.org/ip')

if __name__ == '__main__':
    main()