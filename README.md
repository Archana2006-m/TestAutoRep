# Title
Test Automation Project for Car search in London

**Overview**
This project is a test automation framework designed to automate the testing of [GoogleSearch/car_in_london].
It uses  Selenium, Pytest to perform Web Ui Automation.

 **Key Features**
- Automated testing of [GoogleSearch/car_in_london].
- Support for [Google Chrome browsers]
- Test Automation tool : Selenium web driver
- Design Pattern of Framework : Page object model
- Coding Language : Python
- IDE used:PyCharm

**Prerequisites**
Before setting up the project, ensure you have the following installed:

- **Programming Language**: [ Python 3.o+]
- **Package Manager**: [ pip]
- **Browser Drivers**: [ChromeDriver]
- **Dependencies**: [ Selenium, Pytest, WebDriverManager]
- **Other Tools**: [IDE (PyCharm)]
 
## **Setup Instructions**
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Archana2006-m/TestAutoRep.git
   
**Install Dependencies:**
Install the required Python packages using pip:
pip install -r requirements.txt

Project Structure

WebUIAutomation/car_search_in_london
├── tests/                  # Test scripts       # Example test file
│   └── test_car_search.py
├── pages/                  # Page Object Model (POM) classes
│   ├── google_page.py
│   └── gumtree_page.py
├── utils/                  # Utility functions
│   ├── driver_manager.py
│   ├──logger.py            # common logger function  for all modules               
├── config.py               # Configuration files
├── logging_config.py
└── main.py             
├── requirements.txt        # List of dependencies
└──run_tests.py  

