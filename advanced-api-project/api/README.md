## Advanced Query Features
- **Filtering**:
  - Filter by title: `/books/?title=<title>`
  - Filter by author: `/books/?author__name=<author_name>`
  - Filter by publication year: `/books/?publication_year=<year>`

- **Searching**:
  - Search by title or author: `/books/?search=<search_term>`

- **Ordering**:
  - Order by title: `/books/?ordering=title`
  - Order by publication year (descending): `/books/?ordering=-publication_year`
