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

# Scaling the System Using a Database

## Database Setup

1. **Choose a Database System**: Select a suitable database system such as SQLite, MySQL, or PostgreSQL that aligns with your project's requirements and scalability goals.

2. **Design the Database Schema**: Create a database schema to accommodate product information fields such as title, author, price, and SKU. Define tables and their relationships.

3. **Establish Database Connection**: Write code to establish a connection to the chosen database. Use appropriate libraries and settings for your selected database system.

## Database Population

1. **Modify Scraping Code**: Adjust your existing scraping code to extract relevant product information from the website. Ensure you capture attributes like title, author, price, and SKU.

2. **Insert Records into Database**: After extracting the information, insert the collected records into the database. Map scraped data to appropriate database fields for each record.

## API Service Modification

1. **Query the Database for SKU**: When a search request arrives, query the database to check if the SKU exists. This step helps avoid unnecessary scraping if the information is already available in the database.

2. **Fetch Product Information**: If the SKU is found in the database, fetch the corresponding product information from the database. Utilize database querying mechanisms to retrieve the required fields.

3. **Return Database Response**: Return the fetched product information as the response to the search request. This eliminates the need to scrape the website for frequently searched SKUs.

## Benefits of Using a Database

- Reduced Load on Website: By storing product information in a database, the need for frequent website scraping is minimized, reducing the load on the website's server.

- Enhanced Performance: Database queries are optimized for efficient data retrieval, leading to faster response times compared to website scraping.

- Consistency and Reliability: A database ensures data consistency and reliability, mitigating potential errors associated with scraping.

## Conclusion

Integrating a database into the Sitemap Examiner system optimizes performance and paves the way for scalability. By minimizing scraping and relying on efficient database querying, the system can effectively handle increased user interactions while providing a smoother user experience.

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
