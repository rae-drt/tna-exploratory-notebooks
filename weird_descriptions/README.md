# Weird descriptions

This case study takes inspiration from [unusual newspaper headlines](https://www.theguardian.com/world/2024/feb/01/floating-sauna-rescues-motorists-whose-tesla-plunged-into-oslo-fjord). Working with the theory that these headlines stand out as they contain unexpected combinations of words, this case study presents an entire project in a single notebook: 
- Defining a few metrics to measure the 'weirdness' of a description.
- Gathering data from the Discovery API.
- Calculating the metrics for each description.
- Visualising the results.
- Drawing conclusions from the data.
- Suggesting further work that could be done.

To help with this, a couple of different libraries are used:
- The [`wordfreq`](https://pypi.org/project/wordfreq/) provides easy access to frequency data for words in English based on a large corpus of text.
- [`numpy`](https://numpy.org/) provides a variety of tested and highly trusted mathematical functions.
- [`matplotlib`](https://matplotlib.org/) is a widely used library for drawing graphs in Python.

The notebook is designed to be approachable, and the logic behind the metrics is explained in detail. The notebook is also designed to be run in a single session, with all the data gathered and processed in the notebook itself. The libraries are introduced here; futher details are explored in subsequent case studies.