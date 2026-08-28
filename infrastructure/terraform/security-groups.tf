resource "aws_security_group" "ec2" {
  name        = "allow_http_traffic"
  description = "Allowing inbound HTTP traffic"
  vpc_id      = aws_vpc.main.id

  #inbound rule for port 80
  ingress {
    description = "HTTP port inbound"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]


  }

  #Import rule for HTTPS

  ingress {
    description = "HTTPS port inbound"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #Import rule for SSH

  ingress {
    description = "SSH port inbound"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]

  }

  tags = {
    Name    = "${var.project_name}-sg"
    Project = var.project_name
  }

}


