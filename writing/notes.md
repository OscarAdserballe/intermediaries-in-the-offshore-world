New strucutre:

Motivation:

Public Economics: First, motivating from public finance; the top-end problem: Demand-side to Supply-side in the literature.

Ok, so focusing more on the supply-side. Alstadsæter et al. (2019), Lafitte (2024) as primary examples.

(Mostly) IPE literature: we know a lot about the location of these offshore lcoations, we know a lot about the people demand these services

But we don't know that much about the people in the middle. A couple of scattered results:
1. Harrington (2016) and Hoang (2022) providing solid ethnographic evidence in the form of micro-sociological accounts
2. A bit from the Tax Experiment in Chile from 2024
3. And a little about the location of them.

At the same time, IPE literature ever-increasing focus on these professionals in the middle. Incredibly important - and adding to that supply-side public economics literature.

Contributing with a few results, drawn from the ICIJ data, about the patterns of specialisations of intermediaries:
* Corroboaring a few paper son the locations of where htey're to be found
* Patterns of client specialisation: in a few countries and
* Instrumetns and Legal Technologies
* And trying to affirm a bit of a typology presented in the EU (2017) paper.

Results in line with the notions of relational capitalism consistent with: Neely (2021), Hoang (2022), Harrington (2016), 

Grannoveter 1973: Social Network as a way of linking micro and macro-evidence.


#### In the Applied Network Science branch of things:

Kejriwal \& Dang 2020: Deviating from traditional power-law structure. 

"It should be noted that ICIJ itself claims on its website, dedicated to the Panama Papers (we provide a link in the next section), that mere presence of an entity in the Panama Papers does not suggest that it is engaged in shadowy or illicit activities. In this article, in keeping with this recommendation, we take a more agnostic view and aim to uncover structural insights using the framework of network science"


https://www.eurekalert.org/news-releases/690125:

"It was really unusual. The degree of fragmentation is something I have never seen before," said Kejriwal. "I'm not aware of any other network that has this kind of fragmentation."

Some very special properties of the network



#### The PANA studies: EP's Committee of Inquiry into Money Laundering, Tax Avoidance and Tax Evasion

Two very relevant papers:
Willem Pieter DE GROEN (CEPS) and III: Role of advisors and intermediaries in the schemes revealed in the Panama Papers



Overall policy recommendation from both: Sharpen up levels of self-regulation in these professions usch that they don't negatively ocntribute to the phenomenon of tax avoidance and evasion.

Most intermediaries not located in onshore jurisdictions, so we can't directly enforce regulations against them. But, onshore jurisdictions can can put pressure on offshore jurisdictions to broaden the scope of regulations they have there (de Groen 2017)

* How much hsa been done in this respect? What are the existing regulations?




### The Race Between Tax Enforcement and Tax Planning: Evidence from a Natural Experiment in Chile

Authors: Bustos, Pomeranz, Serrato, Zucman, Belda

Using imlementation of OECD transfer pricing standards as natural experiment. Result: Did not reduce propensity of multinationals "to make tax-motivated payments to their foreign affiliates" and nothing on tax either.

Three steps:
1. Building conceptual framework, implementing some quantitative analysis using administrative micro-data and conduct in-depth qualitatiative interviews to understand the mechanisms at play.
2. Effects of OECD reform:
    * First, showing multinationals engage in tax-motivated transactions using intra-firm flows, exploiting changes in tax rates. 1\% increase in tax rate of destination country, associated with increase in payments to affiliates of between 4.5\% and 4.9\%.
    * Second, diff-in-diff of whether reform was effective at reducing multinationals' propensity to mkae intra-group payments to lower-tax countries.
3. In-depth interviews with transfer pricing experts in Chilean MNEs and consulting firms. Big Four consultants specialising in transfer pricing increased from 8 to 95. Consulting firms see additional enforcement as a business opportunity! Intermediaries benefit from regulation!    

Unlike what has been found for small firms with simple accounting structures, strengthening reporting requirements and paper trails insufficietn to icnrease tax collection from large firms.
Concretely, two lessons:
1. Importance of paper trails for tax monitoring
2. Need for credible enforcement.

###### Role of the Tax Advisory Industry

In-depth qualitiative interviews with experts.
Six primary insights:
1. Reform boon to the tax advisory industry
2. Strong surge in demand for specialised consulting services because of complexity
3. 
4. Supply was highly ealastic: advisory industry could justs redirect professionals to Chile
5. Tax planning advice: centralise cost centeres in fewer locatoins
6. Tax administrators heavily outmatched by consulting firms in number of staff as well as salaries.


### Unfollow the Money

Authors: Stausholm, Garcia-Bernardo

Geographical mapping of corporate tax advisors in line with recent trend of empahsising improtance of micro-level actors.
Empirical approach based on LinkedIn
Located in EU and the OECD rather than in places targetted. Correlates with locations where there's managerial and financial activity.

"States enable tax avoidance, but micro-level actors facilitate it"

States only a necessary condition; not sufficinet.

Results: Really in the major financial centres of the world. New York, San Francisco, London, Hong Kong, Singapore, Zurich, Amsterdam, Luxembourg.

"The tax practitioners we are interested in are solely those who are responsible
for managing and advising on corporate taxation for larger firms. Since this is not
an established function with set titles and accreditations, titles, and backgrounds
can vary between firms and countries. We therefore read job ads and LinkedIn
profiles containing the different types of titles to ensure that we understood the
practitioners behind the titles. Illustrative examples include an ‘International Tax
Manager’ at a large shipping firm, a ‘Tax Manager’ at a large Big Four consulting
firm, and a ‘Head of Corporate Tax’ at a large international bank"


# Future Classification

Are these intermediaries international? 

Are they located offshore or onshore? (cf. Stausholm)


# Questions for Rasmus

What the hell about regulation? Why can we not just legally punish attempts at tax avoidance, if the intent was so lie for example Zucman mentions in his book are laws in place in the US that would allow for this?

Is it sufficiently theoretical?


Target intermediaries from one's own country. At least a huge short-term shock, go medieval on their ass. In fact, not even weaponising interdependence, rather just... penalising one's own countrymen for engagin in illegal activity. A way out from the difficult cooperative games that are played at the international level.



##### Degree distribution of intermediaries

* Show power-alw distribution fits well
* Use MLE to fit power law: Fits far petter than competing fat-tailed distributions like log-normal distributions
* Goodness-of-fit using Kolmogorov-Smirnov statistics. ISSUE: assumes we know parameter a priori - not fitting it a posterriori like here with MLE. Recall Lillefors correction in the context of wehn we test against normal distributions. If this is what we want, this is the seminal paper:
* Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. SIAM Review, 51(4), 661-703. This paper provides a rigorous statistical framework for identifying and validating power-law distributions.
* An alternative to this is just comparing the fit of the power-law distribution to the fit of a log-normal distribution. 
* Note, we already have Kejriwal \& Dang (2020) showing this, so we can just use their results if need be




## Geogprahical Specialisation

##### How many countries do intermediaries incorporate entities in?
* Distribution of the number of countries they incorporate in

Transition: Doesn't account for the fact that some just incorporate more!
* Distirbution of entropy scores

Transition: Groups of countries they incorporate in

Graph of the countries they incorporate in approach: 
* Edge weight increases, if an intermediary incorporates in ocuntries in common. E.g. if he has entities in Singapore and Hong kong they are proivded one more to their weight.
* When visualising, only showing edge to reduce space from about ~125 countries according to rule of some minimum lift OR Cooccurrence threshold (E.g. minimum lift of 1.5 or minimum cooccurence of 10%)
a. Colouring in according to regime type
b. Colouring in according to louvain community detection
* Reporting highest in-betweenness scores 
* Reporting associations with highest lift scores + Fisher exact test to confirm statistical significance


##### Which Jurisidctions do they Incorporate in?
* Power-law distribution of how many they incorporate
* Distribution of the number of jurisdictions they incorporate in

Same transition:
* Distirbution of entropy scores

Same approach as above with the jurisdictions they incorporate in.
* EXCEPT: Colouring in according to legal technology types
* Reporting highest in-betweenness scores
* Reporting associations with highest lift scores + Fisher exact test to confirm statistical significance

##### What are the most common intermediary-country to entity-country/jurisdiction pair? Cyprus and Singapore case studies
* Bipartite graph too difficult to visualise, so we just show the distribution of two countries: Cyprean intermediaries and Singaporean, for example


### Functional Specialisation of Intermediaries

##### Differences in Entropies + Bearer Shares




##### Differences in Degrees:
* CDF of the different types showing it.
* Comparison of random smaple vs. the the ones in the top 500 - e.g. administrators the ones that have an incredibly high degree, whereas we tax experts and legal experts more personal advisory. Not connected to as many.
* Testing signifianace of degree differences using Negative Binomial random component + natural logarithm as the link function?

