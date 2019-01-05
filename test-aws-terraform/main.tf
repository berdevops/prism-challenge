provider "aws" {
  region     = "eu-west-1"
  access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  profile    = "terraform"
}

resource "aws_instance" "web" {
  ami = "ami-00035f41c82244dab"
  instance_type = "t2.micro"
  tags {
    Name = "test-vm"
  }
}

