# Exploring the Discovery API

Hello and welcome to this series of Jupyter notebooks, aiming to illustrate how to use the Discovery API and explore the data you can retrieve. 

## What is Discovery?

[Discovery](https://discovery.nationalarchives.gov.uk/) provides access to the catalogue for [The National Archives](https://www.nationalarchives.gov.uk/). The catalogue contains descriptions of over 32 million records held by The National Archives and more than 2,500 archives across the country. Over 9 million records are available for download. 

An API to Discovery is [available](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/), providing a variety of ways to search the records. The notebooks here introduce this API, showing how to use it to gather data about large numbers of records, or use it to efficiently find exactly the right records for research. The case studies show how these data can then be used in a variety of ways, from visualisation to analysis.
	
The [API sandbox](https://discovery.nationalarchives.gov.uk/API/sandbox/index) provides a place to trial the API, and to show documentation - available endpoints, parameters, and responses. The sandbox is interactive, allowing you to build and test requests in the browser. There is also a [help page](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/) also available, which provides useful information - particularly the terms of use.


## About these notebooks

The notebooks here are shown in two sections: 

- The main series of notebooks introduce the Discovery API, showing how to use it to gather data about large numbers of records easily, and how to filter down to find the records you are interested in conveniently.
- The case studies use the information gathered from the API, showing several different ways of using it. These range from various analysis and visualisation techniques, up to more complex natural language processing (NLP) projects. 

The main series are designed to be worked through in order, as they build on each other. The case studies can be run independently, but build in complexity as they progress. All notebooks install their own requirements wherever possible, so you can start at whichever notebook is most interesting and relevant to you. 

### API introduction

0 - [What is an API?](./0-what-is-an-api.ipynb) - This notebook introduces the concept of an API, and how to interact with one. This one is only necessary if you're not familiar with APIs, or want a refresher.

1 - [Intro to the Discovery API](./1-intro-to-discovery-api.ipynb) - This notebook introduces the Discovery API sandbox and the search endpoint. It goes through how to build a request on the sandbox, and what information you need to build requests in Python, all worked through with a worked example.

2 - [More data and details](./2-working-through-results.ipynb) - This notebook starts by looking at some of the other data you get from the search endpoint, and how it can be used to get a bigger set of results. It then looks at how to use the details endpoint to get more information about specific records, or sets of records.

3 - [Working through collections](./3_working_through_collections.ipynb) - Here we go through endpoints that can be used to gather data about entire collections when given a single record, or build context such as hierarchy above or below a given record. The remaining endpoints of Discovery are also introduced. Finally, the course concludes and the case studies are introduced. 

### Case studies

To demonstrate some of the many different ways you can use data gathered from the Discovery API, some case studies are included as follow-ons from the main series of notebooks. They cover a range of topics and work with different volumes of data - from analysing the data from large collections, to visualisation of a few records. These notebooks are designed to be standalone, so if you have a particular interest in one of them, you can run it independently. They are shown below in order from most approachable to most technical:

- [Weird descriptions](./weird-descriptions/README.md) - Inspired by [unusual newspaper headlines](https://www.theguardian.com/world/2024/feb/01/floating-sauna-rescues-motorists-whose-tesla-plunged-into-oslo-fjord) that can seem to be a jumble of words, this case study looks at all the descriptions in a given series and tries to find the most unusual ones based on word occurrence frequency. Designed to be the most approachable case study, the entire process is run in a single notebook, with explanations of the logic used to calculate the 'weirdness' of a description, and brief introductions into some analysis techniques. 

- [Drawing maps](./mapping/README.md) - With the variety of records held by TNA, it is perhaps unsurprising that many of them are maps, or have locations associated with them. This case study looks in more depth at the [`Folium`](https://python-visualization.github.io/folium/) library, which can be used to draw maps in Python. Folum is introduced in a couple of example notebooks, to show its versatility. A case study is then shown which assumes data has been gathered from ships logs, showing how a chase between two ships can be transformed from a table of data to an animated map showing the ships movements over time.

- [IIIF](./iiif-notebooks/) - IIIF standards are rapidly becoming widespread in digital humanities use, and are introduced here. These two notebooks cover the Presentation and Image APIs, and use an example document from discovery to build up a hypothetical IIIF manifest. The Image API notebook also dissects some live examples, to see what values have been used, and what the effect of changing them is.

- [Exploring and visualising data](./exploring-and-visualising-data/README.md) - Here, the ability to gather metadata about large numbers of records from the API is leveraged, and multiple ways to explore and visualise this data are shown. The first stage of this case study focusses on gathering the data of specific interest, and manipulating it into a useful and portable format. The [`pandas`](https://pandas.pydata.org/) library is introduced to demonstrate Dataframes, and the data is later saved as a CSV. In the second notebook, graphs of the data are drawn, showing how to use the [`matplotlib`](https://matplotlib.org/) library, and highlighting some of the insights these graphs show. The third notebook develops on these insights, introducing some starter statistical analysis techniques to draw more detailed conclusions; working with the [`scipy`](https://www.scipy.org/) and [`sklearn`](https://scikit-learn.org/stable/) libraries to do so. 



- [NLP] Coming soon. 

### Other notebooks

- [Discovery, data analysis, and posibilities with the API](/discovery.ipynb) is a notebook designed for live demonstrations project, as a preview. It is available in the repository, and can be run, but be aware that it is not as polished as the main series. 

## Running the notebooks

Jupyter notebooks are very portable, and can be run in a number of different ways, some options of which are listed below. The links below serve as overall entries to the notebooks, more direct links are provided in the descriptions above for 

- Locally, on your device.
    - [The Jupyter project](https://jupyter.org/) provides several options to run Jupyter notebooks, including on device and in the cloud.
    - VSCode supports Jupyter notebooks via an extension. Good documentation for this is provided on [the VSCode website](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rae-drt/tna-exploratory-notebooks/HEAD). A cloud service that lets you run Jupyter notebooks. It is free to use, and allows your notebooks to be run by anyone with an internet connection. All notebooks aside from the NLP case studies can be run on Binder. Note that, when using Binder, many cells have a large output, and can result in a lot of scrolling. The button here will take you to the main repository on Binder, and you can navigate to the notebook you want from there.
- [Google Colab] Similar to Binder, Colab lets you run Jupyter notebooks in the cloud. It provides the option to use a GPU, a necessity for some of the more computationally intensive notebooks (hence, the only option for the NLP case studies). To run notebooks using Colab, you will need to log in with a Google account. 

### Requirements

#### Interacting with the notebooks
- Python version: all notebooks were designed using Python 3.10, but should work with and reasonably recent version of Python 3.
- All notebooks will attempt to install their own requirements at the start using [Pip](https://pypi.org/project/pip/). If you are running them locally, you may need to install these manually if the notebook fails to do so.
- Most notebooks are lightweight enough to run locally on most devices or via Binder. The NLP case studies are more intensive, and will work better on a device with a compatible GPU or Google Colab.


#### Accounts
- To run the notebooks on Google Colab, you will need a Google account.
- Some of the case studies use data or downloads available from Discovery and behind a paywall. These cells are all optional, and free to access data alternatives are provided.


