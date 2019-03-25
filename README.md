**Repository Name:** whw2019\_Mapping\_Groundwater\_Contaminants

**Project Title:** Mapping Co-Occurrence of Geogenic Groundwater Contaminants of Concern

**Collaborators on this Project**
- Project Lead - Katya Cherukumilli
- Data Science Lead - Rohit Khattar

**The Problem**

300 million people worldwide are at risk of irreversible crippling disorders, internal cancers, and early mortality due to consumption of groundwater containing naturally occurring (&quot;geogenic&quot;) arsenic and fluoride. In recent years, there has been increasing public interest to appropriately manage and protect high-quality groundwater aquifers for drinking water and irrigation in drought-stricken regions (e.g., Western U.S., India, etc.). Our project aims to map the co-occurrence of multiple contaminants since most maps currently focus on an individual contaminant.

**Application Example**

This project seeks to characterize the spatial and temporal heterogeneity and potential co-occurrence of inorganic groundwater contaminants (i.e., As, F-, NO3-, Cr, Se, Mn, and U) in vertical groundwater profiles. The co-occurrence of these emerging contaminants in groundwater aquifers and individual wells has been understudied and underreported. However, recent studies have begun drawing geochemical links between the co-occurrence of various contaminants in the U.S. (nitrate and uranium), Cambodia (arsenic and manganese), and India, China, Mexico and Latin America (arsenic, fluoride, and nitrate).

_Example of an application: In the US, agricultural families in the CA central valley and eastern WA have a greater risk of exposure to nitrate due to the heavy use of nitrate-containing fertilizers that contaminate the local groundwater. The extent to which these rural populations are ALSO simultaneously exposed to arsenic and chromium is not known, but these regions have reported those contaminants as well._

**Existing Methods**

