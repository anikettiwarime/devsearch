# DevSearch - Developer Search and Collaboration Website

Welcome to DevSearch, a web application implemented using Django. DevSearch is a platform that brings together developers, allowing them to connect, showcase their skills through projects, and exchange messages. Whether you're looking to collaborate on a project or simply connect with like-minded developers, DevSearch is the place for you!

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [User Registration](#user-registration)
  - [Dashboard](#dashboard)
  - [Skills and Projects](#skills-and-projects)
  - [Messaging](#messaging)
- [Contributing](#contributing)
- [License](#license)

## Features

DevSearch offers a range of features to make developer collaboration and communication easy and efficient:

- **User Registration and Authentication**: Users can register, create an account, and log in to access the platform's features.

- **User Profiles**: Users can create profiles that showcase their skills, experience, and portfolio of projects.

- **Skills and Projects Showcase**: Developers can list their skills and create projects to showcase their expertise. Other users can view and search for developers based on their skills and project contributions.

- **Messaging System**: DevSearch provides an integrated messaging system, allowing users to communicate and collaborate on projects directly within the platform.

## Getting Started

### Prerequisites

Before you can run DevSearch, you need to have the following software installed on your system:

- Python (3.7+)
- Django (3.0+)
- Git (for version control)

### Installation

1. Clone the DevSearch repository to your local machine:

   ```bash
   git clone https://github.com/anikettiwarime/devsearch.git
   ```

2. Change the working directory to the project folder:

   ```bash
   cd devsearch
   ```

3. Create a virtual environment for your project (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser for the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

Your DevSearch website should now be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

### User Registration

1. Visit the DevSearch website.
2. Click on the "Register" link to create a new account.
3. Fill in the required information, including username, email, and password.
4. Verify your email if required.
5. Once registered and logged in, you can start using the platform.

### Dashboard

Upon logging in, you will be directed to your dashboard. Here, you can:

- View recommended developers and projects.
- Edit your profile to showcase your skills and create projects.
- Connect with other developers and send messages.

### Skills and Projects

1. To showcase your skills, navigate to the "My Profile" section.
2. Edit your profile and add skills.
3. To create a project, go to the "Projects" section and click on "Add Project."
4. Provide project details, including the project name, description, and tags.
5. Other users can now view your profile, skills, and projects.

### Messaging

1. To send messages to other users, visit their profile.
2. Click on the "Message" button to initiate a conversation.
3. Messages are exchanged directly on the platform, making collaboration easy.

