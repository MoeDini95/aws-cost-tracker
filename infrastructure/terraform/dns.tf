data "aws_route53_zone" "main" {
  name = "md-95.com"

}

resource "aws_route53_record" "costtracker" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "costtracker.md-95.com"
  type    = "A"
  ttl     = 300
  records = [aws_instance.app.public_ip]

}

resource "aws_kms_key" "dnssec" {
  provider                 = aws.us_east_1
  customer_master_key_spec = "ECC_NIST_P256"
  deletion_window_in_days  = 7
  key_usage                = "SIGN_VERIFY"
}

resource "aws_route53_key_signing_key" "main" {
  hosted_zone_id             = data.aws_route53_zone.main.zone_id
  key_management_service_arn = "arn:aws:kms:us-east-1:259004904941:key/74eec057-80f5-487f-a7da-a22584e04f17"
  name                       = "MD95KSK"
}

resource "aws_route53_hosted_zone_dnssec" "main" {
  hosted_zone_id = data.aws_route53_zone.main.zone_id
  depends_on     = [aws_route53_key_signing_key.main]
}