
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
* An overview of when we have data from, i.e. incorporations

Plot: Preliminary_Incorporations_over_Time.png

Background of the other Data Sources, to deeper into how we connect the data.
Other Data Sources
* Lafitte legal technologies: connceting to this at entity levels.
* VDem at country level of the entities.
* Enriching the type of intermediaries

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
* How Type I error of 5% breaks down once we have multiple hypotheses tested
* Bonferroni used even though it's highly conservative compared to the others.
* Maybe it's smarter to use Benjamini-Hochberg, but considering hwat's essentially a data minining exercise here, rather be conservative than maximise power.

# Results 

## Overview of the dataset

### Overview of where the relevant elements for our sake are concentrated

Plot: Preliminary_Geography_Overview.png

Highly, highly concentrated. Especially notable in terms of the jurisdictions they incorporate in with some 98% of the entities incorporated represented by just 15 countries.

### Degree Distribution of Intermediaries

Plot: Preliminary_Powerlaw_Fit.png

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

Highest centralityu actors. Using both Eigenvector centrality and betweenness centrality. 

Table: Geography_Cross_Country_Network_Centrality_Scores.png

And all the significant associations between links of countries, ordered by p-value. Given the some 126 nodes, we have to use a Bonferroni correction testing 126*125 Hypotheses with such a tool, but the size and scope of the data allows us to get a lot of significant findings nonetheless - far beyond what could feasibly be shown here in the thesis.

Table: Geography_Cross_Country_Network_Significant_Associations.png 


### Groups of Jurisdictions Served by Intermediaries

Now at the level fo jursidictions. Same approach as above, but concentrating on the jurisdictions intermediaries incorporate in.

Plot: Geography_Distribution_of_Jurisdictions_by_Intermediary.png

And likewise, making a graph out of this but instead connecting them if they use btoh jurisdictions. 

Here, colouring in by legal technologies afforded by the jurisdictions and by Louvain Communities. Nothing really in particular. But inteesting to note, all the central ones really do focus on these more flexible types of legal technologies, all having these kinds of dual-purpose technologies

Plot: Geography_Cross_Country_Network.png

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

# Discussion




# Conclusion


# Appendix


Enrichment process using LangGraph and Agentic AI in general
* More detail, prompts, graphs on how many we have to filter away
* case studies of one of each type in the appendix
having the case study of each of those revealed into the appendix




