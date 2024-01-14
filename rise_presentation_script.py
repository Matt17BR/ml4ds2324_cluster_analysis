import nbformat
import os

# Load the notebook
notebook_path = os.path.join('presentation','merged_2_32.ipynb')
with open(notebook_path, 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Function to set slide type based on cell type and level
def set_slide_type(cell):
    if cell['cell_type'] == 'markdown':
        if cell['source'].startswith('## '):
            return 'slide'
        elif cell['source'].startswith('### '):
            return 'slide'
        elif cell['source'].startswith('#### '):
            return 'slide'
    elif cell['cell_type'] == 'code':
        return 'fragment'
    return None

# Apply the slide type settings
for cell in nb['cells']:
    slide_type = set_slide_type(cell)
    if slide_type:
        if 'metadata' not in cell:
            cell['metadata'] = {}
        if 'slideshow' not in cell['metadata']:
            cell['metadata']['slideshow'] = {}
        cell['metadata']['slideshow']['slide_type'] = slide_type

# Save the modified notebook
modified_notebook_path = os.path.join('presentation','merged_2_32_slides.ipynb')
with open(modified_notebook_path, 'w') as f:
    nbformat.write(nb, f)