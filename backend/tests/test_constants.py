from adapter_processor_v2.constants import AdapterKeys, AllowedDomains


def test_adapter_keys_and_allowed_domains():
    """
    Test the AdapterKeys constants and AllowedDomains enum.
    
    This test ensures that:
    1. Some key constants in AdapterKeys are correctly defined.
    2. The AllowedDomains enum contains the expected values.
    3. The AllowedDomains.list() method returns the correct list of domain values.
    """
    # Test AdapterKeys constants
    assert AdapterKeys.JSON_SCHEMA == "json_schema"
    assert AdapterKeys.ADAPTER_TYPE == "adapter_type"
    assert AdapterKeys.LLM == "LLM"
    assert AdapterKeys.VECTOR_DB == "VECTOR_DB"
    assert AdapterKeys.EMBEDDING == "EMBEDDING"

    # Test AllowedDomains enum
    assert AllowedDomains.ZIPSTACK.value == "@zipstack.com"
    assert AllowedDomains.UNSTRACT.value == "@unstract.com"

    # Test AllowedDomains.list() method
    expected_domains = ["@zipstack.com", "@unstract.com"]
    assert AllowedDomains.list() == expected_domains
