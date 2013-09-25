
# ckanext-pubsub


## Intro

ckanext-pubsub is a [CKAN](http://ckan.org) extension that notifies a [pubsubhubbub](https://code.google.com/p/pubsubhubbub/) server whenever a dataset is published, or substantially modified [1]

## Installation

To install this extension you should first activate the virtualenv that runs your CKAN instance and then run the following command.

     pip install -e git+https://github.com/rossjones/ckanext-pubsub.git#egg=ckanext-pubsub

For development you should check out the code into a useful location as follows (again, as long as the virtualenv is activated)

     git clone git://github.com/rossjones/ckanext-pubsub.git
     cd ckanext-pubsub
     python setup.py develop

## Configuration

Add the plugin to the ckan.plugins setting in your CKAN .ini file

    ckan.plugins = … subpub

Restart your web-server, probably apache

    sudo apache2ctl restart

## Testing

To run the tests for ckanext-pubsub you should run the following command from the folder where you installed ckanext-subpub. This is only really useful if you installed by cloning from git.

    nosetests

## Is it any good?

Yes.



[1] A new resource added, for instance
