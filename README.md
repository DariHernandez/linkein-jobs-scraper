# COMPU TRABAJO SCRAPER
**python version: 3.10**


Extract general jobs data from computrabajo.com in specific location and searching a list of keywords.
The oputput data is saved in the "data.csv" file.
You can setup the project with the config.json file.

# Install
## Third party modules

Open Terminal in project folder and install all modules from pip:
(here a tutorial about [how to open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)) 

``` bash
$ pip install -r requirements.txt
```

# Run

Run the **__main __.py** or the **project folder** with your python 3.10 interpreter.

You can do it from terminal or by **double clicking the file**


## Run sample from terminal:

Before, [open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)

After, type: 

``` bash
$ py __main__.py
```

or

``` bash
$ py .
```

* ## config.json

Project settings file.
More details in the next section.
Create it in the project folder.

# Settings

In the config.json file, there are the locations and keywords for search in the page

## Structure

```json
{
    "computrabajo": "computrabajo.com.mx",
    "keywords":  [
        "web developer", 
        "frontend", 
    ],
    "locations": [
        "Aguascalientes",
        "Baja California",
        "Baja California Sur",
        "Campeche",
        "Chiapas",
        "Chihuahua",
        "Ciudad de Mexico",
    ]
}
```

* ### computrabajo
Url of the specific page where do you can to extract data
* ### keywords
List of word to search in the page
* ### locations
Countries, states or cities where do you want to extract data