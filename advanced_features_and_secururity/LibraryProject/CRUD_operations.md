# CRUD Operations Documentation

## Create
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: 1984
```

## Retrieve
```python
book = Book.objects.get(title="1984")
# Output: 1984 George Orwell 1949
```

## Update
```python
book.title = "Nineteen Eighty-Four"
book.save()
# Output: Nineteen Eighty-Four
```

## Delete
```python
book.delete()
# Output: <QuerySet []>
```
