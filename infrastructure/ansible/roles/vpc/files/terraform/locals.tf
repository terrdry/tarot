# MIT License
# Copyright (c) 2025 Terry Drymonacos

locals {
    name = "ex-${basename(path.cwd)}"
    region = "us-west-2"

    tags = {
    Environment = "dev"
    Owner       = "terryd"
  }
}
