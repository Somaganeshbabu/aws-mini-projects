# AWS Cognito User Pool Project

This project demonstrates the setup and usage of AWS Cognito User Pools for user registration, authentication, and web application integration. It includes everything you need to get started with AWS Cognito and create your own user pool.

## Project Structure
- `index.html`: A straightforward HTML page featuring anchor tags with links to Cognito login and signup pages, allowing you to easily customize the URLs as needed.
- `logged_in.html`: A login page that allows users to sign in with their Cognito credentials.
- `logoutPage.html`: A logout page that displays a "You have been successfully logged out" message.
- `server.py`: A Python script that can be used to run a local web server, allowing you to test your web pages and Cognito setup locally.
- `main.tf`: A Terraform configuration file to create an AWS Cognito User Pool. It configures the user pool, client, and domain with minimal configurations.
## Prerequisites

Before you begin, ensure you have the following:

- [Terraform](https://www.terraform.io/) installed on your system.
- AWS credentials configured with appropriate permissions.
## Getting Started

1. Clone this repository to your local machine.
2. Configure the AWS Cognito User Pool by following the steps in the Terraform configuration file (`main.tf`).

    a. Run `terraform init` to initialize the Terraform environment.

   b. Execute `terraform plan` to preview the changes Terraform will make.

   c. Finally, apply the changes with `terraform apply`.
4. Run the local web server to test the web application.

## Project Author

- [Ganeshbabu Soma](https://github.com/Somaganeshbabu/aws-mini-projects)
- Email: somaganeshbabu@gmail.com
