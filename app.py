# ============================================================
# app.py — Main Flask application for the URL Shortener
# ============================================================
# This file sets up the Flask web server, handles routes, and
# stores URL mappings in a simple Python dictionary.
# ============================================================

import random           # Used to pick random characters for the short code
import string           # Provides letters and digits for the short code
import re               # Used to validate the custom alias pattern
from flask import Flask, render_template, request, redirect, url_for

# ── Create the Flask app instance ──────────────────────────
app = Flask(__name__)

# ── In-memory store: { short_code: original_url } ──────────
# No database is used — data resets every time the server restarts.
url_map = {}


def generate_short_code(length=6):
    """Generate a random 6-character code using letters and digits."""
    characters = string.ascii_letters + string.digits   # a-z A-Z 0-9
    code = ''.join(random.choices(characters, k=length))
    return code


# Allowed pattern for custom aliases: letters, digits, hyphens, underscores
_ALIAS_PATTERN = re.compile(r'^[A-Za-z0-9_-]+$')

def validate_alias(alias):
    """
    Check whether a custom alias string is acceptable.

    Returns (True, None) when valid.
    Returns (False, error_message) when invalid.
    """
    if len(alias) < 2:
        return False, "Custom alias must be at least 2 characters long."
    if len(alias) > 50:
        return False, "Custom alias must be 50 characters or fewer."
    if not _ALIAS_PATTERN.match(alias):
        return False, (
            "Custom alias can only contain letters (A–Z, a–z), "
            "numbers (0–9), hyphens (-), and underscores (_)."
        )
    return True, None


# ── Route: Home page (GET + POST) ──────────────────────────
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    GET  → Show the form where the user can enter a long URL.
    POST → Accept the long URL, create a short code, and show the result.
    """
    short_url = None    # Will hold the shortened URL to display
    error = None        # Will hold any validation error message

    if request.method == 'POST':
        original_url  = request.form.get('original_url',  '').strip()
        custom_alias  = request.form.get('custom_alias',  '').strip()

        # Basic validation — make sure the user entered a URL
        if not original_url:
            error = "Please enter a URL before submitting."
        else:
            # Ensure the URL starts with http:// or https://
            if not original_url.startswith(('http://', 'https://')):
                original_url = 'https://' + original_url

            if custom_alias:
                # ── User provided a custom alias ────────────────
                valid, alias_error = validate_alias(custom_alias)

                if not valid:
                    # Failed character / length check
                    error = alias_error
                elif custom_alias in url_map:
                    # Alias already taken by a previous submission
                    error = f'The alias "{custom_alias}" is already in use. Please choose a different one.'
                else:
                    # Alias is valid and unique — use it directly
                    url_map[custom_alias] = original_url
                    short_url = request.host_url + custom_alias
            else:
                # ── No alias provided — auto-generate a unique code
                code = generate_short_code()
                while code in url_map:
                    code = generate_short_code()

                url_map[code] = original_url
                short_url = request.host_url + code

    return render_template('index.html', short_url=short_url, error=error)


# ── Route: Redirect short code → original URL ───────────────
@app.route('/<string:code>')
def redirect_to_url(code):
    """
    Look up the short code in our dictionary.
    If found → redirect the user to the original URL.
    If not   → show the error page with a 404 status.
    """
    original_url = url_map.get(code)

    if original_url:
        return redirect(original_url)   # 302 redirect by default
    else:
        # Render the custom error page and return HTTP 404
        return render_template('error.html', code=code), 404


# ── Entry point ─────────────────────────────────────────────
if __name__ == '__main__':
    # debug=True enables auto-reload and detailed error pages during development
    app.run(debug=True)
