+++
date = '2015-02-25T00:20:00+02:00'
title = 'What is LibreBorme'
categories = ['LibreBorme']
tags = ['libreborme', 'opendata', 'registro mercantil', 'proyecto de fin de carrera', 'civio']
+++

LibreBorme is my dissertation and it will be mentored by [Carlos Canal](http://www.lcc.uma.es/~canal/) from Universidad de Málaga and [David Cabo](https://twitter.com/dcabo) from [Fundación Ciudadana Civio](http://www.civio.es/).

Progress can be seen in the GitHub repository: [libreborme](https://github.com/PabloCastellano/libreborme), although right now the last commit is from October, when my draft hadn't even been approved. In the coming days I will upload the latest changes to reflect the current state.

I have submitted libreBorme to two different competitions about Free Software, that is, [Concurso Universitario de Software Libre](http://www.concursosoftwarelibre.org/1415/) and [Certamen de Proyectos Libres](http://osl.ugr.es/2014/09/26/premios-a-proyectos-libres-de-la-ugr/) which is organized this year by the Free Software Office of Universidad de Granada (UGR). I expect to have a functional and pretty version for the deadlines!

The following is the text of the draft that was approved last November.

# BORME queries and analysis web platform

# Motivation

In recent years, transparency is a booming subject in the political-institutional field. However, the devil is in the detail and most of the times the word "transparency" is used in a corrupted way because it's a fashion subject and sounds well, independently if the institution is considered to be transparent or not. Or maybe it's just because the definition of this term is different for both parts.

Another common problem is misunderstanding "open data" with "transparency", when reality is that the first one can be used as a tool to get the second, but not necessarily: publishing bus timetables as open data doesn't improve transparency (but it has other benefits).[^1]

In the moment where this document was written, it's less than one year that Spain passed its own Transparency Act[^2]. So far it was the only European country with more than a million inhabitants without one.

The passing was without any doubt an important and long waited fact. However, during the debate period they started to hear conflicting voices about this Act.

The _Open Knowledge Foundation_[^3], one of the most important international non for profit organizations and model for its background in the fight for transparency, provides in their «Open Data Handbook» a definition, with a number of conditions that a dataset must accomplish in order to be considered "Open Data".[^4][^5] The definition is large but it can be summed up as three facts:

- **Availability and Access**. the data must be available as a whole and at no more than a reasonable reproduction cost, preferably by downloading over the internet. The data must also be available in a convenient and modifiable form.
- **Reuse and Redistribution**. the data must be provided under terms that permit reuse and redistribution including the intermixing with other datasets.
- **Universal Participation**. everyone must be able to use, reuse and redistribute - there should be no discrimination against fields of endeavour or against persons or groups. For example, 'non-commercial' restrictions that would prevent 'commercial' use, or restrictions of use for certain purposes (e.g. only in education), are not allowed.

Nowadays there isn't a serious bet about it and only a few institutions apply to the definition when they speak about open data.

Nonetheless in the last years, we have seen that one of the clear strengths of our country, Spain, is that in spite of the general dissatisfaction of institutional politics, civil society organizes and they start to form groups to specialize and work in a proactive way to change things.

In this case, civil society has been organizing for a while to demand true transparency, giving as example transparency exiting in our surrounding countries that are considered model in regards of open data as is the United Kingdom, and they are achieving to speed up the process of transparency in public institutions by doing the work that they should be in the charge of but unfortunately don't do, by making true open datasets.

Some examples of these organizations are _OpenKratio_[^6], _Fundación Ciudadana Civio_[^7] or _Qué Hacen Los Diputados_[^8] (the first one, based in Seville and the rest based in Madrid). At international level we can find, among others, _Sunlight Foundation_[^9] or _Open Knowledge Foundation_ (OKFN), previously quoted.

Their activities program is public and we can find in it: meeting with regional government staff in order to offer advising and collaborate in an altruistic way; organizing conferences about transparency and Open Data in public universities with international speakers that explain the point of view from other countries; collaboration with public administrations to open and visualize datasets; organizing and participating in competitions and _hackathons_ for developing new APIs, mobile apps, etc.

In this context the following project is planned with the goal of address public data of the Mercantile Register in order to _open_ them in a way closer to the OKFN definition and offer them to everyone (be it a human or a Internet robot) willing to make use of them.

# Boletín Oficial del Registro Mercantil (BORME)

_Registro Mercantil Central_ (RMC) is the organization in charge of publishing _BORME_, which in Spanish stands for "Mercantile Register Official Bulletin". BORME publishes newly created societies, societies that have broken up, and some other data the companies must communicate.

Since 2009 it is also published in electronic format. This is a big step, but BORME only contain changes, that is, if we read BORME we can know that a a society has dissolved today, but it will be really hard to know when it was established, since the website doesn't provide a search engine that allows us to find it. Besides, if the constitution date is previous to 2009, it will be even more difficult, since there doesn't exist a document in electronic format and we should request to RMC a paper photocopy of the original document, indicating previously the page number in the BORME, which is also something we must know beforehand. However these datasets are already computerized somewhere. In order to access the history of a company we can use a service provided by _Colegio de Registradores, _which are the Official Registrars and to pay them in concept of professional fees, depending on how many requests we can to realize.

This procedure doesn't meet the definition of open data by OKFN and is contradictory and counter-productive because of the following reasons:

- It doesn't make sense that it's a closed service, since the main goal of Registro Mercantil is to be a public advertisement instrument of the companies.[^10]
- The fact of collecting money makes it harder and contradicts its own function of advertisement.
- It is an obsolete model of work that should have been renewed more than a decade ago. In those days you had to pay a person in charge of finding the requested information in thousand of sheets of hundreds of volumes, but nowadays we live in the Information Society, where it already exists the Internet, where this information is already computerized somewhere and the real cost of that request is near 0€.

Nonetheless, it keeps making sense that they collect money for the services of certificates expedition (another service offered by Colegio de Registradores) since they require a mercantile registrar to certify the data.

Unfortunately on the other hand,the search engine of BORME is only active for section II, which is where they publish Legal Notices, when the really interesting part is section I, where they publish registration data and other data concerning to companies. Finally BORME publishing format is only PDF, where other official documents are published also in XML format and before the beginning of this project the Author contacted the webmaster of BORME, who claimed that this behavior was not going to change in a short time because of _«the current agreement and legislation of the Mercantile Register»_.

# Goal and scope of this project

The goal of this project is developing a platform that automatedly downloads BORME files from January 2nd 2009, the day when they started to publish BORME in electronic format, in order to process them and build its own database with the contained data.

The automatic processing will extract every useful information of the PDF files, by identifying entities and actions. Once the database is generated, the potential will be in the ability of performing queries by fields or even semantic queries.

For example: What other societies do administer the administrators of this company? How many companies closed in 2011?

In order to ease the queries it will be developed additionally a web platform hosted in the cloud using the Django framework with the programming language Python.

The platform will be compatible with OpenStack and Cloud Foundry, both solutions for cloud computing, IaaS and PaaS respectively. Both solutions were chosen of among all existing solutions because these are free software and because of the trust on the organizations supporting them as "cloud standards".

The goal is that the service will be kept online after the project is finished. The author contacted to Fundación Ciudadana Civio and they showed their interest in maintaining the service and to make use of it together with the author. The platform will be autonomous, in the sense that it will be developed and will remain ready to look for new BORMES daily to incorporate new information to the database. This way it will be possible to query the website with the latest information available to the moment.

The source code of the platform will be released with a free software license, since the idea of this project is that as many entities as possible make use of it and we create a community around it.

Eventually, collected data will be given to OpenCorporates. OpenCorporates is an initiative that aims to free companies data worldwide and to "assign an URL to every company in the world", since data from Spanish companies and corporations available are poor compared to those available for other countries.[^11][^12][^13]

# References

[^1]: The New Ambiguity of "Open Government", 2012: http://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2012489
[^2]: [http://www.20minutos.es/noticia/1991399/0/ley-de-transparencia/actitudes-politicas/congreso/](http://www.20minutos.es/noticia/1991399/0/ley-de-transparencia/actitudes-politicas/congreso/)
[^3]: [https://okfn.org/](https://okfn.org/)
[^4]: [http://opendatahandbook.org/en/what-is-open-data/](http://opendatahandbook.org/en/what-is-open-data/)
[^5]: Definición completa de "Abierto": [http://opendefinition.org/od/](http://opendefinition.org/od/)
[^6]: [http://openkratio.org/](http://openkratio.org/)
[^7]: [http://www.civio.es/](http://www.civio.es/)
[^8]: [http://quehacenlosdiputados.net/](http://quehacenlosdiputados.net/)
[^9]: [http://sunlightfoundation.com/](http://sunlightfoundation.com/)
[^10]: [http://www.mjusticia.gob.es/cs/Satellite/es/1215197983369/Estructura\_P/1215198328530/Detalle.html](http://www.mjusticia.gob.es/cs/Satellite/es/1215197983369/Estructura_P/1215198328530/Detalle.html)
[^11]: [http://registries.opencorporates.com/jurisdiction/es](http://registries.opencorporates.com/jurisdiction/es)
[^12]: Zara España SA: [https://opencorporates.com/companies/es/15022510](https://opencorporates.com/companies/es/15022510)
[^13]: Google Inc.: [https://opencorporates.com/companies/us\_ca/C2474131](https://opencorporates.com/companies/us_ca/C2474131)
