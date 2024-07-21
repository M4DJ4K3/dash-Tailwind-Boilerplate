# Dash App
This repository contains a Dash application built with Python. The app is designed using the Dash framework and Tailwind CSS for styling. The application layout includes a navigation bar, a footer, and a content area that dynamically renders pages.

## Overview
The app uses the following components:

- Nav: A navigation bar imported from components.nav.
- Footer: A footer imported from components.footer.
- Tailwind CSS: For styling, included via an external script.

## Installation
Clone the Repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## Create and Activate a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Required Packages:
Make sure you have Dash and other dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

## Run the Application:
```bash
python app.py
```

The app will start running on http://127.0.0.1:8050/ by default.

## App Structure
- app.py: Main file where the Dash app is initialized and configured.
- components/: Contains the Nav and Footer components used in the app.
    - nav.py: Defines the navigation bar component.
    - footer.py: Defines the footer component.
## Code Explanation

- Imports:

```python
from dash import Dash, html, dcc, page_container, page_registry
from components.nav import Nav
from components.footer import Footer
```

- External Scripts:
Tailwind CSS is included for styling:

```python
external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]
```

- App Initialization:
The Dash app is initialized with the external scripts for styling and page management:

```python
app = Dash(__name__, external_scripts=external_scripts, use_pages=True)
```

- Layout:
The layout includes a navigation bar, a horizontal rule, a content area managed by page_container, and a footer:

```python
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        Nav(page_registry.values()),
        html.Hr(className="w-full"),
        page_container,
        Footer()
    ], className="w-full h-screen bg-slate-100 p-5 gap-4 flex flex-col justify-center items-center"
)
```
- Running the App:
The app runs in debug mode if executed directly:

```python
if __name__ == '__main__':
    app.run(debug=True)
```
## Contributing
Fork the Repository: Create your own fork of the repository on GitHub.
Create a Branch: Develop features or fixes in a new branch.
Submit a Pull Request: Once your changes are ready, submit a pull request for review.

##License
This project is licensed under the MIT License - see the LICENSE file for details.