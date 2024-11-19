import requests
import json


# Base URL for Flask Microservice
BASE_URL = "http://127.0.0.1:5004"


def test_home_endpoint():
    """This function tests the home endpoint and makes sure its running."""
    response = requests.get(BASE_URL + "/")
    print("\n[Test: Home Endpoint]")
    print(f"Response: {response.text}")
    assert response.status_code == 200, "Home endpoint did not return status 200"
    print("✅ Home endpoint test passed.")


def test_generate_sku_no_prefix():
    """This function tests the generateSKU endpoint without a prefix."""
    response = requests.post(BASE_URL + "/generateSKU", json={})
    print("\n[Test: Generate SKU Without Prefix]")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, "Generate SKU without prefix failed"
    assert "sku" in response.json(), "SKU not found in response"
    print("✅ Generate SKU without prefix test passed.")


def test_generate_sku_with_prefix():
    """This function tests the generateSKU endpoint with prefix."""
    prefix = "TEST"
    response = requests.post(BASE_URL + "/generateSKU", json={"prefix": prefix})
    print(f"\n[Test: Generate SKU With Prefix '{prefix}']")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, "Generate SKU with prefix failed"
    sku = response.json().get("sku", "")
    assert sku.startswith(prefix), "SKU does not start with the provided prefix"
    print(f"✅ Generate SKU with prefix '{prefix}' test passed.")


def test_generate_sku_invalid_prefix():
    """This function tests the generateSKU endpoint with a invalid prefix thats too long."""
    invalid_prefix = "TOOLONGPREFIX"  # exceeds the valid length
    response = requests.post(BASE_URL + "/generateSKU", json={"prefix": invalid_prefix})
    print(f"\n[Test: Generate SKU With Invalid Prefix '{invalid_prefix}']")
    print(f"Response: {response.json()}")
    assert response.status_code == 400, "Invalid prefix did not return status 400"
    assert "error" in response.json(), "Error message not found in response"
    print(f"✅ Generate SKU with invalid prefix '{invalid_prefix}' test passed.")


if __name__ == "__main__":
    print("\nRunning Tests for SKU Generator Microservice...")
    try:
        test_home_endpoint()
        test_generate_sku_no_prefix()
        test_generate_sku_with_prefix()
        test_generate_sku_invalid_prefix()
        print("\n🎉 All tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
