===============
Toryfied dirbot
===============

This is a Toryfied Scrapy project to scrape websites from public web directories , using Scrapy's HTTP_PROXY and
DOWNLOADER_MIDDLEWARES options which injects dynamic code for anonymity.

This project is only meant for educational purposes.

Items
=====

The items scraped by this project are websites, and the item is defined in the
class::

    dirbot.items.Website

See the source code for more details.

Spiders
=======

This project contains one spider called ``dmoz`` that you can see by running::

    scrapy list

Spider: dmoz
------------

The ``dmoz`` spider scrapes the Open Directory Project (dmoz.org), and it's
based on the dmoz spider described in the `Scrapy tutorial`_

This spider doesn't crawl the entire dmoz.org site but only a few pages by
default (defined in the ``start_pages`` attribute). These pages are:

* http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
* http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/

So, if you run the spider regularly (with ``scrapy crawl dmoz``) it will scrape
only those two pages.

.. _Scrapy tutorial: http://doc.scrapy.org/en/latest/intro/tutorial.html

Pipelines
=========

This project uses a pipeline to filter out websites containing certain
forbidden words in their description. This pipeline is defined in the class::

    dirbot.pipelines.FilterWordsPipeline

HTTP_PROXY
==========

This project uses a HTTP proxy layer to scrape the website data from public domain website..
this project redirects it's traffic from the localhost proxy hosted on port no 8123 ( polipo proxy)


USER_AGENT_LIST
===============

This project uses the USER_AGENT_LIST attribute of Scrapy setting.if defined , scrapy engine uses random user agent from
the USER_AGENT_LIST pool and makes each request using new USER_AGENT

DOWNLOADER_MIDDLEWARES
======================

This project uses the Download middle-wares attribute of scrapy stetting to inject custom code between and request object
and source website,public domain)...

In this project we are injecting two custom modules(class) ,
 1. RandomUserAgentMiddleware:
    to get random user agent for every request scrapy makes to scrape data
 2. ProxyMiddleware:
    to use the custom proxy setup to mask our identity and to scrape the data from public domain website anonymously

usage of TOR and POLIPO
=======================

In this Project , TOR relay and POLIPO proxy to scrape data anonymously

How it works:
-------------
This project uses POLIPO as HTTP proxy to redirect all it's spiders scrapping request to polipo,
POLIPO http proxy (localhost:8123) then, will transfer the traffic to SOCKS proxy (i.e. tor relay  , localhost:9050) and
post this, SOCKS proxy will make request to source website ( public domain).. and
And same goes for response ....source website will respond with data...sock proxy will use internal circuit and transfer
data back to our tor relay(localhost:9050).. tor relay will transfer payload back to polipo (localhost:8123) and polipo
will transfer that to the scrapy engine and to spider

Flow:

* **for request:**
 dmoz-spider==>scrapy engine==>pick random useragent==>localhost:8123==>localhost:9050==>(TOR circuit)==>source(website,public domain)
* **for response:**

 source(website,public domain )==>(TOR circuit)==>localhost:9050==>localhost:8123==>scrapy engine==>dmoz-spider

how to implement this:
----------------------

1.For Scrapy implementation
    use this repository [toryfied dirbot](https://github.com/DharmeshPandav/dirbot.git)

2.For TOR and Polipo setup
    Please refer this step-by-step guide : http://blog.privatenode.in/torifying-scrapy-project-on-ubuntu/
