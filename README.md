HMCTS FormFinder Scraper
------------------------

A [Scrapy](http://scrapy.org) project to download forms and metadata from the current [HMCTS FormFinder](http://hmctsformfinder.justice.gov.uk/HMCTS/FormFinder.do) site on justice.gov.uk

## Usage

Install requirements:

```
$ pip install requirements.txt
```

Run the scraper:

```
$ scrapy crawl formfinder
```

Forms will be saved to the `./output` directory, and metadata will be saved to `.output.jsonl` in [JSONlines](http://jsonlines.org) format.

## Metadata format

Example form:

```
{
  "category": "Adoption",
  "download_size": "75KB",
  "name": "A5",
  "language": "English",
  "title": "Application For Substitution Of One Adoption Agency For Another",
  "url": "http://hmctsformfinder.justice.gov.uk/HMCTS/GetForm.do?court_forms_id=27",
  "download_url": "http://hmctsformfinder.justice.gov.uk/courtfinder/forms/a005-eng.pdf",
  "download_format": "PDF",
  "last_modified": "May 2002",
  "type": "form"
}
```

Example 'leaflet' (form guidance/info):

```
{
  "category": "Probate",
  "download_size": "160KB",
  "name": "PA3",
  "language": "Welsh / Bilingual",
  "title": "Ffioedd Profiant o fis Ebrill 2011 ymlaen. / Probate Fees from April 2011.",
  "url": "http://hmctsformfinder.justice.gov.uk/HMCTS/GetLeaflet.do?court_leaflets_id=2526",
  "associated_form_names": [
    "N3"
  ],
  "download_url": "http://hmctsformfinder.justice.gov.uk/courtfinder/forms/pa003-bil.pdf",
  "download_format": "PDF",
  "last_modified": "April 2011",
  "type": "leaflet"
}
```

Note the `associated_form_names` array - these are references to the form `name` field in form objects, and detail the forms that this leaflet is related to.
