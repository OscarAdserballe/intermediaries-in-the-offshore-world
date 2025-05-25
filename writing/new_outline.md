\section{Outline of the Thesis}

A thorough outline to start with, because of the sheer complexity of the topic, and making sure that one can always return and understand the points we're trying to make across each section.

\subsection{Introduction: Why Intermediaries Matter}

\textbf{Public Finance and the Scope of the Problem} There's a lot of ways to motivate an understanding into this general topic, but the overall problem statement will come from the world of \textbf{public finance}: there's a huge literature on understanding tax evasion, as well as the concrete facts motivating the overarching interest in the offshore world.

\textbf{The 'Offshore' and our Interest in Intermediaries} Following this, we'll draw primarily from the large interdisciplinary literature to understand the offshore world, and why we should be specifically interested in the role of intermediaries specifically.

\subsection{Theory: What We Know (And What We Don't)}

Four main streams of literature feed into our understanding of intermediary specialisation. 

\begin{enumerate}
    \item \textbf{Global Wealth Chains literature} gives us a more macro-oriented view of the structures professionals operate within. This is a more abstract, and far more structural approach to viewing the overall role of intermediaries as professionals placed in these global wealth chains. Rather than focusing on individual relationships, this stream shows us how intermediaries fit into broader patterns of capital flows and regulatory arbitrage.
    \item \textbf{Micro-sociological accounts of Intermediaries} providing qualitatively rich and thick descriptions of the role of intermediaries, usually through ethnographic methods. They emphasise, not least due to their methods and disciplinary background, the relational aspect of intermediaries. From this, we can derive specific mechanisms about why we should expect patterns of geographical specialisation to emerge. The focus on trust, cultural affinity, and professional networks gives us concrete reasons to expect intermediaries won't operate as perfectly fungible service providers. (Also briefly touch on Alstadsæter's work uncovering evasion networks in places like Dubai)
    \item \textbf{Legal technologies and strategies} - taking a step down in abstraction, we leverage a few papers getting us into the specifics of the role of intermediaries as well as the "legal technologies" and strategies they adopt. There's no dedicated stream of literature for this, but leveraging De Groer (2017), we adopt his typology of intermediaries. Lafitte's (2024) thesis on the Market for Tax Havens intermediaries operate within and exercise influence on gives us insight into functional specialisation patterns.
    \item \textbf{ICIJ-based quantitative work} - finally, we'll cover the literature that has leveraged ICIJ data to better understand offshore networks quantitatively. The ICIJ data is a treasure trove of information and a remarkable source to study the offshore world empirically, but it comes with just as many limitations as one would expect in a world that has been rendered purposefully opaque. This will be a high-level overview of what's been done and what we can reasonably expect to generalise from it. Given the nascent state of quantitative work on intermediary networks, this analysis is necessarily exploratory.
\end{enumerate}

\subsection{Data and Methodology: Data and Its Discontents}

The different datasets used in the analysis, and how they were cleaned and prepared for analysis.

\begin{enumerate}
    \item \textbf{ICIJ data structure and cleaning} - it's a complicated dataset, and there are many steps to get it to a point where it makes analytical sense. The more we can escape from the pure graph structure and its adjacency matrices for the sake of analysis, the better. We'll cover the specific challenges: entity disambiguation, temporal issues, missing data patterns, and the fundamental selection bias problem (we only see what leaked).
    \item \textbf{Additional data sources} for entity-level joining - country-level governance indicators, economic data, cultural distance measures, and regulatory environment variables that let us move beyond pure network analysis.
    \item \textbf{Intermediary classification approach} - an LLM-based method to classify a sample of intermediaries by their functional roles. Not perfect, but gets us beyond purely structural measures to understand what these intermediaries actually do.
    \item \textbf{Feature engineering} - the main variables that will be leveraged in the analysis, and how they were derived from the underlying network structure. Entropy measures, specialisation indices, and network centrality metrics.
\end{enumerate}

Three main components in methodology section:

\begin{enumerate}
    \item \textbf{Entropy as a specialisation measure} - covering why entropy is particularly well-suited for measuring the concentration patterns we're interested in. Unlike simple concentration ratios, entropy captures both the number of categories and the evenness of distribution across them.

    \item \textbf{Multiple hypothesis testing corrections} - because we're in an exploratory phase, we'll be testing many relationships. We leverage the Bonferroni method to remain highly conservative and avoid Type I errors. Better to miss some true relationships than to chase false positives.

    \item \textbf{Non-parametric statistical tests} - given the many different sorts of data we'll end up with, and the fact that normality cannot justifiably be assumed for most of our measures, we'll rely heavily on non-parametric approaches. Rank-based tests, permutation methods, and bootstrap confidence intervals.

\end{enumerate}

\subsection{Empirical Section}

The analysis divides into two main empirical sections, corresponding to our two main claims:

\begin{enumerate}
    \item \textbf{Geographical specialisation of intermediaries} - showing that intermediaries tend to concentrate their operations within specific regional or cultural clusters, rather than operating as global generalists. We'll look at entropy measures across jurisdictions, cultural distance patterns, and network clustering by geography.
    \item \textbf{Functional specialisation of intermediaries} - demonstrating that intermediaries tend to focus on specific types of legal structures, client types, or financial arrangements, rather than offering fully generalised services. Here we'll examine specialisation by entity type, transaction patterns, and client characteristics.
\end{enumerate}

The key insight is that both patterns hold simultaneously - intermediaries are specialists along multiple dimensions, not just generalists who happen to be geographically constrained.

\subsection{Discussion: Policy Implications of Intermediary Specialisation}

The main task is defending our two propositions about specialisation and then exploring their implications.

\textbf{Lack of Knowledge on the Mechanisms::} The evidence strongly supports both geographical and functional specialisation, but we need to be honest about alternative explanations. Is this client-driven (clients prefer culturally familiar intermediaries) or supply-driven (intermediaries find it easier to operate within their comfort zones)? The data can't definitively answer this, but the patterns are robust either way.

\textbf{Policy implications:} The most significant implication is for our understanding of state capacity in tax enforcement. Two main ones:
\begin{itemize}
    \item Reinforcing the return of the state. Considering the fact that so many of them provide services to their own countrymen, even greater leverage.
    \item Layered liability regimes: two-fold structure of the personalised tax and investment advice versus the mass marketing of legal structures.
\end{itemize}
The sheer level of specialisation suggests states have considerably more power to tackle domestic tax avoidance and evasion than the standard "race to the bottom" narrative suggests. If intermediaries are specialists rather than perfect substitutes, targeted regulatory approaches become much more feasible.

\textbf{For regulatory design:} Specialisation patterns also have implications for layered liability regimes - if intermediaries cluster in predictable ways, you can design regulations that account for these patterns rather than treating the offshore world as an undifferentiated mass.

\textbf{Limitations and caveats:} Three main ones deserve emphasis.
\begin{itemize}
    \item First, these findings are static - will clients become less specialised in their choice of intermediaries over time, negating these patterns?
    \item Second, we're uncertain about the underlying mechanisms driving specialisation.
    \item Third, the data spans a long time range (through 2020), and patterns may be changing rapidly.
\end{itemize}

\subsection{Seventh Chapter: Conclusion}

Brief summary of main findings and implications. The convergent interest across public finance and IPE literatures in understanding intermediaries turns out to be well-founded - these actors do exhibit systematic patterns that have important implications for both our theoretical understanding and policy responses.

Future research directions include incorporating temporal dynamics, testing the mechanisms behind specialisation patterns, and exploring how these patterns might be shifting in response to recent regulatory changes. There's also potential for coupling these structural findings with cultural and institutional variables to better understand the communities that emerge around offshore finance.