##### Clustering different intermediaries and seeing if they cluster by type
Idea: Though wit hthat many countries and jurisdictions we'd end up with a super sparse matrix, we can do some feature selection exactly by virtue of the fact that countries and officers are so tightly located. We have this long dataframe in this case, with dictionary objects flattened out as columns, which we then proceed to try to cluster then doing some pca/t-sne/mds to visualise in 2-dimensions






# Results 

## Overview of the dataset

### Overview of where the relevant elements for our sake are concentrated

Plot: Preliminary_Geography_Overview.png

Highly, highly concentrated. Especially notable in terms of the jurisdictions they incorporate in with some 98% of the entities incorporated represented by just 15 countries.

### Degree Distribution of Intermediaries

Plot: Preliminary_Powerlaw_Fit.png

Log-likelihood ratio (Power Law vs. Log-normal): R = 57.0287, p-value = 0.0000

Framing this whole thesis: A lot of powerlaw-esque distributions are going to come up. Not least, the degree distribution of intermediaries.

## Geographical Specialisation

### Intermediaries at Country-Level: Highly specialised cliente, jurisdictions not so much.

Starting at the highest aggregation level, where intermediaries are grouped at the country level.

Plot: Geography_Country_Heatmaps_Top5.png
Plot: Geography_Country_Heatmaps_Top6_10.png
Plot: Geography_Country_Heatmaps_Top11_15.png

Intermediaries from a given country have a very strong tendency to serve clients from their own country. Jurisdictions a bit more agnostic: significantly higher entropy of jurisdictions a given country's intermediaries incorproate in compared to where the entities have their main activity. Even though there's not that many jurisdictions the (overwhelming!) majority incorporate in, intermediaries at a country-levle od spread out far more.

We test this formally with a Kolmogorov-Smirnov (two-sample) test, and find that the distributions are significantly different.

Plot: Geography_Country_Level_Entropy_Distribution.png

And as a fun tid-bit, here's Cyprus, well-documented case of high links to Russia. Russia generally underrepresented here, but here we have 12% of all entities incorproate dby intermediaries incorproated here in Russia. In other words, it has very high lift. 

These numbers themselves prime canddiates for fishing expeditions to get the most interesting link, but that is for another thesis.

Plot: Geography_Country_Heatmaps_Cyprus.png

### Groups of Countries Served by Intermediaries

Aggregating up at the level of countries, clear patterns of specialisation especially in the countries they have clients. 
But what of the specific clusters of countries served by intermediaries?

Plot: Geography_Distribution_of_Countries_by_Intermediary.png

At intermediary level, likewise, highly concentrated in clientele across one or two countries. Even as they get bigger, there's very low correlation between the number of countries served and the number of clients served.

Two nodes connecting if an intermediary has at least one entity in both countries. For example, if a given intermeidary has an entity in Singapore, Hong Kong and the Bahamas, three edges are drawn between each pair of countries.
Ending up with a graph of 126 nodes, and a lot of edges.

Table: Summary Statistics (include density, number of nodes, number of edges, etc.)

Let's look at the most important nodes in these networks.  A huge challenge visualising graphs like these, so we filter them with toosl from association analysis. Here, edges only shown if 1) reaches a sufficiently high support threshold (0.008 of all intermediaries' connections in this case), and 2) lift score of 1.5 or higher, guaranteeing that there's signal in the association shown. It's therefore not a visualisation of the entire network, but the most important connections that bear strength and signal. 

(And magic values like the ones here are always dangerous, but this provided, in my opinion, the best overview of a select few without overwhelming the reader iwth too much information. Varying it across lift thresholds and support thresholds, this remains the underlying "backbone" of the network)

Two ways they've been coloured: 1) By Louvain communities. This is an atheoretical approach, but exactly why we want to use this, and 2) By Regime type. Idea: Intermediaries have difficulty operating in several countries with different regime types - relational capital too difficult to build. But again, doesn't seem like they're that important, as doesn't correlate well with the Louvain Communities, nor does anything really pan out in the association analysis and centrality scores.

Plot: Geography_Cross_Country_Network.png

The two graphs, "By Regime (VDem)" and "By Community (Louvain Method)," display a filtered network of countries. This filtering is key: edges are only shown if they represent a connection used by a substantial portion of intermediaries (support ≥0.008) and the connection is significantly stronger than what would be expected by chance (lift score ≥1.5). Therefore, we are looking at a "backbone" of the strongest, most meaningful co-service relationships, not the entire web of connections. The text states this filtered graph has 15 nodes and 23 edges (though 14 nodes are clearly identifiable in the provided image: USA, BMU, CHN, HKG, CYM, VGB, SGP, TWN, MYS, COK, IDN, PAN, SYC, BHS).

1) Interpretation of Graph Structure Itself

Filtered Backbone: The most immediate observation is that the filtering has revealed a sparse but highly structured network. This isn't a dense, undifferentiated hairball; specific pathways and clusters emerge.
Central Core: Both graphs show a relatively central core of interconnected nodes, particularly involving VGB (British Virgin Islands), CYM (Cayman Islands), SGP (Singapore), and their links to HKG (Hong Kong) and BMU (Bermuda).
Regime Heterogeneity (Left Graph):
There isn't a clear, large-scale clustering purely by regime type. For instance, the central cluster mentioned above includes Micro-states (VGB, CYM, BMU), Closed Autocracies (HKG), and Electoral Autocracies (SGP).
Liberal Democracies like USA and TWN (Taiwan) are present but connect to nodes of different regime types (USA to BMU (Micro-state); TWN appears linked into a cluster with SGP (Electoral Autocracy) and VGB/CYM (Micro-states) in the community graph).
This visual evidence supports your textual observation: "Regime type... doesn't seem like they're that important, as doesn't correlate well with the Louvain Communities, nor does anything really pan out in the association analysis and centrality scores."
Community Structure (Right Graph - Louvain): The Louvain method, being atheoretical, reveals data-driven groupings based on the density of connections:
Comm 0 (Dark Blue): This is the largest community, featuring VGB, SGP, CYM, TWN, MYS (Malaysia), IDN (Indonesia), COK (Cook Islands). This group highlights strong ties between several offshore financial centers (VGB, CYM, COK), key Asian economies (SGP, MYS, IDN), and Taiwan. It's notably mixed in terms of regime types (Micro-states, Electoral Autocracies, one Liberal Democracy).
Comm 1 (Brown): Comprises USA, BMU, CHN (China), HKG. This is a potent cluster linking the world's two largest economies and a major Asian financial center (HKG) with a key Micro-state (BMU). Again, regime types are mixed (Liberal Democracy, Micro-state, Closed Autocracies).
Comm 2 (Light Blue): A smaller community of PAN (Panama), SYC (Seychelles), BHS (Bahamas). This groups an Electoral Democracy with an Electoral Autocracy and a Micro-state, suggesting another distinct sphere of intermediary operations.
Connectivity: Most nodes are connected within 2-3 steps in this backbone, indicating that these key players are relatively close in this high-strength network. There are no isolates in the visualized portion.
2) What's Revealed by the Centrality Metrics

(Note: The provided centrality tables are for the full network of 121 nodes, while the graph is a filtered 15-node version. We interpret how the top-ranked nodes from the full network feature in this backbone.)

VGB (British Virgin Islands - Micro-state):
Dominant in the full network: Highest betweenness (0.184) and eigenvector centrality (0.136).
This dominance is visually confirmed in the filtered graph. VGB is a key node in Comm 0, connecting to CYM and SGP directly in this backbone. Its high betweenness suggests it acts as a crucial bridge in many paths within the overall intermediary network.
USA (Liberal Democracy):
Second highest for both betweenness (0.053) and eigenvector (0.135) in the full network.
In the filtered graph, it's part of the distinct Comm 1, primarily linked to BMU. This implies that while the USA has many connections overall, its strongest backbone connections (high support and lift) might be more specific, here pointing towards Bermuda as a key gateway.
HKG & CHN (Closed Autocracies):
HKG: 3rd for eigenvector (0.133) in the full network. CHN: 6th for eigenvector (0.132).
Their appearance in Comm 1, strongly linked to each other and BMU, highlights a significant intermediary axis. Their high eigenvector scores suggest they are connected to other influential nodes.
Micro-states (BMU, BHS, CYM, etc.):
Many Micro-states (VGB, BHS, BMU) feature in the top 10 for betweenness and/or eigenvector centrality in the full network.
The filtered graph underscores their importance: VGB, CYM, BMU, COK, BHS are all present and play significant structural roles in their respective communities. This suggests they aren't just numerous but form critical, high-strength links. BMU's position in Comm 1 linking USA and CHN/HKG is particularly notable.
SGP (Singapore - Electoral Autocracy):
High eigenvector (0.132) and notable betweenness (0.019) in the full network.
Its position in Comm 0 in the filtered graph, connecting to other key players like VGB and CYM, and also to MYS, reflects its role as an important, well-connected hub with strong specific ties.
In essence, high centrality in the full network often translates to a visible structural role in the filtered backbone, indicating these nodes have numerous and strong/significant connections.

