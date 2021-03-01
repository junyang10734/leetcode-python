def fetch_results_to_display(sort_column, sort_order, results_per_page, page_index, results):
    arr = [[name, rel, price] for name, (rel, price) in results.items()]
    arr = sorted(arr, key=lambda x:x[sort_column], reverse=sort_order==1)
    start_index = results_per_page*page_index
    return [name for name, _, _ in arr[start_index:start_index + results_per_page]]


def rankingProducts(numOfProducts, products, sortKey, sortOrder, productsPerRow, rowNumber):
    arr = sorted(products, key=lambda x:x[sortKey], reverse=not sortOrder)
    start_index = productsPerRow*rowNumber
    return [name for name, _, _ in arr[start_index:start_index + productsPerRow]]


if __name__ == '__main__':
    sort_column = 2
    sort_order = 1
    results_per_page = 1
    page_index = 0
    results_length = 5
    results = {'item1': (1, 15), 'item2': (3, 4), 'item3': (10, 8), 'item4': (19, 80), 'item5': (20, 10)}
    res = fetch_results_to_display(sort_column, sort_order, results_per_page, page_index, results)
    print(res)
    
    numOfProducts = 5
    products = [['product1', 10, 5], ['product2', 3, 3], ['product3', 17, 4], ['product4', 9, 4], ['product5', 1, 5]]
    sortKey = 1
    sortOrder = False
    productsPerRow = 3
    rowNumber = 1
    print(rankingProducts(numOfProducts, products, sortKey, sortOrder, productsPerRow, rowNumber))