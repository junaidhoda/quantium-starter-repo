import pytest
from dash import html, dcc
from app import app


def find_component(component, component_type, component_id=None):
    """Recursively search the layout for a component by type and optional id."""
    if isinstance(component, component_type):
        if component_id is None:
            return component
        if getattr(component, "id", None) == component_id:
            return component

    children = getattr(component, "children", None)
    if children is None:
        return None
    if not isinstance(children, list):
        children = [children]

    for child in children:
        result = find_component(child, component_type, component_id)
        if result is not None:
            return result

    return None


def test_header_is_present():
    header = find_component(app.layout, html.H1)
    assert header is not None, "H1 header should be present in the layout"
    assert "Pink Morsel" in header.children, "Header should contain 'Pink Morsel'"


def test_visualisation_is_present():
    chart = find_component(app.layout, dcc.Graph, "sales-chart")
    assert chart is not None, "dcc.Graph with id='sales-chart' should be present"


def test_region_picker_is_present():
    radio = find_component(app.layout, dcc.RadioItems, "region-filter")
    assert radio is not None, "dcc.RadioItems with id='region-filter' should be present"
    assert len(radio.options) == 5, "Region picker should have 5 options"
    values = [o["value"] for o in radio.options]
    assert set(values) == {"all", "north", "east", "south", "west"}
