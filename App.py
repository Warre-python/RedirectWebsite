from flask import Flask, jsonify, request, render_template, redirect

# Initial redirect target
url = "https://www.google.com"

app = Flask(__name__)
#Hello

@app.route('/')
def home():
    # Redirect to the current target URL
    return redirect(url)


@app.route('/changeurl', methods=['GET', 'POST'])
def change_url():
    """Render a small form (GET) and accept form submissions (POST).

    The form in `templates/ChangeUrl.html` posts `new_url`. On POST we
    normalize the URL (add http:// if missing) and update the module-level
    `url` variable so subsequent visits to `/` redirect to the new target.
    """
    global url
    message = None

    if request.method == 'POST':
        data = request.form
        new_url = (data.get('new_url') or '').strip()
        if new_url:
            # Normalize basic input: ensure scheme is present so Flask redirect works
            if not new_url.startswith(('http://', 'https://')):
                new_url = 'http://' + new_url
            url = new_url
            message = f'URL updated to {url}'

    # Render the template. The template file in the repo is `ChangeUrl.html`.
    return render_template('ChangeUrl.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
