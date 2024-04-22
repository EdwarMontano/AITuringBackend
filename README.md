# AITuringBackend

This is the README file for the AITuringBackend project.


## Description

AITuringBackend is a backend application that powers the AITuring web application. It provides various functionalities for the web application, such as user authentication, data processing, and API endpoints.


## Installation

To install and run the AITuringBackend project locally, follow these steps:

1. Clone the repository:

  ```bash
  git clone https://github.com/your-username/AITuringBackend.git
  ```

2. Install the project dependencies:

  ```bash
  cd AITuringBackend
  poetry --version
  poetry env info
  poetry env use $(pyenv which python)
  poetry env info # la version de python debe coincidir 
  poetry shell 
  poetry install
  poetry show # dependencias instaladas == pip list
  poetry add [dependecias]
  pip install -r requirements.txt
  ```

3. Configure the environment variables:

  ```bash
  export AITURING_DB_URL=your_database_url
  export AITURING_API_KEY=your_api_key
  ```

4. Run the application:

  ```bash
  python app.py
  ```

## Usage

Once the application is running, you can access it at [https://aituringbackend-production.up.railway.app/](https://aituringbackend-production.up.railway.app/). Use the following credentials to log in:

- Username: aituringUserTest
- Password: %v!du0NxH4y4

## Contributing

If you would like to contribute to the AITuringBackend project, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

<!-- TODO: Verifer of stage of CMD's -->


