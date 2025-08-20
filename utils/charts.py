import plotly.express as px

def plot_route_trends(route_daily, select_routes):
    """Generate a line chart of selected routes."""
    fig = px.line(
        route_daily[route_daily['route'].isin(select_routes)],
        x='date', y='interest', color='route',
        title='Search Interest Over Time'
    )
    return fig
