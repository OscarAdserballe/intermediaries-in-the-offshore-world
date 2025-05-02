
1. Title slide and research question: 
    What is the role of intermediaries in facilitating the creation of offshore tax havens?

    * We use network theory to study the role of intermediaries in the creation of offshore tax havens
    * A prime target to regulate to crack down on tax avoidance, evasion and the a key driver of inequality.

1. Abstract slide

Intermediaries form the links enabling tax haven use, contributing to tax avoidance and inequality. This study examines these actors as potential regulatory targets. Extending the network analysis of Chang et al. (2023) and drawing on Harrington's (2016) micro-sociological evidence, I analyze International Consortium of Investigative Journalists (ICIJ) leak data. Although ICIJ data has limitations for estimating avoidance scale, it permits generalization about intermediary roles within these networks. A novel agentic method is employed to enrich ICIJ data samples using available information about their role online.

Four propositions emerge: 1) The overall network displays scale-free properties, implying vulnerability to the loss of central intermediaries. 2) Intermediaries exhibit cultural specificity, often catering to distinct client countries and clientele. 3) Intermediary types perform different network roles with varying systemic importance as measured by degree. 4) Network structures respond dynamically to regulation and financial innovation, indicating they are not immutable. This analysis provides insight into the structure and potential vulnerabilities of tax haven networks through the lens of intermediary action.

3. Motivation: Economics and Public Finance
* Original model: Demand-side demand usign Allignham-Sandmo model. Doesn't work well for the top of the distribution nor the audit studies typically used (e.g. Kleven et al. 2011)
* So we're pretty interested in supply-side models and very much in vogue right now

Therefore, alternative methods to capture **sophisticated top-end evasion**:
* Macro statistics on wealth held in tax havens from tax haven central banks, BIS etc. (Zucman 2013; Johannesen and Zucman, 2014; Alstadsæter at al. 2018)
* Micro data on tax evasion from leaks: HSBC, Panama Papers, Paradise Papers, Swiss Leaks, LuxLeaks, etc. (Alstadsæter et al. 2019; Londono-Velez and Avila-Mahecha, 2021)
* Tax Amnesties (US: Guyton et al. 2021; Argentina: Londono-Velez & Tortarolo, 2022; Netherlands: Leenders et al. 2023)

Include Alstadsæter model: Alstadsæter et al. (2019) model, tax evasion and inequality paper:

-> Shifts focus to supply-side and intermediaries. Already get some comparative statics on role of inequalty, price of detection

4. Really, really hard to get data on intermediaries: Micro-sociological accounts of  

Brooke Harrington (2016) and the orle intermediaries play.
(Include pcitre in images/harrington.jpeg)

So we use network theory adn the once-in-a-lifetime opportunity offered by the ICIJ leaks collating Pandora Papers, Panama Papers etc.
And a research tradition started by e.g. Chang et al. (2023) but still highly limited accounts, and mostly focusing on sanctions.

-> How do these networks **actually** look like beyond the micro-sociological evidence we have?

(Include images/chang.png)

5. Concrete example

(Include michael.png)

(Include images/michael_webpage.png)

6. 4 Propostions about intermediaries.

    \item 1) \textbf{Overall vulnerability corresponding with supply-side model}: Scale-free distribution where power-law distribution the nature of htem, and there's significant difficulty reconstituting the network in the case of a loss of an intermediary,
    \item 2) \textbf{Intermediaries tightly culturally bound}: though all following a power-law distribution, there's significant differences across client countries. Intermediaries cater to specific client countries, and importantly, there's differntial levels of vulnerability across differnet countries.
    \item 3) \textbf{Intermediaries serve different roles in the network}: We can further evince differences across the different types of intermediaries. Different roles of intermediaries are more vulnerable than others.
    \item 4) \textbf{Regulation (and innovations) influence network structure}: These networks should not be taken to be immutable.
\
(include images/powerlaw.png)

7. Data and Methods

God damn, if there's nto a lot of cleaning

Datasets
* Primarily: ICIJ data
* Sebastien Lafitte's (2024) data on history of tax haven legal innovations
* WJP on rule of law
* VDem data on regime types

Methods:
* Primarily: Network analysis
* Regression analysis (discontinuity designs, OLS)
* Time-series analysis

8. Enriching intermediaries
Typology:
\textbf{Tax Experts}:
\textbf{Legal Experts}:
\textbf{Administrators}:
\textbf{Investment Advisors}:

Using LangGraph:
(Include images/agent_graph.png)


Into object 

```python
class ClassificationResult(BaseModel):
    """Schema for the classification output"""
    classification: Intermediary = Field(description="The type of intermediary")
    role_muddled: bool = Field(description="Whether the type of intermediary role is muddled")
    role_muddled_reasoning: str = Field(description="Brief justification for the role muddled")
    is_individual: bool = Field(description="Whether the intermediary is an individual")
    job_title: str = Field(description="The job title of the intermediary")
    confidence: Confidence = Field(description="Confidence either low or high. Use low if unsure or information is limited.")
    justification: str = Field(description="Detailed justification for the classification")
    key_evidence: List[str] = Field(description="Specific evidence points supporting the classification")
```


