# VS Code Snippets

Change in settings:
```
"editor.tabCompletion": "on"
```

```
"editor.snippetSuggestions": "top"
```

```
"editor.quickSuggestions": true
```

```
"[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": true
  }
```
Location:


`~/Library/Application Support/Code/User/snippets/markdown.json`

## Usage

![](vs-code-snippet.gif)

## JSON for Example above

```json
"imports data science": {
		"prefix": "import-ds",
		"body": [
			"import pandas as pd",
            "import numpy as np",
            "import os",
            "import matplotlib.pyplot as plt",
            "plt.style.use(\"fivethirtyeight\")",
            "",
            "df = pd.read_csv('$1')"
		],
		"description": "common imports for data science"
	}
```