3) What Interesting Associations are Revealed?

This is where the "lift" scores from your "Significant country associations" table become crucial, as the graph visualizes pairs with lift ≥1.5.

Micro-state Synergy:
The graph clearly shows links like VGB-CYM, and the significant associations table confirms this with strong lift values (e.g., VGB-WSM lift 1.87, WSM-CYM lift 6.78, VGB-CYM lift 1.91). WSM (Samoa) isn't explicitly labeled in the image but its association with VGB, CYM, and SGP is very strong in your tables, and it's likely the 15th node of Comm 0.
CYM-BMU: An extremely high lift of 13.47! This is a very strong connection between two Micro-states, visually shown and grouping them in different communities (Comm 0 and Comm 1 respectively), suggesting they might serve different larger networks but intermediaries operating in one are highly likely to be in the other.
The USA-BMU-China/HKG Nexus (Comm 1):
CHN-BMU: Lift of 15.28 (Closed Autocracy - Micro-state). This is an exceptionally strong association. Intermediaries serving Chinese entities are over 15 times more likely to also serve entities via Bermuda than by random chance compared to how both countries are otherwise represented in the data.
USA-BMU: Lift of 4.92 (Liberal Democracy - Micro-state). Another strong link.
This community suggests Bermuda acts as a significant intermediary hub for dealings related to both the USA and China/HKG, facilitated by a common set of specialized intermediaries. This is a powerful finding, showing a Micro-state bridging major, politically distinct economic powers through these high-strength intermediary channels.
Asian Connections (Comm 0 & others):
SGP-MYS: Lift of 5.27 (Electoral Autocracies). A strong regional pairing, both in Comm 0.
SGP's connections to Micro-states: VGB-SGP (lift 1.60), WSM-SGP (lift 3.04), SGP-CYM (lift 3.89), SGP-COK (lift 4.63). Singapore is strongly and multiply connected to various Micro-states within Comm 0.
PAN-SYC-BHS Nexus (Comm 2):
PAN-SYC: Lift of 3.89 (Electoral Democracy - Electoral Autocracy).
The grouping suggests a distinct network where intermediaries specialize in this combination of jurisdictions. The presence of BHS (Micro-state) further points to the role of such jurisdictions in facilitating these connections.
Cross-Regime Links are Common and Strong: The high lift values are not confined to countries with similar regimes. The CHN-BMU link is a prime example. This strongly reinforces the observation that factors other than regime type (e.g., specific financial services, legal systems, historical ties, efficiency, secrecy) are the primary drivers for the formation of these strong co-service ties by intermediaries.

Full country network: 121 nodes, 2716 edges
Network density: 0.3741
Average degree: 44.89
Average clustering coefficient: 0.7728
Number of connected components: 2
Number of singletons: 0
Percentage of singletons: 0.00%

Top 10 countries by betweenness centrality (excluding XXX):
  node  betweenness  eigenvector  appearances               regime
0  VGB     0.184274     0.135730         6285          Micro-state
1  USA     0.053129     0.134776         1042    Liberal Democracy
2  CHE     0.038620     0.131234         1545    Liberal Democracy
3  GBR     0.028499     0.133304         1258    Liberal Democracy
4  MUS     0.023743     0.129268          139    Liberal Democracy
5  BHS     0.020768     0.131846          489          Micro-state
6  BMU     0.020273     0.128895          103          Micro-state
7  PAN     0.019726     0.096285         1203  Electoral Democracy
8  SGP     0.019164     0.131722          578  Electoral Autocracy
9  URY     0.016748     0.030603          318    Liberal Democracy

Top 10 countries by eigenvector centrality (excluding XXX):
  node  eigenvector  betweenness  appearances               regime
0  VGB     0.135730     0.184274         6285          Micro-state
1  USA     0.134776     0.053129         1042    Liberal Democracy
2  GBR     0.133304     0.028499         1258    Liberal Democracy
3  HKG     0.133292     0.016464         2865     Closed Autocracy
4  JEY     0.132590     0.013250          390          Micro-state
5  CHN     0.132406     0.008508          320     Closed Autocracy
6  CAN     0.132285     0.008778          195    Liberal Democracy
7  BHS     0.1s1846     0.020768          489          Micro-state
8  SGP     0.131722     0.019164          578  Electoral Autocracy
9  CYM     0.131492     0.012494          363          Micro-state

Number of nodes: 121, hypothesis tests (pairs): 7260
Bonferroni p-value threshold (@α=0.05): 6.89e-06
Number of significant associations after Bonferroni correction: 58

Significant country associations after Bonferroni correction:
        u    v             u_regime             v_regime  weight   support         lift    odds_ratio       p_value
76    VGB  WSM          Micro-state          Micro-state     401  0.016719     1.870714  2.824422e+00  7.241295e-46
498   WSM  CYM          Micro-state          Micro-state      84  0.003502     6.784861  9.387888e+00  1.344387e-45
105   VGB  CYM          Micro-state          Micro-state     182  0.007588     1.913291  2.886250e+00  9.578337e-23
775   CHN  BMU     Closed Autocracy          Micro-state      21  0.000876    15.281068  2.019830e+01  3.355431e-19
2405  CYM  BMU          Micro-state          Micro-state      21  0.000876    13.470914  1.762655e+01  4.457315e-18
2032  SGP  MYS  Electoral Autocracy  Electoral Autocracy      38  0.001584     5.273588  6.240315e+00  5.660027e-17
102   VGB  SGP          Micro-state  Electoral Autocracy     242  0.010090     1.597732  2.069418e+00  9.745711e-17
351   PAN  SYC  Electoral Democracy  Electoral Autocracy      47  0.001960     3.888094  4.733658e+00  8.084591e-16
501   WSM  COK          Micro-state          Micro-state      37  0.001543     4.843084  5.821571e+00  1.570407e-15
496   WSM  SGP          Micro-state  Electoral Autocracy      60  0.002502     3.043629  3.460845e+00  1.888695e-14
2044  SGP  BMU  Electoral Autocracy          Micro-state      20  0.000834     8.057245  1.007168e+01  5.067952e-13
488   WSM  SYC          Micro-state  Electoral Autocracy      34  0.001418     4.136473  4.810004e+00  2.362311e-12
2033  SGP  CYM  Electoral Autocracy          Micro-state      34  0.001418     3.886566  4.383929e+00  1.754494e-11
2035  SGP  COK  Electoral Autocracy          Micro-state      25  0.001042     4.631117  5.272066e+00  2.229895e-10
366   PAN  AIA  Electoral Democracy          Micro-state      11  0.000459    11.542372  2.626919e+01  2.519874e-10
1190  USA  BMU    Liberal Democracy          Micro-state      22  0.000917     4.916311  6.087412e+00  4.617713e-10
497   WSM  TWN          Micro-state    Liberal Democracy      20  0.000834     5.480429  6.648518e+00  5.267739e-10
768   CHN  CYM     Closed Autocracy          Micro-state      23  0.000959     4.748898  5.312458e+00  8.314918e-10
2377  EGY  GUF  Electoral Autocracy          Micro-state       3  0.000125   922.461538           inf  1.130874e-09
2465  BLZ  TCA          Micro-state          Micro-state       4  0.000167   235.137255  3.684154e+02  1.818912e-09
2079  TWN  CYM    Liberal Democracy          Micro-state      13  0.000542     8.027394  9.296383e+00  8.881366e-09
1820  NLD  GUF    Liberal Democracy          Micro-state       3  0.000125   374.750000           inf  1.812181e-08
2317  AUS  GUF    Liberal Democracy          Micro-state       3  0.000125   347.594203           inf  2.278884e-08
2170  MUS  CYM    Liberal Democracy          Micro-state      14  0.000584     6.654696  7.540264e+00  2.738194e-08
2617  IRL  GUF    Liberal Democracy          Micro-state       3  0.000125   303.594937           inf  3.439552e-08
2423  CYM  JAM          Micro-state  Electoral Democracy       5  0.000208    41.294766  1.099534e+02  4.168447e-08
2034  SGP  MUS  Electoral Autocracy    Liberal Democracy      17  0.000709     5.074905  5.783408e+00  4.457072e-08
2673  AGO  GUF     Closed Autocracy          Micro-state       2  0.000083  3997.333333  2.397900e+04  6.258255e-08
2579  BMU  GUF          Micro-state          Micro-state       3  0.000125   232.854369           inf  7.692159e-08
419   JEY  BMU          Micro-state          Micro-state      12  0.000500     7.164750  8.199198e+00  1.167070e-07
2188  MUS  GUF    Liberal Democracy          Micro-state       3  0.000125   172.546763           inf  1.905039e-07
2222  RUS  GUF  Electoral Autocracy          Micro-state       3  0.000125   157.789474           inf  2.495751e-07
2700  GUF  JAM          Micro-state  Electoral Democracy       2  0.000083  1998.666667  7.991667e+03  2.920194e-07
1695  ARE  GUF     Closed Autocracy          Micro-state       3  0.000125   136.272727           inf  3.884986e-07
1547  CYP  GUF    Liberal Democracy          Micro-state       3  0.000125   126.231579           inf  4.893986e-07
584   CAN  GUF    Liberal Democracy          Micro-state       3  0.000125   122.994872           inf  5.292771e-07
2494  KOR  GUF    Liberal Democracy          Micro-state       2  0.000083  1453.575758  5.327111e+03  5.735617e-07
642   HKG  CYM     Closed Autocracy          Micro-state      76  0.003169     1.752685  1.977945e+00  6.607307e-07
650   HKG  BMU     Closed Autocracy          Micro-state      31  0.001293     2.519541  3.197566e+00  6.830260e-07
300   ESP  GUF    Liberal Democracy          Micro-state       3  0.000125   100.351464           inf  9.772658e-07
1492  SYC  AIA  Electoral Autocracy          Micro-state       5  0.000208    26.189124  3.590950e+01  1.018646e-06
2571  BMU  IRL          Micro-state    Liberal Democracy       6  0.000250    17.685142  2.017342e+01  1.167818e-06
1066  IMN  GUF          Micro-state          Micro-state       3  0.000125    90.848485           inf  1.318713e-06
502   WSM  MYS          Micro-state  Electoral Autocracy      28  0.001167     2.745713  2.994348e+00  1.539090e-06
2662  KWT  GUF     Closed Autocracy          Micro-state       2  0.000083   841.543860  2.819294e+03  1.782859e-06
2039  SGP  TWN  Electoral Autocracy    Liberal Democracy      13  0.000542     5.041425  5.706195e+00  1.848149e-06
2622  IRL  JAM    Liberal Democracy  Electoral Democracy       3  0.000125   113.848101  1.886842e+02  1.903372e-06
2515  JPN  GUF    Liberal Democracy          Micro-state       2  0.000083   799.466667  2.662556e+03  1.980899e-06
796   CHN  GUF     Closed Autocracy          Micro-state       3  0.000125    74.950000           inf  2.353191e-06
2307  AUS  IRL    Liberal Democracy    Liberal Democracy       5  0.000208    21.999633  2.516997e+01  3.250014e-06
2416  CYM  GUF          Micro-state          Micro-state       3  0.000125    66.071625           inf  3.438839e-06
2303  AUS  KOR    Liberal Democracy    Liberal Democracy       3  0.000125    94.798419  1.358352e+02  3.698537e-06
1389  DMA  DOM          Micro-state  Electoral Democracy       3  0.000125    92.246154  1.258632e+02  4.181584e-06
440   JEY  GUF          Micro-state          Micro-state       3  0.000125    61.497436           inf  4.267125e-06
2126  UKR  GUF  Electoral Autocracy          Micro-state       2  0.000083   515.784946  1.651862e+03  4.846507e-06
2306  AUS  IND    Liberal Democracy  Electoral Democracy       3  0.000125    80.214047  1.086591e+02  6.384382e-06
2004  MEX  GUF  Electoral Democracy          Micro-state       2  0.000083   444.148148  1.408647e+03  6.565322e-06
2369  EGY  AGO  Electoral Autocracy     Closed Autocracy       2  0.000083   461.230769  9.981667e+02  6.771109e-06

