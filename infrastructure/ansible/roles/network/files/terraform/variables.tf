# MIT License
# Copyright (c) 2025 Terry Drymonacos

# Specifies whether the default VPC should be managed by this Terraform configuration.
# Set to true to allow management (such as modification or deletion) of the default VPC.
# Default is false, meaning the default VPC will not be managed.
variable "manage_default_vpc" {
  type        = bool
  description = "Whether to manage the default VPC"
  default     = false
}

# Specifies the name to assign to the default Virtual Private Cloud (VPC).
# This variable is of type string and defaults to "default".
variable "default_vpc_name" {
  type        = string
  description = "Name of the default VPC"
  default     = "default"
}

# Specifies whether to enable DNS hostnames for the default VPC.
# Set to true to allow instances within the VPC to receive DNS hostnames.
variable "default_vpc_enable_dns_hostnames" {
  type        = bool
  description = "Enable DNS hostnames for the default VPC"
  default     = true
}

# Map of tags to apply to resources.
# Type: map(string)
# Default: {}
variable "tags" {
  type        = map(string)
  description = "Tags to apply to resources"
  default     = {}
}

# The `secret_key` variable is used to provide the AWS Secret Key required for authentication.
# Type: string
# Description: AWS Secret Key
variable "secret_key" {
  type        = string
  description = "AWS Secret Key"
  sensitive   = true
}

# AWS Access Key used for authentication.
# This should be a string value representing your AWS IAM access key.
variable "access_key" {
  type        = string
  description = "AWS Access Key"
}
