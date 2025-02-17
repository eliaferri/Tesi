# The Scopus Publication Lens (SPL)

Web app for exploring huge scatter plots of scientific publications found on Scopu. Based on the deepscatter framework, a library for allowing interactive visualization of extremely large datasets in browser, developed by Nomic-AI.

Deepscatter is provided under an NC-CC-BY-SA license for all noncommercial use.


# Documentation

The [autogenerated typescript documentation](https://nomic-ai.github.io/deepscatter/) for deepscatter.


# Quick start


## Running locally.

1. First, install the companion tiling library.

```sh
python3 -m pip install git+https://github.com/bmschmidt/quadfeather
```

2. Then setup this library to run. It will start a local dev server.

```sh
npm run dev
```

3. If you go to `localhost:3344`, you should see an interactive scatterplot. To dig into what you're seeing, open `index.html`.


# Updating data

1. Paste publications-related CSV files in the ```data``` folder.

2. Prepare your data for deepscatter by running the following python scripts:

```sh
python3  parse_data_for_deepscatter.py
python3  keyword_to_geojson.py
```
You should now see 2 more files: ```publications_for_deepscatter.csv``` and ```keywords.geojson```

3. Copy ```keywords.geojson``` in the ```tests/``` folder, overwrite the exising file.

4. Copy ```publications_for_deepscatter.csv``` in the main folder of the project and run the following command in the same folder

```sh
quadfeather --files publications_for_deepscatter.csv --tile_size 50000 --destination tiles
```

5. Displayed data should be updated
