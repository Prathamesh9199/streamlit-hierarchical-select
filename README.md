# Streamlit Hierarchical Select

A modern, high-performance hierarchical selection component for Streamlit, inspired by the Excel filter interaction.

## Features
- 🌲 **Hierarchical Tree View**: Handles nested data structures of arbitrary depth.
- 🔍 **Search & Filter**: Searching for a child node (e.g., "San Francisco") automatically reveals its context (USA > California).
- ✅ **Tri-State Logic**: Correctly handles "Indeterminate" states (partially selected parents).
- 🎨 **Modern UI**: Clean, Anthropic-inspired design that blends seamlessly with Streamlit.

## Installation

```bash
pip install streamlit-hierarchical-select
```

## Usage
```python
import streamlit as st
from streamlit_hierarchical_select import hierarchical_select

data = {
    "North America": {
        "USA": ["New York", "San Francisco"],
        "Canada": ["Toronto", "Vancouver"]
    },
    "Europe": ["London", "Berlin", "Paris"]
}

selected = hierarchical_select(data)
st.write(selected)
```