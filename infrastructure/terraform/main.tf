terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0"
    }
  }



  backend "s3" {
    bucket       = "aws-cost-tracker-tf"
    key          = "terraform.tfstate"
    region       = "us-east-1"
    use_lockfile = true
  }
}



provider "aws" {
  region = "us-east-1"

}