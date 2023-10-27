def index_range(page, page_size):
    # Calculate the start index for the given page and page_size
    start_index = (page - 1) * page_size
    # Calculate the end index by adding the page_size to the start index
    end_index = start_index + page_size
    # Return the start and end indexes as a tuple
    return (start_index, end_index)

