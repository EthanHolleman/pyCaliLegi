# PyCaliLegi

Automate pulling basic information about California legislation using Python 
and the Selenium package.

## Usage

`python pyCaliLegi.py`

```
usage: A small selenium based Python program built by the UC Davis Legeslative Affairs Committee to help automate California legistlation tracking.
       [-h] [-and AND_KEYWORDS [AND_KEYWORDS ...]] [-or OR_KEYWORDS [OR_KEYWORDS ...]] [-sum_size MAX_SUMMARY_SIZE] [-headless] O

positional arguments:
  O                     Path to output file (csv).

optional arguments:
  -h, --help            show this help message and exit
  -and AND_KEYWORDS [AND_KEYWORDS ...], --and_keywords AND_KEYWORDS [AND_KEYWORDS ...]
                        Keywords to search for bills by using "AND" qualifier. Specify up to three words.
  -or OR_KEYWORDS [OR_KEYWORDS ...], --or_keywords OR_KEYWORDS [OR_KEYWORDS ...]
                        Keywords to search for bills by using "OR" qualifier. Specify up to three words.
  -sum_size MAX_SUMMARY_SIZE, --max_summary_size MAX_SUMMARY_SIZE
                        Max number of sentences in include in extended summary.
  -headless, --headless
                        Run browser in headless mode.
```

## Example output

See example csv file at [here](exmples/)

## Special thanks to ...

Special thanks to [LazoCoder]('https://github.com/LazoCoder') for the
[Article-Summarizer](https://github.com/LazoCoder/Article-Summarizer) repo
which was used for creating bill summaries.
