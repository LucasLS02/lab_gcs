
import requests

# Configuração
TOKEN = "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"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
ENDPOINT = "https://api.github.com/graphql"

# Consulta GraphQL
QUERY = """
{
  search(query: "stars:>100000", type: REPOSITORY, first: 100) {
   edges{
      node{
        ... on Repository {
          nameWithOwner
          createdAt
          pullRequests(states: MERGED) {
            totalCount
          }
          updatedAt
      }
    }
  }
  }
}
"""

response = requests.post(ENDPOINT, json={"query": QUERY}, headers=HEADERS)
data = response.json()

for edge in data["data"]["search"]["edges"]:
    repo = edge["node"]
    print(f"Repository: {repo['nameWithOwner']}")
    print(f"Created At: {repo['createdAt']}")
    print(f"Total Merged PRs: {repo['pullRequests']['totalCount']}")
    print(f"Updated At: {repo['updatedAt']}")
    print("------") 
    
    """print(f"Total Releases: {repo['releases']['totalCount']}")
    
    print(f"Primary Language: {repo['primaryLanguage']['name']}")
    
    print(f"Issues Closed Ratio: {closed_issues}/{total_issues}")
    print("------") """