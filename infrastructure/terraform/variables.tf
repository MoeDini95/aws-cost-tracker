variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"

}

variable "instance_type" {
  description = "This is the instance type of the EC2"
  default     = "t3.micro"
}

variable "project_name" {
  description = "The name of the project"
  default     = "aws-cost-tracker"

}