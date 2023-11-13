import os
import requests


def get_render_deployment_status():

    url = "https://api.render.com/v1/services/serviceId"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {os.getenv('RENDER_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    print(response.text)


def update_github_deployment_status(status):
    github_token = os.getenv('WORKFLOW_API_KEY')
    repository = os.getenv('REPOSITORY')
    headers = {'Authorization': f'token {github_token}'}
    data = {
        'state': status,
        'environment': 'Production',
        'description': 'Deployment status from Render',
    }
    response = requests.post(
        f'https://api.github.com/repos/{repository}/deployments',
        headers=headers,
        json=data
    )
    return response
