from flask import Flask, render_template, request
from markupsafe import escape
from googleAPI import get_webtags
from reddit import parse
from buddy import summarize_user_advice, create_html_links
from format import formatter

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index2.html')


@app.route("/test")
def test_route():
    return "<p> This was a tag using htmx</p>"

@app.route("/loading")
def load_progress():
    return render_template('loading.html')


@app.route("/query", methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query = escape(request.form['search'])
        num_of_pages = escape(request.form['numberValue'])
        print(num_of_pages)
        print(query)
        webtags = get_webtags(query, num_of_pages)
        #print(webtags)
        urls = []
        count = 0
        for tag in webtags:
            if(count < int(num_of_pages)):
                urls.append(tag["link"])
                count += 1
        print(urls)

        ret_post = parse(urls, 1)

        output_string = formatter(ret_post, query)
        summed_text = summarize_user_advice(output_string)
        text = create_html_links(summed_text, ret_post)
        return render_template("results.html", text=text, posts=ret_post)