# **Replication package for the ICSE 2025 submission: "Real Faults in Deep Learning Fault Benchmarks: How Real Are They?"**

## Systematic Literature Analysis

The information for the performed systematic literature analysis is contained in folder "SysLitAnalysis". The file "query.txt" contains the query we have used to search Scopus. The file "**analysis.xlsx**" contains information about the whole analysis process. 

In particular, sheet "AbstractAnalysis" containt the list of all papers that the search query returned. The column "AbstractComment" provides comments for the papers that were excluded based on the reading of their abstract. If this column is empty, it means that the paper is kept for further analysis.

The sheet "FullPaperAnalysis" contains details on the analysis of the full text of the papers that survived the abstract analysis stage. The column "Downloaded?" reports whether we were able to obtain and download the full text. The column "HasRealFaults?" reports whether there are real faults involved in the paper. However, these real faults might be not real DL faults. The column "IsIncluded?" gives the final verdict for this stage and has the value "Yes" only for the paper where real faults are likely to be DL faults. 

The sheet "SnowballingAll" contains information on the list of papers snowballed from the 9 papers that were not eliminated after the full text analysis stage. The column "Type of snowballing" indicated whether the paper was obtained via forward or backward snowballing. The sheet "SnowballingNoDuplicates" contains the list with no duplicates and the sheet "SnowballingNew" contains the list of papers that have been snowballed and were not obtained via the initial search string. 

In the sheet "SnowballingNew" we also provide information on abstract and full text analysis for the snowballed papers in the columns "Abstract" and "FullPaperAnalysis" correspondingly. The column "BuggyFixed" performs an initial check on whether the paper is likely to contain buggy and fixed pairs for real DL faults. The papers for which this column has value "Yes" are added to the final list of papers for analysis. 

The sheet "FinalList" contains the list of 10 papers from the initial analysis and 6 papers from snowballing. The column "Link to dataset" contains the link to the replication packages of these papers where their bug datasets are presented. The column "NumberOfBugs" reports number of bugs in each datasets. Column "Keep?" reports the final verdict on whether the dataset in the paper is kept for our manual analysis, while column "Comment" contains justification on why the paper were excluded from analysis.







