# Google-Image Crawler

## <strong>Introduction</strong>

 Build an application to crawl Google Images with Tkinter Python framework and icrawler libraries.

 "This package is a mini framework of web crawlers. With modularization design, it is easy to use and extend. It supports media data like images and videos very well, and can also be applied to texts and other type of files. Scrapy is heavy and powerful, while icrawler is tiny and flexible.

With this package, you can write a multiple thread crawler easily by focusing on the contents you want to crawl, keeping away from troublesome problems like exception handling, thread scheduling and communication.

It also provides built-in crawlers for popular image sites like Flickr and search engines such as Google, Bing and Baidu." - pypi.org

 ## <strong>Installation</strong>

 Use the package tkinter framework to build an application (If you prefer to find out more information about the documentation, please click this link [tkinter-documentation](https://tkdocs.com/tutorial/install.html))

 ```bash 
pip install tk
 ```

Next we continue downloading [pillow](https://pypi.org/project/Pillow/) library

```bash
pip install pillow
```

On the way, we install [icrawler](https://pypi.org/project/icrawler/) library (python version 3.5, recommended)

```bash
pip install icrawler
```

## <strong>Usage</strong>

Clone the project into your computer's home directory

```bash
git clone https://github.com/JosephThien2000/Google_Image_Crawler.git
```

First, you need to download the necessary libraries and modules. Open your <strong>`Command Prompt`</strong> or <strong>`PowerShell`</strong> in the current project's directory and run a command line below:

```bash
pip install -r requirements.txt
```

All necessary libraries and modules we need to be imported

```python
# Import necessary libraries
from tkinter import *
from time import sleep
import os
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
from download_image import *
from google_crawler import *
from pathlib import *
from tkinter.scrolledtext import ScrolledText
```

Next we open the <strong>`Command Prompt`</strong> or <strong>`PowerShell`</strong> that references to the path you clone the project down to run this code

```bash
python main.py
```
 
 ## <strong>Contributing</strong>

 Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## <strong>References</strong>

[Markdown guide](https://www.ionos.com/digitalguide/websites/web-development/markdown/#:~:text=Markdown%20makes%20it%20especially%20easy,italicized%2C%20three%20asterisks%20are%20necessary.)

[Google Images with icrawler library](https://viblo.asia/p/download-a-bunch-of-images-from-google-with-icrawler-july-18-2020-3Q75wn89lWb)

[Tkdocs.com](https://tkdocs.com/tutorial/install.html)

[Make a README](https://www.makeareadme.com/)

[Scrolledtext widget](https://www.geeksforgeeks.org/python-tkinter-scrolledtext-widget/)

[Tkinter structure](https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application)

[Tkinter OOF](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/)

[Tkinter tutorial](https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app)