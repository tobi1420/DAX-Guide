# The following document is a complete guide to successfully connect to the business central API to POST, PUT and GET data
# To ease the process of granting the token for access please use Post Man for testing before writing scripts with python and request.

# For Business Central Cloud tenants one must create an App Registration in Microsoft Azure. Consult this guide if in doubt: https://yzhums.com/20690/

# Go to Azure App Registration https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade
# Create a new registration and enter name and set supported account type to single tenant

# Go to Azure Authentication https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Authentication/
# Add a platform of type Web and set the Redirect URI to https://localhost:8080/login
# Save the Application ID for later use in Postman for Token generation

# Go to API Permission and add a permision https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/CallAnAPI
# Choose Dynamics 365 Business Central and the type Delegated Permision. Mark user_impersonation and Financials.ReadWrtie.All and add the permision
# Apply the same steps but this time choose Application Permision. Mark app_access, API.ReadWrite.All and Automation.ReadWrite.All and add the permision
# Grant Admin Consent for the App by clicking next to add permision. Click yes and all permisions are granted for the application

# Go to Certificates and Secrets https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Credentials
# Create new Client Secret with an Description and an Expiration Date of chosen period
# Save the Client Secrets Value and Secret ID for later use in Postman for Token generation

# Config in Azure is completed

# Go to Business Central and search for 'Microsoft Entra Applications'.
# Create new Application and paste the Application ID in the Client ID Field. Remeber to include the ID in curly brackets {}
# Set the state to 'Enabled'
# Assign permision in Business Central for the Application with the permision role of 'D365 BUS PREMIUM', 'D365 FINANCE' and 'D365 FULL ACCESS'
# Search for 'Microsoft Entra Applications again and ensure that the Application is set to 'Enabled'

# Config in Business Central is Completed

# Go to Postman and test the following endpoint for companies in a given tenant
# https://api.businesscentral.dynamics.com/v2.0/{TENANTID}/sandbox/api/v2.0/companies. The structure of the link will be analyzed later in this guide.
# Of Course an error will occur since the call can not be authorized.

# Go to the tab Authorization and choose 'Oauth 2.0' 
# Choose Add Authentication Data to Request Headers
# In the Request Header View Choose 'Client Credentials' 

# Set the Access Token URL to https://login.microsoftonline.com/{TENANTID}/oauth2/v2.0/token. Tenant ID can be found in the URL to your Business Central.
# Set the Client ID to the Application ID saved earlier (App Registration Overview)
# Set the Client Secret ID to the Client Secret Value saved earlier (This can not be accesed after creation. Please keep it secret, keep it safe)
# Set the Scope to https://api.businesscentral.dynamics.com/.default
# Set the Client Authentication to 'Send Client Credentials in Body'
# Click on 'Get New Access Token' and copy the generated token
# Click on 'Use this token'
# Set the header prefix to 'Bearer'

# Config in Postman is Completed

# Test with the following URL to see if response status is 200 https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/v2.0/companies
# One should receive json data similar to this: 

"""
{
    "@odata.context": "https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/v2.0/companies",
    "value": [
        {
            "id": "b45a2513-9023-ef11-8411-6045bde99c01",
            "systemVersion": "24.5.23489.23968",
            "timestamp": 3972,
            "name": "CRONUS Danmark A/S",
            "displayName": "",
            "businessProfileId": "",
            "systemCreatedAt": "2024-06-05T23:05:22.84Z",
            "systemCreatedBy": "00000000-0000-0000-0000-000000000001",
            "systemModifiedAt": "2024-06-05T23:05:22.84Z",
            "systemModifiedBy": "00000000-0000-0000-0000-000000000001"
        }
    ]
}
"""

# Structure of the Business Central API Endpoint
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/v2.0/companies

# api :                                                     indicate that the https request will be aimed towards an api
# businesscentral.dynamics.com :                            base url for the api
# v2.0 :                                                    api version to be used
# 89a1cf79-7084-42b3-be27-912b312aa9f9 :                    tenant id
# sandbox :                                                 environment
# api :                                                     api type
# v2.0 :                                                    api publisher
# companies :                                               entityname (typically table name)

# Structure of the Central API Endpoint for Custom API's with custom API Group and API Publisher
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items
# Remember, not all entitites can be called out of the box. One must develop Custom API's in AL and remember to set Editable to True in entity config

