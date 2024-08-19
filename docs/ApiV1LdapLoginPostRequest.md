# ApiV1LdapLoginPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_slug** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_login_post_request import ApiV1LdapLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapLoginPostRequest from a JSON string
api_v1_ldap_login_post_request_instance = ApiV1LdapLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapLoginPostRequest.to_json()

# convert the object into a dict
api_v1_ldap_login_post_request_dict = api_v1_ldap_login_post_request_instance.to_dict()
# create an instance of ApiV1LdapLoginPostRequest from a dict
api_v1_ldap_login_post_request_from_dict = ApiV1LdapLoginPostRequest.from_dict(api_v1_ldap_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

