variable "subscription_id" {
  description   = "subscription_id"
  sensitive     = true
}

variable "client_id" {
  description = "appId"
  sensitive = true
}

variable "client_secret" {
  description = "password (Value not Secret ID)"
  sensitive = true
}

variable "tenant_id" {
  description = "tenant"
  sensitive = true
}

variable "resource_group_name" {
  default = "kmlops-resource-group"
}

# list of available region
# https://learn.microsoft.com/th-th/industry/sustainability/sustainability-data-solutions-fabric/deploy-availability
# https://www.azurespeed.com/Information/AzureRegions
variable "location" {
  description   = "region"
  sensitive     = true
}
