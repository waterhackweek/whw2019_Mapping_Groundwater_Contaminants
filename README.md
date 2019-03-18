# Project Title: Mapping Co-Occurrence of Geogenic Groundwater Contaminants of Concern

# Collaborators on this Project:
•	Project Lead - Katya Cherukumilli
•	Data Science Lead - Rohit Khattar

# The Problem:
300 million people worldwide are at risk of irreversible crippling disorders, internal cancers, and early mortality due to consumption of groundwater containing naturally occurring (“geogenic”) arsenic and fluoride. In recent years, there has been increasing public interest in drought-stricken regions (e.g., Western U.S., India, etc.) to appropriately manage and protect high-quality groundwater aquifers for drinking water and irrigation. 

# Application Example:
This project seeks to visualize the spatial and temporal heterogeneity and potential co-occurrence of inorganic groundwater contaminants (i.e., As, F-, NO3-, Se, Mn, and U) in vertical groundwater quality profiles. This work will be pivotal to identify vulnerable populations facing disproportionate health risks from contaminated groundwater (e.g., native, rural, and lower- income minority communities). The co-occurrence numerous emerging inorganic geogenic contaminants of concern (e.g., arsenic, fluoride, nitrate, chromium, manganese, uranium, and selenium) in groundwater aquifers and individual wells has been understudied and underreported. However, recent studies have begun drawing geochemical links between the co-occurrence of various contaminants in the U.S. (nitrate and uranium), Cambodia (arsenic and manganese), and India, China, Mexico and Latin America (arsenic, fluoride, and nitrate).

# Sample Data  : 
1.	International and National Groundwater Databases

•	EAWAG Groundwater Assessment Platform: https://www.eawag.ch/en/research/human-welfare/drinkingwater/gap/

•	India Central Ground Water Board (CGWB) Database

o	http://cgwb.gov.in/GW-data-access.html

o	http://www.india-wris.nrsc.gov.in/GWL/GWL.html?UType=R2VuZXJhbA==?UName= 

•	USGS Water Quality Data: https://water.usgs.gov/owq/data.html

•	WA Department of Ecology: https://ecology.wa.gov/Water-Shorelines/Water-quality/Groundwater/Groundwater-resources

•	British Geologic Survey (BGS): https://www.bgs.ac.uk/research/groundwater/datainfo/datainformation.html

•	International Groundwater Resources Assessment Center (IGRAC) Groundwater Quality Maps: https://www.un-igrac.org/ggis/groundwater-quality

2.	Demographic data

•	US Census: https://www.census.gov/quickfacts/fact/table/US/PST045217

•	World Bank: https://data.worldbank.org

# Specific Objectives/Questions: 
1.	Identify high priority contaminants of concern and geographical regions to map
2.	Compile and wrangle existing water quality data from national databases
a.	Look for data on contaminant concentration, sampling well depth, water quality parameters (pH, DO, Eh, TDS, etc.), and sampling lat/long info. 
3.	Develop 3D map of groundwater contaminants across a certain region (x, y, z)  (ggplot, R?)
4.	Overlay maps to determine potential co-occurrence
5.	Overlay water quality maps with other layers containing socio-economic and demographic information (arc-GIS)
6.	Highlight key populations at risk of detrimental health impacts due to contaminant exposure

# Existing Methods: 

Because disease surveillance and epidemiological data are often not available at the community level, some researchers at EAWAG have begun employing statistical models to predict the occurrence of arsenic and fluoride in groundwater based on various geochemical, lithological, and climatological indicators (e.g., water pH, DO, Eh, [ions], alkalinity, aridity, rock type, temperature). However, two shortcomings of these mapping efforts are that they only model the distribution of groundwater contaminants in two dimensions (x-y) and they only consider one contaminant at a time. Although overlaying existing predictive models hints at the possibility for co-occurring contaminants, by ignoring the key variables affecting water quality like depth and time, these aggregate maps may drastically over-predict co-occurrence and can be misleading. 

# Proposed Methods/Tools:
TBD

# Background Reading: 

# General Groundwater Well Contamination
•	Jasechko, S.; Perrone, D.; Befus, K. M.; Bayani Cardenas, M.; Ferguson, G.; Gleeson, T.; Luijendijk, E.; McDonnell, J. J.; Taylor, R. G.; Wada, Y.; et al. Global aquifers dominated by fossil groundwaters but wells vulnerable to modern contamination. Nat. Geosci. 2017, 10, 425.

# Arsenic
•	Rodríguez-Lado, L.; Sun, G.; Berg, M.; Zhang, Q.; Xue, H.; Zheng, Q.; Johnson, C. A. (2013) Groundwater arsenic contamination throughout China, Science, 341(6148), 866-868, doi:10.1126/science.1237484, Institutional Repository

•	Amini, M.; Abbaspour, K. C.; Berg, M.; Winkel, L.; Hug, S. J.; Hoehn, E.; Yang, H.; Johnson, C. A. (2008) Statistical modeling of global geogenic arsenic contamination in groundwater, Environmental Science and Technology, 42(10), 3669-3675, doi:10.1021/es702859e, Institutional Repository

