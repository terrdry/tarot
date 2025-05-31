# MIT License
# Copyright (c) 2025 Terry Drymonacos

provider "aws" {
    region     = local.region
    access_key = var.access_key
    secret_key = var.secret_key
}
