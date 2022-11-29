# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Checklist(Component):
    """A Checklist component.
Checklist is a component that encapsulates several checkboxes.
The values and labels of the checklist is specified in the `options`
property and the checked items are specified with the `value` property.
Each checkbox is rendered as an input / label pair.

If `Checklist` is given an `id` (which is necessary for use in callbacks) it
will use Bootstrap's custom checkbox style, which hides the native browser
checkbox and renders a custom CSS alternative. See the Bootstrap docs for
details.

https://getbootstrap.com/docs/4.4/components/forms/#checkboxes-and-radios-1

Keyword arguments:

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- className (string; optional):
    The class of the container (div).

- custom (boolean; default True):
    RadioItems uses custom radio buttons by default. To use native
    radios set custom to False.

- inline (boolean; optional):
    Arrange Checklist inline.

- inputClassName (string; default ''):
    The class of the <input> checkbox element.

- inputStyle (dict; optional):
    The style of the <input> checkbox element. Only used if
    custom=False.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- labelCheckedClassName (string; optional):
    Additional CSS classes to apply to the <label> element when the
    corresponding checkbox is checked.

- labelCheckedStyle (dict; optional):
    Additional inline style arguments to apply to <label> elements on
    checked items.

- labelClassName (string; default ''):
    CSS classes to apply to the <label> element for each item.

- labelStyle (dict; optional):
    Inline style arguments to apply to the <label> element for each
    item.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- name (string; optional):
    The name of the control, which is submitted with the form data.

- options (list; optional):
    An array of options.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- style (dict; optional):
    The style of the container (div).

- switch (boolean; optional):
    Set to True to render toggle-like switches instead of checkboxes.
    Ignored if custom=False.

- value (list of string | numbers; optional):
    The currently selected value."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, options=Component.UNDEFINED, value=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, inputStyle=Component.UNDEFINED, inputClassName=Component.UNDEFINED, labelStyle=Component.UNDEFINED, labelCheckedStyle=Component.UNDEFINED, labelClassName=Component.UNDEFINED, labelCheckedClassName=Component.UNDEFINED, inline=Component.UNDEFINED, switch=Component.UNDEFINED, custom=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, name=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'custom', 'inline', 'inputClassName', 'inputStyle', 'key', 'labelCheckedClassName', 'labelCheckedStyle', 'labelClassName', 'labelStyle', 'loading_state', 'name', 'options', 'persisted_props', 'persistence', 'persistence_type', 'style', 'switch', 'value']
        self._type = 'Checklist'
        self._namespace = 'dash_bootstrap_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'custom', 'inline', 'inputClassName', 'inputStyle', 'key', 'labelCheckedClassName', 'labelCheckedStyle', 'labelClassName', 'labelStyle', 'loading_state', 'name', 'options', 'persisted_props', 'persistence', 'persistence_type', 'style', 'switch', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Checklist, self).__init__(**args)