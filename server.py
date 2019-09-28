"""
Install required modules:

pip install lxml
pip install requests
pip install flask
pip install waitress
pip install validators

or

pip install .
#############
Run

python server.py
"""
from waitress import serve
import page_parser  # module for parsing the app page and getting app info
from flask import Flask, request, render_template
import validators
import logging


app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    """ Index page"""
    return render_template("index.tpl")


@app.route("/get-app-info")
def get_app_info():
    """ App Info page
    All page parsing is done by using classes and methods
    from created page_parser module.
    Final result is rendered using
    html template templates/get_automation_stats.tpl.
    """
    url = request.args.get("appname")

    info_to_display = ""

    page = page_parser.Page()

    try:
        if not validators.url(url):
            info_to_display = f'URL {url} is not correct'
            logging.error(info_to_display)
        else:
            page.load(url)
    except (page_parser.ClientRequestError,
            page_parser.BaseConnectionError) as err:
        info_to_display = 'Error occured: ' + err.message
    else:
        # According to this schema the web page will be parsed
        parsing_schema = {
            "App's name":
                "//tr[@class='app-info__row'][position()=1]/td[position()=2]",
            "App's version":
                "//tr[@class='app-info__row'][position()=4]/td[position()=2]",
            "Number of downloads":
                "//tr[@class='app-info__row'][position()=3]/td[position()=2]",
            "Release date":
                "//tr[@class='app-info__row'][position()=5]/td[position()=2]",
            "App's description":
                "//p[@itemprop='description']"
        }
        # We will use xPathParser parser from page_parser
        parser = page_parser.xPathParser()

        page.parse_page(parser, parsing_schema)
        info = page.get_parsed_page()

        # Preparing app info for displaying
        for info_name, info_value in info.items():
            info_to_display += f'<b>{info_name}</b>: {info_value} <br />'
    finally:
        return render_template("get_automation_stats.tpl",
                               info=info_to_display)


serve(app, host="0.0.0.0", port=8080)
