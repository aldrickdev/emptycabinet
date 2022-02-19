# emptycabinet

This project is to help keep inventory of everyday items

## Features

- User should be able to:
  - Login
  - Disable Account
  - Create a Cabinet
    - They should be able to add items to it with at least the name of the item and quantity. Eventually an image
  
## Database Tables

### Base Tables

- User:  
  - id: int pk  
  - email: string
  - name: string
  - hashed_password: string

- Cabinet:
  - id: int pk
  - owner_id: int fk

- Item:
  - id: int pk
  - name: string
  - image: string *`Eventually`*

### Association Tables

- Cabinet and Item
  - cabinet_id: int fk
  - item_id: int fk

### Relationships

| Tables | Relationship |
|--------|--------------|
| User - Cabinet | One to Many |
| Cabinet - Item | One to Many |
