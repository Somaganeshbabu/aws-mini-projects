provider "aws" {
  region = "ap-south-1"
}
resource "aws_cognito_user_pool" "UserPool_sample" {
  name = "UserPool_sampleName"
  
  mfa_configuration ="OFF"


  password_policy{
   minimum_length = 8
   require_lowercase = true
   require_numbers = true
   require_uppercase=true
  require_symbols = true
  }
  
}


resource "aws_cognito_user_pool_client" "pool_client" {
  user_pool_id = aws_cognito_user_pool.UserPool_sample.id
  name = "Client"
  callback_urls = [ "http://localhost:8000/" ]
  supported_identity_providers = [ "COGNITO" ]
  allowed_oauth_flows = [ "code" ]
  allowed_oauth_scopes = [ "email", "openid", "profile"]
  
}

resource "aws_cognito_user_pool_domain" "cognito_domain" {
    user_pool_id = aws_cognito_user_pool.UserPool_sample.id
    domain = "terraform-userpool"
}

output "user_pool_id" {
  value = aws_cognito_user_pool.UserPool_sample.id
}

output "app_client_id" {
  value = aws_cognito_user_pool_client.pool_client.id
}