Filtered graph: 15 nodes, 23 edges

Highest centralityu actors. Using both Eigenvector centrality and betweenness centrality. 

Table: Geography_Cross_Country_Network_Centrality_Scores.png

And all the significant associations between links of countries, ordered by p-value. Given the some 126 nodes, we have to use a Bonferroni correction testing 126*125 Hypotheses with such a tool, but the size and scope of the data allows us to get a lot of significant findings nonetheless - far beyond what could feasibly be shown here in the thesis.

Table: Geography_Cross_Country_Network_Significant_Associations.png 


### Groups of Jurisdictions Served by Intermediaries

Now at the level fo jursidictions. Same approach as above, but concentrating on the jurisdictions intermediaries incorporate in.

The two graphs, "By Legal Technology (Laffitte Dataset)" and "By Community (Louvain Method)," represent a filtered "backbone" of jurisdiction co-usage by intermediaries. This means we are observing the strongest and most significant pairings of jurisdictions where the same intermediaries tend to incorporate entities. The provided text mentions the full network has 41 nodes, while the visualization shows a selection of these (16 nodes are clearly identifiable: CRI, SGP, CYP, GBR, BLZ, AGO, HKG, CYM, COK, MYS, BHS, SYC, PAN, NIU, WSM, USA).

1) Interpretation of Graph Structure Itself

Filtered Core and Periphery: The graph reveals a central, densely connected core and some more peripheral nodes. The core prominently features jurisdictions like BHS, SYC, AGO, WSM, NIU, PAN, USA, and HKG.
Legal Technology Landscape (Left Graph):
The legend shows three categories: "Banking/Corporate/Dual-Purpose" (darker blue), "Dual-Purpose" (bright teal), and "Dual-Purpose/Personal" (brownish-red).
The central cluster is predominantly composed of jurisdictions offering "Dual-Purpose" legal technologies (e.g., BHS, SYC, WSM, NIU, PAN, USA, AGO - all bright teal).
Jurisdictions like HKG and CYM, also part of this central mix or tightly connected, are colored as "Banking/Corporate/Dual-Purpose" (darker blue).
COK is distinctly "Dual-Purpose/Personal" (brownish-red).
Jurisdictions like SGP (darker blue), CYP (bright teal), GBR (bright teal), and BLZ (bright teal) appear more on the periphery of this visualized structure. MYS is grey, suggesting its legal technology type might not be in the displayed legend or it's an uncategorized default.
This visual observation strongly supports your comment: "all the central ones really do focus on these more flexible types of legal technologies, all having these kinds of dual-purpose technologies." The visual center is dominated by these.
Community Structure (Right Graph - Louvain): The Louvain method identifies three communities:
Comm 1 (Brown): This is the largest and most central community in the visualization. It includes USA, PAN, NIU, BHS, SYC, AGO, WSM. This community almost perfectly overlaps with the jurisdictions colored as "Dual-Purpose" in the left graph.
Comm 0 (Dark Blue): A smaller but still significant community, including HKG, CYM, COK. This group combines "Banking/Corporate/Dual-Purpose" (HKG, CYM) with "Dual-Purpose/Personal" (COK). These nodes are also closely connected to the main Comm 1 cluster.
Comm 2 (Light Blue): This community consists of the more peripheral nodes in this visualization: SGP, CRI, CYP, GBR, BLZ, MYS.
Connectivity: The graph shows a single connected component for these visualized nodes, indicating that within this backbone, one can trace a path from any jurisdiction to another.
2) What's Revealed by the Centrality Metrics

(Note: Centrality data is for the full 41-jurisdiction network.)

VGB (British Virgin Islands):
Strikingly Absent: VGB is ranked #1 in both betweenness and eigenvector centrality and has the highest number of appearances in the full jurisdiction network. However, VGB is not visible in the provided filtered graph image. This is a critical observation. It suggests that while VGB is a massively popular and central jurisdiction overall, its connections might be numerous but perhaps individually do not meet the high support/lift thresholds used for this specific "backbone" visualization as strongly as the connections between the visualized nodes. Alternatively, the number of nodes displayed in the visualization might have been capped.
BHS (Bahamas):
Ranked 2nd for both betweenness and eigenvector. Legal tech: "Banking/Corporate/Dual-Purpose/Other Technologies/Personal".
Visibly central in the graph and a core member of Comm 1 (Brown). Its high centrality is reflected in its position in this backbone.
PAN (Panama):
Ranked 3rd for both metrics. Legal tech: "Banking/Corporate/Dual-Purpose".
Also visibly central and a core member of Comm 1.
HKG (Hong Kong) & CYM (Cayman Islands):
HKG: 4th in centrality. CYM: 5th in betweenness, 7th in eigenvector.
Both are present in the graph, forming the core of Comm 0 (Dark Blue) and are well-connected to the larger cluster.
WSM (Samoa), USA, COK (Cook Islands):
All feature in the top 10 for centrality and are visibly important in the graph within Comm 1 or Comm 0. WSM ("Dual-Purpose/Personal") and USA ("None" for legal tech, but behaves like a dual-purpose hub here) are in the central Comm 1. COK ("Dual-Purpose/Personal") is in Comm 0.
SGP (Singapore):
9th by betweenness, 10th by eigenvector.
Appears in the more peripheral Comm 2 in this filtered view, suggesting its strongest co-incorporation links (by lift/support) might be with jurisdictions not as central in this particular representation, or its overall centrality comes from a wider spread of connections.
The centrality data generally aligns with the visualized backbone for most top jurisdictions, with the significant exception of VGB. This indicates that the "strongest co-usage" links (high lift & support) highlight a robust network among BHS, PAN, HKG, CYM, etc., even if the single most popular jurisdiction (VGB) isn't featured in this specific visual cut.

