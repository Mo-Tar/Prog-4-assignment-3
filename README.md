# COMP 3504 - Tool Inventory Management System

## API Overview
This API allows users to search, add, update, and delete tools from a tool inventory.

### Base URL
`http://34.29.246.163:8080/api`

### Authentication
No authentication is required for this API.

---

## Endpoints Overview
- [GET /api/items](#get-items)
- [GET /api/items/{id}](#get-items-by-id)
- [POST /api/items](#post-items)
- [PUT /api/items](#put-items-by-id)
- [DELETE /api/items](#delete-items-by-id)

---

<a id="get-items"></a>
### GET /api/items

**Method**: `GET`

**Endpoint**: `/api/items`

**Parameters**: 
- `name` (query parameter, optional): The name of the item to search for.

**Description**: Retrieves a list of all items in the inventory or searches for items by name.

**Example Request**:
- `GET /api/items`
- `GET /api/items?name=Knock Bits`

---

<a id="get-items-by-id"></a>
### GET /api/items/{id}

**Method**: `GET`

**Endpoint**: `/api/items/{id}`

**Parameters**: 

**Description**: Returns information of an item identified by its ID.

**Example Request**:

- `GET /api/items/3000`

---

<a id="post-items"></a>
### POST /api/items

**Method**: `POST`

**Endpoint**: `/api/items`

**Parameters**: 
- `ItemID` (body parameter): The ID of the item to be added into the inventory.
- `Name`(body parameter): The name of item to be added into the inventory.
- `Quantity`(body parameter): The number of units available for the item.
- `Price`(body parameter): The price of single unit of the item.
- `SupplierID`(body parameter): The supplier ID. 

**Description**: Adds a new item to the inventory.

**Example Request**:
- `POST /api/items`

**Request Body Sample**:
```json
{
  "ItemID": 4000,
  "Name": "New Item Name",
  "Quantity": 19,
  "Price": 12.67,
  "SupplierID": 50015
}
```

---
<a id="put-items-by-id"></a>
### PUT /api/items

**Method**: `PUT`

**Endpoint**: `/api/items`

**Parameters**: 
- `ItemID` (body parameter): The ID of the item to be updated.
- `Quantity` (body parameter): The new quantity value for the item.

**Description**: Updates the quantity of an existing item in the inventory.

**Example Request**:
- `PUT /api/items`

**Request Body Sample**:
```json
{
  "ItemID":3000,
  "Quantity": 19
}
```

---
<a id="delete-items-by-id"></a>
### DELETE /api/items

**Method**: `DELETE`

**Endpoint**: `/api/items`

**Parameters**: 
- `id` (query parameter, optional): The ID of the item to be deleted.
- `name` (query parameter, optional): The name of the item to be deleted.

**Note**: At least one of `id` or `name` must be provided to successfully delete an item.

**Description**: Deletes an item from the inventory by ID or name.

**Example Request**:

- `DELETE /api/items?id=3000`

- `DELETE /api/items?name=Knock Bits`

---

## Contribution
- All team members contributed equally to the development tasks. 
