# sky-api-tests
This repository contains the api test created for sky technical test by Ravi

# branching structure
    1.'master' branch is the main branch
    2.test can be found in 'master' branch

# Folder structure
	1.Al tests are in tests folder
	2.All helper classes are in helpers folder
	3.Test results will be stored in allure-results folder
    4.Reports will be stored in allure-results folder
    5.All endpoints are in helpers/end_points.py file
    6. All helper methods are in helpers/ApitestHelper.py

# Libraries and python version used in framework
	1. python 3.7.9
	2. pytest
	3. requests
	4. allure

# 1. Prerequisites
	1.Need to install Docker
        https://docs.docker.com/get-docker/
    2.Docker should be up and running
        
# 2. Initial setup 
    # With docker
        1. Clone this repository to your local machine
        2.To build images with dependencies run below command from root folder of project
            docker-compose build
        3. To start container with shell in project root folder 
            docker-compose run apitests
        
    # To setup in local machine if docker is not installed
        1. Create a virtual environemnt with python3.7 using pycharm
        2. To install dependencies run 
            python3 -m pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
        
# 3. To run tests
	# Pytest is used to run tests, 
        1. To run all tests run below command from project root folder
            python3 -m pytest
        2. To run all tests in parallel for example in 2 instances use below command
            python3 -m pytest -n 2
        3. To run a specific test file
	        python3 -m pytest python_test_file_name.py

# 3. To exit test framework and docker
        1. To exit from docker container running tests run below command 
            exit
        2. To stop docker container run below command
	        docker-compose down

# 4. Reporting
    allure is used for reporting
       1. To run tests and check results in cli run below command from project root directory
            python3 -m pytest --alluredir=allure-results
       3. To run tests and save results in folder "allure-results"
            python3 -m pytest --alluredir=allure-results
       4. To access allure report, open below url in a browser (reports will be stored in allure-reports folder)
            http://localhost:5050/allure-docker-service/latest-report
       5. Note: It may take upto 3 seconds for the test results to updated on the web page

# 5. Wiki
    1. allure - used for reporting
        https://github.com/fescobar/allure-docker-service-examples/tree/master/allure-docker-python-pytest-example

	2. requests - Used for making requests to REST Api and and get responses (HTTP library) 
		https://requests.readthedocs.io/en/master/
	3. pytest - framework used to run tests
		https://docs.pytest.org/en/stable/






