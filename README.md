# LINKEIN SCRAPER
**python version: 3.10**


Extract general jobs data from linkedin.com in specific location and searching a list of keywords.
The oputput data is saved in the "data.csv" file.
You can setup the project with the config.json file.

# Install
## Third party modules

Open Terminal in project folder and install all modules from pip:
(here a tutorial about [how to open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)) 

``` bash
$ pip install -r requirements.txt
```
## Programs

To run the project, the following programs must be installed:

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

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
    "show_chrome": true,
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

* ### show_chrome
Show (true) or hide (false) the google chrome window
* ### keywords
List of word to search in the page
* ### locations
Countries, states or cities where do you want to extract data

# Ouput data
Sample:
|keyword|location|title|company|date|link|
|---|---|---|---|---|---|
frontend|Michoacan|Frontend Engineer|Ankr|1 week ago|https://mx.linkedin.com/jobs/view/...|
frontend|Michoacan|Front End Developer|Colgate-Palmolive|6 days ago|https://mx.linkedin.com/jobs/view/...|
frontend|Michoacan|Software Engineer II-Front End|Microsoft|2 weeks ago|https://mx.linkedin.com/jobs/view/...|
