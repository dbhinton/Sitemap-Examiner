# Sitemap Examiner

This project consists of a RESTful API service that searches a product sitemap XML and returns product details based on SKU. It also includes a simple web interface to interact with the service.

## System Overview

### RESTful API Service

The RESTful API service performs the following steps:
- Fetches the sitemap XML from the provided URL.
- Parses the XML to extract URLs and their corresponding SKUs.
- Searches for a provided SKU in the list of extracted SKUs.
- Fetches the product page content in parallel using a thread pool.
- Extracts product details (title, author, price) from the fetched HTML content.
- Returns the product information as a JSON response.

### Simple Web Interface

The web interface allows users to:
- Enter a product SKU through a text input field.
- Make an API call to the RESTful service with the provided SKU.
- Display the received product information on the web page.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (version 3.6 or higher)
- Pip (Python package manager)

## Getting Started

1. **Clone the Repository:**

   ```
   git clone https://github.com/dbhinton/sitemap-examiner.git
   cd sitemap-examiner
2. Build and Run the app
`./build.sh && ./run.sh app.py`
3. Go to http://127.0.0.1:5000/
4. Enter a few valid sku's


## Scaling

To scale the system across all sitemap files:
1. Fetch and parse each sitemap XML file concurrently.
2. Combine extracted URLs and SKUs from all sitemaps.
3. Perform searches across the unified list of URLs and SKUs.

## Performance

The system's performance depends on factors like hardware and network capabilities. With parallel processing and caching, it should handle a significant number of users. Load testing is recommended for accurate insights.

## References

Google

## Time Spent

I spent approximately 2.5 hours on this exercise.

## Future Improvements

If I had more time, I would focus on:
- Improving error handling and user feedback.
- Enhancing caching mechanisms for better performance.
- Implementing proper logging and monitoring.
- Adding pagination for search results display.

## Code Critique

While the code is organized and efficient, it can benefit from more detailed comments, especially in complex sections.

## Keyword Searches

To support keyword searches, the system can be updated to:
- Accept a keyword as input.
- Extend the search logic to match the keyword against product elements (title, author, etc.).
- Return relevant results based on keyword matches.