# Fluoride
•	Amini, M.; Mueller, K.; Abbaspour, K. C.; Rosenberg, T.; Afyuni, M.; Møller, K. N.; Sarr, M.; Johnson, C. A. (2008) Statistical modeling of global geogenic fluoride contamination in groundwaters, Environmental Science and Technology, 42(10), 3662-3668, doi:10.1021/es071958y, Institutional Repository

•	Joel Podgorski & Michael Berg (EAWAG) & Pawan Labhasetwar (NEERI), ES&T 2018. Prediction modeling and mapping of groundwater fluoride contamination throughout India.

# Co-Occurring Contamination
•	Kundu, M. C.; Mandal, B. Agricultural Activities Influence Nitrate and Fluoride Contamination in Drinking Groundwater of an Intensively Cultivated District in India. Water. Air. Soil Pollut. 2009, 198 (1–4), 243–252 DOI: 10.1007/s11270-008-9842-5.

•	Lockwood, J. R.; Schervish, M. J.; Gurian, P. L.; Small, M. J. Analysis of Contaminant Co-Occurrence in Community Water Systems. J. Am. Stat. Assoc. 2004, 99 (465), 45–56 DOI: 10.1198/016214504000000061.

•	Jadhav, S. V.; Bringas, E.; Yadav, G. D.; Rathod, V. K.; Ortiz, I.; Marathe, K. V. Arsenic and fluoride contaminated groundwaters: A review of current technologies for contaminants removal. J. Environ. Manage. 2015, 162, 306–325 DOI: 10.1016/j.jenvman.2015.07.020.

•	Buschmann, J.; Berg, M.; Stengel, C.; Sampson, M. L. Arsenic and manganese contamination of drinking water resources in Cambodia: Coincidence of risk areas with low relief topography. Environ. Sci. Technol. 2007, 41 (7), 2146–2152 DOI: 10.1021/es062056k.

•	Wen, D.; Zhang, F.; Zhang, E.; Wang, C.; Han, S.; Zheng, Y. Arsenic, fluoride and iodine in groundwater of China. J. Geochemical Explor. 2013, 135, 1–21 DOI: 10.1016/j.gexplo.2013.10.012.

•	Mahmood, S. J.; Taj, N.; Parveen, F.; Fahmida, U.; Usmani, T. H.; Azmat, R. Arsenic, Fluoride and Nitrate in Drinking Water: The Problem and its Possible Solution. Res. J. Environ. Sci. 2007, 1 (4), 179–184 DOI: 10.3923/rjes.2007.179.184.

•	Singh, A. K.; Bhagowati, S.; Das, T. K.; Yubbe, D.; Rahman, B.; Nath, M.; Obing, P.; Singh, W. S. K.; Renthlei, Z., C.; Pachuau, L.; et al. ASSESSMENT OF ARSENIC, FLUORIDE, IRON, NITRATE AND HEAVY METALS IN DRINKING WATER OF NORTHEASTERN INDIA. ENVIS Bull.  Himal. Ecol. 2003, 16 (2), 1–96.

•	Alarcón-Herrera, M. T.; Bundschuh, J.; Nath, B.; Nicolli, H. B.; Gutierrez, M.; Reyes-Gomez, V. M.; Nuñez, D.; Martín-Dominguez, I. R.; Sracek, O.; Rasool, A.; et al. Co-occurrence of arsenic and fluoride in groundwater of semi-arid regions in Latin America: Genesis, mobility and remediation. J. Hazard. Mater. 2015, 262 (24), 19729–19746 DOI: 10.1016/j.jhazmat.2012.08.005.

•	Kumar, M.; Das, A.; Das, N.; Goswami, R.; Singh, U. K. Co-occurrence perspective of arsenic and fluoride in the groundwater of Diphu, Assam, Northeastern India. Chemosphere 2016, 150, 227–238 DOI: 10.1016/j.chemosphere.2016.02.019.

•	Reyes-Gómez, V. M.; Alarcón-Herrera, M. T.; Gutiérrez, M.; López, D. N. Fluoride and arsenic in an alluvial aquifer system in Chihuahua, Mexico: Contaminant levels, potential sources, and co-occurrence. Water. Air. Soil Pollut. 2013, 224 (2) DOI: 10.1007/s11270-013-1433-4.

•	Pi, K.; Wang, Y.; Xie, X.; Su, C.; Ma, T.; Li, J.; Liu, Y. Hydrogeochemistry of co-occurring geogenic arsenic, fluoride and iodine in groundwater at Datong Basin, northern China. J. Hazard. Mater. 2015, 300, 652–661 DOI: 10.1016/j.jhazmat.2015.07.080.

•	Rango, T.; Vengosh, A.; Dwyer, G.; Bianchini, G. Mobilization of arsenic and other naturally occurring contaminants in groundwater of the main ethiopian rift aquifers. Water Res. 2013, 47 (15), 5801–5818 DOI: 10.1016/j.watres.2013.07.002.

•	Nolan, J.; Weber, K. A. Natural Uranium Contamination in Major U.S. Aquifers Linked to Nitrate. Environ. Sci. Technol. Lett. 2015, 2 (8), 215–220 DOI: 10.1021/acs.estlett.5b00174.