3) What Interesting Associations are Revealed?

Drawing from the graph and the "Significant jurisdiction associations" table:

The Dominant Comm 1 (Brown - "Dual-Purpose" Hubs):
BHS-NIU: Lift 4.64 (Very high significance, p-value ~e-165). A cornerstone link.
NIU-WSM: Lift 5.33 (p-value ~e-134). Another extremely strong link.
NIU-SYC: Lift 4.15 (p-value ~e-85).
SYC-WSM: Lift 3.30 (p-value ~e-73).
This community (BHS, NIU, WSM, SYC, PAN, USA, AGO) is characterized by very high mutual lift values, indicating a strong tendency for intermediaries using one of these jurisdictions (often "Dual-Purpose") to also use others within this group. NIU (Niue) appears to be a particularly critical connector within this cluster.
Comm 0 (Dark Blue - Financial Centers):
HKG-CYM: Lift 5.82 (p-value ~e-21). A very strong pairing of two major financial centers known for sophisticated corporate and banking services.
WSM-CYM: Lift 4.59 (p-value ~e-29). This links Comm 1 (WSM) to Comm 0 (CYM), showing cross-community strength.
Cross-Community High-Lift Examples:
AGO-BLZ: Lift 20.41 (AGO in Comm 1, BLZ in Comm 2). This exceptionally high lift suggests a very specific, niche relationship where intermediaries using AGO are vastly more likely to also use BLZ (Belize), even if they belong to different broader communities in this visualization.
USA-AGO: Lift 8.64 (Both in Comm 1). Reinforces AGO's strong connection profile.
Role of Legal Technology in Associations:
The high-lift associations often pair jurisdictions with similar broad legal technology profiles, especially within Comm 1 (e.g., BHS-NIU, both "Dual-Purpose" or very broad).
However, high lift also occurs between jurisdictions with different listed primary technologies (e.g., WSM "Dual-Purpose/Personal" and CYM "Banking/Corporate/Dual-Purpose"). This suggests that while the type of legal structures is important, the synergies or complementarities between what different jurisdictions offer can also drive co-usage.
Peripheral but Specifically Linked (Comm 2):
Jurisdictions in Comm 2 (SGP, CRI, CYP, GBR, BLZ, MYS) might be less central in this particular backbone view but the "Significant associations" table shows they have numerous statistically significant (often high-lift) pairings. For example, MYS-SGP has a lift of 4.66, AGO-BLZ (as mentioned), GBR-CRI (lift 57.3!), JEY-GGY (lift 197!), IMN-JEY (lift 118!). These incredibly high lift values for pairs involving less central nodes in the graph suggest highly specialized niches.

Plot: Geography_Distribution_of_Jurisdictions_by_Intermediary.png

Full jurisdiction network: 41 nodes, 347 edges
Network density: 0.4232
Average degree: 16.93
Average clustering coefficient: 0.8155
Number of connected components: 1
Number of singletons: 0
Percentage of singletons: 0.00%

Jurisdiction node appearances:

Top 10 jurisdictions by betweenness centrality (excluding XXX):
  node  betweenness  eigenvector  appearances                               jurisdiction_legal_technology
0  VGB     0.196834     0.264054        13533                                       Dual-Purpose/Personal
1  BHS     0.083543     0.258307         2099  Banking/Corporate/Dual-Purpose/Other Technologies/Personal
2  PAN     0.060274     0.245954         6533                              Banking/Corporate/Dual-Purpose
3  HKG     0.058012     0.243551          625                        Banking/Corporate/Other Technologies
4  CYM     0.047955     0.212878          290                              Banking/Corporate/Dual-Purpose
5  WSM     0.027236     0.198658         1352                                       Dual-Purpose/Personal
6  USA     0.019130     0.225509          387                                                        None
7  COK     0.017698     0.122779          954                     Banking/Corporate/Dual-Purpose/Personal
8  CYP     0.016764     0.219042           45                              Banking/Corporate/Dual-Purpose
9  SGP     0.012969     0.194213          355                                  Banking/Other Technologies

Top 10 jurisdictions by eigenvector centrality (excluding XXX):
  node  eigenvector  betweenness  appearances                               jurisdiction_legal_technology
0  VGB     0.264054     0.196834        13533                                       Dual-Purpose/Personal
1  BHS     0.258307     0.083543         2099  Banking/Corporate/Dual-Purpose/Other Technologies/Personal
2  PAN     0.245954     0.060274         6533                              Banking/Corporate/Dual-Purpose
3  HKG     0.243551     0.058012          625                        Banking/Corporate/Other Technologies
4  USA     0.225509     0.019130          387                                                        None
5  CYP     0.219042     0.016764           45                              Banking/Corporate/Dual-Purpose
6  CYM     0.212878     0.047955          290                              Banking/Corporate/Dual-Purpose
7  WSM     0.198658     0.027236         1352                                       Dual-Purpose/Personal
8  JEY     0.198627     0.011335           28                             Dual-Purpose/Other Technologies
9  SGP     0.194213     0.012969          355                                  Banking/Other Technologies

Number of nodes: 41, hypothesis tests (pairs): 820
Bonferroni p-value threshold (@α=0.05): 6.10e-05
Number of significant associations after Bonferroni correction: 81

Significant jurisdiction associations after Bonferroni correction (excluding XXX):
       u    v                             u_jurisdiction_legal_technology                             v_jurisdiction_legal_technology  weight   support          lift  odds_ratio        p_value
