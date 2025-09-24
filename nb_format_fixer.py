import nbformat
nb = nbformat.read("ImageNet_Classification_2_vehicles.ipynb", as_version=4)
nb.metadata.pop("widgets", None)
nbformat.write(nb, "fixed_notebook.ipynb")
