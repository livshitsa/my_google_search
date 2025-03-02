
# my_google_search

**create virtual environment**
- uv venv --seed -p 3.11
- activate virtual enviroment (on mac or linux: source .venv/bin/activate)
- install dependancies: uv pip install -r ./requirements.txt

**mcp config section**
```
"Google Search": {
    "command": "your_path_to_uv_executable",
    "args": [
    "--directory",
    "/location_where_you_placed_python_file/",
    "run",
    "search_server.py"
    ]
}
```