# api :                                                     indicate that the https request will be aimed towards an api
# businesscentral.dynamics.com :                            base url for the api
# v2.0 :                                                    api version to be used
# 89a1cf79-7084-42b3-be27-912b312aa9f9 :                    tenant id
# sandbox :                                                 environment
# api :                                                     api type
# tL :                                                      api publisher
# tLDev :                                                   api group (or folder structure for api)
# v1.0 :                                                    api version
# companies :                                               entityname (typically table name)

# Testing in Postman is Completed

# Make a GET request to the Business Central API in postman: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items

"""
{
    "@odata.context": "https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/$metadata#items",
    "value": [
        {
            "@odata.etag": "W/\"JzE5OzM4Njc0OTQ5MzcyMDA4NTI0NjYxOzAwOyc=\"",
            "no": "1000",
            "allowInvoiceDisc": true,
            "allowOnlineAdjustment": true,
            "alternativeItemNo": "",
            "applicationWkshUserID": "",
            "assemblyBOM": false,
            "assemblyPolicy": "Assemble_x002D_to_x002D_Stock",
            "automaticExtTexts": false,
            "baseUnitOfMeasure": "STK",
            "blockReason": "",
            "blocked": false,
            "budgetProfit": 0,
            "budgetQuantity": 0,
            "budgetedAmount": 0
        }
    ]
}
"""

# Make a GET request to the Business Central API with python: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items

import requests
BASEURL  = "https://api.businesscentral.dynamics.com"
API_VERSION = "v2.0"
COMPANY_ID = "89a1cf79-7084-42b3-be27-912b312aa9f9"
ENVIRONMENT = "sandbox"
TYPE = "api"
PUBLISHER = "tL"
API_GROUP = "tLDev"
API_PUBLISHER_VERSION = "v1.0"
ENTITY_NAME = "items"
ENDPOINT = f"{BASEURL}/{API_VERSION}/{COMPANY_ID}/{ENVIRONMENT}/{TYPE}/{PUBLISHER}/{API_GROUP}/{API_PUBLISHER_VERSION}/{ENTITY_NAME}"

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5idXNpbmVzc2NlbnRyYWwuZHluYW1pY3MuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5LyIsImlhdCI6MTczMjg4MjU4OCwibmJmIjoxNzMyODgyNTg4LCJleHAiOjE3MzI4ODY0ODgsImFpbyI6ImsyQmdZRGpoeExkbWZzTkNxWFdhVElrSnFSYzJBd0E9IiwiYXBwaWQiOiJiZmI5OTBjYy05MjY5LTQxNDEtYmNiMy1iODhjZjY1Yzc5NTciLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84OWExY2Y3OS03MDg0LTQyYjMtYmUyNy05MTJiMzEyYWE5ZjkvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3OTE1MWQ5OC03NGQzLTRjYWMtOGIwOC1mNWUxYTgxZmQ0ZjgiLCJyaCI6IjEuQWE4QWVjLWhpWVJ3czBLLUo1RXJNU3FwLVQzdmJabHNzMU5CaGdlbV9Ud0J1SjhkQVFDdkFBLiIsInJvbGVzIjpbIkF1dG9tYXRpb24uUmVhZFdyaXRlLkFsbCIsImFwcF9hY2Nlc3MiLCJBZG1pbkNlbnRlci5SZWFkV3JpdGUuQWxsIiwiQVBJLlJlYWRXcml0ZS5BbGwiXSwic3ViIjoiNzkxNTFkOTgtNzRkMy00Y2FjLThiMDgtZjVlMWE4MWZkNGY4IiwidGlkIjoiODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5IiwidXRpIjoieEtNVkNjZHRxay1FWEk4Wlh5VzRBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjYgNyJ9.talbnnnz6FtPVmSERvLGJnjkUxLRloXyYvE_dCybGG2kSiGdng16nvyWzTSR-zwF1AxbTjCr6C8EZarEpctBfq_7wKhZccrTAGU-1f_C7v_1lavgZrhgUsxDlfCW30eNhVz06Keuj8vCM-l_6XquvfmSyVmDeFQlPEUuaAcj893sbEAhWHMcOTuY7wavVWxf0uRtKYSP_rg8ZALGeOR_n4jTJ80Ti0y4HPx0ok_8hU4N6PXJOnPOadSDBI0gxraskt3gvij8o3X6OW2PMBKEfw0GXivXiyfSBYDieBUYU2b836BiUCznS7oDqwWGbZob9cwUuJp8XlYdDJEn9PiCrw"

