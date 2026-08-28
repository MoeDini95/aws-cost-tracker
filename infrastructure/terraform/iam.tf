# IAM Role

resource "aws_iam_role" "ec2" {
  name = "aws-cost-explorer"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }


      }
    ]
  })

}

#Ec2 Bacic policy

resource "aws_iam_role_policy_attachment" "ec2_basic" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"

}

# Read policy for Cost explorer

resource "aws_iam_role_policy_attachment" "cost_explorer" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AWSBillingReadOnlyAccess"
}

#Instance profile

resource "aws_iam_instance_profile" "ec2" {
  name = "ec2_profile"
  role = aws_iam_role.ec2.name
}