### JSS_tools

This is a collection of small tool routines to make working with the data returned by python-jss easier.

At their core they turn the XML from the JSS into python data structures. It also converts the strings returned to valid python types where possible.

Included are a small number of utility routines, most notably `convert` to convert strings to python data types, `Jopen` to open up a connection to the JSS, `c_attributes_write` to write changed extension attributes in a computer record back to the JSS.

For details on the functions `pydoc ./jss_tools.py` will get you the
documentation.

#### Design decisions

When working with the JSS the most expensive part of the operation is always the query to the JSS. This is why none of these routines actually perform the query. I leave the decision about when to do it to you.

At the moment there are some data structures that are arrays of dictionaries. I'd appreciate feedback on perhaps changing this to dictionaries of dictionaries with `id` or `name` as key for the outer dictionary.

If there is a python-jss call not covered that you would like then please reach out. My JSS is not well populated for some things so I have no need for some and no data to test but I can get around that if you can supply the XML returned by your JSS (sanitised, of course).

#### examples.py

A tiny file with some examples. It isn't meant to be run, just read as examples.

### compliance.py

Real world example. Somebody wanted a list of Macs not running the right OS
and build so I gave them the output of this.

### sanitise.py

Another real world example. This is what I used to sanitise the JSS data so I could safely show it in my presentation.

### XWorld2018.key

The presentation.
