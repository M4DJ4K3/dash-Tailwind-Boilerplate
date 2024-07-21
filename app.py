# Import packages
from dash import Dash, html, dcc, page_container, page_registry
from components.nav import Nav
from components.footer import Footer

external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]

# Initialize the app - incorporate css
app = Dash(__name__, external_scripts=external_scripts, use_pages=True)

# App layout
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        Nav(page_registry.values()),
        html.Hr(className="w-full"),
        page_container,
        Footer()
    ], className="w-full h-screen bg-slate-100 p-5 gap-4 flex flex-col justify-center items-center"
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
