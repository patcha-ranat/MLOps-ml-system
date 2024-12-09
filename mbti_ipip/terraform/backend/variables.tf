variable "subscription_id" {
  description = "subscription_id"
  sensitive   = true
}

variable "client_id" {
  description = "appId"
  sensitive   = true
}

variable "client_secret" {
  description = "password (Value not Secret ID)"
  sensitive   = true
}

variable "tenant_id" {
  description = "tenant"
  sensitive   = true
}

variable "resource_group_name" {
  default = "kmlops-tfstate"
}

variable "location" {
  description = "region"
  sensitive   = true
}

variable "storage_account_name" {
  default = "tfstatesakmlops"
}

variable "storage_container_name" {
  default = "tfstatesckmlops"
}

variable "container_access_type" {
  default = "private"
}