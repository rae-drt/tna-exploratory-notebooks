# discovery-api-notebook

Hello and welcome to this series of Jupyter notebooks that will help you get started with the Discovery API.

## What is Discovery?

[Discovery](https://discovery.nationalarchives.gov.uk/) provides access to the catalogue for [The National Archives](https://www.nationalarchives.gov.uk/). The catalogue contains descriptions of over 32 million records held by The National Archives and more than 2,500 archives across the country. Over 9 million records are available for download. 

The archive is split into record series, with series split into lower and lower levels. At the highest level, record series typically represent Governmental Departments (if the record is held by TNA) or Archive (if the record is held elsewhere). Note: TNA holds records from the last 1,000 years – there are departments that no longer exist, so the list of departments may be longer than expected. 

The list of record series/departments can be found here – {url}. For these notebooks, we will be focusing on records at TNA. 

An API to Discovery is available, which allows you to search the catalogue and download records. This API is what we will be using in these notebooks; demonstrating that with the number of records avaiable, using the API can be a much more efficient way of finding valuable records, and can provide insights that would be difficult to find otherwise.

## About these notebooks

There are two general aims with these notebooks: 
- Showing how to work with the Discovery API, and why you might want to use (and automate) it.
- Looking into a few different things you may want to do with the data. 

The notebooks are designed to be run in order, but you can also jump around or skip a notebook if you want. The first starts off introducingt the concept of an API, with the following ones building up from there - if you already know the basics of interacting with API's, you may want to jump ahead to where we start to discuss data. 


# NON Useful, to be rewritten

## Gathering information

The key thing you need when working with an API is the documentation. This provides information on what requests you can build: what endpoints are available, what query parameters you can use, what methods they accept, and so on. This information is often provided either directly alongside, or is similarly accessible as, the API. 

The [main help page](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/) provides useful information - particularly the terms of use, information on catalogue levels, and requests to limit rates of use. From this page, you can navigate to the [API sandbox](https://discovery.nationalarchives.gov.uk/API/sandbox/index). This page works as more thorough documentation of the API's functionality - showing available endpoints, parameters, and responses. The sandbox is interactive, allowing you to build and test requests in the browser.

At this stage, try it out! Have a go with the sandbox and see what you can retrieve.

There are a range of bits of information that are key and can be gathered from the sandbox. These include the base URL, endpoints relevent to queries we want to make and the methods these endpoints use. 

## What is Discovery

so start by selecting the first letter of the department you are looking for. Selecting details of your record series at this level provides an overview of the series, including a description, date range, and physical description, among other data. 

The other option is to browse by hierarchy – the boxes to the side of the main list. These are the first “child” level series of the main series selected on the left of the page. Clicking on their details button provides similar details to the main record series (although often to a reduced level), while clicking on their title takes you one level “deeper” into the hierarchy. These steps can be repeated, until you reach a page such as this – this is the edge of the tree, each entry on a page like this are actual records. 

Powering Discovery is a database; it is this database that stores the information about each record and is queried every time (either by the web user interface, or the API). It is the sheer number of records in Discovery that make using the API a valuable option. Rather than having to use the web interface separately for each unique query, following the rest of this notebook you will be able to automate its use - allowing you to filter more efficiently and retrieve large amounts of data more effectively. 