HEADER = {
    "Authorization" : f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "If-Match": "*"
}

response = requests.get(url=ENDPOINT, headers=HEADER)
status =  response.status_code
raw_data = response.json()
data = dict(raw_data)['value']
print(data)

# Make a POST request to the Business Central API in postman: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items
# Remember to send the data or body as the type raw and json. Also structure the data as a dictionary/json element

body = {
    "no": "1000000",
    "description": "Charizard!"
}

"""

{
    "@odata.context": "https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/$metadata#items/$entity",
    "@odata.etag": "W/\"JzE5OzEzNTkzNjE3MzE4ODc5NjkwMDQxOzAwOyc=\"",
    "no": "1000000",
    "allowInvoiceDisc": true,
    "allowOnlineAdjustment": true,
    "alternativeItemNo": "",
    "applicationWkshUserID": "",
    "assemblyBOM": false,
    "assemblyPolicy": "Assemble_x002D_to_x002D_Stock",
    "automaticExtTexts": false,
    "baseUnitOfMeasure": "",
    "blockReason": "".
    "description" : "Charizard!"
}

"""

# Make a POST request to the Business Central API with python: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items

import requests
BASEURL  = "https://api.businesscentral.dynamics.com"
API_VERSION = "v2.0"
COMPANY_ID = "89a1cf79-7084-42b3-be27-912b312aa9f9"
ENVIRONMENT = "sandbox"
TYPE = "api"
PUBLISHER = "tL"
API_GROUP = "tLDev"
API_PUBLISHER_VERSION = "v1.0"
ENTITY_NAME = "items"
ENDPOINT = f"{BASEURL}/{API_VERSION}/{COMPANY_ID}/{ENVIRONMENT}/{TYPE}/{PUBLISHER}/{API_GROUP}/{API_PUBLISHER_VERSION}/{ENTITY_NAME}"

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5idXNpbmVzc2NlbnRyYWwuZHluYW1pY3MuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5LyIsImlhdCI6MTczMjg4MjU4OCwibmJmIjoxNzMyODgyNTg4LCJleHAiOjE3MzI4ODY0ODgsImFpbyI6ImsyQmdZRGpoeExkbWZzTkNxWFdhVElrSnFSYzJBd0E9IiwiYXBwaWQiOiJiZmI5OTBjYy05MjY5LTQxNDEtYmNiMy1iODhjZjY1Yzc5NTciLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84OWExY2Y3OS03MDg0LTQyYjMtYmUyNy05MTJiMzEyYWE5ZjkvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3OTE1MWQ5OC03NGQzLTRjYWMtOGIwOC1mNWUxYTgxZmQ0ZjgiLCJyaCI6IjEuQWE4QWVjLWhpWVJ3czBLLUo1RXJNU3FwLVQzdmJabHNzMU5CaGdlbV9Ud0J1SjhkQVFDdkFBLiIsInJvbGVzIjpbIkF1dG9tYXRpb24uUmVhZFdyaXRlLkFsbCIsImFwcF9hY2Nlc3MiLCJBZG1pbkNlbnRlci5SZWFkV3JpdGUuQWxsIiwiQVBJLlJlYWRXcml0ZS5BbGwiXSwic3ViIjoiNzkxNTFkOTgtNzRkMy00Y2FjLThiMDgtZjVlMWE4MWZkNGY4IiwidGlkIjoiODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5IiwidXRpIjoieEtNVkNjZHRxay1FWEk4Wlh5VzRBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjYgNyJ9.talbnnnz6FtPVmSERvLGJnjkUxLRloXyYvE_dCybGG2kSiGdng16nvyWzTSR-zwF1AxbTjCr6C8EZarEpctBfq_7wKhZccrTAGU-1f_C7v_1lavgZrhgUsxDlfCW30eNhVz06Keuj8vCM-l_6XquvfmSyVmDeFQlPEUuaAcj893sbEAhWHMcOTuY7wavVWxf0uRtKYSP_rg8ZALGeOR_n4jTJ80Ti0y4HPx0ok_8hU4N6PXJOnPOadSDBI0gxraskt3gvij8o3X6OW2PMBKEfw0GXivXiyfSBYDieBUYU2b836BiUCznS7oDqwWGbZob9cwUuJp8XlYdDJEn9PiCrw"

HEADER = {
    "Authorization" : f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "If-Match": "*"
}

body = {
    "no": "1000002",
    "description": "Mew!"
}

