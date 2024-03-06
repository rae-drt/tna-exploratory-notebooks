# Exploring the Discovery API

Hello and welcome to this series of Jupyter notebooks, aiming to illustrate how to use the Discovery API and explore the data you can retrieve. 


## What is Discovery?

[Discovery](https://discovery.nationalarchives.gov.uk/) provides access to the catalogue for [The National Archives](https://www.nationalarchives.gov.uk/). The catalogue contains descriptions of over 32 million records held by The National Archives and more than 2,500 archives across the country. Over 9 million records are available for download. 

The archive is split into record series, with series split into lower and lower levels. At the highest level, record series typically represent Governmental Departments (if the record is held by TNA) or Archive (if the record is held elsewhere). Note: TNA holds records from the last 1,000 years – there are departments that no longer exist, so the list of departments may be longer than expected. The list of record series/departmental division can be found [here](https://discovery.nationalarchives.gov.uk/browse). For these notebooks, we will be focusing on records at TNA. 

### Discovery API

An API to Discovery is available, which allows you to search the catalogue and download records. This API is what we will be using in these notebooks; demonstrating that with the number of records available, using the API can be a much more efficient way of finding valuable records, and can provide insights that would be difficult to find otherwise.

Documentation, and a place to trial this API is available in the [API sandbox](https://discovery.nationalarchives.gov.uk/API/sandbox/index). This page works as a thorough documentation of the API's functionality - showing available endpoints, parameters, and responses. The sandbox is interactive, allowing you to build and test requests in the browser. There is also a [help page](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/) also available, which provides useful information - particularly the terms of use, information on catalogue levels, and requests to limit rates of use.



## About these notebooks

There are two general aims with these notebooks: 
- Showing how to work with the Discovery API, and why you might want to use (and automate) it.
- Looking into a few different things you may want to do with the data. 

These two aims match with the two main stages to these notebooks. Stage 1 introduces different endpoints available in the API, building functions to gather large volumes of accurate and useful data from them. Stage 2 then splits off into different pathways, using and expanding on different data from Discovery to build rich insights into the data.

The notebooks are designed to be run in order, but you can also jump around or skip a notebook if you want. 

### Stage 1 notebooks

0 - [What is an API?](./0-what-is-an-api.ipynb) - This notebook introduces the concept of an API, and how to interact with one. If you already know the basics of interacting with API's, you may want to jump ahead to where we start to discuss data.

1 - [Intro to the Discovery API](./1-intro-to-discovery-api.ipynb) - This notebook introduces the Discovery API sandbox and the search endpoint. It goes through how to build a request on the sandbox, and what information you need to build requests in Python, all worked through with a worked example.

2 - [More data and details](./2-working-through-results.ipynb) - This notebook starts by looking at some of the other data you get from the search endpoint, and how it can be used to get a bigger set of results. It then looks at how to use the details endpoint to get more information about specific records, or sets of records.

3 - [Working through collections](./3_working_through_collections.ipynb) - Here we go through endpoints that can be used to gather data about entire collections when given a single record, or build context such as hierarchy above or below a given record. The remaining endpoints of Discovery are also introduced. Finally, the course concludes and the case studies are introduced. 

### Stage 2 notebooks

- [Drawing graphs](./drawing-graphs/) - Using the example of someone investigating whether there is any relation between a records start date or duration and the length of its description, this pair of notebooks takes you through the process of:

    1. Gathering the appropriate data from Discovery API
    2. Data manipulation using `panads`
    3. Drawing graphs using `matplotlib`

- [Visualising and Mapping](./mapping-and-visualising-ships/) - These notebooks take a look at the number of records available in the [ADM series](https://discovery.nationalarchives.gov.uk/browse/r/h/C4). The [Visualising notebook](./mapping-and-visualising-ships/) looks at the wider information, gathering insights such as record series with longer descriptions, or time periods with more records. The [Mapping notebook](./mapping-and-visualising-ships/mapping-dead-reckoning.ipynb) takes a look at what can be done with digitised records to enhance the information available; in this case, taking ships logs, mapping their voyages, and including other pertinent information such as weather and events that happened along the way.

- [Drawing on maps](./mapping/) - These notebooks look at the different possibilities when drawing data onto world maps, with a technical focus on using the [`Folium`](https://python-visualization.github.io/folium/) library. The notebooks prefixed wtih `demo_` ([e.g. demo_ship_chase](./mapping/demo_ship_chase.ipynb)) are worked examples, showing how different features of Folium can be used with real data to create an interactive map. Notebooks prefixed with `features_` ([e.g. features_markers](./mapping/features_markers.ipynb)) demonstrate groups of similar features in Folium - with markers showing different ways to indicate locations on a map and provide information; overlays showing how historic maps can be used in conjuction with modern ones; and the further features showing some examples from the Foliumn plugins. 

- [Weird description](./weird-description/) - This notebook looks at all the descriptions in a given series, and tries to find the most unusual ones based on word occurrence frequency.

- [NLP] Harshad add your description here :) 