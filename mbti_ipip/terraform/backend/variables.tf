# Provider

variable "subscription_id" {
  type        = string
  description = "subscription_id"
  sensitive   = true
}

variable "client_id" {
  type        = string
  description = "appId"
  sensitive   = true
}

variable "client_secret" {
  type        = string
  description = "password (Value not Secret ID)"
  sensitive   = true
}

variable "tenant_id" {
  type        = string
  description = "tenant"
  sensitive   = true
}

# Resource Group

variable "resource_group_name" {
  type    = string
  default = "kmlops-tfstate"
}

variable "location" {
  type        = string
  description = "region"
  sensitive   = true
}

# Backend Storage

variable "storage_account_name" {
  type    = string
  default = "tfstatesakmlops"
}

variable "storage_container_name" {
  type    = string
  default = "tfstatesckmlops"
}

variable "container_access_type" {
  type    = string
  default = "private"
}