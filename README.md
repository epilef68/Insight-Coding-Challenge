# Table of Contents <a name="description"></a>

1. [Python Version](README.md#python-version)
2. [Required Packages](README.md#required-packages)
3. [Details of Implementation](README.md#details-of-implementation)
4. [Repo directory structure](README.md#repo-directory-structure)

## Python Version <a name="python-version"></a>

[Back to Table of Contents](README.md#table-of-contents)

This code was written to use Python 3.1.

## Required Packages <a name="required-packages"></a>

[Back to Table of Contents](README.md#table-of-contents)

This code doesn't use any third party packages. It does, however, use the defaultdict data type available from the collections package, as well as heapq, datetime and statistics which should all come standard with Python 3.1.


## Details of Implementation <a name="details-of-implementation"></a>

[Back to Table of Contents](README.md#table-of-contents)

In this coding challenge we developed an algorithm to read in values and create a running medium through a heap algorithm. This is done to decrease the computational time as heap structures are well suited for calculating a medium.



## Repo directory structure <a name="repo-directory-structure"></a>
[Back to Table of Contents](README.md#table-of-contents)

My Repo Structure
├── README.md
├── run.sh
├── src
│   └── find_political_donors.py
├── input
│   └── itcont.txt
├── output
|   └── medianvals_by_zip.txt
|   └── medianvals_by_date.txt
├── insight_testsuite
└── run_tests.sh
└── tests
└── test_1
|   ├── input
|   │   └── itcont.txt
|   |__ output
|   │   └── medianvals_by_zip.txt
|   |__ └── medianvals_by_date.txt

