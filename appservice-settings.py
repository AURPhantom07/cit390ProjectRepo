import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.web import WebSiteManagementClient

# Replace with your own info
KEYVAULT_NAME = "cit390vault02"
RESOURCE_GROUP = "cit390"
APP_SERVICE_NAME = "signapp"
SUBSCRIPTION_ID = "9dffb6a1-5883-4aa6-9608-81366d20df7c"

# Build the vault URL
KV_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

# Authenticate
credential = DefaultAzureCredential()

# Create clients
secret_client = SecretClient(vault_url=KV_URI, credential=credential)
web_client = WebSiteManagementClient(credential, SUBSCRIPTION_ID)

# Get current App Service settings
app_settings = web_client.web_apps.list_application_settings(RESOURCE_GROUP, APP_SERVICE_NAME)
current_settings = app_settings.properties or {}

# List all secrets in the Key Vault
secret_properties = secret_client.list_properties_of_secrets()

for secret_prop in secret_properties:
    original_name = secret_prop.name
    env_var_name = original_name.replace("-", "_").upper()

    # Create Key Vault reference format
    # Note: Leaving version blank uses latest version automatically
    key_vault_ref = f"@Microsoft.KeyVault(SecretUri={KV_URI}secrets/{original_name})"

    print(f"Linking {env_var_name} to Key Vault secret {original_name}")
    current_settings[env_var_name] = key_vault_ref

# Push updated settings to App Service
web_client.web_apps.update_application_settings(
    RESOURCE_GROUP,
    APP_SERVICE_NAME,
    {"properties": current_settings}
)

print("All secrets successfully linked to App Service via Key Vault references.")
