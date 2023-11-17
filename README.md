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