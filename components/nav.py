from dash import html, dcc, callback, Output, Input

def Nav(list_of_pages):
    # The main function to generate the navigation links
    def create_nav(current_path):
        nav_links = []  # List to accumulate the components

        for entry in list_of_pages:
            # Check if the current path matches the entry's relative path
            relative_classname = ""
            if entry["relative_path"] == current_path:
                relative_classname = "underline underline-offset-2"
            nav_links.append(
                html.Div(
                    dcc.Link(f"{entry['name']}", href=entry["relative_path"], className=relative_classname)
                )
            )

        return html.Div(nav_links, id='print', className="flex flex-row gap-4")

    # Define the callback within the component
    @callback(
        Output('nav-container', 'children'),
        [Input('url', 'pathname')]
    )
    def update_nav(pathname):
        return create_nav(pathname)

    return html.Div(id='nav-container')