response = requests.post(url=ENDPOINT, headers=HEADER, json=body)
status =  response.status_code
print(status)

# Make a PUT request to the Business Central API with Postman: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items('no=1000000')
# For PUT Requests remember that the primary key must be added to the endpoint via. the Odata protocol syntax.
# Also remember to includ the key value pair "If-Match" : "*" to the header sent to the API.

body = {
    "description": "Blastoise!"
}

"""

{
    "@odata.context": "https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/$metadata#items/$entity",
    "@odata.etag": "W/\"JzE5OzEzNTkzNjE3MzE4ODc5NjkwMDQxOzAwOyc=\"",
    "no": "1000000",
    "allowInvoiceDisc": true,
    "allowOnlineAdjustment": true,
    "alternativeItemNo": "",
    "applicationWkshUserID": "",
    "assemblyBOM": false,
    "assemblyPolicy": "Assemble_x002D_to_x002D_Stock",
    "automaticExtTexts": false,
    "baseUnitOfMeasure": "",
    "blockReason": "".
    "description" : "Blastoise!"
}

"""

# Make a PUT request to the Business Central API with python: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items('no=1000000')
# For PUT Requests remember that the primary key must be added to the endpoint via. the Odata protocol syntax.
# Also remember to include the key value pair "If-Match" : "*" to the header sent to the API.

import requests
BASEURL  = "https://api.businesscentral.dynamics.com"
API_VERSION = "v2.0"
COMPANY_ID = "89a1cf79-7084-42b3-be27-912b312aa9f9"
ENVIRONMENT = "sandbox"
TYPE = "api"
PUBLISHER = "tL"
API_GROUP = "tLDev"
API_PUBLISHER_VERSION = "v1.0"
ENTITY_NAME = "items"
ENDPOINT = f"{BASEURL}/{API_VERSION}/{COMPANY_ID}/{ENVIRONMENT}/{TYPE}/{PUBLISHER}/{API_GROUP}/{API_PUBLISHER_VERSION}/{ENTITY_NAME}"

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5idXNpbmVzc2NlbnRyYWwuZHluYW1pY3MuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5LyIsImlhdCI6MTczMjg4MjU4OCwibmJmIjoxNzMyODgyNTg4LCJleHAiOjE3MzI4ODY0ODgsImFpbyI6ImsyQmdZRGpoeExkbWZzTkNxWFdhVElrSnFSYzJBd0E9IiwiYXBwaWQiOiJiZmI5OTBjYy05MjY5LTQxNDEtYmNiMy1iODhjZjY1Yzc5NTciLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84OWExY2Y3OS03MDg0LTQyYjMtYmUyNy05MTJiMzEyYWE5ZjkvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3OTE1MWQ5OC03NGQzLTRjYWMtOGIwOC1mNWUxYTgxZmQ0ZjgiLCJyaCI6IjEuQWE4QWVjLWhpWVJ3czBLLUo1RXJNU3FwLVQzdmJabHNzMU5CaGdlbV9Ud0J1SjhkQVFDdkFBLiIsInJvbGVzIjpbIkF1dG9tYXRpb24uUmVhZFdyaXRlLkFsbCIsImFwcF9hY2Nlc3MiLCJBZG1pbkNlbnRlci5SZWFkV3JpdGUuQWxsIiwiQVBJLlJlYWRXcml0ZS5BbGwiXSwic3ViIjoiNzkxNTFkOTgtNzRkMy00Y2FjLThiMDgtZjVlMWE4MWZkNGY4IiwidGlkIjoiODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5IiwidXRpIjoieEtNVkNjZHRxay1FWEk4Wlh5VzRBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjYgNyJ9.talbnnnz6FtPVmSERvLGJnjkUxLRloXyYvE_dCybGG2kSiGdng16nvyWzTSR-zwF1AxbTjCr6C8EZarEpctBfq_7wKhZccrTAGU-1f_C7v_1lavgZrhgUsxDlfCW30eNhVz06Keuj8vCM-l_6XquvfmSyVmDeFQlPEUuaAcj893sbEAhWHMcOTuY7wavVWxf0uRtKYSP_rg8ZALGeOR_n4jTJ80Ti0y4HPx0ok_8hU4N6PXJOnPOadSDBI0gxraskt3gvij8o3X6OW2PMBKEfw0GXivXiyfSBYDieBUYU2b836BiUCznS7oDqwWGbZob9cwUuJp8XlYdDJEn9PiCrw"

