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
  default = "kmlops-resource-group"
}

variable "location" {
  description = "region"
  sensitive   = true
}

variable "service_plan_os_type" {
  default = "Linux"
}

variable "service_plan_sku_name" {
  description = "recommend 'F1', 'B1', 'P0V3', 'P1V3'"
  default     = "F1"
}

variable "web_app_name" {
  default = "kmlops-ipip-mbti-azure"
}

variable "web_app_docker_image_name" {
  description = "docker_image:tag"
  default     = "patcharanat/kde-public-repo:v1.0.0"
}

variable "web_app_docker_registry_url" {
  description = "Fixed for docker hub, may vary by registry provider"
  default     = "https://index.docker.io"
}

variable "web_app_always_on" {
  description = "'false' required for sku 'F1'"
  default     = false
}

variable "registry_username" {
  type        = string
  description = "Docker Hub Email"
  sensitive   = true
}

variable "registry_password" {
  type        = string
  description = "Docker Hub Email"
  sensitive   = true
}