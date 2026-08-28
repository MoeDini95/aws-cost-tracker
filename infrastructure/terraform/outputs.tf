# Print EC2

output "ec2_public_ip" {
  description = "Public IP address of the main EC2 instance"
  value       = aws_instance.app.public_ip

}

output "ec2_public_dns" {
  description = "Public DNS info"
  value       = aws_instance.app.public_dns

}

output "vpc_id" {
  description = "Print VPC ID"
  value       = aws_vpc.main.id

}