HEADER = {
    "Authorization" : f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "If-Match": "*"
}

body = {
    "description": "Mew!"
}

response = requests.put(url=f"{ENDPOINT}(no='1000001')", headers=HEADER, json=body)
status =  response.status_code
print(status)

# Make a DELETE request to the Business Central API with Postman: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items('no=1000001')
# For DELETE Requests remember that the primary key must be added to the endpoint via. the Odata protocol syntax.
# Also remember to include the key value pair "If-Match" : "*" to the header sent to the API.

"""
204 No Content
"""

# Make a DELETE request to the Business Central API with Postman: 
# https://api.businesscentral.dynamics.com/v2.0/89a1cf79-7084-42b3-be27-912b312aa9f9/sandbox/api/tL/tLDev/v1.0/items('no=1000001')
# For DELETE Requests remember that the primary key must be added to the endpoint via. the Odata protocol syntax.
# Also remember to include the key value pair "If-Match" : "*" to the header sent to the API.

import requests
BASEURL  = "https://api.businesscentral.dynamics.com"
API_VERSION = "v2.0"
COMPANY_ID = "89a1cf79-7084-42b3-be27-912b312aa9f9"
ENVIRONMENT = "sandbox"
TYPE = "api"
PUBLISHER = "tL"
API_GROUP = "tLDev"
API_PUBLISHER_VERSION = "v1.0"
ENTITY_NAME = "items"
ENDPOINT = f"{BASEURL}/{API_VERSION}/{COMPANY_ID}/{ENVIRONMENT}/{TYPE}/{PUBLISHER}/{API_GROUP}/{API_PUBLISHER_VERSION}/{ENTITY_NAME}"

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL2FwaS5idXNpbmVzc2NlbnRyYWwuZHluYW1pY3MuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5LyIsImlhdCI6MTczMjg4MjU4OCwibmJmIjoxNzMyODgyNTg4LCJleHAiOjE3MzI4ODY0ODgsImFpbyI6ImsyQmdZRGpoeExkbWZzTkNxWFdhVElrSnFSYzJBd0E9IiwiYXBwaWQiOiJiZmI5OTBjYy05MjY5LTQxNDEtYmNiMy1iODhjZjY1Yzc5NTciLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84OWExY2Y3OS03MDg0LTQyYjMtYmUyNy05MTJiMzEyYWE5ZjkvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3OTE1MWQ5OC03NGQzLTRjYWMtOGIwOC1mNWUxYTgxZmQ0ZjgiLCJyaCI6IjEuQWE4QWVjLWhpWVJ3czBLLUo1RXJNU3FwLVQzdmJabHNzMU5CaGdlbV9Ud0J1SjhkQVFDdkFBLiIsInJvbGVzIjpbIkF1dG9tYXRpb24uUmVhZFdyaXRlLkFsbCIsImFwcF9hY2Nlc3MiLCJBZG1pbkNlbnRlci5SZWFkV3JpdGUuQWxsIiwiQVBJLlJlYWRXcml0ZS5BbGwiXSwic3ViIjoiNzkxNTFkOTgtNzRkMy00Y2FjLThiMDgtZjVlMWE4MWZkNGY4IiwidGlkIjoiODlhMWNmNzktNzA4NC00MmIzLWJlMjctOTEyYjMxMmFhOWY5IiwidXRpIjoieEtNVkNjZHRxay1FWEk4Wlh5VzRBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjYgNyJ9.talbnnnz6FtPVmSERvLGJnjkUxLRloXyYvE_dCybGG2kSiGdng16nvyWzTSR-zwF1AxbTjCr6C8EZarEpctBfq_7wKhZccrTAGU-1f_C7v_1lavgZrhgUsxDlfCW30eNhVz06Keuj8vCM-l_6XquvfmSyVmDeFQlPEUuaAcj893sbEAhWHMcOTuY7wavVWxf0uRtKYSP_rg8ZALGeOR_n4jTJ80Ti0y4HPx0ok_8hU4N6PXJOnPOadSDBI0gxraskt3gvij8o3X6OW2PMBKEfw0GXivXiyfSBYDieBUYU2b836BiUCznS7oDqwWGbZob9cwUuJp8XlYdDJEn9PiCrw"

HEADER = {
    "Authorization" : f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "If-Match": "*"
}

body = {
    "description": "Mew!"
}

response = requests.delete(url=f"{ENDPOINT}(no='1000002')", headers=HEADER, json=body)
status =  response.status_code
print(status)
