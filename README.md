# Web Scrapper: Fetch Users from Public API

This Python script fetches user details from a public API endpoint using the GET method and displays selected information in a readable format.

---

## Task Overview

- Calls the public API:
[https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)

- Displays for each user:
- Name
- Username
- Email
- City (from `address.city`)
- Only prints users whose city name starts with the letter **"S"** (optional bonus).
- Handles API errors (like connection failure or empty response).

---

## Example Output

```

User 1:
Name: Chelsey Dietrich
Username: Kamren
Email: [Lucio_Hettinger@annie.ca](mailto:Lucio_Hettinger@annie.ca)
City: South Christy
-------------------

User 2:
Name: Clementina DuBuque
Username: Moriah.Stanton
Email: [Rey.Padberg@karina.biz](mailto:Rey.Padberg@karina.biz)
City: San Antonio
-----------------

```

---

## How to Run

1. Make sure Python 3 is installed.
2. Install the required library:
```bash
   pip install requests
```

3. Run the script:
```bash
    python fetch_users.py
```

---

## Requirements

* Python 3.x
* `requests` library

---

## Notes

* The script automatically skips users whose city name does not start with 'S'.
* Includes proper error handling for API request failures and empty data responses.

---

**Author:** Sumit Beniwal
