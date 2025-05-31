# MIT License
# Copyright (c) 2025 Terry Drymonacos

################################################################################
# VPC Module
################################################################################


resource "aws_vpc" "main" {
    cidr_block = "10.0.0.0/16"
    instance_tenancy = "default"

    tags = local.tags
}
