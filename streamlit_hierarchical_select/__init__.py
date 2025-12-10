import os
import streamlit.components.v1 as components

# Create a _RELEASE flag. We switch this to True when publishing.
_RELEASE = True

if not _RELEASE:
    # DEVELOPMENT MODE
    _component_func = components.declare_component(
        "hierarchical_select",
        path="./frontend"
    )
else:
    # PRODUCTION MODE
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend")
    _component_func = components.declare_component("hierarchical_select", path=build_dir)

def hierarchical_select(data, key=None):
    """
    Create a new instance of "hierarchical_select".
    
    Parameters
    ----------
    data: dict
        Nested dictionary representing the hierarchy
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    """
    # Helper to parse dictionary to tree structure expected by JS
    def parse_dict_to_tree(data, parent_id=""):
        tree = []
        for k, v in data.items():
            current_id = f"{parent_id}/{k}" if parent_id else k
            node = {"id": current_id, "label": str(k)}
            if isinstance(v, dict):
                node["children"] = parse_dict_to_tree(v, current_id)
            elif isinstance(v, list):
                node["children"] = [{"id": f"{current_id}/{item}", "label": str(item)} for item in v]
            else:
                node["children"] = [{"id": f"{current_id}/{v}", "label": str(v)}]
            tree.append(node)
        return tree

    tree_data = parse_dict_to_tree(data)
    return _component_func(data=tree_data, key=key, default=[])