72   BHS  NIU  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                                Dual-Purpose     386  0.016094      4.637842    8.502932  1.804861e-165
108  NIU  WSM                                                Dual-Purpose                                       Dual-Purpose/Personal     286  0.011925      5.334951    8.862534  9.678686e-134
106  NIU  SYC                                                Dual-Purpose                                       Dual-Purpose/Personal     239  0.009965      4.154049    6.043520   1.893220e-85
122  SYC  WSM                                       Dual-Purpose/Personal                                       Dual-Purpose/Personal     270  0.011258      3.300968    4.532462   4.504114e-73
3    PAN  SYC                              Banking/Corporate/Dual-Purpose                                       Dual-Purpose/Personal     649  0.027060      1.642049    2.289738   2.503294e-49
73   BHS  SYC  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                       Dual-Purpose/Personal     301  0.012550      2.370327    3.018443   2.617132e-48
123  SYC  AGO                                       Dual-Purpose/Personal                                                        None     102  0.004253      4.606523    6.378007   2.195871e-40
4    PAN  USA                              Banking/Corporate/Dual-Purpose                                                        None     228  0.009506      2.162882    3.932764   1.333474e-39
121  SYC  USA                                       Dual-Purpose/Personal                                                        None      99  0.004128      4.228423    5.655857   9.606116e-36
143  USA  AGO                                                        None                                                        None      51  0.002126      8.635744   11.218651   1.494814e-32
2    PAN  NIU                              Banking/Corporate/Dual-Purpose                                                Dual-Purpose     426  0.017762      1.644516    2.248934   1.876348e-32
174  WSM  CYM                                       Dual-Purpose/Personal                              Banking/Corporate/Dual-Purpose      75  0.003127      4.587839    6.123636   1.311024e-29
1    PAN  BHS                              Banking/Corporate/Dual-Purpose  Banking/Corporate/Dual-Purpose/Other Technologies/Personal     796  0.033189      1.392226    1.719501   3.870631e-29
74   BHS  USA  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                                        None     100  0.004169      2.952556    3.764600   1.330213e-23
162  WSM  HKG                                       Dual-Purpose/Personal                        Banking/Corporate/Other Technologies     103  0.004295      2.923493    3.492955   4.587816e-23
204  HKG  CYM                        Banking/Corporate/Other Technologies                              Banking/Corporate/Dual-Purpose      44  0.001835      5.822323    7.115374   3.155765e-21
182  AGO  BLZ                                                        None                     Banking/Corporate/Dual-Purpose/Personal      19  0.000792     20.411001   30.735831   3.194295e-20
107  NIU  USA                                                Dual-Purpose                                                        None      60  0.002502      3.910042    4.675913   1.051439e-19
6    PAN  AGO                              Banking/Corporate/Dual-Purpose                                                        None     177  0.007380      1.775420    2.543424   3.800276e-18
163  WSM  AGO                                       Dual-Purpose/Personal                                                        None      65  0.002710      3.150483    3.746938   1.300518e-16
184  AGO  GBR                                                        None                                                        None      18  0.000751     14.562234   19.339080   2.529135e-16
183  AGO  CYP                                                        None                              Banking/Corporate/Dual-Purpose      14  0.000584     20.387128   30.261913   3.153513e-15
187  AGO  CRI                                                        None                                                        None      12  0.000500     25.366473   42.103479   1.449247e-14
140  USA  WSM                                                        None                                       Dual-Purpose/Personal      62  0.002585      2.842010    3.298829   8.949097e-14
7    PAN  GBR                              Banking/Corporate/Dual-Purpose                                                        None      54  0.002252      2.447472    5.378608   1.497930e-13
76   BHS  AGO  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                                        None      77  0.003210      2.403913    2.845673   3.059375e-13
145  USA  URY                                                        None                                                        None      11  0.000459     22.723859   36.304311   6.956245e-13
128  SYC  BLZ                                       Dual-Purpose/Personal                     Banking/Corporate/Dual-Purpose/Personal      22  0.000917      5.961383    8.879582   3.055167e-12
75   BHS  WSM  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                       Dual-Purpose/Personal     193  0.008047      1.631135    1.810783   3.938791e-12
147  USA  CYP                                                        None                              Banking/Corporate/Dual-Purpose      12  0.000500     16.526443   22.849939   4.681206e-12
221  CYP  URY                              Banking/Corporate/Dual-Purpose                                                        None       6  0.000250    106.595556  153.301282   1.770305e-11
141  USA  GBR                                                        None                                                        None      14  0.000584     10.711583   13.181545   4.394753e-11
10   PAN  CRI                              Banking/Corporate/Dual-Purpose                                                        None      26  0.001084      3.079077   13.941786   7.443534e-11
296  CYM  BMU                              Banking/Corporate/Dual-Purpose          Corporate/Dual-Purpose/Other Technologies/Personal      12  0.000500     13.058439   15.937500   1.212081e-10
281  SGP  MUS                                  Banking/Other Technologies                     Banking/Dual-Purpose/Other Technologies      12  0.000500     12.868679   16.174241   1.245482e-10
223  CYP  MLT                              Banking/Corporate/Dual-Purpose  Banking/Corporate/Dual-Purpose/Other Technologies/Personal       5  0.000208    140.257310  213.616071   2.107595e-10
291  CYM  MUS                              Banking/Corporate/Dual-Purpose                     Banking/Dual-Purpose/Other Technologies      11  0.000459     14.440285   17.925420   2.356751e-10
247  IMN  JEY                                      Corporate/Dual-Purpose                             Dual-Purpose/Other Technologies       5  0.000208    118.968254  167.776999   5.467439e-10
190  GBR  CRI                                                        None                                                        None       6  0.000250     57.309438   76.409600   8.457568e-10
197  GBR  BLZ                                                        None                     Banking/Corporate/Dual-Purpose/Personal       7  0.000292     33.978547   41.777528   1.448573e-09
109  NIU  AGO                                                Dual-Purpose                                                        None      41  0.001709      2.825165    3.148024   2.413046e-09
80   BHS  URY  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                                                        None      15  0.000625      5.713197   10.494242   5.617780e-09
245  IMN  CYM                                      Corporate/Dual-Purpose                              Banking/Corporate/Dual-Purpose       8  0.000334     18.378544   23.977710   9.359620e-09
186  AGO  URY                                                        None                                                        None       8  0.000334     17.474681   23.967496   1.189653e-08
133  SYC  MLT                                       Dual-Purpose/Personal  Banking/Corporate/Dual-Purpose/Other Technologies/Personal      10  0.000417      8.699626   17.367569   3.557272e-08
13   PAN  BLZ                              Banking/Corporate/Dual-Purpose                     Banking/Corporate/Dual-Purpose/Personal      37  0.001543      2.226798    4.135872   4.546178e-08
200  HKG  BLZ                        Banking/Corporate/Other Technologies                     Banking/Corporate/Dual-Purpose/Personal      12  0.000500      7.549062    9.312515   4.793669e-08
205  HKG  MUS                        Banking/Corporate/Other Technologies                     Banking/Dual-Purpose/Other Technologies      12  0.000500      7.309410    8.946550   7.002179e-08
127  SYC  URY                                       Dual-Purpose/Personal                                                        None      12  0.000500      6.611716   10.430855   7.160769e-08
274  MYS  SGP                     Banking/Dual-Purpose/Other Technologies                                  Banking/Other Technologies      18  0.000751      4.659349    5.140345   7.866706e-08
81   BHS  BLZ  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                     Banking/Corporate/Dual-Purpose/Personal      20  0.000834      3.746359    5.125353   1.178230e-07
117  NIU  URY                                                Dual-Purpose                                                        None      10  0.000417      8.406590   12.227949   1.336022e-07
185  AGO  NZL                                                        None                                                        None       6  0.000250     19.659016   28.100000   3.921873e-07
259  JEY  GGY                             Dual-Purpose/Other Technologies                              Banking/Corporate/Dual-Purpose       3  0.000125    197.670330  287.352000   4.043468e-07
273  MYS  MUS                     Banking/Dual-Purpose/Other Technologies                     Banking/Dual-Purpose/Other Technologies       8  0.000334     11.668917   13.607186   4.080018e-07
34   VGB  NIU                                       Dual-Purpose/Personal                                                Dual-Purpose     610  0.025434      1.136781    1.399469   4.685939e-07
144  USA  CRI                                                        None                                                        None       7  0.000292     13.994165   18.093311   5.079957e-07
341  ATG  KNA                               Banking/Dual-Purpose/Personal                               Banking/Dual-Purpose/Personal       2  0.000083   1262.315789         inf   5.945672e-07
83   BHS  CYP  Banking/Corporate/Dual-Purpose/Other Technologies/Personal                              Banking/Corporate/Dual-Purpose      16  0.000667      4.062718    5.788998   6.184441e-07
246  IMN  GGY                                      Corporate/Dual-Purpose                              Banking/Corporate/Dual-Purpose       3  0.000125    153.743590  217.618182   8.790654e-07
9    PAN  CYP                              Banking/Corporate/Dual-Purpose                              Banking/Corporate/Dual-Purpose      28  0.001167      2.284307    4.414270   9.418028e-07
165  WSM  BLZ                                       Dual-Purpose/Personal                     Banking/Corporate/Dual-Purpose/Personal      15  0.000625      4.362208    5.508601   1.033238e-06
124  SYC  GBR                                       Dual-Purpose/Personal                                                        None      18  0.000751      3.673176    4.480112   1.258699e-06
17   PAN  NZL                              Banking/Corporate/Dual-Purpose                                                        None      16  0.000667      2.936966   10.708608   1.349279e-06
130  SYC  CYP                                       Dual-Purpose/Personal                              Banking/Corporate/Dual-Purpose      13  0.000542      4.775128    6.356767   1.626109e-06
260  JEY  BMU                             Dual-Purpose/Other Technologies          Corporate/Dual-Purpose/Other Technologies/Personal       4  0.000167     45.082707   55.287037   1.798988e-06
207  HKG  SGP                        Banking/Corporate/Other Technologies                                  Banking/Other Technologies      26  0.001084      2.810519    3.038397   2.532998e-06
125  SYC  HKG                                       Dual-Purpose/Personal                        Banking/Corporate/Other Technologies      67  0.002794      1.771940    1.906485   3.978648e-06
12   PAN  MLT                              Banking/Corporate/Dual-Purpose  Banking/Corporate/Dual-Purpose/Other Technologies/Personal      15  0.000625      2.898322   10.037780   3.991385e-06
146  USA  BLZ                                                        None                     Banking/Corporate/Dual-Purpose/Personal       8  0.000334      8.127759    9.376811   5.967660e-06
308  MUS  THA                     Banking/Dual-Purpose/Other Technologies                                                        None       2  0.000083    380.698413         inf   6.790584e-06
237  CRI  URY                                                        None                                                        None       3  0.000125     77.367742   94.944444   7.752236e-06
148  USA  NZL                                                        None                                                        None       5  0.000208     15.493540   20.577661   1.353510e-05
297  CYM  GGY                              Banking/Corporate/Dual-Purpose                              Banking/Corporate/Dual-Purpose       4  0.000167     25.447215   36.806527   1.373667e-05
258  JEY  CYM                             Dual-Purpose/Other Technologies                              Banking/Corporate/Dual-Purpose       5  0.000208     14.768473   18.055683   1.953562e-05
112  NIU  BLZ                                                Dual-Purpose                     Banking/Corporate/Dual-Purpose/Personal      11  0.000459      4.547827    5.379000   2.442846e-05
11   PAN  URY                              Banking/Corporate/Dual-Purpose                                                        None      19  0.000792      2.325098    4.624445   3.787814e-05
309  MUS  LCA                     Banking/Dual-Purpose/Other Technologies                     Banking/Corporate/Dual-Purpose/Personal       2  0.000083    190.349206  392.114754   4.060545e-05
346  ABW  TCA                                          Other Technologies                     Banking/Corporate/Dual-Purpose/Personal       1  0.000042  23984.000000         inf   4.169446e-05
339  GIB  VCT                                        Banking/Dual-Purpose                                       Dual-Purpose/Personal       1  0.000042  23984.000000         inf   4.169446e-05
111  NIU  CYP                                                Dual-Purpose                              Banking/Corporate/Dual-Purpose       9  0.000375      5.043954    6.103238   5.710970e-05
And likewise, making a graph out of this but instead connecting them if they use btoh jurisdictions. 

