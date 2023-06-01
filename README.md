<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/linkedin-jobs-scraper/blob/master/logo.png?raw=true' alt='LinkedIn Jobs Scraper' height='80px'/>

# LinkedIn Jobs Scraper

Extract general jobs data from linkedin.com in specific location and searching a list of keywords.

Start date: **2022-05-31**

Last update: **2023-04-13**

Project type: **personal's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

The oputput data is saved in the \\\"data.csv\\\" file.\r
You can setup the project with the config.json file.\r
\r
## Output data\r
Sample:\r
|keyword|location|title|company|date|link|\r
|---|---|---|---|---|---|\r
frontend|Michoacan|Frontend Engineer|Ankr|1 week ago|https://mx.linkedin.com/jobs/view/...|\r
frontend|Michoacan|Front End Developer|Colgate-Palmolive|6 days ago|https://mx.linkedin.com/jobs/view/...|\r
frontend|Michoacan|Software Engineer II-Front End|Microsoft|2 weeks ago|https://mx.linkedin.com/jobs/view/...|

# Install

## Third party modules\r
\r
Open Terminal in project folder and install all modules from pip:\r
(here a tutorial about [how to open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)) \r
\r
\\`\\`\\` bash\r
$ pip install -r requirements.txt\r
\\`\\`\\`\r
## Programs\r
\r
To run the project, the following programs must be installed:\r
\r
* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

In the config.json file, there are the locations and keywords for search in the page\r
\r
## Structure\r
\r
\\`\\`\\`json\r
{\r
    \\\"show_chrome\\\": true,\r
    \\\"keywords\\\":  [\r
        \\\"web developer\\\", \r
        \\\"frontend\\\", \r
    ],\r
    \\\"locations\\\": [\r
        \\\"Aguascalientes\\\",\r
        \\\"Baja California\\\",\r
        \\\"Baja California Sur\\\",\r
        \\\"Campeche\\\",\r
        \\\"Chiapas\\\",\r
        \\\"Chihuahua\\\",\r
        \\\"Ciudad de Mexico\\\",\r
    ]\r
}\r
\\`\\`\\`\r
\r
### show_chrome\r
Show (true) or hide (false) the google chrome window\r
### keywords\r
List of word to search in the page\r
### locations\r
Countries, states or cities where do you want to extract data

# Run

Run the **__main __.py** or the **project folder** with your python 3.10 interpreter.\r
\r
You can do it from terminal or by **double clicking the file**\r
\r
\r
## Run sample from terminal:\r
\r
Before, [open terminal in project folder for windows](https://github.com/DariHernandez/tutorials/tree/master/open%20terminal%20(cmd)%20in%20project%20folder%20in%20windows)\r
\r
After, type: \r
\r
\\`\\`\\` bash\r
$ py __main__.py\r
\\`\\`\\`\r
\r
or\r
\r
\\`\\`\\` bash\r
$ py .\r
\\`\\`\\`


