import onedrivesdk_fork
import requests
from onedrivesdk_fork.helpers import GetAuthCodeServer


redirect_uri = 'http://localhost:5000/getAToken'
client_secret = 'bC0FS4jxwf51~5c45_qYf.SoA2hiw0ou_~'
client_id='587dc278-3dc9-454b-b6df-9bec73890ac9'
api_base_url='https://api.onedrive.com/v1.0/'
scopes = ['wl.signin','wl.offline_access','onedrive.readwrite']

http_provider = onedrivesdk_fork.HttpProvider()
auth_provider = onedrivesdk_fork.AuthProvider(
    http_provider=http_provider,
    client_id=client_id,
    scopes=scopes)

client = onedrivesdk_fork.OneDriveClient(api_base_url, auth_provider, http_provider)

auth_url = client.auth_provider.get_auth_url(redirect_uri)
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)

root_folder = client.item(drive='me', id='root').children.get()
id_of_file = root_folder[0].id

client.item(drive='me', id=id_of_file).download('./path_to_download_to.txt')