Here, colouring in by legal technologies afforded by the jurisdictions and by Louvain Communities. Nothing really in particular. But inteesting to note, all the central ones really do focus on these more flexible types of legal technologies, all having these kinds of dual-purpose technologies

Plot: Geography_Cross_Jurisdiction_Network.png

Likewise, providing top 10 centrlaity scores by both eigenvector and betweenness centrality.

Table: Geography_Cross_Country_Network_Centrality_Scores.png

Table: Geography_Cross_Country_Network_Significant_Associations.png 

## Functional Specialisation of Intermediaries

In Aggregate considering the 'Geogrpahy' of Intermediaries. Now going more granular into the specific role they serve.
Exploring, in a sense, whether we see something like the typology proposed by that EU (2017) paper bearing out in the data

Shares of intermediares in the two groups

Plot: Specialisation_Classification_Distribution_Comparison.png

Only using the random sample here, as top intermediaries are not representative of the whole population.

A random sample enriched using the process going through the enrichment rpcoess of the individual 

This is the random sample we have left, after filtering out those we couldn't confidently classify:

Plots: Appendix_Filtering_of_Enrichment.png

### Different Levels of Connectivity: Personalised Advice vs. Aid in Incorporation

Most improtantly, how many entities does eahc group incorporate?

We've already seen a subtle hint: More administrators and legal experts in the top of intemrediareis degree distribution compared to tax experts and investment advisors, but let's look at this more closely.

Difficutl to visualise a powerlaw distribution using usual moments of distributions, so showing the CDF with log-degree on the x-axis.

Plot: Specialisation_CDF_of_Degrees_by_Classification_Random_Sample.png

Using two-sample KS-test to test significance along with a Bonferroni correction of the 4 types of pairs, giving us 4*3 pairs we're testing.

4 of these are signifiant. Tax Expert and Investment Advisors not significantly different, nor are Legal Experts and Administrators, but the cross-cuting of the two groups are all significant!

Also make sense in the sense that these are the two groups that are most similar to each other, and therefore most likely to be confused with each other.


### Different Activities: Instruments and Service Offerings

5 metrics to summarise an intermediary:
1. Entropy of jurisdictions - do they incorporate in a lot of different jurisdictions, or are they more concentrated?
2. Entropy of countries - do they have a lot of different clients, or are they more concentrated?
3. ENtropy of regimes of countries they incorporate in - do they have a lot of different regimes, or are they more concentrated?
4. Entropy of Legal Technologies in jurisdictions they incorporate in - do they have a lot of different legal technologies, or are they more concentrated?
5. Do they use bearer instruments or not? (One-hot encoding)

Comparing the average of all of these:

Plot: Specialisation_Average_Entropy_and_Bearer_Usage_by_Classification.png




Constructing eight networks, each providing a different lens on the Panama Papers
]
Noting that it's the only paper to their knowledge that has done this kind of network-theoretic study of the ICIJ papers.

It's an excellent paper for us to get a sense of the overall entwork; however, done entirely agnostic of the udnerlying subject matter, nearly. It's pubilshed in a network science paper, and thus only considers high-level ways they are different from usual networks and tryign to presetn broad and general summary statsitics of it.

Descirbing book by Obermayer and Obermaier (2016) as key to understanding this.

Intermediaries: Book writes it's "lawyers, accountants and banks" (p. 3 of Kyeyrjwal)

Includes definitions from the ICIJ page to explain it.


Most important dataset: edge_links on it. Defining the  network of as {(a, R, b)} where a is connected to b (notice: directed relation, not undirected, though for our purposes this will be the same) by some labelled relation R.

They use Panama Papers only.


THey use density of the edges: number of edges dividied by total possible number of edges.


Huge about theirs: consider the network in aggregate; all nodes are grouped into one, whether it be addresses, officers or entities. Show both out-degree and in-degree follow power law. We here restrict what we do to only intermediaries as the central nodes considered.


Key finding: Isolated nature of nodes. Triad counts (number of triads connected, is very, very low compared to generating a random graph with teh same size and degree)


"The triad census seems to suggest transactions of a one-way nature, or one that favors secrecy, since three-way interactions are statistically dampened compared to random graphs with similar topology. This is the first indication that the Panama Papers, though a complex system, may not obey the usual laws that other complex systems with social actors and relationships seem to. Later, we provide more evidence that lends further credence to this claim."


Note: G_intermediary they consider: only retaining links in G that are typed as "iontermediary of"
Some particularly instructive results here:
1) a power-law distribution as well (i.e. predominantly between intermediaries and entities incroporated. This is the same as we see here.)
2) Connectivtiy of it: Connected components also follow a power-law distribution. But like wise, we ahve no cores.

Incredibly isolated components, resistant to targetting:
"A bridge in a connected component is an edge that, were it to be removed, would lead in the connected component ‘breaking’ into two connected components. The results in Table 5 show that the percentage of bridges (as a percentage of the number of edges) is high in all networks, and is extreme (100%) in the largest component in Gi. This suggests that every edge in the largest component in Gi is a bridge, which is true for graphs that are star-like or linear chains (or a combination of the two)."

Low density of the edges in general; this holds true across all the subgraphs they construct.

They just remove the nodes with more than one country associated with them!!! These are the interesting ones!


"We find that the country assortativity is generally high across all four networks, but is especially high in the intermediary network Gi. In other words, when A is an inter- mediary of B, they are very likely to belong to the same, rather than different, country. This is in accordance with what we would ordinarily expect, rather than in highly illicit networks"

"Even more disturbingly, the larger components have high entropy (compared to their size) but low density, on average, suggesting that targeting or investigating nodes in the larger components would also have limited utility in cracking down on overall illicit activity. Finally, one aspect of the data that we did not cover in this article, is the dynamic nature of entities: offshore companies can quietly and quickly change ownership and beneficia- ries in many jurisdictions, intermediaries can be replaced or shut down, and new shell companies can emerge, all in short order. Robustness is, therefore, an inherent feature of this system in more ways than one."

Not a single graph has displayed small-wrold properties! Notion that we can reach any node within a few steps - again, this star-like or linear-like structure, where it takes a long time to get to the others:

"The small-world phenomenon, a concept in graph theory, describes a network where nodes have relatively short average path lengths and exhibit high clustering, meaning that local communities are tightly knit. This "smallness" suggests that despite having many nodes and connections, most nodes can be reached from any other node through only a few step"

Huh, I guess this is what I'm doing?

"A longer-term goal is to reconcile entities in all of these different datasets, possibly after supplementing the datasets with external records and datasets, with the goal of either reinforcing or disputing the findings in this article through an analysis of the reconciled (and more complete) graph. We also plan to study the influence of intermediaries and other nodes using established centrality metrics from the literature."


The ICIJ data
* Cleaning it
* Scope, what it is etc.
* When the data was from, etc.
* An overview of when we have data from, i.e. incorporations

The empirical core of this thesis rests upon the International Consortium of Investigative Journalists (ICIJ) Offshore Leaks Database. This resource serves as the primary data source, acting as a valuable, albeit imperfect, "proxy" for the opaque universe of offshore finance (cf. EU, 2017). The general idea underpinning its use here is that while any direct numerical estimates derived solely from the leaks (e.g., total wealth hidden) will surely be biased due to the data's inherent incompleteness, the qualitative nature of the interactions captured within the data – the patterns of relationships between clients, intermediaries, and jurisdictions – appears more reliable for understanding the structure and dynamics of the offshore system.

The use of the ICIJ Offshore Leaks Database for this type of research is increasingly established. For example, Alstadsæter et al. (2019), Londoño-Vélez \& Ávila-Mahecha (2021), and Chang et al. (2023a; 2023b). 

Some direct network analysis, but not much. Most relevant for our purposes is the work of Chang et al. (2023a; 2023b), as well as a more direct network study (Kejriwal \& Dang, 2020) looking at the usual properties networks exhibit. They note:

"It was really unusual. The degree of fragmentation is something I have never seen before," said Kejriwal. "I'm not aware of any other network that has this kind of fragmentation."

Use this paper to describe the ICIJ data in detail!

from Kejriwal \& Dang (2020):


Plot: Preliminary_Incorporations_over_Time.png

\section{External Data Sources}
\label{sec:3_2}

