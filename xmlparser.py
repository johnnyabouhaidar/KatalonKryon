from bs4 import BeautifulSoup

# Read the HTML file

def get_element_data(file):
    with open(file, 'r') as file:
        html = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Define the tag you want to find
    tag_to_find = ['input','textarea']
    class_to_find = 'name'

    # Find all tags with the specified tag and class
    items = soup.find_all(tag_to_find)

    # List to store the results
    ids = []

    # Iterate through each found item and extract the text
    for item in items:
        ids.append(item["id"])

    # Print the results
    print(ids)

    tag_to_find=['span']
    items = soup.find_all(tag_to_find)


    # List to store the results
    names = []

    # Iterate through each found item and extract the text
    for item in items:
        if item.text != '' and item.text !='*' and item.text !='Required':
            names.append(item['id'])

    print(names)

    combined_dict = dict(zip(names, ids))

    print(combined_dict)
    return combined_dict

get_element_data("form.html")

