import os
import requests
import re
from dotenv import load_dotenv

# Handling environmental issues

# If running on local IDE else GitHub Actions
if os.getenv('GITHUB_ACTIONS') == "true":
    GH_TOKEN = os.getenv('ACCESS_TOKEN')

else:
    load_dotenv()
    GH_TOKEN = os.getenv('GITHUB_TOKEN')

# Set the base URL for GitHub's API
base_url = 'https://api.github.com'

# Define the username for which you want to retrieve pull requests
username = 'sqali'

# Construct the API endpoint URL for listing pull requests by the specified user
endpoint = f'{base_url}/search/issues?q=is:pr+author:{username}&per_page=1000'

# Set headers including the authorization token
headers = {
    'Authorization': f'token {GH_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Send a GET request to the API endpoint
response = requests.get(endpoint, headers=headers)

contributions_dictionary = {}

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the list of pull requests
    pull_requests = data['items']
    # Print information about each pull request
    for pr in pull_requests:
        if pr['pull_request']['merged_at']:
            contributions_dictionary[pr['title']] = pr['html_url']

else:
    print(f"Failed to retrieve pull requests: {response.status_code}")

# Converted the dictionary into a Pandas DataFrame
TITLE_list = []
URL_list = []

for key, value in contributions_dictionary.items():

    TITLE_list.append(key)
    URL_list.append(value)

# List of repositories to check for updates, you can also add new repositories (dont forget to add them in the opensourceproject.md page)
repository_list = ["keras", "scikit"]

# Iterate over the repositories to check for new pull requests
for repo in repository_list:
    pattern = re.compile(rf'\b{repo}\b')
    with open('_pages/opensource-projects.md', 'r+') as md_file:
        content = md_file.readlines()
        
        for title, url in zip(TITLE_list, URL_list):
            if repo in url:
                if url not in ''.join(content):
                    # Find the line where the repository section starts
                    repo_section_line = next((i for i, line in enumerate(content) if repo.capitalize() in line), None)
                    
                    if repo_section_line is not None:
                        # Insert the pull request just below the repository section line
                        content.insert(repo_section_line + 1, f"- [{title}]({url})\n")
        
        # Move the file cursor to the beginning and write the updated content back
        md_file.seek(0)
        md_file.writelines(content)
        md_file.truncate()
