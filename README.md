# SKU GENERATOR MICROSERVICE - Zachary Johnson (JOHNSZA5)

## OVERVIEW
The **SKU Generator Microservice** provides an API to generate unique Stock Keeping Units (SKUs) with optional prefixes. It ensures each SKU is unique and allows users to specify a prefix for customization. 

## COMMUNICATION CONTRACT 

### 1. Health Check Endpoint
- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Returns a simple message to confirm the microservice is running.

#### Example Request:
A `GET` request to `/` checks if the service is running.

- **Request URL**: `http://127.0.0.1:5004/`
- **Response (Plain Text)**:  
  ```
  SKU Generator Microservice is running. Use /generateSKU with a POST request to generate SKUs.
  ```

---

### 2. Generate SKU Endpoint
- **Endpoint**: `/generateSKU`
- **Method**: `POST`
- **Description**: Generates a unique SKU. Optionally, a prefix can be provided.

#### Request Body (JSON):
| Field  | Type   | Required | Description                                      |
|--------|--------|----------|--------------------------------------------------|
| prefix | String | No       | Optional prefix for the SKU. Maximum length: 7. |

#### Response (JSON):
| Field | Type   | Description                          |
|-------|--------|--------------------------------------|
| sku   | String | Generated unique SKU with the prefix.|

If the prefix is invalid (length ≥ 8), the service responds with a `400 Bad Request` and an error message.

---

## EXAMPLE PROGRAMMATIC CALLS AND RESPONSES

### 1. Generating a SKU Without a Prefix
**Request Body:**
```json
{}
```

**Response:**
```json
{
  "sku": "SOSGWMNH"
}
```

---

### 2. Generating a SKU With a Correct Prefix
**Request Body:**
```json
{
  "prefix": "TEST"
}
```

**Response:**
```json
{
  "sku": "TESTVGSJ"
}
```

---

### 3. Generating a SKU With an incorrect Prefix
**Request Body:**
```json
{
  "prefix": "TOOLONGPREFIX"
}
```

**Response:**
```json
{
  "error": "Prefix too long"
}
```

---

## INSTRUCTIONS FOR RECIEVING DATA
To receive data, use any HTTP client to make a `POST` request to `/generateSKU` with a JSON payload. Example response formats are shown above.

**Python Example (Using `requests`):**
```python
import requests

# Set the base URL
url = "http://127.0.0.1:5004/generateSKU"

# Example without a prefix
response = requests.post(url, json={})
print(response.json())  # Output: {"sku": "SOSGWMNH"}

# Example with a valid prefix
response = requests.post(url, json={"prefix": "TEST"})
print(response.json())  # Output: {"sku": "TESTVGSJ"}

# Example with an invalid prefix
response = requests.post(url, json={"prefix": "TOOLONGPREFIX"})
print(response.json())  # Output: {"error": "Prefix too long"}
```

---

## RUNNING THE MICROSERVICE

1. Cloning the repository:
   ```
   git clone https://github.com/ZackJohnson1/Microservice_A.git
   cd Microservice_A
   ```

2. Installing dependencies:
   ```
   pip install flask
   ```

3. Starting the microservice:
   ```
   python3 sku_generator.py
   ```

4. Access the service at:
   - **Base URL**: `http://127.0.0.1:5004`

---

## PLEASE NOTE
- Ensure your application sends proper JSON in the request body.
- Handle `400 Bad Request` responses gracefully by checking for the `"error"` field in the response.