### Background of the other Data Sources, to deeper into how we connect the data.
Other Data Sources
* Lafitte legal technologies: connceting to this at entity levels.
* VDem at country level of the entities.
* Enriching the type of intermediaries


To contextualize the patterns observed within the ICIJ data, several external data sources are employed.

A key resource is the Historical Tax Havens Database (HTHD) developed by Laffitte (2024). This dataset documents the historical evolution of "offshore legal architecture," tracking the adoption of specific legal technologies (e.g., banking secrecy, IBCs) across tax havens over time. This dataset will be utilized to explore whether specific patterns observed in the ICIJ data – such as the prevalence of certain offshore instruments or shifts in intermediary activity – align temporally with the historical innovations documented in the HTHD.

The World Justice Project (WJP) Rule of Law Index provides comprehensive country-level metrics on governance. Its specific use is to investigate potential correlations between the home country's rule of law environment and the patterns of specialization or network positioning observed among the intermediaries serving clients from that country.

VDEM (Varieties of Democracy) Regime Type Data will be used exactly analogously.

Data from the World Inequality Database (WID), specifically metrics on wealth inequality at the country level, will also be incorporated.  This serves primarily to see if we can confirm some of the comparative statics Alstadsæter and Zucman derive, trying to verify whether there's anything to their supply-side model.

\section{Using Agentic AI to Scrape Data on Intermediaries.}
\label{sec:3_3}

A significant challenge in utilizing the ICIJ data for the purposes of this thesis is that intermediaries are often classified generically within the database. To analyze the specific roles and potential influence of different types of intermediaries, as outlined in the typology adapted from the EU (2017) paper (see Section 2.1.4), a more granular classification is required. To achieve this classification at scale, an approach employing agentic AI is utilized.

The core idea is to use an AI agent loop to automate the process of gathering information about and classifying the intermediaries listed in the ICIJ data. The basic workflow is illustrated in Figure \ref{fig:agent_loop_placeholder}.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{agent_graph.png} % Assuming you have agent_graph.png
    \caption{Agent Setup for Intermediary Classification}
    \label{fig:agent_loop_placeholder}
\end{figure}

In brief, the process involves an AI agent orchestrating online searches for each intermediary identified in the ICIJ data. It begins with generic searches, reads and interprets the initial results, and then formulates more specific search queries based on the information discovered or identified as lacking. This iterative process involves up to three search queries per intermediary, scouring the top 15 most relevant web results identified through query-result embedding similarity using the Tavily Search API (though the tool is relatively generic and its specific choice is not critical to the methodology). This effectively replaces the time-consuming need for manual searching of the intermediaries.

Based on the information gathered, the AI agent then classifies the intermediary according to the EU (2017) typology (Tax Expert, Legal Expert, Administrator, Investment Advisor), adding a few additional relevant fields (e.g., specific job title). Crucially, the agent also provides a confidence score for its classification judgment, allowing for filtering or weighting in subsequent analyses.

There are a few obvious limitations associated with this approach that warrant discussion:

* The "Small Spiders" Problem. Kimberly Kay Hoang notes of one of the ultra-wealthy board directors she interviews, that despite the entities he was behind were revealed in the Panama Papers, nothing traces back to him. Instead, a group of "fall guys", as she terms them, are the ones that fall victim to the public's search-light. Those that have public profiles skew the bias towards the less illict people involved even stronger.
* Temporal Misalignment: A primary concern is that all online searches are conducted based on information available today, whereas the ICIJ data pertains to activities that may have occurred years or even decades prior. This introduces two potential issues:
    \begin{enumerate}
        \item The process might be biased towards identifying intermediaries who are still active or have a significant online presence currently.
        \item It implicitly assumes that the role an intermediary plays today (as reflected online) is equivalent to the role they played at the time relevant to the ICIJ data.
    \end{enumerate}



Plot: Methods_Agent_Graph.png 

Intermediaries
* Country associated with them
* Relation to entities

Entities
* Country associated
* Jurisdiction incorporated in
* Bearer instruments attached

Network Theory and ICIJ data used for this kind of enquiry
* Public Econ papers it's been used
* Kejriwal \& Dang (2020)
* Chang et al. (2023a and 2023b) most close to what we're doing here.

Concepts from Network Theory
* Overall data model
* Centrality scores and in-betweeneness 
* Louvain community detection
* Power-law distribution
* Density of a graph
* (Entropy)

Unsupervised Learning - and especially Association Analysis
* Non-parametric notion of it
* Discovering patterns of high density without a target label
* Lift scores

Testing significance of the results
* Fisher exact test where we can - notion of this contingency table. Ideal for association analysis and for dummy variables like whether they're connected to entities using bearer instruments
* Mann-Whitney U test for continuous variables - non-parametric test
* Two-sample Kolmogorov-Smirnov test for continuous variables for comparing - again, non parametric test

Multiple Hypothesis Testing
* How Type I error of 5\% breaks down once we have multiple hypotheses tested
* Bonferroni used even though it's highly conservative compared to the others.
* Maybe it's smarter to use Benjamini-Hochberg, but considering hwat's essentially a data minining exercise here, rather be conservative than maximise power.







This section details the data sources and methodological approaches employed in this thesis. It begins by describing the primary data source, the ICIJ Offshore Leaks Database, outlining its structure, content, strengths, and limitations. Subsequently, it discusses the external datasets used to provide contextual information. Finally, it introduces a novel methodology utilizing agentic AI to enrich the classification of intermediaries within the icij dataset.

\section{The ICIJ Offshore Leaks Database}
\label{sec:3_1}
The core datasets loaded for this analysis include:
\begin{itemize}
    \item \texttt{nodes-entities.csv}: Information on offshore companies, trusts, foundations.
    \item \texttt{nodes-officers.csv}: Details on individuals or companies acting in official capacities (directors, shareholders, beneficiaries).
    \item \texttt{nodes-intermediaries.csv}: Data on firms or individuals facilitating the creation and management of offshore structures.
    \item \texttt{nodes-addresses.csv}: Physical address information linked to other nodes.
    \item \texttt{nodes-others.csv}: Nodes not fitting the primary categories.
    \item \texttt{relationships.csv}: The edge list defining connections between nodes, including the type of relationship.
\end{itemize}
A multi-modal and multi-relational graph, that often involved dealing with it at various level of abstractions, and breaking the dimensionality of it. For example, most network algorithms cannot deal with multi-relational graphs (in fact, a tetrapartite graph composed of addresses, entities, officers and intermediaries!), built and formulated as traditional adjacency matrices operations, so often switching between different representations of the data, ranging from granular edge lists with the full ontology of the data model, to those squashed down into a format that can be represented as a single adjacency matrix (i.e. an edge list with only a single type of source- and end node).

Usual trick for dealing with bipartite graphs is projecting it down by connecting two nodes if they share a common node type, that one wants to eliminate. For example, for getting rid of address node type, relations like the following would be transformed as such:

Intermediary1 -- Address -- Intermediary2
-> Intermediary1 -- Intermediary2

This process can be done iteratively on all node types that one wants to eliminate:
Intermediary1 -- Entity -- Address -- Officer -- Intermediary2
-> Intermediary1 -- Intermediary2

And from here, traditional network algorithms calculating the likes of eigenvector centrality etc. can be applied.

Whenever moving between the different representations of the graph, will be made clear in the empirical section.


Note: ICIJ data is in principle directed, but in practice this is not especially important. Here, treated solely as an undirected graph.

Addressing the Limitations: While these issues are real, they are not prohibitive for their use in this thesis.
\begin{enumerate}
    \item Regarding the first point (bias towards current intermediaries), this primarily impacts the coverage or statistical power of the classification – we may only be able to confidently classify a subset (e.g., 50\%) of all intermediaries. This is acceptable, provided the unclassifiable intermediaries are not systematically different in ways that correlate with the research questions. The issue becomes problematic only if there is a systematic bias in identifiability across types (e.g., if it is inherently much harder to find information online about legal experts compared to tax experts due to differing needs for discretion or public visibility). The significant threat here is the bias in who provides public information - it will only be the intermediaries whose activities are not inherently illegal. A bias towards, in a sense, the least dangerous intermediaries as those being revealed.
    \item Regarding the second point (role stability), the assumption that roles remain consistent is arguably less problematic. Given the highly specialized nature of functions like tax advisory, legal structuring, administration, and investment management within the offshore context, and the considerable barriers to entry (qualifications, reputation, networks) for each, frequent switching between these core roles by individuals or firms seems relatively unlikely.
\end{enumerate}
In my view, it is the only pragmatically feasible method to do this given the constraints of this thesis.
\section{Use of LLMs in the Broader Paper}
\label{sec:3_4}

LLMs have also been used to polish the text of this thesis and used for idea generation.

Used Google Gemini models mainly, with the seed configured to 42:
\begin{itemize}
    \item gemini-2.5-pro-preview-05-06
    \item gemini-2.5-pro-experimental-03-25
\end{itemize}