Because disease surveillance and epidemiological data are often not available at the community level, some researchers at [EAWAG](https://www.eawag.ch/en/research/humanwelfare/drinkingwater/wrq/risk-maps/) have begun employing statistical models to predict the occurrence of arsenic and fluoride in groundwater based on various geochemical, lithological, and climatological indicators (e.g., water pH, DO, Eh, [ions], alkalinity, aridity, rock type, temperature). However, two shortcomings of these mapping efforts are that they only model the distribution of groundwater contaminants in two dimensions (x-y) and they only consider one contaminant at a time. Although overlaying existing predictive models hints at the possibility for co-occurring contaminants, by ignoring the key variables affecting water quality like depth and time, these aggregate maps may drastically over-predict co-occurrence and can be misleading. This work will be pivotal to identify vulnerable populations facing disproportionate health risks from contaminated groundwater (e.g., native, rural, and lower-income minority communities).

**Specific Objectives**

1. Data visualization of categorical geospatial data
    - This will be done by identifying contaminants of concern and geographical regions based on the available data.
2. Compile and wrangle existing water quality data from national databases
    - Look for data on contaminant concentration, sampling well depth, water quality parameters (pH, DO, Eh, TDS, etc.), and sampling lat/long info.
3. 3D Data visualization of categorical geospatial data: Possibly a 3-D map using mapping JS libraries in Tethys
4. Overlay maps to determine potential co-occurrence
5. Data Integration:  Overlay water quality maps with other layers containing socio-economic and demographic information
6. Public information communication application: Highlight key populations at risk of detrimental health impacts due to contaminant exposure

**Proposed Methods/Tools**

We would like to build a web application based on Tethys ([Click Here](http://docs.tethysplatform.org)) that a user may search for high co-occurrence of contaminants in their region of interest. This application may possibly provide the following features:

- Regional data shown as a raster overlay on the map
- Ability to search and zoom to a specific location of interest to the user by allowing user to search by zip/location. Use google&#39;s/OpenMap&#39;s reverse geolocation api to obtain a location.
- Possibly do some geo-processing using ArcGIS or a geoprocessing python package to show user some more detailed data by kriging or interpolating in case we don&#39;t have a lot of detailed data in that region
- Host data containing socio-economic/demographic fields as available layers on the application so people may overlay those with contaminant data to draw potential impact of these factors

**Sample Data**

***International and National Groundwater Databases***

1. EAWAG Groundwater Assessment Platform [(GAP)](https://www.eawag.ch/en/research/human-welfare/drinkingwater/gap/): GAP provides following datasets as Shapefiles (downloading possibly could be automated):
    - GroundWater Quality Prediction (Worldwide Data)
    - Global Arsenic/Fluoride concentrations
    - UNICEF Prediction maps
    - Geology, Climate and Population Maps

1. International Groundwater Resources Assessment Center (IGRAC) Groundwater Quality Maps: [Click here](https://www.un-igrac.org/ggis/groundwater-quality)

***Indian Databases***

1. India Central Ground Water Board (CGWB) Database: [Click Here](http://cgwb.gov.in/GW-data-access.html) and [here](http://www.india-wris.nrsc.gov.in/GWL/GWL.html?UType=R2VuZXJhbA==?UName=)
    - This source contains well data from India for the post Monsoon 2016 season. 
    - There is a csv download option available that provides inches of rainfall measured.

1. Indian Water Tool: The IWT is the first of its kind, a comprehensive, high-resolution, user-friendly, and publicly available tool to help companies, and other water users identify their water risks, and plan their interventions for water management in India.
    - We have the source code and a good [documentation](https://www.indiawatertool.in/Methodology/index.html?page=3) available to utilize this data if we need to.

***US Databases***

1. USGS Water Quality Data:[Here](https://water.usgs.gov/owq/data.html)
2. WA Department of Ecology: [Here](https://ecology.wa.gov/Water-Shorelines/Water-quality/Groundwater/Groundwater-resources)
    - Has water data including wells data, water quality survey from 2014 in terms of geodatabases

***Demographic data***

- US Census: [Here](https://www.census.gov/quickfacts/fact/table/US/PST045217)
- World Bank: [Here](https://data.worldbank.org)


**Background Reading**

1. ***General Groundwater Well Contamination***

    - Jasechko, S.; Perrone, D.; Befus, K. M.; Bayani Cardenas, M.; Ferguson, G.; Gleeson, T.; Luijendijk, E.; McDonnell, J. J.; Taylor, R. G.; Wada, Y.; et al. Global aquifers dominated by fossil groundwaters but wells vulnerable to modern contamination. _Nat. Geosci._2017, _10_, 425.

1. ***Arsenic***

    - Rodríguez-Lado, L.; Sun, G.; Berg, M.; Zhang, Q.; Xue, H.; Zheng, Q.; Johnson, C. A. (2013)  Groundwater arsenic contamination throughout China,  _Science_, 341(6148), 866-868, [doi:10.1126/science.1237484](http://doi.org/10.1126/science.1237484), [Institutional Repository](https://www.dora.lib4ri.ch/eawag/islandora/object/eawag:7346)
    - Amini, M.; Abbaspour, K. C.; Berg, M.; Winkel, L.; Hug, S. J.; Hoehn, E.; Yang, H.; Johnson, C. A. (2008)  Statistical modeling of global geogenic arsenic contamination in groundwater,  _Environmental Science and Technology_, 42(10), 3669-3675, [doi:10.1021/es702859e](http://doi.org/10.1021/es702859e), [Institutional Repository](https://www.dora.lib4ri.ch/eawag/islandora/object/eawag:5733)

1. ***Flouride***
    - Amini, M.; Mueller, K.; Abbaspour, K. C.; Rosenberg, T.; Afyuni, M.; Møller, K. N.; Sarr, M.; Johnson, C. A. (2008)  Statistical modeling of global geogenic fluoride contamination in groundwaters,  _Environmental Science and Technology_, 42(10), 3662-3668, [doi:10.1021/es071958y](http://doi.org/10.1021/es071958y), [Institutional Repository](https://www.dora.lib4ri.ch/eawag/islandora/object/eawag:5789)
    - Joel Podgorski &amp; Michael Berg (EAWAG) &amp; Pawan Labhasetwar (NEERI), ES&amp;T 2018. _Prediction modeling and mapping of groundwater fluoride contamination throughout India._

1. ***Co-Occurring Contamination***

    - Kundu, M. C.; Mandal, B. Agricultural Activities Influence Nitrate and Fluoride Contamination in Drinking Groundwater of an Intensively Cultivated District in India. _Water. Air. Soil Pollut._2009, _198_ (1–4), 243–252 DOI: 10.1007/s11270-008-9842-5.
    - Lockwood, J. R.; Schervish, M. J.; Gurian, P. L.; Small, M. J. Analysis of Contaminant Co-Occurrence in Community Water Systems. _J. Am. Stat. Assoc._2004, _99_ (465), 45–56 DOI: 10.1198/016214504000000061.
    - Jadhav, S. V.; Bringas, E.; Yadav, G. D.; Rathod, V. K.; Ortiz, I.; Marathe, K. V. Arsenic and fluoride contaminated groundwaters: A review of current technologies for contaminants removal. _J. Environ. Manage._2015, _162_, 306–325 DOI: 10.1016/j.jenvman.2015.07.020.
    - Buschmann, J.; Berg, M.; Stengel, C.; Sampson, M. L. Arsenic and manganese contamination of drinking water resources in Cambodia: Coincidence of risk areas with low relief topography. _Environ. Sci. Technol._2007, _41_ (7), 2146–2152 DOI: 10.1021/es062056k.
    - Wen, D.; Zhang, F.; Zhang, E.; Wang, C.; Han, S.; Zheng, Y. Arsenic, fluoride and iodine in groundwater of China. _J. Geochemical Explor._2013, _135_, 1–21 DOI: 10.1016/j.gexplo.2013.10.012.
    - Mahmood, S. J.; Taj, N.; Parveen, F.; Fahmida, U.; Usmani, T. H.; Azmat, R. Arsenic, Fluoride and Nitrate in Drinking Water: The Problem and its Possible Solution. _Res. J. Environ. Sci._2007, _1_ (4), 179–184 DOI: 10.3923/rjes.2007.179.184.
    - Singh, A. K.; Bhagowati, S.; Das, T. K.; Yubbe, D.; Rahman, B.; Nath, M.; Obing, P.; Singh, W. S. K.; Renthlei, Z., C.; Pachuau, L.; et al. ASSESSMENT OF ARSENIC, FLUORIDE, IRON, NITRATE AND HEAVY METALS IN DRINKING WATER OF NORTHEASTERN INDIA. _ENVIS Bull.  Himal. Ecol._2003, _16_ (2), 1–96.
    - Alarcón-Herrera, M. T.; Bundschuh, J.; Nath, B.; Nicolli, H. B.; Gutierrez, M.; Reyes-Gomez, V. M.; Nuñez, D.; Martín-Dominguez, I. R.; Sracek, O.; Rasool, A.; et al. Co-occurrence of arsenic and fluoride in groundwater of semi-arid regions in Latin America: Genesis, mobility and remediation. _J. Hazard. Mater._2015, _262_ (24), 19729–19746 DOI: 10.1016/j.jhazmat.2012.08.005.
    - Kumar, M.; Das, A.; Das, N.; Goswami, R.; Singh, U. K. Co-occurrence perspective of arsenic and fluoride in the groundwater of Diphu, Assam, Northeastern India. _Chemosphere_2016, _150_, 227–238 DOI: 10.1016/j.chemosphere.2016.02.019.
    - Reyes-Gómez, V. M.; Alarcón-Herrera, M. T.; Gutiérrez, M.; López, D. N. Fluoride and arsenic in an alluvial aquifer system in Chihuahua, Mexico: Contaminant levels, potential sources, and co-occurrence. _Water. Air. Soil Pollut._2013, _224_ (2) DOI: 10.1007/s11270-013-1433-4.
    - Pi, K.; Wang, Y.; Xie, X.; Su, C.; Ma, T.; Li, J.; Liu, Y. Hydrogeochemistry of co-occurring geogenic arsenic, fluoride and iodine in groundwater at Datong Basin, northern China. _J. Hazard. Mater._2015, _300_, 652–661 DOI: 10.1016/j.jhazmat.2015.07.080.
    - Rango, T.; Vengosh, A.; Dwyer, G.; Bianchini, G. Mobilization of arsenic and other naturally occurring contaminants in groundwater of the main ethiopian rift aquifers. _Water Res._2013, _47_ (15), 5801–5818 DOI: 10.1016/j.watres.2013.07.002.
    - Nolan, J.; Weber, K. A. Natural Uranium Contamination in Major U.S. Aquifers Linked to Nitrate. _Environ. Sci. Technol. Lett._2015, _2_ (8), 215–220 DOI: 10.1021/acs.estlett.5b00174.
