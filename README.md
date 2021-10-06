
# csv-diff-python3

[![Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](README.md/#herb-requirements)
[![testing](https://github.com/blue-monk/csv-diff-python3/actions/workflows/testing.yml/badge.svg)](https://github.com/blue-monk/csv-diff-python3/actions/workflows/testing.yml)
[![coverage](https://github.com/blue-monk/csv-diff-python3/blob/gh-pages/coverage.svg)](https://blue-monk.github.io/csv-diff-python3/)
[![License](https://img.shields.io/github/license/blue-monk/csv-diff-python3)](LICENSE)


## :herb: Overview

A simple command-line tool to see the difference between two CSV files.

This tool reports in the following style, and you can choose how to report.

1. Report the number of differences and line numbers
2. Report diff marks along with the contents of each CSV line
    * You can choose the following report styles
        * Horizontal (Side-by-side) display style
        * Vertical display style
    * You can choose to report only the lines with differences or all lines


---
:palm_tree: DEMO

![DEMO](appendix/csv-diff-animation.gif)

---


## :herb: Table of Contents

* [**Why csv-diff?**](#herb-why-csv-diff)
* [**Feature**](#herb-features)
* [**Requirements**](#herb-requirements)
  * [Runtime](#runtime)
  * [CSV files](#csv-files)
* [**Installation**](#herb-installation)
  * [With pip](#with-pip)
  * [Manual Installation](#manual-installation)
* [**Run**](#herb-run)
  * [If installed with pip](#if-installed-with-pip)
  * [If installed manually](#if-installed-manually)
* [**How to use**](#herb-how-to-use)
  * [Get Help](#get-help)
  * [One example](#one-example)
* [**Notices**](#herb-notices)
* [**Known Issues**](#herb-known-issues)
* [**Contributing**](#herb-contributing)
  * [Reporting Bugs / Feature Requests](#reporting-bugs--feature-requests)
* [**License**](#herb-license)


## :herb: Why csv-diff?

The `diff` command that compares files is unaware of key columns (like primary keys in a database).
Therefore, it may give undesired results in detecting differences in CSV files that have key columns.

For example, consider comparing the contents of tables in two databases that are inaccessible to each other. 
One way is to output each database's data as a CSV file and compare it.
In this case, the `diff` command does not pay attention to the key columns, so lines with different keys may be compared.
It is not possible to make an accurate judgment of the difference with the key in mind.

This tool, on the other hand, recognizes key columns and detects differences.
Specify the key columns as an argument at the time of execution. You can get the comparison result you want.


## :herb: Features

* CSV delimiter, line feed character, presence/absence of header, etc. are automatically determined (can be specified)
* Make a comparison after matching with the key columns
* You can specify columns that are not compared
* Differences can be displayed side-by-side (more suitable when the number of columns is small)
* Differences can be displayed in vertical order (more suitable when the number of columns is large)
* Differences are indicated by the following marks, which we call DIFF-MARK
     * `!`: There is a difference
     * `<`: Exists only on the left side
     * `>`: Exists only on the right side
* It is also possible to display only the number of differences and the line number with the difference
* It is possible to compare one file with commas and one file with tabs
* Low memory consumption
* Only Python standard modules are used and provided as a single file, so it is easy to install even on an isolated environment


## :herb: Requirements

### Runtime
* Python3.6 or later

### CSV files
* Must be sorted by key columns


## :herb: Installation

### With pip

```sh
pip install git+https://github.com/blue-monk/csv-diff-python3
```
It may be safer to install it on a virtual environment created with venv.

### Manual installation

Place `csvdiff.py` in any directory on the machine where Python 3 is installed.  
It will be easier to use if you place it in a directory defined on PATH.

## :herb: Run

### If installed with pip

```sh
$ csvdiff3 -h
```

### If installed manually

```sh
$ python csvdiff.py -h
```
or
```shell
$ chmod +x csvdiff.py
$ ./csvdiff.py -h
```

## :herb: How to use

See the [Wiki](https://github.com/blue-monk/csv-diff-python3/wiki) for more details.
* [Wiki/Command](https://github.com/blue-monk/csv-diff-python3/wiki/Command)
* [Wiki/How to use](https://github.com/blue-monk/csv-diff-python3/wiki/How-to-use)

### Get help
```sh
$ ./csvdiff.py -h
```

### One example

Here is one example with the following sample data in `appendix/csv_samples/`.  
See the [Wiki/How to use](https://github.com/blue-monk/csv-diff-python3/wiki/How-to-use) for more details.

#### Sample data

Suppose the keys are the 0th column and the 2nd column.

* sample_lhs.csv
    ```csv
    head1, head2, head3, head4, head5
    key1-2, value1-2, key2-2, value2-2, 20201224T035908
    key1-3, value1-3, key2-3, value2-3, 20201224T180527
    key1-4, value1-4, key2-4, value2-4, 20201225T104851
    key1-5, value1-5, key2-5, value2-5, 20201225T142142
    ```

* sample_rhs.csv
    ```csv
    head1, head2, head3, head4, head5
    key1-1, value1-1, key2-1, value2-1, 20210108T142358
    key1-2, value1-3, key2-2, value2-z, 20210108T174216
    key1-4, value1-4, key2-4, value2-4, 20210109T090245
    key1-5, value1-v, key2-5, value2-5, 20210109T111231
    ```

#### Example of use

To view the contents of different lines, Use the `-d` (`--show-difference-only`) option.  
If you also want to see the number of differences, put the `-c` option (`--show-count`).

```sh
$ ../../src/csvdiff3/csvdiff.py sample_lhs.csv sample_rhs.csv -k 0,2 -dc

============ Report ============

* Differences
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sample_lhs.csv                                                        sample_rhs.csv                                                       Column indices with difference
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                   >  2 ['key1-1', 'value1-1', 'key2-1', 'value2-1', '20210108T142358']
2 ['key1-2', 'value1-2', 'key2-2', 'value2-2', '20201224T035908']  !  3 ['key1-2', 'value1-3', 'key2-2', 'value2-z', '20210108T174216']  @ [1, 3, 4]
3 ['key1-3', 'value1-3', 'key2-3', 'value2-3', '20201224T180527']  <
4 ['key1-4', 'value1-4', 'key2-4', 'value2-4', '20201225T104851']  !  4 ['key1-4', 'value1-4', 'key2-4', 'value2-4', '20210109T090245']  @ [4]
5 ['key1-5', 'value1-5', 'key2-5', 'value2-5', '20201225T142142']  !  5 ['key1-5', 'value1-v', 'key2-5', 'value2-5', '20210109T111231']  @ [1, 4]

* Count & Row number
same lines           : 0
left side only    (<): 1 :-- Row Numbers      -->: [3]
right side only   (>): 1 :-- Row Numbers      -->: [2]
with differences  (!): 3 :-- Row Number Pairs -->: [(2, 3), (4, 4), (5, 5)]
```
* Differences are indicated by the following DIFF-MARKs
     * `!` : There is a difference
     * `<` : Exists only on the left side
     * `>` : Exists only on the right side

* The number displayed before each CSV line data is the line number of the actual file
  * line number is 1 based

* For rows with differences, the column indices with differences will be displayed after `@`
  * column index is 0 based


## :herb: Notices

* *For large amounts of data*

  In the case of a horizontal report,  
  it takes longer than a vertical report because all lines are scanned in advance to collect information for report formatting.  
  For large amounts of data, consider vertical reports.

## :herb: Known Issues

* *Workaround for only one line*

    If the CSV file contains only one line, it will be recognized as a header.  
    You need to specify the option `-H n` to be recognized as CSV without a header.


## :herb: Contributing

### Reporting Bugs

We welcome you to use the GitHub issue tracker to report bugs or suggest features.


## :herb: License

csv-diff-python3 is released under the MIT license. Please read the [LICENSE](LICENSE) file for more information.



