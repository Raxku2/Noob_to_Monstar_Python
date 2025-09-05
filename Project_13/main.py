import requests

def get_repo_stats(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    
    response = requests.get(url)
    data = response.json()

    print("\n=== GitHub Repository Stats ===")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Owner: {data['owner']['login']}")
    print(f"Description: {data.get('description', 'No description')}")
    print(f"Stars ⭐: {data.get('stargazers_count', 0)}")
    print(f"Forks 🍴: {data.get('forks_count', 0)}")
    print(f"Watchers 👀: {data.get('watchers_count', 0)}")
    print(f"Open Issues: {data.get('open_issues_count', 0)}")
    print(f"License: {data['license']['name'] if data.get('license') else 'No license'}")
    print(f"Last Updated: {data.get('updated_at', 'N/A')}")
    print(f"Clone URL: {data.get('clone_url', 'N/A')}")
    print("==============================\n")


def main():
    print("GitHub Repo Stats Viewer")
    repo_input = input("Enter repository (owner/repo): ").strip()
    
    if "/" not in repo_input:
        print("❌ Invalid format! Please enter in the form owner/repo (e.g. torvalds/linux)")
    else:
        owner, repo = repo_input.split("/")
        get_repo_stats(owner, repo)



main()