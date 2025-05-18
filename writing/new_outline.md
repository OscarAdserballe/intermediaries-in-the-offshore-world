
# Abstract


# Motivation

Public Economics: Demand-side -> Supply-side.

Public Economics: Problem statement of tax evasion

Research Gap: 

# Theory
Phil of Sci: Some critical realism? Mostly an inductive approach.

Global Wealth Chains and role of Intermediaries

Relational Capitalism
* Neely (2021) and rest of M&O course from there

What we know about Intermediaries so far:
* Harrington (2016)
* Hoang (2022)
* Tax Experiment in Chile (2024)
* Unfollow the money

The Havens they're located in, and the secrecy strategies used.


A typology of intermediaries and their role
* EU (2017) paper.

# Data and Methodology

The ICIJ data
* Cleaning it
* Scope, what it is etc.
* When the data was from, etc.

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
* Entropy

Unsupervised Learning - and especially Association Analysis
* Non-parametric notion of it
* Discovering patterns of high density without a target label
* Lift scores
* Fisher exact test

GLMs and Regression designs
* Negative Binomial Regressions - those damn degree distributions difficult otherwise

Other Data Sources
* Lafitte legal technologies: connceting to this at entity levels.
* VDem at country level of the entities.
* Enriching the type of intermediaries

# Results 

## Preliminiary about Intermediaries

##### Degree distribution of intermediaries
* Show power-alw distribution fits well
* Test significance against other distributions? Random Graph?


## Geogprahical Specialisation

##### Which Countries are Intermediaries Based in?
* Just a basic bar plot of 15 biggest + pie chart showing how much that covers

##### How many countries do intermediaries incorporate entities in?
* Power-law distribution of how many they incorporate
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
Looking across the different types of entropy scores and the share of entities whom use bearer instruments.
HOW TO TEST SIGNIFICANCE HERE?


##### Differences in Degrees:
* CDF of the different types showing it.
* Comparison of random smaple vs. the the ones in the top 500 - e.g. administrators the ones that have an incredibly high degree, whereas we tax experts and legal experts more personal advisory. Not connected to as many.
* Testing signifianace of degree differences using Negative Binomial random component + natural logarithm as the link function?

##### Clustering different intermediaries and seeing if they cluster by type
Idea: Though wit hthat many countries and jurisdictions we'd end up with a super sparse matrix, we can do some feature selection exactly by virtue of the fact that countries and officers are so tightly located. We have this long dataframe in this case, with dictionary objects flattened out as columns, which we then proceed to try to cluster then doing some pca/t-sne/mds to visualise in 2-dimensions


##### Case Studies of One of Each Type in The Appendix
Having the case study of each of those revealed into the appendix









