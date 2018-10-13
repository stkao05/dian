# Getting started

__Running dev server__
```
bundle exec jekyll serve
```


# Development log

__Current status__

Wrote Python script to convert raw post data (.html) to Jekyll post format (markdown). However, there are still some data sanitization and normalizing needs to be performed:

- The post content contains HTML tags such as `<script/>`, `<table>`, `<img>`
- Need to re-write img URL to URL in the Jekyll format
- Blog categories needs to be setup


Approach:
- `raw/` directory should remain untouched to make sure source is not broken mistakenly in the future
- Make sure all data properly are transfer from raw markdown format first. Then perform sanitation work there from there
- Incremental data sanitation

