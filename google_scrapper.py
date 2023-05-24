from googlesearch import search

def get_search_links(query, num_results):
    search_results = search(query, num_results=num_results)
    links = []
    for result in search_results:
        links.append(result)
    return links

search_query = "inurl:shop_category.php?id="
num_results = 50
search_links = get_search_links(search_query, num_results)

for link in search_links:
    print(link)
