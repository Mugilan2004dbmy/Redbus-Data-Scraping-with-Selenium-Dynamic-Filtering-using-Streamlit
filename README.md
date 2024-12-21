# **🚌 Red Bus Data Scraping with Selenium & Dynamic Filtering using Streamlit**  

This repository provides a comprehensive solution for scraping, storing, and visualizing bus travel data from the **Red Bus** website. The project integrates **Selenium** for web scraping, **SQL** for data storage, and **Streamlit** for data visualization.

## **📑 Table of Contents:**  
- **🔹 Introduction**  
- **🔹 Skills Acquired**  
- **🔹 Problem Statement**  
- **🔹 Approach**  
- **🔹 Project Structure**  
- **🔹 Prerequisites**  
- **🔹 Installation**  
- **🔹 Usage**  
- **🔹 Contributing**

## **📖 Introduction:**  
This project offers a robust solution for collecting, analyzing, and visualizing bus travel data from the Red Bus platform. It is divided into three main components:  
1. **Web Scraping Script**: Extracts data from the Red Bus website.  
2. **SQL Script**: Stores the scraped data in a SQL database.  
3. **Streamlit App**: Visualizes the data stored in the SQL database.

## **💡 Skills Acquired:**  
- **🔍 Web Scraping** using Selenium  
- **🐍 Python Programming**  
- **📊 Data Visualization** with Streamlit  
- **💾 SQL Database Management**  

## **🔍 Problem Statement:**  
The **Red Bus Data Scraping and Filtering with Streamlit Application** aims to transform the transportation industry by providing a complete solution for collecting, analyzing, and visualizing bus travel data. The project automates the extraction of detailed data from Redbus, such as bus routes, schedules, prices, and seat availability, improving operational efficiency and strategic planning within the transportation sector.

## **⚙️ Approach:**  
### **Data Scraping:**  
- **🧑‍💻 Selenium** is used to automate the extraction of data from the Red Bus website, including routes, schedules, prices, and seat availability.

### **Data Storage:**  
- The scraped data is stored in a **SQL database** for structured access.

### **Streamlit Application:**  
- A **Streamlit app** is developed to display and filter the scraped data.  
- Filters like bus type, route, price range, star rating, and availability are implemented.

### **Data Analysis/Filtering with Streamlit:**  
- SQL queries are executed to retrieve and filter data based on user inputs.  
- **Streamlit** allows users to interactively filter the data through the app.

## **🗂️ Project Structure:**  
- **red_bus_scraping.ipynb**: Jupyter notebook for Selenium script to scrape data.  
- **sql_script.ipynb**: Jupyter notebook for SQL script to insert scraped data into the database.  
- **streamlit_app.py**: Script for the Streamlit app to display the data.

## **⚙️ Prerequisites:**  
Ensure the following are installed before getting started:  
- **Python 3.x**  
- **Jupyter Notebook**  
- **Selenium**  
- **Streamlit**  
- **SQL Database** (e.g., SQLite, MySQL, PG Admin4)

## **💻 Installation:**  
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mugilan2004dbmy/Redbus-Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit
   cd red_bus_scraping
   ```
2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your SQL database** and update the connection details in `sql_script.ipynb` and `streamlit_app.py`.

## **🚀 Usage:**  
1. **Run the web scraping script:**  
   Open `red_bus_scraping.ipynb` in Jupyter Notebook and execute the cells to scrape data from the Red Bus website.  
2. **Insert data into the SQL database:**  
   Open `sql_script.ipynb` in Jupyter Notebook and execute the cells to insert data into your SQL database.  
3. **Run the Streamlit app:**  
   ```bash
   streamlit run streamlit_app.py
   ```  
   This will start the Streamlit server and open the app in your default web browser.

## **💬 Contributing:**  
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request for review. For significant changes, open an issue first to discuss your proposed changes.
