# Blog

A website that allows owner to post and manage blog entries. 

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - Front-end toolkit

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
* [Python 3] (https://www.python.org/downloads/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/GraceMurigi/blogsite.git
   ```
3. Create and activate your virtual environment
   ```sh
   python3 -m venv venv
   ```
   ```sh
   source path-to-venv/bin/activate
   ```
4. Install the project dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Setup DB (SQLite)
    ```sh
   python manage.py makemigrations
   ```
   ```sh
   python manage.py migrate
   ```
5. Create admin account
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server
    ```sh
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [w3schools] (https://www.w3schools.com/howto/howto_css_blog_layout.asp) - Layout Inspiration 
